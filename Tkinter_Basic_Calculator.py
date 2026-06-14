import tkinter as tk

root = tk.Tk()
root.title('Calculator')
root.geometry('100x180')

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=3, sticky="ew") # nsew north south.....

numbers = [7,8,9,
           4,5,6,
           1,2,3,
           0, "+", " ",
           "-","*",'/',]


def button_click(num): 
    entry.insert(tk.END, str(num))

def clear(): 
    entry.delete(0, tk.END)

def equal():
    expression = entry.get()
    result = eval(expression)
    entry.delete(0, tk.END)
    entry.insert(0, str(result))

for i, num in enumerate(numbers):
    tk.Button(root, text=str(num), command = lambda n = num: button_click(n)).grid(
        row = i//3 + 1, column = i%3, ipadx = 10)
    

btn_equal = tk.Button(root, text = "=", command = equal).grid(row = 4, column = 2, ipadx = 10)

btn_clear = tk.Button(root, text = "C", command = clear).grid(columnspan = 3, sticky ='ew')
root.mainloop()

