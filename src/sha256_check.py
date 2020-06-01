from hashlib import sha256
# made by EvilScript
from colorama import Fore, Style
import sys


def main(argv):
    if argv.count(argv[0]) == len(argv):
        print(Fore.GREEN + 'Gli hash sono identici')
    else:
        print(Fore.RED + 'Gli hash sono differenti')


if __name__ == '__main__':
    sha256_hash = sha256()
    try:
        with open(sys.argv[1], "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
            main([sha256_hash.hexdigest(), sys.argv[2]])
    except IndexError:
        print(Fore.RED + 'Qualcosa è andato storto!\n' + Fore.BLUE + 'Usage: python sha256_check *file* *sha256*')
    except OSError as err:
        print(err)
    print(Style.RESET_ALL)