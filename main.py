import tkinter as tk
from tkinter import StringVar

class Model:
    def __init__(self):
        self.text = ""

class ViewModel:
    def __init__(self, model):
        self.model = model
        self.observable_text = StringVar()

    def update_model(self, new_text):
        self.model.text = new_text
        self.observable_text.set(new_text)

def on_entry_change(*args):
    vm.update_model(entry_var.get())

root = tk.Tk()
root.title("MVVM Demo")

model = Model()
vm = ViewModel(model)

entry_var = StringVar()
entry_var.trace_add('write', on_entry_change)

entry = tk.Entry(root, textvariable=entry_var)
entry.pack()

label = tk.Label(root, textvariable=vm.observable_text)
label.pack()

root.mainloop()
