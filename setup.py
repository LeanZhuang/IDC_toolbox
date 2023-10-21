"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['GUI.py']
DATA_FILES = ['model/formatted.py',
              'model/generate_base.py',
              'model/load_data.py',
              'model/match_acc_exp.py',
              'model/xls_2_xlsx.py',
              'model/IDC_path.py']
OPTIONS = {'includes':['pandas', 'openpyxl', 'xldr', 'xlrd']}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
