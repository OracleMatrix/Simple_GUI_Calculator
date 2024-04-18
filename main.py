from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from customtkinter import *

root = CTk()
root.title('Calculator')
root.geometry('400x400')
root.resizable(False, False)


def calc_task():
    expression = textbox.get(1.0, 'end-1c')
    try:
        result = eval(expression)
        textbox.delete(1.0, 'end')
        textbox.insert('end', str(result))
    except Exception as e:
        textbox.delete(1.0, 'end')
        messagebox.showerror("Error", "Invalid Input")


def calculate():
    button1.configure(command=lambda: textbox.insert(END, "1"))
    button2.configure(command=lambda: textbox.insert(END, "2"))
    button3.configure(command=lambda: textbox.insert(END, "3"))
    button4.configure(command=lambda: textbox.insert(END, "4"))
    button5.configure(command=lambda: textbox.insert(END, "5"))
    button6.configure(command=lambda: textbox.insert(END, "6"))
    button7.configure(command=lambda: textbox.insert(END, "7"))
    button8.configure(command=lambda: textbox.insert(END, "8"))
    button9.configure(command=lambda: textbox.insert(END, "9"))
    button0.configure(command=lambda: textbox.insert(END, "0"))
    button_dot.configure(command=lambda: textbox.insert(END, "."))
    button_clear.configure(command=lambda: textbox.delete(1.0, END))
    button_plus.configure(command=lambda: textbox.insert(END, " + "))
    button_minus.configure(command=lambda: textbox.insert(END, " - "))
    button_multiply.configure(command=lambda: textbox.insert(END, " * "))
    button_divide.configure(command=lambda: textbox.insert(END, " / "))
    button_equal.configure(command=calc_task)


textbox = CTkTextbox(root, width=300, height=60, font=('Helvetica', 20), corner_radius=15)
textbox.pack(pady=5, padx=5)

button1 = CTkButton(root, text="1", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button2 = CTkButton(root, text="2", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button3 = CTkButton(root, text="3", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button4 = CTkButton(root, text="4", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button5 = CTkButton(root, text="5", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button6 = CTkButton(root, text="6", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button7 = CTkButton(root, text="7", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button8 = CTkButton(root, text="8", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button9 = CTkButton(root, text="9", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button0 = CTkButton(root, text="0", width=90, height=50, corner_radius=20, fg_color='white', text_color='black',
                    hover_color='#cce2ea', command=calculate)
button_dot = CTkButton(root, text=".", width=90, height=50, corner_radius=20, fg_color="gray", hover_color='#5b6b71',
                       command=calculate)
button_clear = CTkButton(root, text="C", width=90, height=50, corner_radius=20, fg_color="gray", hover_color='#5b6b71',
                         command=calculate)
button_plus = CTkButton(root, text="+", width=70, height=50, corner_radius=20, command=calculate)
button_equal = CTkButton(root, text="=", width=380, height=50, corner_radius=20, command=calculate)
button_multiply = CTkButton(root, text="*", width=70, height=50, corner_radius=20, command=calculate)
button_divide = CTkButton(root, text="/", width=70, height=50, corner_radius=20, command=calculate)
button_minus = CTkButton(root, text="-", width=70, height=50, corner_radius=20, command=calculate)

button7.place(relx=0.04, rely=0.2)
button8.place(relx=0.29, rely=0.2)
button9.place(relx=0.54, rely=0.2)
button4.place(relx=0.04, rely=0.360)
button5.place(relx=0.29, rely=0.360)
button6.place(relx=0.54, rely=0.360)
button1.place(relx=0.04, rely=0.52)
button2.place(relx=0.29, rely=0.52)
button3.place(relx=0.54, rely=0.52)
button_dot.place(relx=0.04, rely=0.68)
button0.place(relx=0.29, rely=0.68)
button_clear.place(relx=0.54, rely=0.68)
button_plus.place(relx=0.79, rely=0.2)
button_minus.place(relx=0.79, rely=0.360)
button_multiply.place(relx=0.79, rely=0.52)
button_divide.place(relx=0.79, rely=0.68)
button_equal.place(relx=0.03, rely=0.84)

root.bind("1", lambda e: textbox.insert(END, "1"))
root.bind("2", lambda e: textbox.insert(END, "2"))
root.bind("3", lambda e: textbox.insert(END, "3"))
root.bind("4", lambda e: textbox.insert(END, "4"))
root.bind("5", lambda e: textbox.insert(END, "5"))
root.bind("6", lambda e: textbox.insert(END, "6"))
root.bind("7", lambda e: textbox.insert(END, "7"))
root.bind("8", lambda e: textbox.insert(END, "8"))
root.bind("9", lambda e: textbox.insert(END, "9"))
root.bind("0", lambda e: textbox.insert(END, "0"))
root.bind(".", lambda e: textbox.insert(END, "."))
root.bind("+", lambda e: textbox.insert(END, "+"))
root.bind("-", lambda e: textbox.insert(END, "-"))
root.bind("*", lambda e: textbox.insert(END, "*"))
root.bind("/", lambda e: textbox.insert(END, "/"))
root.bind("<Return>", lambda e: calc_task())

root.mainloop()
