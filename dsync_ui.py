# dsync User Interface Module v0.1.?
# by: Dylan Dwyer
# //////////////////////////////////

import sys, os,\
       Tkinter, tkMessageBox, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

global status_ui_text
global os_type, is_gui
status_ui_text = '...'

def set_ui_modes(os_type, is_gui):
    pass

# displays a message (error or notice) via appropriate interface
def message(message_text, message_type):
    print message_text
    if message_type == 'error':
        tkMessageBox.showerror('dsync', message_text)
    else:
        tkMessageBox.showinfo('dsync', message_text)

# updates present status
def status(status_text):
    status_ui_text = status_text
    print status_ui_text

# display choice prompt

