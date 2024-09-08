from tkinter import *

def btnclick(number):
    global val
    val = val + str(number)
    data.set(val)

def btnclear():
    global val
    val = ""
    data.set("")

def btnEquals():
    global val
    try:
        result = str(eval(val))
        data.set(result)
    except Exception as e:
        data.set("Error")
        val = ""

root = Tk()
root.title("SIMPLE CALCULATOR")
root.geometry("500x500")
val = ""
data = StringVar()

display = Entry(root, textvariable=data, bd=29, justify="right", bg="powder blue", font=("arial", 20))
display.grid(row=0, columnspan=4)

btn7 = Button(root, text="7", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(7))
btn7.grid(row=1, column=0)
btn8 = Button(root, text="8", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(8))
btn8.grid(row=1, column=1)
btn9 = Button(root, text="9", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(9))
btn9.grid(row=1, column=2)
btn_add = Button(root, text="+", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick('+'))
btn_add.grid(row=1, column=3)

btn4 = Button(root, text="4", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(4))
btn4.grid(row=2, column=0)
btn5 = Button(root, text="5", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(5))
btn5.grid(row=2, column=1)
btn6 = Button(root, text="6", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(6))
btn6.grid(row=2, column=2)
btn_sub = Button(root, text="-", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick('-'))
btn_sub.grid(row=2, column=3)

btn1 = Button(root, text="1", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(1))
btn1.grid(row=3, column=0)
btn2 = Button(root, text="2", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(2))
btn2.grid(row=3, column=1)
btn3 = Button(root, text="3", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(3))
btn3.grid(row=3, column=2)
btn_mul = Button(root, text="*", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick('*'))
btn_mul.grid(row=3, column=3)

btnC = Button(root, text="C", font=("arial", 12, "bold"), bd=12, height=2, width=6, bg="#e74c3c", fg="white", command=btnclear)
btnC.grid(row=4, column=0)
btn0 = Button(root, text="0", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick(0))
btn0.grid(row=4, column=1)
btn_equal = Button(root, text="/", font=("arial", 12, "bold"), bd=12, height=2, width=6, command=lambda: btnclick('/'))
btn_equal.grid(row=4, column=2)
btn_div = Button(root, text="=", font=("arial", 12, "bold"), bd=12, height=2, width=6, bg="#2ecc71", fg="white", command=btnEquals)
btn_div.grid(row=4, column=3)

root.mainloop()
