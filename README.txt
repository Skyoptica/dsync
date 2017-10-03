// dsync Directory Syncing Utility
----------------------------------

!! not yet at alpha stage

The idea behind dsync is to allow the easy creation of persistent relationships between two directories. What does that mean? Let's say I have an SD card from my digital camera and I always like to import my files in a certain pattern. Or maybe I need to shuffle some files around in a project when I prepare it for export/distribution.

Pass a directory to dsync and it will check for an existing config file for that directory. If one doesn't exist it will create and open a new config file in your favorite editor, pre-filled with many common config examples. If a config file exists, it will begin executing the instructions provided by the config file. In the case of multiple targets being configured for the same source directory, it will prompt the user to choose which one to execute.

... it's still a work in progress, check back for updates. =)