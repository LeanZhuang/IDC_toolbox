import pandas as pd

from model.load_data import load_accured
from model.convert_xlsx import convert_xlsx
from model.IDC_path import idc_path


def period_list(check):
    table_list = check['费用表月份'].to_list()
    table_list = list(map(str, table_list))
    table_list = [period.replace('-', '') for period in table_list]
    table_list = [period.replace('2023', '23') for period in table_list]
    table_list = list(set(table_list))

    generate_list = check['费用所属月份'].to_list()
    generate_list = list(map(str, generate_list))
    generate_list = [period.replace('-', '') for period in generate_list]
    generate_list = list(set(generate_list))

    resource_list = check['资源类型'].to_list()
    resource_list = list(map(str, resource_list))
    resource_list = list(set(resource_list))

    return table_list, generate_list, resource_list


def filter_dict_values(dictionary, date_list):
    """筛选需要的预提表
    """

    # dictionary: {'2310': df, ...}
    filtered_table_list = []

    for date in date_list:
        if date in dictionary:
            filtered_table_list.append(dictionary[date])

    return filtered_table_list


def general_match(check, no_bandwidth_dict, bandwidth_dict):
    """通用筛选
    """

    # 载入费用表list，费用所属期间list，资源list
    table_list, generate_list, resource_list = period_list(check)

    ## 筛选需要的费用表
    filtered_no_bandwidth_values = filter_dict_values(no_bandwidth_dict, table_list)
    filtered_bandwidth_values = filter_dict_values(bandwidth_dict, table_list)

    ## 筛选费用发生期间
    # 创建空dataframe
    no_bandwidth_need = pd.DataFrame([])
    bandwidth_need = pd.DataFrame([])

    # 拼接dataframe，生成汇总的大预提表
    for database in filtered_no_bandwidth_values:
            no_bandwidth_need = pd.concat([no_bandwidth_need, database])

    for database in filtered_bandwidth_values:
            bandwidth_need = pd.concat([bandwidth_need, database])

    no_bandwidth_need['费用期间'] = no_bandwidth_need['费用期间'].astype(str)
    bandwidth_need['费用期间'] = bandwidth_need['费用期间'].astype(str)

    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['费用期间'].isin(generate_list)]
    bandwidth_need = bandwidth_need[bandwidth_need['费用期间'].isin(generate_list)]

    ## 筛选资源类型
    no_bandwidth_need_2 = pd.DataFrame([])
    # print(resource_list)

    resource_list += ['电路', '传输', '电流', '占用', '服务', '改造', '光纤', '专线', '其他', '费']

    for resource in resource_list:
        no_bandwidth_need_choice = no_bandwidth_need[no_bandwidth_need['费用类型（机架、带宽、光纤/电路、其他）'].str.contains(resource)]

        no_bandwidth_need = no_bandwidth_need[~no_bandwidth_need['费用类型（机架、带宽、光纤/电路、其他）'].str.contains(resource)]

        no_bandwidth_need_2 = pd.concat([no_bandwidth_need_2, no_bandwidth_need_choice])

    no_bandwidth_need = no_bandwidth_need_2


    return no_bandwidth_need, bandwidth_need



def match_nornal():
    """匹配正常的预提表，非变更合同
    """

    this_path = idc_path()

    # 加载预提表和中间底稿
    no_bandwidth_dict, bandwidth_dict = load_accured()
    convert_xlsx()

    check = pd.read_excel(this_path + '/temp/中间底稿.xlsx')
    no_bandwidth_need, bandwidth_need = general_match(check, no_bandwidth_dict, bandwidth_dict)


    # 匹配合同号
    contract_id = check['合同编号'].to_list()
    contract_id = list(set(contract_id))

    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['当前计提合同'].isin(contract_id)]
    bandwidth_need = bandwidth_need[bandwidth_need['当前计提合同'].isin(contract_id)]

    no_bandwidth_need = no_bandwidth_need.iloc[:, :25]
    bandwidth_need = bandwidth_need.iloc[:, :29]

    # 保存中间表
    bandwidth_need.to_excel(this_path + '/temp/带宽.xlsx', index=False)
    no_bandwidth_need.to_excel(this_path + '/temp/非带宽.xlsx', index=False)


def match_change(supplier: str):
    """匹配变更合同的预提表
    """

    this_path = idc_path()

    # 加载预提表和中间底稿
    no_bandwidth_dict, bandwidth_dict = load_accured()
    convert_xlsx()


    check = pd.read_excel(this_path + '/temp/中间底稿.xlsx')
    no_bandwidth_need, bandwidth_need = general_match(check, no_bandwidth_dict, bandwidth_dict)

    main_supplier = supplier

    # 匹配符合的供应商
    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['供应商'] == main_supplier]
    bandwidth_need = bandwidth_need[bandwidth_need['供应商'] == main_supplier]


    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['当前计提合同'].str.startswith('L')]
    no_bandwidth_need = no_bandwidth_need.iloc[:, 0:25]

    bandwidth_need = bandwidth_need[bandwidth_need['当前计提合同'].str.startswith('L')]
    bandwidth_need = bandwidth_need.iloc[:, 0:29]


    # 保存中间表
    bandwidth_need.to_excel(this_path + '/temp/带宽.xlsx', index=False)
    no_bandwidth_need.to_excel(this_path + '/temp/非带宽.xlsx', index=False)


def start_match(is_change: bool, supplier: str = None):
    """开始匹配
    """
    if is_change == False:
        match_nornal()
    else:
        match_change(supplier=supplier)

# start_match(True, 'aaa')