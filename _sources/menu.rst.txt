菜单
========

编辑
----

.. image:: /_images/edit_menu.png

.. _同时编辑多个节点:

同时编辑多个节点
****************

.. image:: /_images/multi_edit.png

同时设置多个同类型节点
常用于设置Read节点帧范围

.. figure:: /_images/multi_edit_choose.png

  如果选中的节点包含多个类型会要求用户选择

分离图层
********

.. image:: /_images/shuffle_layer.png

为选中节点的每个图层(Layer)创建一个Shuffle

分离rgba
********

.. image:: /_images/shuffle_rgba.png

为选中节点的rgba通道各创建一个shuffle

重命名PuzzleMatte
******************

.. image:: /_images/rename_channels.png

为选中节点中的PuzzleMatte通道指定新的名称
提升节点可读性

.. figure:: /_images/rename_channels_result.png

  效果

.. _标记为稍后启用:

标记为稍后启用
****************

将选中节点标为稍后启用, 用于加快预览

在首选项中有相关设置使其在保存时自动重新开启

可以使用 :ref:`禁用所有稍后启用节点` 来快速禁用所有

输出当前帧png
**************

为选中节点当前帧创建一张png

设置帧范围
**********

.. image:: /_images/set_framerange.png

为选中读取节点设置帧范围

.. tip::

    适用情况较限定, 推荐使用\ :ref:`同时编辑多个节点`\ 代替

转换为相对路径
****************

将选中读取节点的素材路径转为相对路径

.. attention::

    这是从老版本插件继承的功能,尚未测试

.. _禁用所有稍后启用节点:

禁用所有稍后启用节点
*************************

将所有\ :ref:`标记为稍后启用`\ 的节点禁用

修正读取错误
**************

.. figure:: /_images/fix_error_read_before.png

  在有读取节点错误时先拖入正确的素材

.. figure:: /_images/fix_error_read_after.png

  会比较文件名将报错的素材替换为同名正确的素材

Reload所有
******************

一次性点击所有读取节点的Reload

检查缺帧
********

检查所有读取节点的素材缺帧状况

在Nuke打开和保存文件时会自动执行此命令

.. figure:: /_images/check_dropframes_normal.png

  无素材缺帧的正常情况

.. figure:: /_images/check_dropframes.png

  如果有缺帧

.. figure:: /_images/check_dropframes_node.png

  节点上会显示

.. figure:: /_images/check_dropframes_console.png

  错误控制台上也会显示

检查素材更新
********************

比较素材修改日期和当前脚本工程文件日期

在Nuke打开文件时会自动执行此命令

.. figure:: /_images/check_mtime_normal.png

  无素材更新的正常情况

.. figure:: /_images/check_mtime.png

  如果有素材更新


转换单帧为序列
********************

将所有单帧的读取节点转换为序列

.. image:: /_images/frame2sequence.png

.. figure:: /_images/frame2sequence_before.png

  工程中需要替换成序列的单帧节点

.. figure:: /_images/frame2sequence_after.png

  所有符合条件的节点都会被替换

匹配抽帧
*********************

根据为选中节点的 rgb 通道创建对应的 TimeWrap 节点用于匹配抽帧。

如果每一帧都不同，则提示用户未检测到抽帧而不创建节点。

.. image:: /_images/Nuke10.5_2019-11-05_16-19-39.png

对话框选项:

起始帧

  匹配起始帧

结束帧

  匹配结束帧

阈值

  匹配阈值，0 到 1。 rgb 亮度变化平均值大于阈值算作帧有变化。

.. figure:: /_images/Nuke10.5_2019-11-05_16-24-22.png

  匹配结果

编辑/整理
---------------

用于整理节点

.. _整理所选节点(竖式摆放):

整理所选节点(竖式摆放)
*******************************

比原生自动摆放方法效果更好的竖式自动摆放

.. figure:: /_images/orgnize_before.png

  整理前

.. figure:: /_images/orgnize_after.png

  整理后

清理无用节点
***********************

删除未被写入节点使用的节点

.. figure:: /_images/delete_unused_before.png

  清理前

.. image:: /_images/delete_unused_after.png

.. figure:: /_images/delete_unused_after_2.png

  清理后

所有Gizmo转Group
************************

交付给雾插件环境前对脚本使用此命令以脱离插件依赖

根据背板重命名所有节点
************************

通过背板对节点批量命名

.. figure:: /_images/rename_by_backdrop_before.png

  命名前

.. figure:: /_images/rename_by_backdrop_after.png

  命名后

.. _节点添加Dots变成90度:

节点添加Dots变成90度
**********************

.. figure:: /_images/add_dot_to_90_before.png

  执行前

.. figure:: /_images/add_dot_to_90_after.png

  执行后

.. note::

  这是一个实验性功能

所有节点添加Dots变成90度
*************************

对所有节点执行 :ref:`节点添加Dots变成90度`

合成
----

.. _自动合成:

|comp_icon| 自动合成
*******************************

自动合成当前导入的素材

1.
  .. figure:: /_images/comp_prepare.png

    导入素材

2.
  .. figure:: /_images/comp_run.png

    执行

3.
  .. figure:: /_images/comp_result.png

    结果

.. _自动合成设置:

|comp_icon| 自动合成设置
*******************************************

.. image:: /_images/comp_setting.png

对 :ref:`自动合成` 进行设置。


Redshift 预合成
***************

将选中的Redshift素材节点进行分层预合成

.. figure:: /_images/precomp_redshift.png

  一键搭建所需框架

Arnold 预合成
***************

将选中的 Arnold 素材节点进行分层预合成

.. figure:: /_images/precomp_arnold.png

  一键搭建所需框架

自动预合成
**********************

根据分层检测使用的素材类型，并使用对应的预合成。

支持：

- RedShift
- Arnold


|cgteamwork_icon| CGTeamWork
---------------------------------

.. image:: /_images/cgtw_menu.png

此菜单只在安装了CGTeamWork之后才会出现

登录
****

.. image:: /_images/cgtw_login.png

用于自动登录失效时临时进行手动登录, 推荐之后重开Nuke和CGTeamWork使用自动登录

添加note
*********

.. image:: /_images/cgtw_note.png

为CGTeamWork上的对应镜头添加备注

提交单帧
*********
将\ :ref:`wlf_Write`\ 节点输出的单帧提交

.. warning::

    正规的提交不应该是单帧应是mov

提交视频
********

将\ :ref:`wlf_Write`\ 节点输出的视频提交

.. _创建项目色板:

创建项目色板
****************

.. image:: /_images/cgtw_csheet.png

为项目创建色板

此功能在CGTeamWork右键菜单中也能访问

创建项目文件夹
******************

.. image:: /_images/cgtw_dir_creation.png

为项目中的每个匹配镜头建立一个空文件夹

帮助
----

.. image:: /_images/help_menu.png

吾立方插件 文档
***************

本文档的入口

吾立方网站
**********

公司官网

工具
----

.. image:: /_images/tool_menu.png

每次使用前带需要设置的操作

.. _批量自动合成:

|comp_icon| 批量自动合成
**************************

.. image:: /_images/batchcomp.png

合成/自动合成的批量版本
直接自动合成大量镜头

.. image:: /_images/batchcomp_run.png

使用多线程, 内存不足时会等待足够的空闲内存再继续。

.. figure:: /_images/batchcomp_result.png

  批量合成日志

.. _创建色板:

创建色板
********

为一个文件夹中的图像文件(.jpg, .png, .jpeg)创建html色板

.. _上传工具:

上传mov
********

.. image:: /_images/uploader.png

上传工作成果至服务器或CGTeamWork

扫描空文件夹
************

.. image:: /_images/scanner.png

用于快速找出无素材的镜头

分离exr
*******

.. image:: /_images/split_exr.png

把多层的exr文件分成多个单层的exr文件

分割当前文件(根据背板)
**********************

.. image:: /_images/split_by_backdrop.png

把多包含多个镜头的文件根据背板(Backdrop)分离成多个单镜头的文件

.. |comp_icon| image:: /_images/comp_icon.png

.. |cgteamwork_icon| image:: /_images/cgteamwork_icon.png
