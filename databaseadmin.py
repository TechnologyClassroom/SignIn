# Database Administration to accompany Sign In Software

# Michael McMahon

# This INCOMPLETE program allows editing a database that helps people to sign in.  The database can be analyzed for reporting purposes and grant writing.

# To help develop this program, install python, open the file in IDLE, make changes, save, and press F5.  Alternatively, install python, open a terminal, edit databaseadmin.py with the text editor of your choice, and run python databaseadmin.py.

# Requirements
# Password protected
# Offline
# Add entries to database
# Edit database

# Load Tkinter GUI library, SQLite database, and math for statistics.
import sqlite3, math

# Load GUI library tkinter and ttk to improve the appearance of tkinter.  Try importing Tkinter for Python 2.  If there is an error, import tkinter for Python 3.
try:
    from Tkinter import *
    import ttk
except ImportError:
    from tkinter import *
    import tkinter.ttk
