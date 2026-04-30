import tkinter as tk

#function to add numbers
def add_numbers():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1+num2
    result_label.config(text="result:"+str(result))

#create window
root=tk.Tk()
root.title("Addition using Labels")
root.geometry("300x200")

#labels and entry boxes
label1=tk.Label(root,text="enter first number:")
label1.pack()

entry1=tk.Entry(root)
entry1.pack()

label2=tk.Label(root,text="enter second number:")
label2.pack()

entry2=tk.entry(root)
enrty2.pack()

#Button
add_button=tk.Button(root,text="add".command=add_numbers)
add_button.pack()

#result label
result_label=tk.Label(root,text="result:")
result_label.pack()

#Run the GUI
root.mainloop()
