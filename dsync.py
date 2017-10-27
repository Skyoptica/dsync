# dsync file-sync utility v0.1.?
# by: Dylan Dwyer
# //////////////////////////////

import sys, os, time, platform, argparse, shutil
import dsync_var, dsync_config, dsync_ui

# adapt to current OS
dsync_var.os_type = platform.system().lower()

# register argparse flags...
cliparser = argparse.ArgumentParser()
cliparser.add_argument('pos_dir', nargs='?', default=None)
cliparser.add_argument('--dir', help='specify directory to process')
cliparser.add_argument('-g', '--gui', help='start in gui mode',
                       action='store_true')
cliparser.add_argument('-m', '--menu', help='show tool menu',
                       action='store_true')
cliparser.add_argument('-c', '--config', help='configure specified directory',
                       action='store_true')
cli = cliparser.parse_args()

# determine gui or cli context
dsync_var.is_gui = cli.gui or True
dsync_ui.initialize_ui()

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
if cli.dir == None:
    subject = cli.pos_dir
else:
    subject = cli.dir

# dsync_ui.message(subject)
# dsync_ui.status(str(sys.argv))
dsync_ui.status('Current Working dir:\n'+os.getcwd())

# if no Subject was passed, show menu instead...
if subject is None or cli.menu:
    dsync_ui.show_tool_menu()
# establish absolute path for Subject
subject = os.path.abspath(subject)
# check validity of Subject
if not os.path.isdir(subject):
    dsync_ui.message('Invalid Subject Directory:\n'+subject+\
                     '', 'error')
    sys.exit()
    

# start config mode if no config present or intitiated by user
if cli.config or not dsync_config.is_configured(subject):
    dsync_config.config_mode(subject)


sys.exit()
