#!D:\shipoya\myvenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==8.1.2','console_scripts','pip'
__requires__ = 'pip==8.1.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==8.1.2', 'console_scripts', 'pip')()
    )
