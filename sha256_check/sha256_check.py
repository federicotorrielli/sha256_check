from hashlib import sha256
from colorama import Fore, Style
import sys


# made by EvilScript
ERROR_MSG = (
    Fore.RED + 'Whoopsie! Something went wrong...\n' 
    + Fore.BLUE + 'Usage: python sha256_check *file* *sha256*\n'
    "Or sha256_check --gui "
)

def main(argv):
    if argv.count(argv[0]) == len(argv):
        print(Fore.GREEN + 'Hash are identical')
    else:
        print(Fore.RED + 'Hash are different')


def sha256_check():
    sha256_hash = sha256()
    try:
        with open(sys.argv[1], "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            main([sha256_hash.hexdigest(), sys.argv[2]])
    except IndexError:
        print(ERROR_MSG)

    except OSError as err:
        print(err)
    print(Style.RESET_ALL)
