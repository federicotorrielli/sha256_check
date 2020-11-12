"""
sets up the command line interface
"""

import sys

from .gui_sha256_check import gui_check
from .sha256_check import sha256_check, ERROR_MSG

def main():
    """parses command line params and runs appropriate function"""
    if len(sys.argv) == 1:
        print(ERROR_MSG)
        return

    if sys.argv[1] in ["--gui", "-g"]:
        gui_check()
    else: 
        sha256_check()
