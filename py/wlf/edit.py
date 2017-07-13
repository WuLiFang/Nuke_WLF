# -*- coding: UTF-8 -*-
"""Edit existed content in workfile."""

import os
import re
import colorsys
import random

import nuke

__version__ = '1.0.2'


def all_knobs_name(node):
    """Return all knobs name as a list."""

    _ret = []
    for n in node.allKnobs():
        _ret.append(n.name())
    return _ret


def rename_all_nodes():
    """Rename all nodes by them belonged backdrop node ."""

    for i in nuke.allNodes('BackdropNode'):
        _nodes = i.getNodes()
        j = i['label'].value().split('\n')[0].split(' ')[0]
        for k in _nodes:
            if k.Class() == 'Group' and not '_' in k.name() and not (k['disable'].value()):
                name = k.name().rstrip('0123456789')
                k.setName(name + '_' + j + '_1', updateExpressions=True)
            elif not '_' in k.name() \
                    and (not nuke.exists(k.name() + '.disable') or not (k['disable'].value())):
                k.setName(k.Class() + '_' + j + '_1', updateExpressions=True)


def swap_knob_value(knob_a, knob_b):
    """Swap two same type knob value."""
    value_a, value_b = knob_a.value(), knob_b.value()
    knob_a.setValue(value_b)
    knob_b.setValue(value_a)


def update_toolsets(toolset_name, toolset_path):
    """Replace name matched node with given toolset."""

    for i in nuke.allNodes():
        if toolset_name in i.name() and 'python' not in i['label'].value():
            i.selectOnly()
            n = nuke.loadToolset(toolset_path)
            for k in i.allKnobs():
                knob_name = k.name()
                if knob_name in ['name', '', 'label']:
                    pass
                elif knob_name in all_knobs_name(n):
                    n[knob_name].setValue(i[knob_name].value())
            nuke.delete(i)


def channels_rename(prefix='PuzzleMatte'):
    """Shuffle channel to given name channel in mask_extra layer."""

    n = nuke.selectedNode()

    # Record viewer status
    existed_viewer = nuke.activeViewer()
    _raw = dict.fromkeys(['has_viewer', 'viewer_input', 'viewer_channels'])
    _raw_viewer = {}
    if existed_viewer:
        existed_viewer = existed_viewer.node()
        _raw['has_viewer'] = True
        _raw['viewer_input'] = existed_viewer.input(0)
        if not _raw['viewer_input']:
            existed_viewer.setInput(0, n)
        for knob in existed_viewer.knobs():
            _raw_viewer[knob] = existed_viewer[knob].value()
    else:
        _raw['has_viewer'] = False
        existed_viewer = nuke.createNode('Viewer')
        existed_viewer.setInput(0, n)

    # Set viewer
    nuke.activeViewer().activateInput(0)
    layer_contactsheet = nuke.nodes.LayerContactSheet(showLayerNames=1)
    layer_contactsheet.setInput(0, n)
    existed_viewer.setInput(0, layer_contactsheet)
    existed_viewer['channels'].setValue('rgba')

    # Prepare dictionary
    dict_ = {}
    for i in n.channels():
        if i.startswith(prefix):
            dict_[i] = ''
    channel_names = dict_.keys()

    # Sort object on rgba order
    def _rgba_order(name):
        ret = name.replace(prefix + '.', '!.')

        repl = {'.red': '.0_', '.green': '.1_',
                '.blue': '.2_', '.alpha': '.3_'}
        for k, v in repl.iteritems():
            ret = ret.replace(k, v)
        return ret
    channel_names.sort(key=_rgba_order)

    # Set text style
    def _text_stylize(text):
        ret = text
        repl = {'.red': '.<span style=\"color:#FF4444\">red</span>',
                '.green':  '.<span style=\"color:#44FF44\">green</span>',
                '.blue': '.<span style=\"color:#4444FF\">blue</span>'}
        for k, v in repl.iteritems():
            ret = ret.replace(k, v)
        return ret
    stylized_channel_names = map(_text_stylize, channel_names)

    # Set panel from dictionary
    panel = nuke.Panel('MaskShuffle')
    for i in enumerate(channel_names):
        i = i[0]
        panel.addSingleLineInput(
            stylized_channel_names[i], dict_[channel_names[i]])

    # Show panel
    panel.show()
    nuke.delete(layer_contactsheet)

    # Recover Viewer Status
    if _raw['has_viewer']:
        existed_viewer.setInput(0, _raw['viewer_input'])
        for knob in existed_viewer.knobs():
            try:
                existed_viewer[knob].setValue(_raw_viewer[knob])
            except TypeError:
                pass
    else:
        nuke.delete(existed_viewer)
    n.selectOnly()

    # Create copy
    for i in enumerate(channel_names):
        i = i[0]
        # Create copy node every 4 channels
        count = i % 4
        if count == 0:
            n = nuke.createNode('Copy')
            # Set two input to same node
            if n.input(1):
                n.setInput(0, n.input(1))
            elif n.input(0):
                n.setInput(1, n.input(0))
        # Prepare 'to' channel name
        _input = panel.value(stylized_channel_names[i])
        if _input:
            value_to = 'mask_extra.'\
                + _input.replace(' ', '_').replace('.', '_')
            nuke.Layer('mask_extra', [value_to])
        else:
            value_to = 'none'
        # Set node
        n['from' + str(count)].setValue(channel_names[i])
        n['to' + str(count)].setValue(value_to)
        # Delete empty copy node
        if count == 3:
            if not list(i for i in
                        [n['to0'].value(), n['to1'].value(),
                         n['to2'].value(), n['to3'].value()]
                        if i != 'none'):
                n.input(0).selectOnly()
                nuke.delete(n)


def split_by_backdrop():
    """Split workfile to multiple file by backdrop."""

    text_saveto = '保存至:'
    text_ask_if_create_new_folder = '目标文件夹不存在, 是否创建?'

    # Panel
    panel = nuke.Panel('splitByBackdrop')
    panel.addFilenameSearch(text_saveto, os.getenv('TEMP'))
    panel.show()

    # Save splited .nk file
    save_path = panel.value(text_saveto).rstrip('\\/')
    noname_count = 0
    for i in nuke.allNodes('BackdropNode'):
        label = repr(i['label'].value()).strip(
            "'").replace('\\', '_').replace('/', '_')
        if not label:
            noname_count += 1
            label = 'noname_{0:03d}'.format(noname_count)
        if not os.path.exists(save_path):
            if not nuke.ask(text_ask_if_create_new_folder):
                return False
        dir_ = save_path + '/splitnk/'
        dir_ = os.path.normcase(dir_)
        if not os.path.exists(dir_):
            os.makedirs(dir_)
        filename = dir_ + label + '.nk'
        i.selectOnly()
        i.selectNodes()
        nuke.nodeCopy(filename)
    os.system('explorer "' + dir_ + '"')
    return True


def link_zdefocus():
    """Link all zdefocus node to '_ZDefocus' node."""

    n = nuke.toNode('_ZDefocus')
    if not n:
        return False
    for i in nuke.allNodes('ZDefocus2'):
        if i.name().startswith('_'):
            continue
        i['size'].setExpression('_ZDefocus.size')
        i['max_size'].setExpression('_ZDefocus.max_size')
        i['disable'].setExpression(
            '( [ exists _ZDefocus ] ) ? !_ZDefocus.disable : 0')
        i['center'].setExpression(
            '( [exists _ZDefocus] ) ? _ZDefocus.center : 0')
        i['dof'].setExpression(
            '( [exists _ZDefocus] ) ? _ZDefocus.dof : 0')
        i['label'].setValue('[\n'
                            'set trg parent._ZDefocus\n'
                            'if { [ exists $trg ] } {\n'
                            '    knob this.math [value $trg.math]\n'
                            '    knob this.z_channel [value $trg.z_channel]\n'
                            '}\n'
                            ']')
    return True


def get_min_max(src_node, channel='depth.Z'):
    '''
    Return the min and max values of a given node's image as a tuple

    args:
       src_node  - node to analyse
       channels  - channels to analyse. This can either be a channel or layer name
    '''
    min_color = nuke.nodes.MinColor(
        channels=channel, target=0, inputs=[src_node])
    inv = nuke.nodes.Invert(channels=channel, inputs=[src_node])
    max_color = nuke.nodes.MinColor(channels=channel, target=0, inputs=[inv])

    cur_frame = nuke.frame()
    nuke.execute(min_color, cur_frame, cur_frame)
    min_v = -min_color['pixeldelta'].value()

    nuke.execute(max_color, cur_frame, cur_frame)
    max_v = max_color['pixeldelta'].value() + 1

    for n in (min_color, max_color, inv):
        nuke.delete(n)
    return min_v, max_v


def set_random_glcolor(n):
    """Set node glcolor a random hue color."""

    if nuke.exists('{}.gl_color'.format(n.name()))\
            and not n['gl_color'].value()\
            and not n.name().startswith('_'):

        color = colorsys.hsv_to_rgb(random.random(), 0.8, 1)
        color = tuple(int(i * 255) for i in color)
        n['gl_color'].setValue(
            color[0] << 24 | color[1] << 16 | color[2] << 8)


def enable_rsmb(prefix='_'):
    """Enable all rsmb node with given prefix."""

    for i in nuke.allNodes('OFXcom.revisionfx.rsmb_v3'):
        if i.name().startswith(prefix):
            i['disable'].setValue(False)


def fix_error_read():
    """Try fix all read nodes tha has error."""

    while True:
        _created_node = []
        for i in (i for i in nuke.allNodes('Read') if i.hasError()):
            _filename = nuke.filename(i)
            if os.path.basename(_filename).lower() == 'thumbs.db':
                nuke.delete(i)
            if os.path.isdir(_filename):
                _filename_list = nuke.getFileNameList(_filename)
                for f in _filename_list:
                    _read = nuke.createNode(
                        'Read', 'file "{}"'.format('/'.join([_filename, f])))
                    _created_node.append(_read)
                nuke.delete(i)
        if not _created_node:
            break


def delete_unused_nodes(message=False):
    """Delete all unused nodes."""

    def _is_used(n):
        if n.name().startswith('_')\
                or n.Class() in ['BackdropNode', 'Read', 'Write', 'Viewer', 'GenerateLUT']:
            return True
        nodes_dependent_this = (n for n in n.dependent()
                                if n.Class() not in [''] or n.name().startswith('_'))
        return bool(nodes_dependent_this)

    count = 0
    while True:
        for i in nuke.allNodes():
            if not _is_used(i):
                nuke.delete(i)
                count += 1
                break
        else:
            break

    print('Deleted {} unused nodes.'.format(count))
    if message:
        nuke.message(
            '<font size=5>删除了 {} 个未使用的节点。</font>\n'
            '<i>名称以"_"(下划线)开头的节点及其上游节点将不会被删除</i>'.format(count))


def replace_sequence():
    '''
    Replace all read node to specified frame range sequence.
    '''
    # Prepare Panel
    panel = nuke.Panel('单帧替换为序列')
    render_path_text = '限定只替换此文件夹中的读取节点'
    panel.addFilenameSearch(render_path_text, 'z:/SNJYW/Render/')
    first_text = '设置工程起始帧'
    panel.addExpressionInput(first_text, int(
        nuke.Root()['first_frame'].value()))
    last_text = '设置工程结束帧'
    panel.addExpressionInput(last_text, int(nuke.Root()['last_frame'].value()))

    confirm = panel.show()
    if confirm:
        render_path = panel.value(render_path_text)

        first = int(panel.value(first_text))
        last = int(panel.value(last_text))
        flag_frame = None

        nuke.Root()['proxy'].setValue(False)
        nuke.Root()['first_frame'].setValue(first)
        nuke.Root()['last_frame'].setValue(last)

        for i in nuke.allNodes('Read'):
            file_path = nuke.filename(i)
            if file_path.startswith(render_path):
                search_result = re.search(r'\.([\d]+)\.', file_path)
                if search_result:
                    flag_frame = search_result.group(1)
                file_path = re.sub(
                    r'\.([\d#]+)\.',
                    lambda matchobj: r'.%0{}d.'.format(len(matchobj.group(1))),
                    file_path)
                i['file'].setValue(file_path)
                i['format'].setValue('HD_1080')
                i['first'].setValue(first)
                i['origfirst'].setValue(first)
                i['last'].setValue(last)
                i['origlast'].setValue(last)

        n = nuke.toNode('_Write')
        if n:
            if flag_frame:
                flag_frame = int(flag_frame)
                n['custom_frame'].setValue(flag_frame)
                nuke.frame(flag_frame)
            n['use_custom_frame'].setValue(True)


def set_project_root_by_name(path='E:'):
    """Set project root by underscore splitted filename."""

    nuke.root()['project_directory'].setValue(os.path.dirname(
        path + '/' + os.path.basename(nuke.scriptName()).split('.')[0].replace('_', '/')))


def split_layers(node):
    """Splits each and every layer from the selected node into their own pipes."""

    channels = node.channels()

    layers = []
    valid_channels = ['red', 'green', 'blue', 'alpha', 'black', 'white']

    for channel in channels:
        layer_name = channel.split('.')[0]
        layer = []
        for i in channels:
            if i.startswith(layer_name):
                layer.append(i)
        while len(layer) < 4:
            layer.append(layer_name + ".white")
        if layer not in layers:
            layers.append(layer)

    for i in layers:
        layer = i[0].split('.')[0]
        ch1 = i[0].split('.')[1]
        ch2 = i[1].split('.')[1]
        ch3 = i[2].split('.')[1]
        ch4 = i[3].split('.')[1]

        if ch1 not in valid_channels:
            ch1 = "red red"
        else:
            ch1 = '%s %s' % (ch1, ch1)

        if ch2 not in valid_channels:
            ch2 = "green green"
        else:
            ch2 = '%s %s' % (ch2, ch2)

        if ch3 not in valid_channels:
            ch3 = "blue blue"
        else:
            ch3 = '%s %s' % (ch3, ch3)

        if ch4 not in valid_channels:
            ch4 = "alpha alpha"
        else:
            ch4 = '%s %s' % (ch4, ch4)

        prefs = "in %s %s %s %s %s" % (layer, ch1, ch2, ch3, ch4)
        shuffle = nuke.createNode('Shuffle', prefs, inpanel=False)
        # shuffle.knob( 'label' ).setValue( layer )
        shuffle.setInput(0, node)


def shuffle_rgba(node):
    """Create rgba shuffle."""
    channels = ['red', 'green', 'blue', 'alpha']
    for channel in channels:
        shuffle = nuke.nodes.Shuffle(label=channel)
        shuffle.setInput(0, node)
        for color in channels:
            shuffle[color].setValue(channel)


def nodes_to_relpath(nodes):
    """Convert given nodes's file knob to relative path."""

    perfix = r'[value root.project_directory]'
    proj_dir = nuke.root().knob('project_directory').getValue()
    for read_node in nodes:
        if read_node.knob('file') is not None:
            old_path = read_node.knob('file').getValue()
            new_path = old_path.replace(proj_dir, perfix)
            read_node.knob('file').setValue(new_path)


def nodes_add_dots(nodes=None):
    """Add dots to orgnize node tree."""

    if not nodes:
        nodes = nuke.selectedNodes()

    def _add_dot(output_node, input_num):
        input_node = output_node.input(input_num)
        if not input_node \
                or input_node.Class() in ['Dot'] \
                or abs(output_node.xpos() - input_node.xpos()) < output_node.screenWidth() \
                or abs(output_node.ypos() - input_node.ypos()) <= output_node.screenHeight():
            return None
        if output_node.Class() in ['Viewer'] or output_node['hide_input'].value():
            return None

        _dot = nuke.nodes.Dot(inputs=[input_node])
        output_node.setInput(input_num, _dot)
        _dot.setXYpos(
            input_node.xpos() + input_node.screenWidth() / 2 - _dot.screenWidth() / 2,
            output_node.ypos() + output_node.screenHeight() / 2 - _dot.screenHeight() /
            2 - (_dot.screenHeight() + 5) * input_num
        )

    def _all_input_add_dot(node):
        for input_num in range(node.inputs()):
            _add_dot(node, input_num)

    for n in nodes:
        if n.Class() in ['Dot']:
            continue
        _all_input_add_dot(n)


def gizmo_to_group(gizmo):
    """Convert given gizmo node to gruop node."""

    if not isinstance(gizmo, nuke.Gizmo):
        return gizmo

    _selected = gizmo['selected'].value()
    _group = gizmo.makeGroup()

    # Set Input.
    for i in range(gizmo.inputs()):
        _group.setInput(i, gizmo.input(i))
    # Set Output.
    for n in nuke.allNodes():
        for i in range(n.inputs()):
            if n.input(i) is gizmo:
                n.setInput(i, _group)

    # Set position and name.
    if gizmo.shown():
        _group.showControlPanel()
    _group.setXYpos(gizmo.xpos(), gizmo.ypos())
    _name = gizmo['name'].value()
    nuke.delete(gizmo)
    _group.setName(_name)
    _group['selected'].setValue(_selected)

    return _group


def all_gizmo_to_group():
    """Convert all gizmo node to group node."""

    for n in nuke.allNodes():
        # Avoid scripted gizmo.
        if nuke.knobChangeds.get(n.Class()):
            continue

        gizmo_to_group(n)


if __name__ == '__main__':
    gizmo_to_group(nuke.selectedNode())