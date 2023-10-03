// MY PYTHON EDITOR IS BROKEN :(
import hashlib 
from tkinter import *
from tkinter import messagebox
from firebase import firebase

firebase = firebase.FirebaseApplication("/",None)
registration_window = Tk()
registration_window.title("REGISTER")
registration_window.geometry("400x400")
registration_window.configure(bg="cyan")

login_username_entry=""
login_password_entry=""

def login(): 
    print("Login Function!")
    global login_username_entry
    global login_password_entry
    username=login_username_entry.get()
    password=login_password_entry.get()
    encrypted_password=hashlib.md5(password.encode())
    hexadec_password=encrypted_password.hexdigest()
    get_password=firebase.get("/", username)
    print(hexadec_password)
    if (get_password != None):
        if(get_password == hexadec_password):
            messagebox.showinfo("Logged In","Successfully Loged In :)")
        else: 
            messagebox.showinfo("Error","Please Check Your Password!")
    else:
        messagebox.showerror("Error","User not registered! \n Get yourself registered first to login")
    
def register(): 
    print("register function")
    username=username_entry.get()
    password=password_entry.get()
    encoded= hashlib.md5(password.encode())
    encode = encoded.hexdigest()
    print(encode)
    firebase.put("/",username,encode)
    messagebox.showinfo("Registered","User is registered: ")
    
def login_window():
    login_window = Tk()
    login_window.title("LOGIN")
    login_window.geometry("400x400")
    login_window.configure(bg="MediumOrchid")
    
    global login_username_entry
    global login_password_entry
    registration_window.destroy()
    
    log_heading_label = Label(login_window, text="Log In" ,fg="Orange", font = 'arial 20 bold',bg="White")
    log_heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)
    
    login_username_label = Label(login_window, text="Username : " , fg="Orange",font = 'arial 13 bold',bg="White")
    login_username_label.place(relx=0.3,rely=0.4, anchor=CENTER)
    
    login_username_entry = Entry(login_window)
    login_username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)
    
    login_password_label = Label(login_window, text="Password : " , font = 'verdana',bg="White",fg="Orange")
    login_password_label.place(relx=0.3,rely=0.5, anchor=CENTER)
    
    login_password_entry = Entry(login_window)
    login_password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)
    
    btn_login = Button(login_window, text="Log In" , font = 'verdana , command=login, relief=FLAT,bg="white",fg="orange")
    btn_login.place(relx=0.5,rely=0.65, anchor=CENTER)
    
    login_window.mainloop()
    
    
heading_label = Label(registration_window, text="Register" , font = 'verdana',bg="darkorchid",fg="DarkGoldenrod1")
heading_label.place(relx=0.5,rely=0.2, anchor=CENTER)

username_label = Label(registration_window, text="Username : " , font = 'verdana',bg="darkorchid",fg="DarkGoldenrod1")
username_label.place(relx=0.3,rely=0.4, anchor=CENTER)

username_entry = Entry(registration_window)
username_entry.place(relx=0.6,rely=0.4, anchor=CENTER)

password_label = Label(registration_window, text="Password :  " , font = 'verdana',bg="darkorchid",fg="DarkGoldenrod1")
password_label.place(relx=0.3,rely=0.5, anchor=CENTER)

password_entry = Entry(registration_window)
password_entry.place(relx=0.6,rely=0.5, anchor=CENTER)

btn_reg = Button(registration_window, text="Sign Up" , font = 'verdaba' ,command=register, fg="DarkGoldenrod1",padx=10,bg="DarkOrchid4")
btn_reg.place(relx=0.5,rely=0.75, anchor=CENTER)

btn_login_window = Button(registration_window, text="Log In" , font = 'verdana' ,  command=login_window,bg="DarkOrchid4",fg="DarkGoldenrod1")

btn_login_window.place(relx=0.9,rely=0.06, anchor=CENTER)
registration_window.mainloop()
