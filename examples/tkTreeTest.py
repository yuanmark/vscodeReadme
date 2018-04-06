
import tkinter
import tkinter.ttk

#keyin: tkloop, find tk/ttk import/mainloop, title='test treeview'
win = tkinter.Tk()
win.title('tk grid test')

#test
#keyin: ttktree, find ttk-09-treeview, tab,enter
#建立TK tree物件：tree
tree=tkinter.ttk.Treeview(win)
tree['columns']=('one','two')
tree.column('one', width=100 )
tree.column('two', width=100)
tree.heading('one', text='coulmn A')
tree.heading('two', text='column B')

#keyin: ttktree, find ttk-09-treeview-insert, tab,1,tab, 'end'/0=>keep 'end'
id1=tree.insert('' , 'end', text='id1', values=('1A','1B')) #end/0: insert from end/head of parent
idchild = tree.insert(id1, 'end', text='child of id1', values=('1a','1b'))
idchild = tree.insert(id1, 'end', text='child of id1', values=('1b','1c')) #依據idchild再加一個child
#same, tab,2,tab, keep 'end'
id2=tree.insert('' , 'end', text='id2', values=('2A','2B')) #end/0: insert from end/head of parent
idchild = tree.insert(id2, 'end', text='child of id2', values=('2a','2b'))

#依據tkgrid, find tk-00-grid-說明，打入最簡grid
tree.grid()

win.mainloop()