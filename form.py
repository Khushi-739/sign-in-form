import tkinter
from tkinter import * 
from tkinter import messagebox

m = tkinter.Tk()
m.title("LOGIN")
m.geometry('925x500+300+200')
m.configure(bg="#fff")
m.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    if username=='admin' and password =='1234':
        screen=Toplevel(m)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text='Hello Everyone!',bg='#fff',font=('Arial',50,'bold')).pack(expand=True)
        screen.mainloop()
    elif username!='admin' and password!='1234':
        messagebox.showerror("Invalid","Invalid username and password")
    elif password!='1234':
        messagebox.showerror("Invalid","invalid password")
    elif username!='admin':
        messagebox.showerror("Invalid","invalid username")
        
photo = PhotoImage(file = r"C:\Users\rushi\Downloads\login.png")
Label(m,image=photo,bg='white').place(x=50,y=50)

frame=Frame(m,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text='SIGN_IN',fg='#57a1f8',bg='white',font=('Arial',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'username')

user=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Arial',11))
user.place(x=26,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=286,height=2,bg='black').place(x=25,y=107)

def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=35,fg='black',border=2,bg='white',font=('Arial',11))
code.place(x=26,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
Frame(frame,width=286,height=2,bg='black').place(x=25,y=177)

Button(frame,width=31,pady=7,text='Sign-In',bg='#57a1f8',fg='white',border=0,font=('Arial',11,'bold'),command=signin).place(x=25,y=204)
label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Arial',11))
label.place(x=60,y=270)

sign_up=Button(frame,width=6,text='Sign-Up',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=('Arial',11,'bold'))
sign_up.place(x=215,y=268)



m.mainloop()