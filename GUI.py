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
            start_match(True, input_value)
        else:
            start_match(False)
        generate_base()
        showinfo("Execution Complete", "已生成底稿，请查看文件夹")
    except Exception as e:
        showinfo("Execution Error", 'ERROR!\n'+str(e))


# 切换匹配模型
def toggle_start_match():
    if start_match_var.get():
        input_entry.configure(state='normal')
    else:
        input_entry.configure(state='disabled')


# GUI 框架
root = tk.Tk()
root.title("IDC 底稿生成器 Ver 0.22 beta")

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口的宽度和高度
window_width = 450
window_height = 250

# 计算窗口在屏幕上的左上角位置
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 3

# 设置窗口的尺寸和位置
root.geometry(f"{window_width}x{window_height}+{x}+{y}")


# Start Match variable
start_match_var = tk.BooleanVar(value=False)

# Start Match checkbox
start_match_checkbox = ttk.Checkbutton(root,
                                       text="是否为换合同（默认为否）",
                                       variable=start_match_var, command=toggle_start_match)
start_match_checkbox.pack(pady=5, expand=True)

# Input Label
input_label = ttk.Label(root, text="若为换合同，输入供应商全称:")
input_label.pack(expand=True)

# Input Entry
input_entry = ttk.Entry(root, state='disabled')
input_entry.pack(expand=True)

# Execute Actions button
execute_button = ttk.Button(root, text="开始生成", command=execute_actions)
execute_button.pack(pady=20, expand=True)

root.mainloop()
