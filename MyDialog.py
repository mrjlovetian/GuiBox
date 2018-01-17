# coding=utf-8

import tkinter as tk

class MyMrjDilog(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("MRJ_title")
        self.setup_UI()

    def setup_UI(self):
        row1 = tk.Frame(self)
        row1.pack(fill='x')

        tk.Label(row1, text="姓名", width=8).pack(side=tk.LEFT)
        self.name = tk.StringVar()
        tk.Entry(row1, textvariable=self.name, width=20).pack(side=tk.LEFT)

        row2 = tk.Frame(self)
        row2.pack(fill='x')

        tk.Label(row2, text="年龄", width=8).pack(side=tk.LEFT)
        self.age = tk.IntVar()
        tk.Entry(row2, textvariable=self.age, width=20).pack(side=tk.LEFT)

        row3 = tk.Frame(self)
        row3.pack(fill='x')

        tk.Button(row3, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(row3, text="确定", command=self.ok).pack(side=tk.RIGHT)


    def ok(self):
        self.userinfo = [self.name.get(), self.age.get()]
        self.destroy()

    def cancel(self):
        self.userinfo = None
        self.destroy()

