Grade校色
-------------------

本节介绍利用 ``Grade`` 节点快速从匹配色调的方法

#.

  .. figure:: /_images/grade_1.png

    存在源素材和目标色调参考

#.

  .. figure:: /_images/grade_2.png

    在源素材上创建一个 ``Grade`` 节点

#.

  .. figure:: /_images/grade_3.png

    点击 ``gain`` 右侧色块开始取目标色

#.

  .. figure:: /_images/grade_4.png

    将查看器连接至目标色调参考

#.

  .. figure:: /_images/grade_5.png

    在查看器中按住 ``Ctrl+Shift`` 在要匹配的区域进行框选取色

#.

  .. figure:: /_images/grade_6.png

    点击 ``whitepoint`` 右侧色块开始取素材色

#.

  .. figure:: /_images/grade_7.png

    在查看器中按住 ``Ctrl+Shift+Alt`` 在要匹配的区域进行框选取色

#.

  .. figure:: /_images/grade_8.png

    效果, 如果要匹配多个区域请使用mask 或者 ``ColorLookup`` , ``VectorField`` 节点

.. note::

  nuke取色操作:

  ``Ctrl`` : 单个点取色

  ``Ctrl+Shift`` : 区域取色

  以上两个操作时附加 ``Alt`` : 取色时在当前节点前取色(不受当前节点调色影响)
