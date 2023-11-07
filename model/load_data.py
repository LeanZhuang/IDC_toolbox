import pandas as pd
from model.IDC_path import idc_path

def load_accured() -> list:
    """读取预提表并生成中间文件，随后生成预提表清单

    Returns:
        list: 带宽与非带宽的预提表清单
    """
    this_path = idc_path()

    filenames = ['2302', '2303', '2304', '2305', '2306', '2307', '2308', '2309']
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

    return no_bandwidth_list, bandwidth_list

# load_accured()