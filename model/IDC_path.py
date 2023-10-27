import os
import sys


def idc_path():

    # 脚本调试
    this_path = os.path.abspath(__file__)
    this_path = os.path.dirname(this_path)
    this_path = os.path.dirname(this_path)


    # macOS 打包路径，配置文件 -> content
    # this_path = os.path.dirname(os.path.realpath(sys.executable))
    # this_path = os.path.dirname(this_path)
    # this_path = os.path.dirname(this_path)


    return this_path
