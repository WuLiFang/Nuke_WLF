开发
==============

利用 GNU Make 搭建开发环境

Makefile 使用的环境变量:

NUKE_PYTHON

  本机 Nuke 内置 python 路径。

PYTHON27

  python2.7 路径，用于安装依赖，推荐使用最新版。
  因为 Nuke 内置 python 太老了，不能使用 pip + https。

测试
------------

``make test``
