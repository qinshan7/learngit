from tkinter import *

root = Tk()

root.geometry('400x500')
root.title('计算之神')

frame_show = Frame(width=300, height=150, bg='#dddddd')
frame_show.pack()

sv = StringVar()
sv.set('0')

i = ''

show_lable = Label(frame_show, text=i, \
                   bg='yellow', width=25, height=1, \
                   font=("黑体", 50, 'bold'), \
                   justify=LEFT, anchor='e')
show_lable.pack( padx=10, pady=10 )

def delete():
    global i
    i = i[:-1]
    show_lable['text'] = i
def clear():
    global i
    i = ''
    show_lable['text'] = i

def w():
    show_lable['text'] = '我怎么知道'
def e():
    show_lable['text'] = '我要发了'

def operation(op):
    global i
    i += op
    show_lable['text'] = i

def equal():
    global i
    try:
        if i != '':
            i = '%s'%eval(i)
            show_lable['text'] = i
    except:
        show_lable['text'] = '计算式错误'

frame_bord = Frame( width=400, height=350, bg='#CCCCCC' )
b_del = Button( frame_bord, text="←", width=10, height=2, \
               command=delete )
b_del.grid( row=0, column=2 )
b_del = Button( frame_bord, text="C", width=10, height=2, \
               command=clear ).grid( row=0, column=0 )
b_del = Button( frame_bord, text="±", width=10, height=2, \
               command=e ).grid( row=0, column=1 )
b_del = Button( frame_bord, text="CE", width=10, height=2, \
               command=clear ).grid( row=0, column=3 )



b_1 = Button(frame_bord, text='1', width=10, height=4, \
             command=lambda :operation('1')).grid(row=1, column=0)
b_2 = Button(frame_bord, text='2', width=10, height=4, \
             command=lambda :operation('2')).grid(row=1, column=1)
b_3 = Button(frame_bord, text='3', width=10, height=4, \
             command=lambda :operation('3')).grid(row=1, column=2)
b_4 = Button(frame_bord, text='4', width=10, height=4, \
             command=lambda :operation('4')).grid(row=1, column=3)
b_5 = Button(frame_bord, text='5', width=10, height=4, \
             command=lambda :operation('5')).grid(row=2, column=0)
b_6 = Button(frame_bord, text='6', width=10, height=4, \
             command=lambda :operation('6')).grid(row=2, column=1)
b_7 = Button(frame_bord, text='7', width=10, height=4, \
             command=lambda :operation('7')).grid(row=2, column=2)
b_8 = Button(frame_bord, text='8', width=10, height=4, \
             command=lambda :operation('8')).grid(row=2, column=3)
b_9 = Button(frame_bord, text='9', width=10, height=4, \
             command=lambda :operation('9')).grid(row=3, column=1)
b_0 = Button(frame_bord, text='0', width=10, height=4, \
             command=lambda :operation('0')).grid(row=3, column=2)

b_d = Button(frame_bord, text='=', width=10, height=4, \
             command=equal).grid(row=3, column=3)
b_w = Button(frame_bord, text='.', width=10, height=4, \
             command=lambda :operation('.')).grid(row=3, column=0)

b_w = Button(frame_bord, text='help', width=5, height=2, \
             command=w).grid(row=5, column=1)

b_jia = Button(frame_bord, text='+', width=10, height=2, \
             command=lambda :operation('+')).grid(row=4, column=0)
b_jian = Button(frame_bord, text='-', width=10, height=2, \
             command=lambda :operation('-')).grid(row=4, column=1)
b_cheng = Button(frame_bord, text='*', width=10, height=2, \
             command=lambda :operation('*')).grid(row=4, column=2)
b_chu = Button(frame_bord, text='/', width=10, height=2, \
             command=lambda :operation('/')).grid(row=4, column=3)

frame_bord.pack(padx=10, pady=10)

root.mainloop()
