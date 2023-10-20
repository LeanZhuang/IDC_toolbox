import os
import glob
import pandas as pd


def xls_2_xlsx():
    """将下载文件夹内最新的xls文件转换为xlsx文件
    """

    # 设置下载文件夹路径和目标文件夹路径
    download_folder = "/Users/zhuangyuhao/Downloads"
    middle_folder = "temp"

    # 获取下载文件夹内最新的xls文件
    latest_file = max(glob.glob(os.path.join(download_folder, "*.xls")), key=os.path.getctime)

    # 读取xls文件
    df = pd.read_excel(latest_file)

    # 将数据保存为xlsx文件
    df.to_excel('./temp/中间底稿.xlsx', index=False)
