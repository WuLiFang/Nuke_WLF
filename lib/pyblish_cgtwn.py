# -*- coding=UTF-8 -*-
"""CGTeamWork pyblish plug-in.  """

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import logging
import os
import webbrowser

import nuke
import pyblish.api

import cgtwq
from cgtwn import Task
from node import wlf_write_node
from wlf.files import copy
from wlf.path import PurePath

LOGGER = logging.getLogger('wlf.pyblish_cgtwn')

# pylint: disable=no-init


class CollectTask(pyblish.api.InstancePlugin):
    """获取Nuke文件对应的CGTeamWork任务.   """

    order = pyblish.api.CollectorOrder
    label = '获取对应任务'
    families = ['Nuke文件']

    def process(self, instance):

        assert isinstance(instance, pyblish.api.Instance)

        task = Task.from_shot(PurePath(instance.name).shot)
        instance.context.data['task'] = task
        LOGGER.info('任务 %s', task)


class CollectUser(pyblish.api.ContextPlugin):
    """获取当前登录的用户帐号.   """

    order = pyblish.api.CollectorOrder
    label = '获取当前用户'

    def process(self, context):
        assert isinstance(context, pyblish.api.Context)

        name = cgtwq.current_account()

        context.data['artist'] = name
        context.data['accountID'] = cgtwq.current_account_id()
        context.create_instance(
            '制作者: {}'.format(name),
            family='制作者'
        )


class CollectFX(pyblish.api.ContextPlugin):
    """获取特效素材.   """
    order = pyblish.api.CollectorOrder + 0.1
    label = '获取特效素材'

    def process(self, context):
        task = context.data['task']
        assert isinstance(task, Task)
        filebox = task.get_filebox('fx')
        dir_ = filebox.path
        context.create_instance(
            '有特效素材' if os.listdir(dir_) else '无特效素材',
            folder=dir_,
            family='特效素材'
        )


class OpenFolder(pyblish.api.InstancePlugin):
    """打开非空的文件夹.   """

    order = pyblish.api.ValidatorOrder
    label = '打开素材文件夹'
    families = ['特效素材']

    def process(self, instance):
        if os.listdir(instance.data['folder']):
            webbrowser.open(instance.data['folder'])


class VadiateArtist(pyblish.api.InstancePlugin):
    """检查任务是否分配给当前用户。  """

    order = pyblish.api.ValidatorOrder
    label = '检查制作者'
    families = ['制作者']

    def process(self, instance):
        assert isinstance(instance, pyblish.api.Instance)
        context = instance.context
        task = context.data['task']
        assert isinstance(task, Task)
        current_id = context.data['accountID']
        current_artist = context.data['artist']

        id_ = task['account_id']
        if current_id not in id_.split(','):
            LOGGER.error('用户不匹配: %s -> %s',
                         current_artist, task['artist'])
            raise cgtwq.AccountError(
                owner=id_, current=current_id)


class VadiateFrameRange(pyblish.api.InstancePlugin):
    """检查帧范围是否匹配上游.  """

    order = pyblish.api.ValidatorOrder
    label = '检查帧范围'
    families = ['帧范围']

    def process(self, instance):
        assert isinstance(instance, pyblish.api.Instance)
        task = instance.context.data['task']
        assert isinstance(task, Task)

        n = task.import_video('animation_videos')
        upstream_framecount = int(n['last'].value() - n['first'].value() + 1)
        current_framecount = int(
            instance.data['last'] - instance.data['first'] + 1)
        if upstream_framecount != current_framecount:
            LOGGER.error('工程帧数和上游不一致: %s -> %s',
                         current_framecount, upstream_framecount)
            raise ValueError(
                'Frame range not match.',
                upstream_framecount,
                current_framecount)


class VadiateFPS(pyblish.api.InstancePlugin):
    """检查帧速率是否匹配数据库设置.   """

    order = pyblish.api.ValidatorOrder
    label = '检查帧速率'
    families = ['帧速率']

    def process(self, instance):
        task = instance.context.data['task']
        assert isinstance(task, Task)

        database = task.module.database
        fps = database.get_data('fps', is_user=False)
        if not fps:
            LOGGER.warning('数据库未设置帧速率: %s', database.name)
        else:
            current_fps = instance.data['fps']
            if float(fps) != current_fps:
                LOGGER.error('帧速率不一致: %s -> %s', current_fps, fps)
                raise ValueError('Not same fps', fps, current_fps)


class UploadWorkFile(pyblish.api.InstancePlugin):
    """上传工作文件至CGTeamWork.   """

    order = pyblish.api.IntegratorOrder
    label = '上传工作文件'
    families = ['Nuke文件']

    def process(self, instance):
        assert isinstance(instance, pyblish.api.Instance)
        workfile = instance.data['name']
        task = instance.context.data['task']
        assert isinstance(task, Task)
        dest = task.get_filebox('workfile').path + '/'
        # dest = 'E:/test_pyblish/'

        copy(workfile, dest)


class UploadJPG(pyblish.api.InstancePlugin):
    """上传单帧至CGTeamWork.   """

    order = pyblish.api.IntegratorOrder
    label = '上传单帧'
    families = ['Nuke文件']

    def process(self, instance):
        task = instance.context.data['task']
        assert isinstance(task, Task)

        n = wlf_write_node()
        path = nuke.filename(n.node('Write_JPG_1'))
        dest = task.get_filebox('image').path + '/{}.jpg'.format(task.shot)
        # dest = 'E:/test_pyblish/{}.jpg'.format(task.shot)
        copy(path, dest)