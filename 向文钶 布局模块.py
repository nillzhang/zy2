if __name__ == "__main__":

    #音乐初始化
    pygame.mixer.init()
    # 异常抛出，防止没有放音乐文件
    try:
        pygame.mixer.music.load('music1.ogg')
    except Exception as e:
        print(type(e), e)
        tk.messagebox.showinfo("提示", "无文件music.ogg或改文件路径不对")
        sys.exit()
    pygame.mixer.music.set_volume(0.5)
    # 创建变量
    var = tk.IntVar()
    # 给变量赋初值为30
    var.set(30)

    # 番茄动态计时
    lb1 = tk.Label(root, text='0', bg='Tomato', fg='white', font='Verdana 16 bold', width=7, height=1)
    lb1.place(x=130, y=100)

    # 番茄固定时间
    lb2 = tk.Label(root, text='0', bg='Tomato', fg='white', font='Verdana 16 bold', width=5, height=1)
    lb2.place(x=60, y=100)

    # 剩余时间/总时间
    lb3 = tk.Label(root, text=' ', bg='Tomato', fg='white', font='Verdana 16 bold', width=14, height=2)
    lb3.place(x=50, y=44)

    # 番茄个数显示
    lb4 = tk.Label(root, text='0', bg='Tomato', fg='white', font='Verdana 16 bold', width=7, height=1)
    lb4.place(x=90, y=20)

    # 左上角的 番茄：
    lb5 = tk.Label(root, text='已完成学习周期：', bg='Tomato', fg='white', font='Verdana 16 bold', width=8, height=1)
    lb5.place(x=5, y=20)

    # 按钮
    ##创造一个frame来收纳按钮
    fr1 = tk.LabelFrame(root,bg='LightGreen',text='选择番茄钟时长', relief='groove', bd=1,)
    fr1.pack(side='right')
    r0 = tk.Radiobutton(fr1, text='1min', variable=var, bg='LightGreen', value=60)
    r0.pack()
    r1 = tk.Radiobutton(fr1, text='30min', variable=var, bg='LightGreen', value=1800)
    r1.pack()
    r2 = tk.Radiobutton(fr1, text='45min', variable=var, bg='LightGreen', value=2700)
    r2.pack()
    r3 = tk.Radiobutton(fr1, text='60min', variable=var, bg='LightGreen', value=3599)
    r3.pack()
    Checkbutton = tk.Checkbutton(fr1, text="是否禁止音乐", fg='black', bg='LightGreen', command=music_allow)
    Checkbutton.pack()

    # 开启一个番茄
    #利用多线程，避免进入番茄钟后，退出按钮失效
    Button1 = tk.Button(root, text='开启一个学习周期', bg='orange', fg='black', font='Verdana 13 bold',width=15,
                      height=1, command=lambda: threading.Thread(target=tomato_clock, daemon=True,args=(var.get(),)).start())
    Button1.place(x=70, y=150)

    # 休息一下
    Button2 = tk.Button(root, text='休息一下', bg='cornflowerblue', fg='black', font='Verdana 13 bold',
                        width=15, height=1, command=lambda: threading.Thread(target=relax, daemon=True).start())
    Button2.place(x=70, y=200)

    # 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
    button = tk.Button(root, text="退出", fg='black', bg='YellowGreen', width=15, command=root.quit)
    # 将按钮放置在主窗口内
    button.place(x=105, y=250)