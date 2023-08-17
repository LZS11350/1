import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random
import time
import sys

def logout():
    messagebox.showwarning("警告", "您正在注销地球Online账号")
    root.withdraw()  # 隐藏原来的窗口
    progress_window = tk.Toplevel(root)  # 创建一个新的顶级窗口作为进度窗口
    progress_window.title("注销进度")
    progress_window.geometry("270x150")
    title_progress = tk.Label(progress_window, text="正在注销中...", font=("Arial", 16), bg="white")  # 创建标题标签
    title_progress.pack(pady=20)
    progress_bar = ttk.Progressbar(progress_window, length=200)  # 创建一个进度条
    progress_bar.pack(pady=20)
    
    def update_progress():
        for i in range(101):
            progress_bar['value'] = i  # 更新进度条的值
            progress_window.update()  # 更新进度窗口
            time.sleep(random.uniform(0.01, 0.3))  # 随机延迟一段时间
        messagebox.showinfo("提示", "地球Online账号注销已完成")
        progress_window.destroy()  # 关闭进度窗口
        root.after(0, exit_program)  # 调用退出程序函数
    
    def exit_program():
        progress_window.destroy()  # 关闭进度窗口
        root.destroy()  # 关闭主窗口，退出程序
        sys.exit()
    
    root.after(0, update_progress)  # 在主事件循环开始之前调用update_progress函数

def exit_program():
    root.destroy()  # 关闭主窗口，退出程序
    sys.exit()
root = tk.Tk()  # 创建主窗口
root.title("地球Online注销")
root.geometry("270x300")
root.configure(bg="white")  # 设置窗口背景颜色为白色

title_label = tk.Label(root, text="地球Online注销", font=("Arial", 16), bg="white")  # 创建标题标签
title_label.pack(pady=20)

account_label = tk.Label(root, text="账号：", bg="white")  # 创建账号标签
account_label.pack()
account_entry = tk.Entry(root)  # 创建账号输入框
account_entry.pack(pady=5)

password_label = tk.Label(root, text="密码：", bg="white")  # 创建密码标签
password_label.pack()
password_entry = tk.Entry(root, show="*")  # 创建密码输入框，显示为*
password_entry.pack(pady=5)

logout_button = tk.Button(root, text="注销", command=logout)  # 创建注销按钮，点击时调用logout函数
logout_button.pack(pady=10)

exit_button = tk.Button(root, text="退出", command=exit_program)  # 创建退出按钮，点击时调用exit_program函数
exit_button.pack()

root.mainloop()  # 进入主事件循环
