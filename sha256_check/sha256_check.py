from hashlib import sha256
from colorama import Fore, Style
import sys

# Made by Federico Torrielli

def check_sha256(filename, hash):
    """
    Given a filename and a sha256 hash, print 'Hash is identical' if the hashes are the same,
    or 'Hash is different' otherwise.
    """
    with open(filename, 'rb') as f:
        data = f.read()
        if sha256(data).hexdigest() == hash:
            print(Fore.GREEN + 'Hash is identical')
        else:
            print(Fore.RED + 'Hash is different')

def main():
    """
    Checks if the program was run with the correct number of arguments,
    if not, prints an error message and exits.
    """
    try:
        check_sha256(sys.argv[1], sys.argv[2])
    except IndexError:
        print(Fore.RED + 'Whoopsie! Something went wrong...\n' + Fore.BLUE
        + 'Usage: python sha256_check *file* *sha256*')
    except OSError as err:
        print(err)
    print(Style.RESET_ALL)

if __name__ == '__main__':
    main()
