"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['dsync.py']
DATA_FILES = ['dsync_global.default.yml']
OPTIONS = {'argv_emulation': True, 'no_chdir': True}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
