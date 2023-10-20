import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from model.xls_2_xlsx import xls_2_xlsx
from model.match_acc_exp import start_match
from model.generate_base import generate_base

def execute_actions():
    try:
        xls_2_xlsx()
        if start_match_var.get():
            input_value = input_entry.get()
            start_match(False, input_value)
        else:
            start_match(False)
        generate_base()
        showinfo("Execution Complete", "已生成底稿，请查看文件夹")
    except Exception as e:
        showinfo("Execution Error", 'ERROR!\n'+str(e))

def toggle_start_match():
    if start_match_var.get():
        input_entry.configure(state='normal')
    else:
        input_entry.configure(state='disabled')

root = tk.Tk()
root.title("IDC 底稿生成器")
root.geometry("300x200")
# Convert XLS to XLSX button
# convert_button = ttk.Button(root, text="Convert XLS to XLSX", command=xls_2_xlsx)
# convert_button.pack(pady=10)

# Start Match variable
start_match_var = tk.BooleanVar(value=False)

# Start Match checkbox
start_match_checkbox = ttk.Checkbutton(root,
                                       text="是否为换合同（默认为否）",
                                       variable=start_match_var, command=toggle_start_match)
start_match_checkbox.pack(pady=10, expand=True)

# Input Label
input_label = ttk.Label(root, text="若为换合同，输入供应商全称:")
input_label.pack(expand=True)

# Input Entry
input_entry = ttk.Entry(root, state='disabled')
input_entry.pack(expand=True)

# Generate Base Files button
# generate_button = ttk.Button(root, text="Generate Base Files", command=generate_base)
# generate_button.pack(pady=10)

# Execute Actions button
execute_button = ttk.Button(root, text="开始生成", command=execute_actions)
execute_button.pack(pady=20, expand=True)

root.mainloop()