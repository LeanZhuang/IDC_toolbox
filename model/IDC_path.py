import os
import sys


def idc_path():

    # 脚本调试
    this_path = os.path.abspath(__file__)
    this_path = os.path.dirname(this_path)
    this_path = os.path.dirname(this_path)


    # cx_Freeze 打包路径
    # this_path = os.path.dirname(os.path.realpath(sys.executable))


    return this_path
