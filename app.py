import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("500x350")
root.title("Password Manager")

# Text variable
siteName_var = tk.StringVar()
email_var = tk.StringVar()
password_var = tk.StringVar()
 
# utility functions
def resetField():
    siteName_var.set("")
    email_var.set("")
    password_var.set("")

def getEmailAndPassword():
    siteName = siteName_var.get()
    email = email_var.get()
    password = password_var.get()
    msg = "Email: "+email+"\nPassword: "+password

    if(siteName != "" and email != "" and password != ""):
        if(messagebox.askquestion("Check your details", msg) == "yes"):
            with open("passwords.txt","a+") as f:
                f.write(siteName +" | "+ email +" | " + password + "\n")
            resetField()
        else:
            resetField()
    else:
        messagebox.showinfo("Incomplete Details", "Please fill all the required details")


siteNameLabel = tk.Label(root, text="Website name:", font=("Arial",15)).place(x=30, y=50)
siteNameInput = tk.Entry(root, textvariable=siteName_var, width=20, font=('Arial',15)).place(x=250,y=50)

emailLabel = tk.Label(root, text="Email ID:", font=("Arial",15)).place(x=30, y=90)
emailInput = tk.Entry(root, textvariable=email_var, width=20, font=('Arial',15)).place(x=250,y=90)

passwordLabel = tk.Label(root, text="Password:", font=("Arial",15)).place(x=30, y=130)
passwordInput = tk.Entry(root, textvariable=password_var, show="*", width=20, font=('Arial',15)).place(x=250,y=130)

button = tk.Button(root,text="Submit",command=getEmailAndPassword, font=('Arial',10)).place(x=250,y=170)

root.mainloop()