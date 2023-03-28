import tkinter as tk
import subprocess

# 定義選項
dut_options = ["1", "2", "3"]
role_options = ["a", "b", "c"]
chip_options = ["", "chip HPA", "chip SGA"]

# 定義選單改變時的事件
def on_option_change(*args):
    dut = dut_var.get()
    role = role_var.get()
    chip = chip_var.get()
    cmd = ["python", "xxx.py", f"--dut{dut}", "--role", role]
    if chip:
        cmd.append(chip)
    subprocess.run(cmd)

# 建立主視窗
root = tk.Tk()

# 建立選項變數
dut_var = tk.StringVar(root)
role_var = tk.StringVar(root)
chip_var = tk.StringVar(root)

# 設定預設值
dut_var.set(dut_options[0])
role_var.set(role_options[0])
chip_var.set(chip_options[0])

# 建立下拉式選單
dut_option_menu = tk.OptionMenu(root, dut_var, *dut_options, command=on_option_change)
role_option_menu = tk.OptionMenu(root, role_var, *role_options, command=on_option_change)
chip_option_menu = tk.OptionMenu(root, chip_var, *chip_options, command=on_option_change)

# 設定選單位置
dut_option_menu.pack()
role_option_menu.pack()
chip_option_menu.pack()

# 建立按鈕
execute_button = tk.Button(root, text="執行", command=on_option_change)
execute_button.pack()

# 啟動主迴圈
root.mainloop()
