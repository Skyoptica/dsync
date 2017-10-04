# dsync file-sync utility v0.1.?
# by: Dylan Dwyer
# //////////////////////////////

import sys, os, time, platform,\
import sys, os, time, platform
import dsync_config, dsync_ui,\
       comarg

# adapt to current OS
global os_type
os_type = platform.system().lower()

# determine gui or cli context
global is_gui
is_gui = comarg.is_mode('gui') or True

dsync_ui.set_ui_modes(os_type, is_gui)

global config_dir
if 'darwin' in os_type:
    config_dir = os.path.expanduser('~/Library/Application Support/dsync')
elif 'windows' in os_type:
    config_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'dsync')
elif 'linux' in os_type:
    config_dir = os.path.expanduser('~/.dsync')
else:
    dsync_ui.message('Operating System Unknown: '+os_type, 'error')
    sys.exit()

dsync_config.initialize(config_dir)

# identify subject directory
if comarg.mode_value('dir', '!null') == '!null':
    subject = comarg.positional_value(1, '')
else:
    subject = comarg.mode_value('dir', '')

dsync_ui.message(subject, 'notice')
dsync_ui.message(str(sys.argv), 'notice')
dsync_ui.message(os.getcwd(), 'notice')

# start config mode if no config present or intitiated by user
if comarg.is_mode('config') or not dsync_config.is_configured(subject):
    dsync_config.config_mode(subject)

print 'start dsync ops...'

sys.exit()
