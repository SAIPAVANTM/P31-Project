import tkinter as tk

root = tk.Tk()

root.title("GUVI P31")
root.geometry("600x600")

entry = tk.Entry(root)
entry.grid(row=0,column=1)


def proper_fun(a):
    old_data = entry.get()
    new_data = old_data + str(a)
    entry.delete('0',tk.END)
    entry.insert('0',new_data)

c = 1
for i in range(1,4):
    for j in range(3):
        tk.Button(root,text=c,command= lambda j=c: proper_fun(j)).grid(row=i,column=j)
        c = c+1

operator = ['+','-','*','/']
for i in range(len(operator)):
    tk.Button(root,text=operator[i],command= lambda j=operator[i]: proper_fun(j)).grid(row=i+1,column=3)

def equalfuntion():
    data = entry.get()
    output = eval(data)
    entry.delete('0',tk.END)
    entry.insert(0,output)


equal_to = tk.Button(root,text="=",command=equalfuntion).grid(row=4,column=2)

root.mainloop()
