# dsync Variables Module v0.1.?
# by: Dylan Dwyer
# /////////////////////////////

import sys, os

# static vars
global_config_file_name = 'dsync_global.yml'
global_config_default = 'dsync_global.default.yml'

config_index_file_name = 'dsync_index.yml'

resource_dir = os.path.dirname(__file__)

# dynamic vars
os_type = None
is_gui = None

config_dir = None

status_ui_text = None

