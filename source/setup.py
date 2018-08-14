
##############################################################
# 作成日：2018/05/29
# 作成者：戸田滉洋
#
# 更新日：2018/05/29
# 更新者：戸田滉洋
# Copyright © 2018 Flugell System Studio. All rights reserved.
##############################################################
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from cx_Freeze import setup, Executable

import os
os.environ['TCL_LIBRARY'] = r"C:\App_system\Anaconda3\envs\hitex\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\App_system\Anaconda3\envs\hitex\tcl\tk8.6"

base = "Console"

#if sys.platform == "win32":
#    base = "Win32GUI"

if not True:
    import codecs


opt = dict(
    build_exe = dict(
        packages = [],
        excludes = [],
        includes = ['numpy.core._methods', 'numpy.lib.format','numpy.matlib','tkinter','tkinter.filedialog','pandas','configparser','mysql','insert_config'],
        include_files = [(r'C:\App_system\Anaconda3\envs\hitex\Lib\site-packages\scipy'),
                         (r'C:\App_system\Anaconda3\envs\hitex\DLLs\tk86t.dll'),
                         (r'C:\App_system\Anaconda3\envs\hitex\DLLs\tcl86t.dll')],
    ),
)

exe = Executable(script='D:\FSS\HITEX\DB_insert_data\source\insert_main.py', base=base)

setup(name = "insert_DB",
    version='1.0',
    options = opt,
    executables = [exe])
