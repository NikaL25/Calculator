from tkinter import *
user_expression = ''


def press(number):
    global user_expression
    user_expression += str(number)
    equation.set(user_expression)

def evaluate_expression():
    try:
        global user_expression
        result = str(eval(user_expression))
        equation.set(result)
        user_expression = ""
    except:
        equation.set("Syntax Error")
        user_expression = ""
        
def clear_expression():
    global user_expression
    user_expression = ''
    equation.set('')


root = Tk()
root.configure(background="grey")
root.title('Calculator by codewithcurious.com')
root.geometry('280x280')

equation = StringVar()

text_entry_box = Entry(root, textvariable=equation, width=20)
text_entry_box.grid(columnspan=4, ipadx=100)

# Define buttons for digits and operators
buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9', 
         '0',
    '+', '-', '*',
    '/', '=', 'Clear'
]

row_num, col_num = 2, 0
for button_text in buttons:
    button = Button(root, text=f' {button_text} ', fg='black', bg='#8f8f8f', height=2, width=7)
    if button_text == '=':
        button.config(command=evaluate_expression)
    elif button_text == 'Clear':
        button.config(command=clear_expression)
    else:
        button.config(command=lambda b=button_text: press(b))
    button.grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 2:
        col_num = 0
        row_num += 1


root.mainloop()
