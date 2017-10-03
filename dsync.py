# dsync file-sync utility v0.1
# by: Dylan Dwyer
# ////////////////////////////

import sys, os, time, platform,\
       dsync_config, dsync_ui, comarg

# determine gui or cli context
is_gui = comarg.is_mode('gui')
is_gui = True

# adapt to current OS
global os_type
os_type = platform.system().lower()
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

if comarg.mode_value('dir', '!null') == '!null':
    subject = comarg.positional_value(1, '')
else:
    subject = comarg.mode_value('dir', '')

dsync_ui.message(subject, 'notice')
dsync_ui.message(str(sys.argv), 'notice')
# start config mode if no config present or intitiated by user
if comarg.is_mode('config') or not dsync_config.is_configured(subject):
    dsync_config.config_mode(subject)

print 'start dsync ops...'
