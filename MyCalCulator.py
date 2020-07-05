from tkinter import *

def btnClck(numbers):
    try:
        global operator
        if operator=="error":
            operator=""
        operator= operator + str(numbers)
        text_Input.set(operator)
    except:
        operator="error"
        text_Input.set(operator)
def btbClear():
    global operator
    operator =""
    text_Input.set(operator)
def btnEquals():
    try:
        global operator
        result = str(eval(operator))
        text_Input.set(result)
    except:
        operator = "error"
        text_Input.set(operator)

calc=Tk()
calc.title("Calculator")
operator=""
text_Input = StringVar()
txtDisplay = Entry(calc,font=('arial',20,'bold'),textvariable=text_Input,bd=20,insertwidth=4,
                   bg="powder blue",justify='right').grid(columnspan=4)
btn7=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(7),font=('arial',20,'bold'),text="7").grid(row=1,column=0)
btn8=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(8),font=('arial',20,'bold'),text="8").grid(row=1,column=1)
btn9=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(9),font=('arial',20,'bold'),text="9").grid(row=1,column=2)
btnAddition=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck("+"),font=('arial',20,'bold'),text="+").grid(row=1,column=3)
#============================================================================================================================
btn4=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(4),font=('arial',20,'bold'),text="4").grid(row=2,column=0)
btn5=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(5),font=('arial',20,'bold'),text="5").grid(row=2,column=1)
btn6=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(6),font=('arial',20,'bold'),text="6").grid(row=2,column=2)
btnSubtract=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck("-"),font=('arial',20,'bold'),text="-").grid(row=2,column=3)
#============================================================================================================================
btn1=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(1),font=('arial',20,'bold'),text="1").grid(row=3,column=0)
btn2=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(2),font=('arial',20,'bold'),text="2").grid(row=3,column=1)
btn3=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck(3),font=('arial',20,'bold'),text="3").grid(row=3,column=2)
btnMultiplication=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck("*"),font=('arial',20,'bold'),text="*").grid(row=3,column=3)
#============================================================================================================================
btn0=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",font=('arial',20,'bold'),text="0").grid(row=4,column=0)
btnClear=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=btbClear,font=('arial',20,'bold'),text="c").grid(row=4,column=1)
btnEquals=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=btnEquals,font=('arial',20,'bold'),text="=").grid(row=4,column=2)
btnDivision=Button(calc,padx=16,pady=16,bd=8,fg="black",bg="powder blue",command=lambda:btnClck("/"),font=('arial',20,'bold'),text="/").grid(row=4,column=3)
#============================================================================================================================
calc.mainloop()
