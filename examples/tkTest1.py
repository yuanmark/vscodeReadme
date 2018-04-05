import tkinter
#import tkinter.ttk
win = tkinter.Tk()
win.title('tk grid test')

'''
grid的使用方式:
編號從0開始
label1.grid(row=0, column=0, sticky='w'+'e'+'n'+'s') #sticky只是黏貼方式，size變化行為不管
labelTest.grid(row=4, column=0, sticky='w'+'e'+'n'+'s')
label2.grid(row=1, column=1, columnspan=2, sticky='w'+'e'+'n'+'s')
entry1.grid(row=0, column=2, sticky='w'+'e'+'n'+'s')
entry2.grid(row=1, column=3, sticky='w'+'e'+'n'+'s')
entry3=tkinter.Entry(win)
entry3.insert(0, 'entry_3')
entry3.grid(row=2, column=0, rowspan=1, columnspan=3, sticky='w'+'e'+'n'+'s', padx=0, ipadx=0)
labelObj.grid(row=5, column=0, columnspan=2, sticky='w'+'e')

column/row-configure: 當視窗size變化時，元件大小縮放控制：
weight: 視窗改變時每一個格子的相對變化比例，weight=0表示不變
例子：
win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=5)
win.rowconfigure(0, weight=0)
win.rowconfigure(1, weight=0)
win.rowconfigure(2, weight=1)

Button(form, text='GO').grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky=W+E+N)
entry3=tkinter.Entry(win, text='column span entry')
entry3.grid(row=2, column=0, rowspan=1, columnspan=3, sticky='w'+'e', padx=0, ipadx=0)
'''

#建立TK entry(輸入)物件：entryTest, text='this is an entryTest'
entryTest=tkinter.Entry(win)
entryTest.insert(0, 'this is an entryTest')


labelObj=tkinter.Label(win, 
    text='labelTest\nabc\ndef', 
    height=3, width=15, justify='left', anchor='e',
    relief='raised', 
    padx=10, pady=5,
    bg='red', fg='yellow')

#TK label物件：labelTest, 
labelTest=tkinter.Label(win, text='this is a test')

#建立TK label物件：label1, text='label 1'
label1=tkinter.Label(win, text='label 1')
#label1.pack()

#建立TK label物件：label2, text='label 2'
label2=tkinter.Label(win, text='label 2', bg='red', anchor="w") #n, ne, e, se, s, sw, w, nw, or c.
#label2.pack()

#建立TK entry(輸入)物件：entry1, text='this is an entry1'
entry1=tkinter.Entry(win)
entry1.insert(0, 'this is an entry1')
#建立TK entry(輸入)物件：entry2, text='this is an entry2'
entry2=tkinter.Entry(win)
entry2.insert(0, 'this is an entry2')
#建立TK entry(輸入)物件：entry3, text='this is an entry3'
entry3=tkinter.Entry(win)
entry3.insert(0, 'this is an entry3')



label1.grid(row=0, column=0, sticky="w"+"e")
entry1.grid(row=0, column=2, sticky="w"+"e")
label2.grid(row=1, column=1, columnspan=2, sticky="w"+"e")
entry2.grid(row=1, column=3, sticky="w"+"e")
entryTest.grid(row=1, column=4, sticky="w"+"e")
entry3.grid(row=2, column=0, rowspan=1, columnspan=3, sticky="w"+"e"+"n"+"s", padx=0, ipadx=0)
labelTest.grid(row=4, column=0, sticky="w"+"e")
labelObj.grid(row=5, column=0, columnspan=2, sticky="w"+"e")

win.columnconfigure(0, weight=1)
win.columnconfigure(1, weight=1)
win.columnconfigure(2, weight=1)
win.columnconfigure(3, weight=1)
win.rowconfigure(0,weight=1)
win.rowconfigure(1,weight=1)
win.rowconfigure(2,weight=1)
win.rowconfigure(3,weight=1)

#-----------------
win.mainloop()