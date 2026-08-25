import tkinter as tk
import random
import threading

i = 0
colors = ['white','red','green','yellow','blue','pink','orange']

def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0,width)
    b = random.randrange(0,height)
    window.title("你被骗了")
    window.geometry("300x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,text="你被骗了",bg=random.choice(colors),font=("宋体",17),width=20,height=4).pack()
    window.mainloop()
def boom2():
    a = 50 + (i+1)*20
    b = 50 + (i+1)*20
    window = tk.Tk()
    window.title("你被骗了")
    window.geometry("300x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,text="你被骗了",bg=random.choice(colors),font=("宋体",17),width=20,height=4).pack()
    window.mainloop()

def boom3():
    a = 1650 - (i+1)*20
    b = 50 + (i+1)*20
    window = tk.Tk()
    window.title("你被骗了")
    window.geometry("300x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window,text="你被骗了",bg=random.choice(colors),font=("宋体",17),width=20,height=4).pack()
    window.mainloop()


threads = []
for i in range(100):
    t = threading.Thread(target = boom)
    threads.append(t)
    threads[i].start()

threads = []
for i in range(40):
    t = threading.Thread(target = boom2)
    threads.append(t)
    threads[i].start()

i = 0
threads = []
for i in range(40):
    t = threading.Thread(target = boom3)
    threads.append(t)
    threads[i].start()