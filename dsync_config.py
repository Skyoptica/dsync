# dsync Configuation Module v0.1
# by: Dylan Dwyer
# ///////////////////////////////

import yaml, os, sys,\
       dsync_ui

global config_dir

# read or create global config file
def initialize(init_config_dir):
    # initialize shared variables
    config_dir = init_config_dir
    # checks for existence of (or creates) config directory
    if not os.path.isdir(config_dir):
        try:
            os.makedirs(config_dir)
        except Exception as error:
            dsync_ui.message('There was an error creating the dsync config directory:\n'+str(error), 'error')
            sys.exit()
    # load global configuration file


# checks for existence of configurations file
def is_configured(path):
    return False



# config mode
def config_mode(path):
    return '...'
