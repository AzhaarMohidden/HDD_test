from dep import name as nm
from dep import load as ld
import time
import os
import sys
def  mkfs_ini():
    print("Initiating MKFS..")
    name_select = str(raw_input('Input new name for Partition: '))
    commant_1 = "sudo mkfs -V -t vfat -n " + name_select + " /dev/sdb1"
    print("Making File system --> Vfat.." )
    time.sleep(1)
    os.system(commant_1)
    print("Mounting system....")
    os.system("sudo mount /dev/sdb1 /media/cltws/exthdd")
    print("Storage mounted")
def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Uhhhh... please enter ")
def fdisk_ini():
    print("Preparing to run Fdisk Utility...")
    time.sleep(1)
    nm.fdisk_info()
    os.system("sudo fdisk /dev/sdb")
    time.sleep(1)
def run_lsblk():
    print("Running bulk storage analysis...")
    os.system("lsblk")
    os.system("echo \"|\" > found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdb   >> found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdc   >> found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdd   >> found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sde   >> found_hdd.txt")
    os.system("echo \"|->\" && lsblk | grep sdf   >> found_hdd.txt")
    print("\n  ")
    print("\n  ")
    os.system("bash t.sh")
    print('''\033[0;37m
    ''')
    os.system("cat found_hdd.txt")
    print('''\033[1;31m
            ''')
def copy_foo():
    os.system("cp /media/cltws/sda2/kali-linux-2016.2-amd64.iso /media/cltws/exthdd/")
def ans_yes():
    while(ans == True):
        global ans
        ld.mn_ld(" Running bulkstorage analysis...")
        run_lsblk()
        ans = yes_or_no("Do you want to scan storage again? ")
    if(ans == False):
        fdisk_ini()
global ans
ans = False
nm.display_azhaar()
os.system("sudo mount /dev/sda2 /media/cltws/sda2 ")
ld.mn_ld(" Running bulkstorage analysis...")
run_lsblk()
#os.system("echo -n \"|-> \"  && lsblk | grep sdc >> found_hdd.txt")
#os.system("echo -n \"|-> \"  && lsblk | grep sdd >> found_hdd.txt")
print("\n  ")
print("\n  ")
ans = yes_or_no("Do you want to scan storage again? ")
if (ans == True):
    ans_yes()
else:
    fdisk_ini()
print("Fdisk Completed...")
mkfs_ini()
copy_ans = yes_or_no("Start copy test?...")
if (copy_ans == True):
    copy_foo()
