from tkinter import *

def button_clicked():
  miles = int(input.get())
  km = miles * 1.609
  km_label.config(text=f"{km}")



window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Label

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)
km_label = Label(text="0")
km_label.grid(column=1, row=1)

#Button

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=7)
input.grid(column=1, row=0)




window.mainloop()