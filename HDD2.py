from dep import name as nm
from dep import load as ld
import time
import os
import sys
def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")
def run_lsblk():
    print("Running bulk storage analysis...")
    os.system("lsblk")
    os.system("echo \"|\" > found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdb   >> found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdc   >> found_hdd.txt")
    print("\n  ")
    print("\n  ")
    os.system("bash t.sh")
    print('''\033[0;37m
    ''')
    os.system("cat found_hdd.txt")
    print('''\033[1;31m
            ''')
global ans
ans = False
nm.display_azhaar()
ld.mn_ld(" Running bulkstorage analysis...")
run_lsblk()
#os.system("echo -n \"|-> \"  && lsblk | grep sdc >> found_hdd.txt")
#os.system("echo -n \"|-> \"  && lsblk | grep sdd >> found_hdd.txt")
print("\n  ")
print("\n  ")
