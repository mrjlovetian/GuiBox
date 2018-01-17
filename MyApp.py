# coding=utf-8
import tkinter as tk
from MyDialog import MyMrjDilog

class MyMrjApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("用户信息")
        self.name = "余洪江"
        self.age = 28
        self.setup_UI()

    def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text="姓名：", width=8).pack(side=tk.LEFT)
        self.la = tk.Label(row1, text=self.name, width=8)
        self.la.pack(side=tk.LEFT)

        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Label(row2, text="年龄：", width=8).pack(side=tk.LEFT)
        self.lb = tk.Label(row2, text=self.age, width=8)
        self.lb.pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.pack(fill="x")
        tk.Button(row3, text="设置", width=8, command=self.setup_config).pack(side=tk.RIGHT)

    def setup_config(self):
        res = self.ask_userinfo()
        if res is None:
            return

        self.name, self.age = res
        self.la.config(text=self.name)
        self.lb.config(text=self.age)


    def ask_userinfo(self):
        inputDilog = MyMrjDilog()
        self.wait_window(inputDilog)
        return inputDilog.userinfo