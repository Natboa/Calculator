import tkinter
from tkinter import *
import ast

root = Tk()

root.title("Calculator App")

#Entry, the line on the top
display = Entry(root)
display.grid(row = 1, columnspan = 6)

#the typed buttons are added to the line on top
i = 0
def get_number(num):
    global i
    display.insert(i, num)
    i+=1



#seperate function that includes incrementing i with the length of the operator
def get_operation(operator):
    global i
    display.insert(i, operator)
    i += len(operator)

def delete_num():
    global i
    display.delete(i - 1, END)
    i -= 1

def clear_display():
    display.delete(0, END)
    global i
    i = 0

def calculate():
    global i
    entire_string = display.get()
    try:
        node = ast.parse(entire_string, mode ="eval")
        result = eval(compile(node, '<string', 'eval'))
        clear_display()
        display.insert(0,result)
        i = len(display.get())
    except Exception:
        clear_display()
        display.insert(0,"Error")

#creating the number buttons
count = 1
for x in range(3):
    for y in range(3):
        #using lambda so the function is called only when the button is clicked and not in creation of button (callback function)
        button = Button(root, text = count, width = 3, height = 2, command = lambda num = count: get_number(num))
        button.grid(row = x + 2, column = y)
        count+=1
button0 = Button(root, text = 0, width = 3, height = 2, command = lambda :get_number(0))
button0.grid(row = 5, column = 1)

#weeks button
def weeks():
    clear_display()
    label = tkinter.Label(root, text = "Please enter your age")
    label.grid(row = 7, columnspan = 6)
    buttonW = Button(root, text="Send", width=4, height=2, command = lambda :weeks_calculate())
    buttonW.grid(row=8, columnspan = 6)

def weeks_calculate():
    try:
        age = int(display.get())
        if age<0 or 100<age:
            label = tkinter.Label(root, text="incorrect age, try again")
            label.grid(row=9, columnspan=6)
            label.after(3000, label.destroy)
            clear_display()
        else:
            weeks_left = (80 - age) * 52
            label2 = tkinter.Label(root, text=f"on average,\n you have {weeks_left} weeks left to live.")
            label2.grid(row=112, columnspan=20)
    except ValueError:
        label = tkinter.Label(root, text="Please enter a valid number")
        label.grid(row=9, columnspan=6)
        label.after(3000, label.destroy)
        clear_display()






#creating the operation buttons
operations = ['+','-','*','/','*3.14','%','(','^',')','**2']
count = 0
for x in range(4):
    for y in range(3):
        if count < len(operations):
            button = Button(root, text=operations[count], width=3, height=2, bg="grey", command = lambda operator = operations[count]: get_operation(operator))
            button.grid(row=x + 2, column=y + 3)
            count+=1

#clear button
buttonCLR = Button(root, text = "CLR", width = 3, height = 2, bg = "orange", command = lambda :clear_display())
buttonCLR.grid(row = 5, column = 0)

#equals button
buttonEQ = Button(root, text = "=", width = 3, height = 2, command = lambda :calculate())
buttonEQ.grid(row = 5, column = 2)

#delete button
buttonDEL = Button(root, text = "DEL", width = 3, height = 2, bg = "orange", command = lambda :delete_num())
buttonDEL.grid(row = 5, column = 4)

#weeks button
buttonDEL = Button(root, text = "⛧",width = 3, height = 2, bg = "dark red", command = lambda :weeks())
buttonDEL.grid(row = 5, column = 5)


root.mainloop()