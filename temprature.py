
import tkinter

root = tkinter.Tk()  # creating a window
root.title("Temperature Converter")  # setting the size of the window
root.config(bg="#082530")  # setting the background color for the window

l1 = tkinter.LabelFrame(root, text="Celsius to Farenheit", padx=20, pady=20, bd=4, bg='#0b3141')
l1.grid(row=2, column=0)

e1 = tkinter.Entry(l1, state="disable", bd=4, bg="light blue")
e1. grid(row=4, column=0)

# defining function that will activate Celsius to Fahrenheit
def cel_active():
    e2.configure(state='disable')
    e1.configure(state="normal")


btn_active = tkinter.Button(root, text="Active -Celsius to Fahrenheit", command=cel_active, bd=4, bg='#1e8bb7')
btn_active.grid(row=6, column=0)

l2 = tkinter.LabelFrame(root, text="Fahrenheit to Celsius", padx=20, pady=20, bd=4, bg='#0b3141')
l2.grid(row=2, column=5)

e2 = tkinter.Entry(l2, state="disable", bd=4,)
e2.grid(row=4, column=5)

# defining function that will activate Fahrenheit to Celsius
def far_active():
    e1.configure(state="disable")
    e2.configure(state="normal")


btn_active1 =tkinter.Button(root, text="Active -Fahrenheit to Celsius", command=far_active, bd=4, bg='#1e8bb7')
btn_active1.grid(row=6, column=5)


def close():
    root.destroy()

# defining function that will exit the window/ program

exit_btn = tkinter.Button(text="Exit Program", command=close, bd=4, bg='#1e8bb7')
exit_btn.grid(row=9, column=6)

# defining function for converting fahrenheit to celsius
def convert_C():
    if e1["state"] == "normal" and e1.get() != "":
        celsius = float(e1.get())
        fahrenheit = (celsius*9/5)+32
        result_entry.insert(0, str(fahrenheit))

# defining function for converting celsius to fahrenheit
def convert_f():
    if e2["state"] == "normal" and e2.get() != "":
        fahrenheit = float(e2.get())
        celsius = (fahrenheit-32)*5/9
        result_entry.insert(0, celsius)


result_btn = tkinter.Button(root, text="Convert C-F", command=convert_C, bd=4, bg='#1e8bb7')
result_btn.grid(row=7, column=2)

result_btn2 = tkinter.Button(root, text="Convert F-C", command=convert_f, bd=4, bg='#1e8bb7')
result_btn2.grid(row=7, column=4)

result_entry = tkinter.Entry(root, bg="light blue", bd=4)
result_entry.grid(row=8, column=2)

# defining function that will delete the figure in the input_boxes
def clear():
    e1.delete(0)
    e2.delete(0)
    result_entry.delete(0)


clear_btn = tkinter.Button(root, text="Clear", command=clear, bd=4, bg='#1e8bb7')
clear_btn.grid(row=8, column=6)

root.mainloop()
