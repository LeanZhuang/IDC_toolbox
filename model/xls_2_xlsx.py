# import os
# import glob
# import pandas as pd
# from model.IDC_path import idc_path


# def xls_2_xlsx():
#     """将下载文件夹内最新的xls文件转换为xlsx文件
#     """

#     # 获取IO内最新的xls文件
#     latest_file = max(glob.glob(os.path.join("./IO", "*.xls")), key=os.path.getctime)

#     # 读取xls文件
#     df = pd.read_excel(latest_file)

#     # 将数据保存为xlsx文件
#     df.to_excel('./temp/中间底稿.xlsx', index=False)


import os
import glob
import pandas as pd
from model.IDC_path import idc_path


def xls_2_xlsx_2():

    """将下载文件夹内最新的xls文件转换为xlsx文件，采用了相对路径"""

    #设置路径
    this_path = idc_path()

    # IO_path = this_path + '/IO/'

    input_path = '/Users/zhuangyuhao/Downloads'

    # 获取IO内最新的xls文件
    xls_files = [os.path.join(input_path, file) for file in os.listdir(input_path) if file.startswith('export')]
    latest_file = max(xls_files, key=os.path.getctime)

    # 读取xls文件
    df = pd.read_excel(latest_file)

    # 获取保存目录的绝对路径
    save_directory = this_path + "/temp"

    # 设置保存文件的绝对路径
    save_file_path = save_directory + "/中间底稿.xlsx"

    # 将数据保存为xlsx文件
    df.to_excel(save_file_path, index=False)

# xls_2_xlsx_2()