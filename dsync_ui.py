# dsync User Interface Module v0.1.?
# by: Dylan Dwyer
# //////////////////////////////////

import sys, os
import Tkinter, tkMessageBox, tkSimpleDialog,\
       dsync_var


# initializaes whatever libraries required for current UI mode
def initialize_ui():
    if dsync_var.is_gui:
        root = Tkinter.Tk()
        root.withdraw()

# displays a message (error or notice) via appropriate interface
def message(message_text, message_type = 'notice'):
    print message_text
    if dsync_var.is_gui:
        if message_type == 'error':
            tkMessageBox.showerror('dsync', message_text)
        else:
            tkMessageBox.showinfo('dsync', message_text)

# updates present status
def status(status_text):
    dsync_var.status_ui_text = status_text
    print dsync_var.status_ui_text

# display main menu
def show_tool_menu():
    message('- displaying main menu -')
    sys.exit()
