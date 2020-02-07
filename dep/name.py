def fdisk_info():
    print('''\033[0;37m
      DOS (MBR)
   a   toggle a bootable flag
   b   edit nested BSD disklabel
   c   toggle the dos compatibility flag

  Generic
   d   delete a partition
   F   list free unpartitioned space
   l   list known partition types
   n   add a new partition
   p   print the partition table
   t   change a partition type
   v   verify the partition table
   i   print information about a partition

  Misc
   m   print this menu
   u   change display/entry units
   x   extra functionality (experts only)

  Script
   I   load disk layout from sfdisk script file
   O   dump disk layout to sfdisk script file

  Save & Exit
   w   write table to disk and exit
   q   quit without saving changes

  Create a new label
   g   create a new empty GPT partition table
   G   create a new empty SGI (IRIX) partition table
   o   create a new empty DOS partition table
   s   create a new empty Sun partition table
   ''')
def display_azhaar():
    print("****HDD Check tool****")
    print('''\033[1;31m
   ______                __           __   __
  / ____/_______  ____ _/ /____  ____/ /  / /_  __  ___
 / /   / ___/ _ \/ __ `/ __/ _ \/ __  /  / __ \/ / / (_)
/ /___/ /  /  __/ /_/ / /_/  __/ /_/ /  / /_/ / /_/ /
\____/_/   \___/\__,_/\__/\___/\__,_/  /_.___/\__, (_)
       ___        __                         /____/
      /   |____  / /_  ____ _____ ______
     / /| /_  / / __ \/ __ `/ __ `/ ___/
    / ___ |/ /_/ / / / /_/ / /_/ / /
   /_/  |_/___/_/ /_/\__,_/\__,_/_/

    ''')
def display_clt():
        print('''\033[1;36m
    ,o888888o.    8 8888   8888888 8888888888
   8888     `88.  8 8888         8 8888
,8 8888       `8. 8 8888         8 8888
88 8888           8 8888         8 8888
88 8888           8 8888         8 8888
88 8888           8 8888         8 8888
88 8888           8 8888         8 8888
`8 8888       .8' 8 8888         8 8888
   8888     ,88'  8 8888         8 8888
    `8888888P'    8 888888888888 8 8888
\033[0;37m
        ''')
