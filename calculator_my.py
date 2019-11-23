import tkinter
import tkinter.messagebox
import re

#计算情况
operators = ('+','-','*','/')
def button(btn):
    content = contentshow.get()
    if content.startwith('.'):
        content = '0'+ content

    if btn in '1234567890':
        content += btn
    elif btn=='.':
        lastpart = re.split(r'\+|-|\|*/',content)[-1]
        if '.' in lastpart:
            tkinter.messagebox.showerror('error','Repating decimal point')
            return
        else:
            content += btn
    elif btn == 'clear':
        content = ''
    elif btn == '=':
        # noinspection PyBroadException
        try:
            content = str(eval(content))
        except:
            tkinter.messagebox.showerror('error','Expression error')
            return
    elif btn in operators:
        if content.endswith(operators):
           tkinter.messagebox.showerror('error','Operators cannot be used continuously')
           return
        content += btn
    contentshow.set(content)
#设计主体框
main = tkinter.Tk()
#geometry()   ...widthxheight+x+y
main.geometry('300x270+400+100')
main.resizable(False,False)
main.title('calculator')

#设计按钮事件,导入内容

#刷新变量
contentshow = tkinter.StringVar(main,'')
#文本框内容
contenttext = tkinter.Entry(main,textvariable=contentshow)
contenttext['state'] = 'readonly'
contenttext.place(x=10,y=10,width=280,height=20)


#放按钮
btnclear = tkinter.Button(main,text='clear',bg='blue',command=lambda:button('clear'))
btnclear.place(x=170,y=40,width=80,height=20)
number = list('1234567890.=')
index=0
for row in range(4):
    for col in range(3):
        a = number[index]
        index += 1
        allnumber = tkinter.Button(main,text=a,bg='yellow',command=lambda x=a:button(x))
        allnumber.place(x=20 + col * 70, y=80 + row * 50, width=50, height=20)

for index,operator in enumerate(operators):
    btnoperator = tkinter.Button(main,text=operator,bg='orange',command=lambda b=operator:button(b))
    btnoperator.place(x=230, y=80 + index * 30, width=50, height=20)

main.mainloop()