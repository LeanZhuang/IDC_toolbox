import pandas as pd
from model.IDC_path import idc_path
import os


def load_accured() -> list:
    """读取预提表并生成中间文件，随后生成预提表清单

    Returns:
        list: 带宽与非带宽的预提表清单
    """
    this_path = idc_path()

    name_list = []

    folder_path = this_path + '/预提表'
    file_names = os.listdir(folder_path)
    for file_name in file_names:
        file_name = file_name[:4]
        name_list.append(file_name)

    filenames = list(set(name_list))
    # print(filenames)

    no_bandwidth_list = []
    bandwidth_list = []

    for filename in filenames:
        try:
            expense_bandwidth = pd.read_pickle(this_path + f'/pkl/{filename} 带宽.pkl')
            expense_no_bandwidth = pd.read_pickle(this_path + f'/pkl/{filename} 非带宽.pkl')
        except FileNotFoundError:
            expense_bandwidth = pd.read_excel(this_path + f'/预提表/{filename} 带宽.xlsx')
            expense_no_bandwidth = pd.read_excel(this_path + f'/预提表/{filename} 非带宽.xlsx')
            expense_bandwidth.to_pickle(this_path + f'/pkl/{filename} 带宽.pkl')
            expense_no_bandwidth.to_pickle(this_path + f'/pkl/{filename} 非带宽.pkl')

        no_bandwidth_list.append(expense_no_bandwidth)
        bandwidth_list.append(expense_bandwidth)

    # print(len(bandwidth_list))
    return no_bandwidth_list, bandwidth_list

# load_accured()