from tkinter import *

calc= Tk()
calc.title("Antony's calculator")
calc.geometry("350x475")
calc.configure(bg= "#2067F1")
calc.resizable(False, False)
calc.iconbitmap("calc.ico")
expression= ""
equation= StringVar()
equation.set("0")

def equalpress():
    try:
        global expression
        total= str(eval(expression))
        equation.set(total)
        expression=""
    except:
        equation.set("Error")
        expression= ""


def press(num):
    global expression
    expression= expression+str(num)
    equation.set(expression)

def clear():
    global expression
    expression=""
    equation.set("0")

button_frame= Frame(calc,bg="#359AF0")
button_frame.pack()

display_panel= Entry(button_frame, textvariable= equation, justify="right")
button1= Button(button_frame, text= "1", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(1))
button2= Button(button_frame, text= "2", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(2))
button3= Button(button_frame, text= "3", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(3))
button4= Button(button_frame, text= "4", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(4))
button5= Button(button_frame, text= "5", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(5))
button6= Button(button_frame, text= "6", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(6))
button7= Button(button_frame, text= "7", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(7))
button8= Button(button_frame, text= "8", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(8))
button9= Button(button_frame, text= "9", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(9))
button10= Button(button_frame, text= "0", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press(0))
button11= Button(button_frame, text= "+", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press("+"))
button12= Button(button_frame, text= "-", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press("-"))
button13= Button(button_frame, text= "*", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press("*"))
button14= Button(button_frame, text= "/", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press("/"))
decimal_button= Button(button_frame, text= ".", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= lambda:press("."))
equal_button= Button(button_frame, text= "=", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 36, height= 3, command= equalpress)
clear_button= Button(button_frame, text= "AC", font= ("times new roman",12), relief= "ridge", borderwidth= 1, bg= "#22EBB0", width= 8, height= 3, command= clear)


display_panel.grid(row=0,column= 0, columnspan= 4, ipadx= 100, ipady= 20, pady= 30)

button1.grid(row=1,column= 0)
button2.grid(row=1,column= 1)
button3.grid(row=1,column= 2)
button11.grid(row=1,column= 3)

button4.grid(row=2,column= 0)
button5.grid(row=2,column= 1)
button6.grid(row=2,column= 2)
button12.grid(row=2,column= 3)

button7.grid(row=3,column= 0)
button8.grid(row=3,column= 1)
button9.grid(row=3,column= 2)
button13.grid(row=3,column= 3)

button10.grid(row=4,column= 0)
decimal_button.grid(row=4,column= 1)
clear_button.grid(row=4,column= 2)
button14.grid(row=4,column= 3)

equal_button.grid(row=5,column=0, columnspan= 4)

calc.mainloop()

