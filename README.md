# SignIn

This project is not complete, you should use
[chronophore](https://github.com/mesbahamin/chronophore) instead unless you want
to practice your development skills.

SignIn kiosk software to aid educational environments

![Screenshot](https://github.com/TechnologyClassroom/SignIn/blob/master/docs/SignIn.PNG?raw=true "Screenshot")

This is an INCOMPLETE project to create a sign in solution for a building, room,
or small youth organization.

Instead of dedicating a full size computer all day with an overly complex
barrier to entry, imagine a tiny Raspberry Pi connected to a monitor, keyboard,
and mouse at the front of the building.  This low cost computer could act as a
simple Sign In solution to track attendance in your building.

This would be an excellent beginner project for someone with little experience
with python.

[Download link](https://github.com/TechnologyClassroom/SignIn/archive/master.zip)

## Progress
- signin.py has a draft of a GUI.
- Our old 10mb database converted into a 2mb SQLite database.
- The scripts are compatible with Python 2.7 and 3.x.


## Requirements
Requirements are listed in the
[requirements.md file](https://github.com/TechnologyClassroom/SignIn/blob/master/docs/requirements.md).


## Python Modules
These libraries are included by default with python 2 and 3 as the Python
Standard Library.

- tkinter for a Graphical User Interface
- ttk to improve the aesthetics of tkinter
- sqlite3 for a database
- math for statistical analysis


## Why Python?

- Python is easy to install.
- Python works on all operating systems including GNU/Linux, Mac OS X, and
  Windows.
- Python works well with old computers and low powered computers.
- Python is a beginner language, yet is powerful enough for professional use.
- Python is easy to read, write, and modify.
- Python is open source.
- Python is interpreted so compiling the code is not necessary to test changes.
- Python manages RAM automatically.


## How to install Python

- GNU/Linux Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check
that Python is installed by running this command from a terminal:

```
python -V
```

- Mac Installation Instructions

Python is already installed on your system, but the version that ships with the
OS is reported to have a broken Tkinter library.

Note: To install Tkinter, you must install ActiveSlate which is closed source.

Download the suggest python 2 or python 3 and ActiveSlate from
[this link](https://www.python.org/download/mac/tcltk/).  Installing software
will require administrator privilages.


- Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows
is through [ninite.  Ninite](https://ninite.com/python/) is a website that
allows you to install many programs at once without accidentally installing
adware.  The ninite download program can be left on your system and used as an
updater in the future.


## Helpful resources

- https://www.codecademy.com/learn/python
- http://www.tkdocs.com/
- http://www.pyvideo.org/
- https://docs.python.org/
- https://docs.python.org/3/library/index.html
- https://docs.python.org/3/library/math.html
- https://docs.python.org/3/library/tk.html
- https://thenewboston.com/videos.php?cat=99
- https://docs.python.org/3/library/sqlite3.html

## How to install a test environment

To help develop this program, install python, open the file in IDLE, make
changes, save, and press F5 to run the script.  Alternatively, install python,
open a terminal, edit signin.py with the text editor of your choice, and run
python scriptname.py.
