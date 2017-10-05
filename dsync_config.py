# dsync Configuration Module v0.1.?
# by: Dylan Dwyer
# /////////////////////////////////

import sys, os, shutil
import dsync_var, dsync_ui,\
       yaml

# read or create global config file
def initialize():
    # checks for existence of (or creates) config directory
    if not os.path.isdir(dsync_var.config_dir):
        try:
            os.makedirs(dsync_var.config_dir)
        except Exception as error:
            dsync_ui.message(
                'There was an error creating the dsync config directory:\n'\
                +str(error), 'error')
            sys.exit()
            
    # load global configuration file
    global_config_path = os.path.join(dsync_var.config_dir,
                                      dsync_var.global_config_file_name)
    if not os.path.isfile(global_config_path):
        try:
            default_config = os.path.join(dsync_var.resource_dir,
                                          dsync_var.global_config_default)
            shutil.copyfile(default_config, global_config_path)
        except Exception as error:
            dsync_ui.message(
                'There was an error creating the initial dsync config file:\n'\
                +str(error), 'error')
            sys.exit()

# checks for existence of subject config file
def is_configured(subject):
    return False



# config mode
def config_mode(subject):
    dsync_ui.status('Configuring directory:\n'+subject)
    sys.exit()
