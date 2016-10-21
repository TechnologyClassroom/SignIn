# Sign In Software

# Michael McMahon

# This INCOMPLETE program allows people to sign in.

# To help develop this program, install python, open the file in IDLE, make changes, save, and press F5.  Alternatively, install python, open a terminal, edit signin.py with the text editor of your choice, and run python signin.py.

# Requirements
# Allow people to sign in.
# Offline
# If more than 3 are signed within 3 seconds, undo previous actions.
# Search by first or last name
# Add suggestion for a name


# Load Tkinter GUI library, SQLite database, and math for statistics.
import sqlite3, math

# Load GUI library tkinter and ttk to improve the appearance of tkinter.  Try importing Tkinter for Python 2.  If there is an error, import tkinter for Python 3.
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    import tkinter.ttk

class AllWidgets():
    def __init__(self, root):
    
        self.frame = Frame(root)
        
        self.build_window()
        
        self.frame.pack()
        
        menubar = Menu(root)
        root['menu'] = menubar
        
        menu_file = Menu(menubar)
        menu_file.add_command(label="Quit", command=self.quit)
        
        menubar.add_cascade(menu=menu_file, label='File')
        
        
    def build_window(self):
        # Add a picture
        p = PhotoImage(file="image.gif")
        l=Label(self.frame, image=p)
        l.image = p
        l.pack(side=TOP)

        # Add text
        Label(self.frame, text="Welcome!  Sign In here!\n").pack(side=TOP)
        
        # Add search box
        Entry(self.frame, text="Entry").pack(side=TOP)

        # Add list of names
        lb = Listbox(self.frame, height=4)
        lb.pack(side=TOP)
        for x in ('Name 1', 'Name 2', 'Name 3', 'Name 4'):
            lb.insert('end', x)

        # Add button
        Button(self.frame, text="Sign In").pack(side=TOP)

        # For people that are not in the list, they can write their first and last name here.  This will be added to a textfile instead of the database.
        Label(self.frame, text="If your name is missing from the list,\nwrite your first and last name here.").pack(side=TOP)
        
        # Add Text box
        t = Text(self.frame, height=2, width=30)
        t.pack(side=TOP)
        t.insert(END, "Example: Michael McMahon")
        
        # Add button
        Button(self.frame, text="Add Name").pack(side=TOP)
        

    def quit(self):
        self.frame.quit()

if __name__ == '__main__':
    root = Tk()
    
    app = AllWidgets(root)
    
    root.mainloop()
