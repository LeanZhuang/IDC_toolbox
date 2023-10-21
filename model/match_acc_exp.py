import pandas as pd
import os
from model.load_data import load_accured
from model.xls_2_xlsx import xls_2_xlsx_2
from model.IDC_path import idc_path


def match_nornal():
    this_path = idc_path()

    """匹配正常的预提表，非变更合同
    """
    # 加载预提表
    no_bandwidth_list, bandwidth_list = load_accured()

    xls_2_xlsx_2()

    check = pd.read_excel(this_path + '/temp/中间底稿.xlsx')


    contract_id = check['合同编号'].to_list()
    contract_id = list(set(contract_id))

    no_bandwidth_need = pd.DataFrame([])
    bandwidth_need = pd.DataFrame([])


    for id in contract_id:
        for database in no_bandwidth_list:
            database = database[database['当前计提合同'] == id]
            no_bandwidth_need = pd.concat([no_bandwidth_need, database])

    for id in contract_id:
        for database in bandwidth_list:
            database = database[database['当前计提合同'] == id]
            bandwidth_need = pd.concat([bandwidth_need, database])

    no_bandwidth_need = no_bandwidth_need.iloc[:, :25]
    bandwidth_need = bandwidth_need.iloc[:, :29]

    period_list = check['费用表月份'].to_list()

    period_list = list(map(str, period_list))

    period_list = [period.replace('-', '') for period in period_list]
    period_list = list(set(period_list))

    bandwidth_need['费用期间'] = bandwidth_need['费用期间'].astype(str)
    no_bandwidth_need['费用期间'] = no_bandwidth_need['费用期间'].astype(str)


    bandwidth_need = bandwidth_need[bandwidth_need['费用期间'].isin(period_list)]
    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['费用期间'].isin(period_list)]


    # 保存中间表
    bandwidth_need.to_excel(this_path + '/temp/带宽.xlsx', index=False)
    no_bandwidth_need.to_excel(this_path + '/temp/非带宽.xlsx', index=False)


def match_change(supplier: str):
    """匹配变更合同的预提表

    Args:
        supplier (str): 供应商名称
    """

    this_path = idc_path()

    # 加载预提表
    no_bandwidth_list, bandwidth_list = load_accured()

    # 加载中间表
    xls_2_xlsx_2()

    check = pd.read_excel(this_path + '/temp/中间底稿.xlsx')

    main_supplier = supplier

    no_bandwidth_need = pd.DataFrame([])
    bandwidth_need = pd.DataFrame([])


    # 匹配符合的供应商
    for database in no_bandwidth_list:
        database = database[database['供应商'] == main_supplier]
        no_bandwidth_need = pd.concat([no_bandwidth_need, database])

    for database in bandwidth_list:
        database = database[database['供应商'] == main_supplier]
        bandwidth_need = pd.concat([bandwidth_need, database])

    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['当前计提合同'].str.startswith('L')]
    no_bandwidth_need = no_bandwidth_need.iloc[:, 0:25]

    bandwidth_need = bandwidth_need[bandwidth_need['当前计提合同'].str.startswith('L')]
    bandwidth_need = bandwidth_need.iloc[:, 0:29]


    period_list = check['费用表月份'].to_list()

    period_list = list(map(str, period_list))

    period_list = [period.replace('-', '') for period in period_list]
    period_list = list(set(period_list))

    bandwidth_need['费用期间'] = bandwidth_need['费用期间'].astype(str)
    no_bandwidth_need['费用期间'] = no_bandwidth_need['费用期间'].astype(str)


    bandwidth_need = bandwidth_need[bandwidth_need['费用期间'].isin(period_list)]
    no_bandwidth_need = no_bandwidth_need[no_bandwidth_need['费用期间'].isin(period_list)]

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

start_match(True, 'aaa')