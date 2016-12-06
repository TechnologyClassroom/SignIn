"""A re-written signin.py that uses multiple classes to build different windows
for each different feature: upload a .csv file, sign-in for existing members,
registration for new members."""


import sqlite3, math

try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    import tkinter.ttk

import time
from datetime import date

from tkinter import filedialog 

#main window that prompts user to upload a .csv file to be imported into a database table 
class FirstWindow():
    def __init__(self, master):

        self.master = master
        self.frame = Frame(master)

        self.build_window()

        self.frame.grid()

        menubar = Menu(master)
        master['menu'] = menubar

        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(menu=menu_file, label="File")

    def build_window(self):
        Label(self.frame, text="Welcome! Upload your existing Registration Log!\n").grid(row=0)

        upload = Button(self.frame, text="Upload", command=self.upload_file).grid(row=1, sticky=W)
        skip = Button(self.frame, text="Skip", command = self.new_window1).grid(row=1, column=1, sticky=W)


    def upload_file(self):
        self.file = filedialog.askopenfile(mode='r', filetypes=[("Csv file", "*.csv")], title='Select File')
        print(self.file)
        
    def new_window1(self):
        root2 = Toplevel(self.master)
        myGUI = SecondWindow(root2)
        
    def quit(self):
        master.destroy()


class SecondWindow():
    Users = sqlite3.connect('registration')
    global curr
    curr = Users.cursor()
        
    def __init__(self, master):

        self.entry2 = StringVar()
        self.entry3 = StringVar()
        self.entry4 = StringVar()
        
        self.master = master
        self.frame = Frame(master)

        self.build_window()

        self.frame.grid()
    
        menubar = Menu(master)
        master['menu'] = menubar

        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(menu=menu_file, label="File")

    def build_window(self):
    
        Label(self.frame, text="Welcome! Sign in here!", anchor=CENTER).grid(row=0, columnspan=2)
        global e
        e = Entry(self.frame)
        e.grid(row=1, columnspan=2)
        e.insert(0, 'Select your name')

        global lb
        lb = Listbox(self.frame, height=4)
        yscroll = Scrollbar(self.frame)
        yscroll = Scrollbar(command=lb.yview, orient=VERTICAL)
        yscroll.grid(row=3)
        lb.configure(yscrollcommand = yscroll.set)

        curr.execute('SELECT FirstName, LastName FROM "ClubhouseUsers"')
        for row in curr:
            lb.insert(END, row)
        lb.grid(row=3, columnspan=2)
        lb.bind('<Return>', self.get_list)

        button1 = Button(self.frame, text="Sign in!", command=self.addUser)
        button1.grid(row=4, columnspan=2)

        Label(self.frame, text="If your name is missng from the list, \n write your first and last name here.\nIf you are not a member, please register.").grid(row=5, columnspan=2)
        e2 = Entry(self.frame, textvariable=self.entry2)
        e2.grid(row=6, columnspan=2)
        e2.insert(0, 'Ex: Briana Mayes')
        button2 = Button(self.frame, text="Add Name", command=self.addItem)
        button2.grid(row = 7)
        button3 = Button(self.frame, text="Register", command=self.new_window2)
        button3.grid(row=7, column=1)

    def get_list(self, event):
        #get selected line index
        index = lb.curselection()[0]
        #get line's text
        seltext = lb.get(index)
        e.delete(0,50)
        e.insert(0, seltext)

        
    def addUser(self):
        content = e.get()
        user = content.split()
        today = time.strftime("%x" + " " + "%I:%M:%S")
        today = today.split()
        curr.execute('INSERT INTO SignInUsers (FirstName, LastName, Date, Time) VALUES (?,?,?,?)', (user[0], user[1], today[0], today[1]))
        tkinter.messagebox.showinfo("Sign in", "You have successfully signed in")
        
    def addItem(self):
        lb.insert(END, e2.get())
                         
    def new_window2(self):
        root3 = Toplevel(self.master)
        myGUI = ThirdWindow(root3)

    def quit(self):
        master.destroy()
        Users.commit()
        Users.close()

class ThirdWindow():
    def __init__(self, master):
        self.master = master
        self.frame = Frame(master)

        self.build_window()

        self.frame.grid()

        menubar = Menu(master)
        master['menu'] = menubar

        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)

        menubar.add_cascade(menu=menu_file, label="File")

    def build_window(self):
        Label(self.frame, text="First Name:").grid(row=0, sticky=W)
        Label(self.frame, text="Last Name:").grid(row=1, sticky=W)
        Label(self.frame, text="Date of Birth:").grid(row=2, sticky=W)
        Label(self.frame, text="Gender:").grid(row=3, sticky=W)
        Label(self.frame, text="Race/Ethnicity:").grid(row=4, sticky=W)
        Label(self.frame, text="Street Address:").grid(row=5, sticky=W)
        Label(self.frame, text="City:").grid(row=6, sticky=W)
        Label(self.frame, text="State:").grid(row=7, sticky=W)
        Label(self.frame, text="Postal Code:").grid(row=8, sticky=W)
        Label(self.frame, text="Country:").grid(row=9, sticky=W)
        Label(self.frame, text="Phone:").grid(row=10, sticky=W)
        Label(self.frame, text="Email:").grid(row=10, sticky=W)
        Label(self.frame, text="School:").grid(row=11, sticky=W)
        Label(self.frame, text="Parent 1 First Name:").grid(row=12, sticky=W)
        Label(self.frame, text="Parent 1 Last Name:").grid(row=13, sticky=W) 
        Label(self.frame, text="Parent 1 Phone Number:").grid(row=14, sticky=W)
        Label(self.frame, text="Parent 1 Email:").grid(row=15, sticky=W)
        Label(self.frame, text="Parent 2 First Name:").grid(row=16, sticky=W)
        Label(self.frame, text="Parent 2 Last Name:").grid(row=17, sticky=W)
        Label(self.frame, text="Parent 2 Phone Number:").grid(row=18, sticky=W)
        Label(self.frame, text="Parent 2 Email:").grid(row=19, sticky=W)

        e3 = Entry(self.frame, textvariable=entry3).grid(row=0, column=1)
        e4 = Entry(self.frame, textvariable=entry4).grid(row=1, column=1)
        e5 = Entry(self.frame).grid(row=2, column=1)
        e6 = Entry(self.frame).grid(row=3, column=1)
        e7 = Entry(self.frame).grid(row=4, column=1)
        e8 = Entry(self.frame).grid(row=5, column=1)
        e9 = Entry(self.frame).grid(row=6, column=1)
        e10 = Entry(self.frame).grid(row=7, column=1)
        e11 = Entry(self.frame).grid(row=8, column=1)
        e12 = Entry(self.frame).grid(row=9, column=1)
        e13 = Entry(self.frame).grid(row=10, column=1)
        e14 = Entry(self.frame).grid(row=11, column=1)
        e15 = Entry(self.frame).grid(row=12, column=1)
        e16 = Entry(self.frame).grid(row=13, column=1)
        e17 = Entry(self.frame).grid(row=14, column=1)
        e18 = Entry(self.frame).grid(row=15, column=1)
        e19 = Entry(self.frame).grid(row=16, column=1)
        e20 = Entry(self.frame).grid(row=17, column=1)
        e21 = Entry(self.frame).grid(row=18, column=1)
        e22 = Entry(self.frame).grid(row=19, column=1)

        button4 = Button(self.frame, text = "Submit", command=registerNewUser).grid(row = 20,column=0)
        button5 = Button(self.frame, text= "Cancel", command=self.quit).grid(row=20, column=1)

        def quit(self):
            master.destroy()

if __name__ == "__main__":
    master = Tk()
    app = FirstWindow(master)
    master.mainloop()
