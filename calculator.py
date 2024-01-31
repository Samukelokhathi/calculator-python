from tkinter import *
import tkinter.ttk as ttk


window = Tk()

window.title("Calculator")
window.geometry("300x500")


expression = ''

screen = Label(window, bg="white", text="0".rjust(11), font=('Arial', 40, "bold"), justify="right")
screen.place(y=2, relwidth=1, height=50)

def update_screen():
    global screen, expression
    screen.config(text=expression.rjust(9))


def add_to_expression(char):
    global expression
    char = f'{char}'

    if char in ['+', '*', '-', '/', '.'] and expression[-1] in ['+', '*', '-', '/', '.']:
        return


    expression += char

    if expression == '0' + char:
       expression = char

    if expression[0] in ('+', '*', '-', '/'):
        expression = '0'

    if expression[0] in ['.']:
        expression = '0.'
        print(expression)



    update_screen()
    print(expression)


def equalPress():
    global expression
    expression = str(eval(expression))
    print(expression)
    update_screen()

def clear_field():
    global expression
    expression = "0"
    update_screen()


button_9 = Button(window, text='9', command=lambda: add_to_expression(9))
button_9.place(x=150, y=200 + 20, width=60, height=50)

button_8 = Button(window, text='8', command=lambda: add_to_expression(8))
button_8.place(x=80, y=220, width=60, height=50)

button_7 = Button(window, text='7', command=lambda: add_to_expression(7))
button_7.place(x=10, y=200+20, width=60, height=50)

button_4 = Button(window, text="4", command=lambda: add_to_expression(4))
button_4.place(x=10, y=280, width=60, height=50)

button_5 = Button(window, text='5', command=lambda:add_to_expression(5))
button_5.place(x=80, y=280, width=60, height=50)

button_6 = Button(window, text='6', command=lambda: add_to_expression(6))
button_6.place(x=150, y=280, width=60, height=50)

button_1 = Button(window, text='1', command=lambda: add_to_expression(1))
button_1.place(x=10, y=340, width=60, height=60)

button_2 = Button(window, text='2', command=lambda: add_to_expression(2))
button_2.place(x=80, y=340, width=60, height=60)

button_3 = Button(window, text='3', command=lambda: add_to_expression(3))
button_3.place(x=150, y=340, width=60, height=60)

button_0 = Button(window, text='0', command=lambda: add_to_expression(0))
button_0.place(x=80, y=410, width=60, height=50)

button_decimal = Button(window, text='.', command=lambda: add_to_expression('.'))
button_decimal.place(x=150, y=410, width=60, height=50)



divide_btn = Button(window, text="/", command=lambda: add_to_expression('/'))
divide_btn.place(x=220, y=200 + 20, width=60, height=50)

minus_btn = Button(window, text="-", command=lambda: add_to_expression('-'))
minus_btn.place(x=220, y=250 + 30, width=60, height=50)

plus_btn = Button(window, text="+", command=lambda: add_to_expression('+'))
plus_btn.place(x=220, y=300 + 40, width=60, height=60)

times_btn = Button(window, text="*", command=lambda: add_to_expression('*'))
times_btn.place(x=220, y=160, width=60, height=50)

equals_btn = Button(window, text='=', command=equalPress)
equals_btn.place(x=220, y=410, width=60, height=50)

clear_btn = Button(window, text='c', command=clear_field, fg='blue',background='dark gray')
clear_btn.place(x=10, y=410, width=60, height=50)





open_bracket_btn = Button(window, text='(', command=lambda: add_to_expression('('))
open_bracket_btn.place(x=10, y=160, width=60, height=50)

closing_bracket_btn = Button(window, text=')', command=lambda: add_to_expression(')'), width=6, height=3)
closing_bracket_btn.place(x=80, y=160, width=60, height=50)








def delete():
    global expression
    expression = expression[:-1]
    if expression == '':
        print(0)
        expression = '0'

    update_screen()
    print(expression)

delete_btn=Button(window,text="DEL",fg="red",command=delete)
delete_btn.place(x=150, y=160, width=60, height=50)















# def check_if_won():
#     global positions, currentPlayer
#
#     for winPos in winPositions:
#         if all(positions[pos - 1]["player"] == currentPlayer for pos in winPos):
#             messagebox.showinfo("Winner", f"Player {currentPlayer} wins!")
#             window.quit()








window.mainloop()















#
#
#
# import tkinter as tk
#
# expression = ""
# equation = tk.StringVar()
#
#
# def equal():
#     global expression
#     total_sum = str(eval(expression))
#     equation.set(total_sum)
#     expression = ''  # Move this line after equation.set(total_sum) to clear expression
#     update_screen()
#
#
# def button_click(char):
#     global expression
#     expression += char
#     update_screen()
#
#
# def update_screen():
#     entry.delete(0, tk.END)
#     entry.insert(tk.END, expression)

#
# root = tk.Tk()
# root.title("Calculator")
#
# entry = tk.Entry(root, textvariable=equation, font=('Arial', 20))
# entry.place(x=0, y=0, relwidth=1)  # Entry expands horizontally to fill the window
#
# button_texts = [
#     '7', '8', '9', '/',
#     '4', '5', '6', '*',
#     '1', '2', '3', '-',
#     '0', '.', '=', '+'
# ]
#
# row_num = 1
# col_num = 0
#
# for text in button_texts:
#     if text == '=':
#         button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 20), command=equal)
#     else:
#         button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 20),
#                            command=lambda t=text: button_click(t))
#
#     # Calculate button coordinates and size relative to the window
#     button_x = col_num / 4  # Divide by 4 because there are 4 columns
#     button_y = row_num / 5  # Divide by 5 because there are 5 rows
#     button_width = 1 / 4  # 1/4 of the window width
#     button_height = 1 / 5  # 1/5 of the window height
#
#     button.place(relx=button_x, rely=button_y, relwidth=button_width, relheight=button_height)
#
#     col_num += 1
#     if col_num > 3:
#         col_num = 0
#         row_num += 1
#
# root.geometry("400x600")  # Set an initial window size



p = ttk.Progressbar(value=10)
p.pack()
# root.mainloop()
