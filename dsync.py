# dsync file-sync utility v0.1.?
# by: Dylan Dwyer
# //////////////////////////////

import sys, os, time, platform, shutil
import dsync_var, dsync_config, dsync_ui,\
       comarg

# adapt to current OS
dsync_var.os_type = platform.system().lower()

# determine gui or cli context
dsync_var.is_gui = comarg.is_mode('gui') or True

os_type = dsync_var.os_type
if 'darwin' in os_type:
    dsync_var.config_dir\
        = os.path.expanduser('~/Library/Application Support/dsync')
elif 'windows' in os_type:
    dsync_var.config_dir\
        = os.path.join(os.getenv('LOCALAPPDATA'), 'dsync')
elif 'linux' in os_type:
    dsync_var.config_dir\
        = os.path.expanduser('~/.dsync')
else:
    dsync_ui.message('Operating System Unknown: '+dsync_var.os_type, 'error')
    sys.exit()

dsync_config.initialize()

# identify subject directory
if comarg.mode_value('dir', None) == None:
    subject = comarg.positional_value(1, None)
else:
    subject = comarg.mode_value('dir', None)

# dsync_ui.message(subject)
# dsync_ui.status(str(sys.argv))
dsync_ui.status('Current Working dir:\n'+os.getcwd())

# if no Subject was passed, show menu instead...
if subject is None or comarg.is_mode('menu'):
    dsync_ui.show_main_menu()
# establish absolute path for Subject
subject = os.path.abspath(subject)
# check validity of Subject
if not os.path.isdir(subject):
    dsync_ui.message('Invalid Subject Directory:\n'+subject+\
                     '', 'error')
    sys.exit()
    

# start config mode if no config present or intitiated by user
if comarg.is_mode('config') or not dsync_config.is_configured(subject):
    dsync_config.config_mode(subject)


sys.exit()
