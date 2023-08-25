import tkinter as tk
import tkinter.messagebox
from winsound import Beep
import threading
import sys
import pygame
import time

# 用于统计完成的番茄钟个数
count = 0
# 线程切换标志
thread_flag = True
# 音乐开关标志
music_flag = True

# 调用Tk()创建主窗口
root = tk.Tk()
# 给主窗口起一个名字，也就是窗口的名字
root.title('阳光四人组的学习钟')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root.geometry('460x300')
root.configure(bg='blue')