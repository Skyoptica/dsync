# dsync Configuration Module v0.1.?
# by: Dylan Dwyer
# /////////////////////////////////

import sys, os
import dsync_ui,\
       yaml

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


# checks for existence of subject config file
def is_configured(subject):
    return False



# config mode
def config_mode(subject):
    return '...'
