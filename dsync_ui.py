# dsync User Interface Module v1.0
# by: Dylan Dwyer
# ////////////////////////////////

import Tkinter, tkMessageBox, tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

# displays a message (error or notice) via apprpriate interface
def message(message_text, message_type):
    print message_text
    if message_type == 'error':
        tkMessageBox.showerror('dsync', message_text)
    else:
        tkMessageBox.showinfo('dsync', message_text)

# updates present status
def status(status_text):
    print message_text
