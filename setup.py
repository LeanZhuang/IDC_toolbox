# 使用cx_Freeze打包时的setup

from cx_Freeze import setup, Executable

setup(name='GUI',
      version='0.20',
      description='',
      executables=[Executable('GUI.py',base='Win32GUI')])
