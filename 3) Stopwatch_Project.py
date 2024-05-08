import tkinter as tk

root = tk.Tk()
root.title("STOPWATCH")
root.geometry("200x200")

display = tk.Label(root,text="00:00:00")
display.grid(row=0,column=1)
print(display.cget("text"))



stop_btn = tk.Button(root,text="Stop")
stop_btn.grid(row=1,column=1)

reset = tk.Button(root,text="Reset")
reset.grid(row=1,column=2)

def timings(seconds,minutes):
    print(seconds)
    old_data = display.cget("text") 
    b = old_data.split(':')  
    b[-1] = str(seconds)   
    if seconds>=60:
        seconds = 0
        minutes +=  1
        b[-2] = str(minutes) 
    display.config(text=':'.join(b))
    seconds = seconds+1
    if minutes == 2 and seconds == 32:
        return 1
    root.after(200,timings,seconds,minutes)

def starting_function():
    timings(1,0)

start_btn = tk.Button(root,text="Start",command=starting_function)
start_btn.grid(row=1,column=0)


root.mainloop()
