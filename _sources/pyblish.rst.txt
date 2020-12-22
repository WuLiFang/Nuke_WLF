发布
========

工作流程上使用 `Pyblish <http://pyblish.com/>`_ 发布框架

发布分为4个阶段进行: ``收集`` -> ``检查`` -> ``提取`` -> ``集成``


界面
----------

.. figure:: /_images/pyblish_ui.png

  界面分为三个标签页: ``概览``, ``详细``, ``日志``, 在顶部可以切换

  右下方随当前状态变化有最多4个按钮:

  - |reset| : 重置当前阶段到 ``收集`` 前

  - |validate| : 执行, 完成 ``检查`` 阶段后停止

  - |publish| : 执行, 完成 ``发布`` 阶段后停止

  - |stop| : 终止当前操作


.. |reset| image:: /_images/pyblish_button_reset.png
    :align: middle

.. |validate| image:: /_images/pyblish_button_validate.png
    :align: middle

.. |publish| image:: /_images/pyblish_button_publish.png
    :align: middle

.. |stop| image:: /_images/pyblish_button_stop.png
    :align: middle

在初始状态下发布面板使用浮动窗口, 但也可以手动设置固定位置并保存在工作区中

.. figure:: /_images/pyblish_menu.png

  在Nuke面板空白处选择 ``Windows`` - ``Custom`` - ``发布`` 即可创建固定面板

  然后使用Nuke菜单 - ``Workspace`` - ``Save Workspace...``  即可保存工作区

自动化
--------------

插件已经配置了自动触发发布

- 读取工程时: 重置并进行至 ``检查`` 阶段后

- 保存工程时: 重置并进行至 ``检查`` 阶段后

- 退出工程时: 如果工程没有未保存的更改, 进行至 ``发布`` 阶段后

错误处理
----------

.. figure:: /_images/pyblish_traytip.png

  在发布过程中失败会有气泡提示原因

.. figure:: /_images/pyblish_panel_log.png

  气泡提示只显示简略信息, 详细信息在 ``日志`` 标签页中查看(在上方切换)
