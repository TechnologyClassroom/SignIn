# SignIn
SignIn software to aid educational environments

![Screenshot](https://github.com/TechnologyClassroom/SignIn/blob/master/SignIn.PNG?raw=true "Screenshot")

This is an INCOMPLETE project to create a sign in solution for a building, room, or small youth organization.

This would be an excellent beginner project for someone with little experience with python.

<a href="https://github.com/TechnologyClassroom/SignIn/archive/master.zip">Download link</a>

# Progress
- signin.py has a draft of a GUI.
- Our old 10mb database converted into a 2mb SQLite database.
- The scripts are compatible with Python 2.7 and 3.x.


# Requirements
* Password protected administrator program
* Offline for student safety
* Add entries to database with minimal student information
* Edit database through administrator program
* Statistical analysis through administrator program
* Dosage reporting (How long did participants stay?)
* Includes a sign-out capability
* Gender reports (how many members on any given timeframe were male, female, etc.)
* Compare trends from one period to another
* Track mentoring information
* Track volunteers - Which mentors are around when members are around?
* Customizable reports/custom queries with custom fields
* Under-represented group reporting
* Answers A&P report questions for a given time period (for example, Jan1-July1 or July2-Dec 31)
  * What is the daily average number of members?
  * What is the daily average percent (%) of female members?
  * What is the daily average percent (%) of teen members (ages 13-18)?
  * What is the weekly average number of Mentors?
  * What is the total number active* members?
  * What is the total number active* mentors
  * What areas/schools are members coming from?

*Active = attended at least once in the last 6 months



# Python Modules
These libraries are included by default with python 2 and 3 as the Python Standard Library.

- tkinter for a Graphical User Interface
- ttk to improve the aesthetics of tkinter
- sqlite3 for a database
- math for statistical analysis


# Why Python?

- Python is easy to install.
- Python works on all operating systems including GNU/Linux, Mac OS X, and Windows.
- Python works well with old computers and low powered computers.
- Python is a beginner language, yet is powerful enough for professional use.
- Python is easy to read, write, and modify.
- Python is open source.
- Python is interpreted so compiling the code is not necessary to test changes.
- Python manages RAM automatically.


# How to install Python

  * GNU/Linux Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check that Python is installed by running this command from a terminal:

    python -V

  * Mac Installation Instructions

Python is probably already installed on your GNU/Linux system.  You can check that Python is installed by running this command from a terminal:

    python -V

You can also download a newer version <a href="https://www.python.org/ftp/python/2.7.11/python-2.7.11-macosx10.6.pkg">Python 2.7</a> or <a href="https://www.python.org/ftp/python/3.5.1/python-3.5.1-macosx10.6.pkg">Python 3</a> and install (requires administrator privilages).

Note: The default version of Python and Tkinter that ship with Sierra will break.

  * Windows Installation Instructions

The easiest way to install Python (and many other common programs) for Windows is through <a href="https://ninite.com/python/">ninite.  Ninite</a> is a website that allows you to install many programs at once without accidentally installing adware.  The ninite download program can be left on your system and used as an updater in the future.


# Helpful resources

- https://www.codecademy.com/learn/python
- http://www.tkdocs.com/
- http://www.pyvideo.org/
- https://docs.python.org/
- https://docs.python.org/3/library/index.html
- https://docs.python.org/3/library/math.html
- https://docs.python.org/3/library/tk.html
- https://thenewboston.com/videos.php?cat=99
- https://docs.python.org/3/library/sqlite3.html

# How to install a test environment

To help develop this program, install python, open the file in IDLE, make changes, save, and press F5 to run the script.  Alternatively, install python, open a terminal, edit signin.py with the text editor of your choice, and run python scriptname.py.
