import os

def idc_path():
    this_path = os.path.abspath(__file__)
    this_path = os.path.dirname(this_path)
    this_path = os.path.dirname(this_path)
    return this_path