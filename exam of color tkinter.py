from tkinter import *
from tkinter import messagebox
import random
root = Tk()
colors = ['Yellow','Blue','Green','Brown','Gray','Black','White','Orange','Red','Pink']
time = 60
score = 0
#============start=================
def start(event):
    global score
    if time == 60 :
        score +=1
        Time()
    Color()
#============color==================
def Color():
    global time
    global score
    if time > 0:
        Entry_color.focus_set()
        if Entry_color.get().lower() == colors[1].lower():
            score +=1
        else:
            score -=1
        Entry_color.delete(0,END)
        random.shuffle(colors)            
        label_color.config(fg=str(colors[1]),text=str(colors[0]))
        label_info.config(text='score :' + str(score))
#============= count or time ==============
def Time ():
    global time
    if time > 0 :
        time -=1
        label_time.config(text='time :' + str(time))
        label_time.after(1000 , Time)
        if time == 0 :
            messagebox.showerror('ERROR','your time is ended !!!!!!!! if you want play again you should click the right button on mouse!!!!')
#============reset====================
def reset(event):        
    global time
    global score
    score = 0
    time = 60
    label_info.config(text='if you want to start you should use Enter key' , font=('tahoma',12,'bold'))
    label_time.config(text='time :' + str(time), font=('tahoma',12,'bold'))
    label_color.config(text='this is place for color!!!!', font=('tahoma',12,'bold'),fg='black')
#===========entry=====================
Entry_color = Entry(root,bg='yellow',fg = 'black')
Entry_color.place(x = 140 , y = 100)
#============label================
label_info = Label(root,text='if you want to start you should use Enter key' , font=('tahoma',12,'bold'))
label_time = Label(root,text='time :' + str(time), font=('tahoma',12,'bold'))
label_color = Label(root,text='this is place for color!!!!', font=('tahoma',12,'bold'))
label_info.place(x = 0 , y = 0)
label_time.place(x =0 , y = 25)
label_color.place(x =0 , y = 50)
#=============window==============
root.config(bg='purple')
root.resizable(0,0)
root.title('Exam of color')
window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = screen_width - window_width * 2
y = screen_height - window_height * 3
root.geometry('{}x{}-{}-{}'.format(window_width, window_height,x,y))
#===============Bind=============
root.bind('<Return>',start)
root.bind('<Button-3>',reset)
#==============loop==============
root.mainloop()
