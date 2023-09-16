#python code for simple calculator
#importing everything from tkinter module
from tkinter import *
#create a gui window
suj=Tk()
#add title to gui window
suj.title("Calculator")
#set background to gui window
suj.configure(background='grey')
expression=''
equation=StringVar()
expression_field=Entry(suj,textvariable=equation).grid(columnspan=5,ipadx=60)
#function for evaluating the expression
def e():
    try:
        global expression
        ans=str(eval(expression))
        equation.set(ans)
        expression=''
    except:
        equation.set('error')
        expression=''
#function to update the expression
def press(num):
    global expression
    expression=expression+str(num)
    equation.set(expression)
#function to clear the expression
def clea():
    global expression
    expression=''
    equation.set(expression)
#creating buttons in the gui window
b1=Button(suj,fg='black',text='1',command=lambda:press('1'),height=2,width=7).grid(row=1,column=0)
b2=Button(suj,fg='black',text='2',command=lambda:press('2'),height=2,width=7).grid(row=1,column=1)
b3=Button(suj,fg='black',text='3',command=lambda:press('3'),height=2,width=7).grid(row=1,column=2)
b4=Button(suj,fg='black',text='4',command=lambda:press('4'),height=2,width=7).grid(row=2,column=0)
b5=Button(suj,fg='black',text='5',command=lambda:press('5'),height=2,width=7).grid(row=2,column=1)
b6=Button(suj,fg='black',text='6',command=lambda:press('6'),height=2,width=7).grid(row=2,column=2)
b7=Button(suj,fg='black',text='7',command=lambda:press('7'),height=2,width=7).grid(row=3,column=0)
b8=Button(suj,fg='black',text='8',command=lambda:press('8'),height=2,width=7).grid(row=3,column=1)
b9=Button(suj,fg='black',text='9',command=lambda:press('9'),height=2,width=7).grid(row=3,column=2)
b0=Button(suj,fg='black',text='0',command=lambda:press('0'),height=2,width=7).grid(row=4,column=0)
add=Button(suj,fg='black',text='+',bg='pink',command=lambda:press('+'),height=2,width=7).grid(row=1,column=4)
sub=Button(suj,fg='black',text='-',bg='pink',command=lambda:press('-'),height=2,width=7).grid(row=2,column=4)
mul=Button(suj,fg='black',text='*',bg='pink',command=lambda:press('*'),height=2,width=7).grid(row=3,column=4)
div=Button(suj,fg='black',text='/',bg='pink',command=lambda:press('/'),height=2,width=7).grid(row=4,column=4)
clear=Button(suj,fg='black',text='clear',bg='pink',command=lambda:clea(),height=2,width=7).grid(row=4,column=1)
dec=Button(suj,fg='black',text='.',command=lambda:press('.'),height=2,width=7).grid(row=5,column=0)
equal=Button(suj,fg='black',text='=',bg='pink',command=lambda:e(),height=2,width=7).grid(row=4,column=2)
#configuration for gui window
suj.geometry('250x225')
#starting the gui
suj.mainloop()