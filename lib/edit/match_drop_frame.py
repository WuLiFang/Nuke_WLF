# -*- coding=UTF-8 -*-
"""Match drop frame from a node.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import typing  # pylint:disable=unused-import

import nuke
from six.moves import range

import nuketools
from nuketools import utf8 as _


def get_time_wrap_data(n, start, end, tolerance=0.001):
    """Get timewrap data from a node

    Args:
        n (nuke.Node): Node
        start (int): Start frame
        end (int): End frame
        tolerance (float, optional): Match tolerance. Defaults to 0.001.

    Returns:
        typing.List[int]: Data for timewrap.
    """
    # type: (nuke.Node, int, int, int) -> typing.List[int]

    assert isinstance(n, nuke.Node)

    nodes = []  # type: typing.List[nuke.Node]
    ret = []
    try:

        n_time_offset = nuke.nodes.TimeOffset(
            inputs=[n],
            time_offset=1
        )  # type: nuke.Node
        nodes.append(n_time_offset)
        n_merge = nuke.nodes.Merge2(
            inputs=[n, n_time_offset],
            operation='difference')  # type: nuke.Node
        nodes.append(n_merge)
        n_curve_tool = nuke.nodes.CurveTool(
            inputs=[n_merge],
            avgframes=0,
            ROI='{} {} {} {}'.format(0, 0, n.width(), n.height())
        )  # type: nuke.Node
        nodes.append(n_curve_tool)

        nuke.execute(n_curve_tool, start, end)
        k = n_curve_tool['intensitydata']  # type: nuke.Knob
        source_f = start
        for f in range(start, end+1):
            v = sum(k.getValueAt(f)[:3]) / 3
            if v > tolerance:
                source_f = f
            ret.append(source_f)
    finally:
        for i in nodes:
            nuke.delete(i)
    return ret


def create_time_wrap(data, start=1):
    """Create time wrap from time wrap data.

    Args:
        data (typing.List[int]): Frame lookup list for each frame from start.
        start (int, optional): Start frame. Defaults to 1.

    Returns:
        nuke.nodes.TimeWrap: Created node.
    """
    # type: typing.List[int] -> nuke.nodes.TimeWrap
    curve_points = [(start, data[0])]  # type.List[type.Tuple[int, int]]
    end = start + len(data)
    for index, i in enumerate(data):
        f = start + index
        if curve_points[-1][1] == i and f < end:
            # skip same value (not apply to last frame)
            continue
        curve_points.append((f, i))

    n = nuke.nodes.TimeWarp(
        lookup='{{ curve K {}}}'.format(
            ' '.join('x{} {}'.format(i[0], i[1])
                     for i in curve_points))
    )  # type: nuke.Node

    return n


@nuketools.undoable_func('匹配抽帧')
def show_dialog():
    """GUI dialog for `get_timewrap_data`

    Returns:
        type.Optional[nuke.node.TimeWrap]: created node
    """
    try:
        n = nuke.selectedNode()
    except ValueError:
        nuke.message(_('请先选择节点'))
        return

    def _tr(key):
        return _({
            'start': '起始帧',
            'end': '结束帧',
            'tolerance': '阈值',
        }.get(key, key))

    panel = nuke.Panel(_('匹配抽帧'))
    panel.addExpressionInput(_tr('start'), nuke.numvalue('root.first_frame'))
    panel.addExpressionInput(_tr('end'), nuke.numvalue('root.last_frame'))
    panel.addExpressionInput(_tr('tolerance'), 0.001)

    if not panel.show():
        return

    start = int(panel.value(_tr('start')))
    end = int(panel.value(_tr('end')))
    tolerance = float(panel.value(_tr('tolerance')))

    data = get_time_wrap_data(n, start, end, tolerance)

    if len(set(data)) == len(data):
        nuke.message(_('未检测到抽帧'))
        return

    n_time_wrap = create_time_wrap(data, start)
    n_time_wrap['label'].setValue(_('抽帧匹配: {}'.format(n.name())))
    nuke.zoom(nuke.zoom(), (n_time_wrap.xpos(), n_time_wrap.ypos()))
    return n_time_wrap
