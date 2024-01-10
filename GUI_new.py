import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

from model.convert_xlsx import convert_xlsx
from model.match_acc_exp import start_match
from model.generate_base import generate_base

# 执行程序
def execute_actions():
    try:
        convert_xlsx()
    except Exception as e:
        showinfo("Load Error", "xls 保存 xlsx 失败\n检查是否存在相应文件\n\n依旧存在问题，请反馈:zhuangyuhao@baidu.com")

    try:
        if start_match_var.get():
            input_value = input_entry.get()
            # start_match(True, input_value)
            generate_list = start_match(True, input_value)
        else:
            # start_match(False)
            generate_list = start_match(False)
        generate_base()
        showinfo("Execution Complete", f"已生成底稿，请查看文件夹。\n \n该单涉及费用期间为{generate_list}")
    except Exception as e:
        showinfo("Execution Error", 'ERROR!\n'+str(e))


# 切换匹配模型
def toggle_start_match():
    if start_match_var.get():
        input_entry.configure(state='normal')
    else:
        input_entry.configure(state='disabled')


root = tk.Tk()
root.title("IDC工具箱 Ver 0.30 beta")
# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 500
window_height = 320

# 计算窗口在屏幕上的左上角位置
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3

# 设置窗口的尺寸和位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# 创建标签容器
tab_control = ttk.Notebook(root)

# 创建第一个标签页
tab1 = ttk.Frame(tab_control, style='Tab1.TFrame')
tab_control.add(tab1, text='IDC-sys底稿生成')

# 在第一个标签页上添加内容
# label1 = ttk.Label(tab1, text='这是标签页1')
# label1.pack()

# 创建第二个标签页
tab2 = ttk.Frame(tab_control, style='Tab2.TFrame')
tab_control.add(tab2, text='标签页2')

# 在第二个标签页上添加内容
label2 = ttk.Label(tab2, text='这是标签页2')
label2.pack()


# Start Match variable
start_match_var = tk.BooleanVar(value=False)

# Start Match checkbox
start_match_checkbox = ttk.Checkbutton(tab1,
                                       text="是否为换合同（默认为否）",
                                       variable=start_match_var, command=toggle_start_match)
start_match_checkbox.pack(pady=5, expand=True)

# Input Label
input_label = ttk.Label(tab1, text="若为换合同，输入供应商全称:")
input_label.pack(expand=True)

# Input Entry
input_entry = ttk.Entry(tab1, state='disabled')
input_entry.pack(expand=True)

# Execute Actions button
execute_button = ttk.Button(tab1, text="开始生成", command=execute_actions)
execute_button.pack(pady=20, expand=True)


# 将标签容器放置在主窗口中
tab_control.pack(expand=1, fill="both")

# 启动主循环
root.mainloop()
