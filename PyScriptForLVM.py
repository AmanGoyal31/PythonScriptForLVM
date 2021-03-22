import os
print("Python Script For LVM Partition")
print("----Elasticity to Data Node----")
print("Make sure you have Attached extra Hard Disk")
print("""1 to create only a Physical Volume
         2 to create setup upto a Volume Group 
         3 to create complete  Logical Volume with mount 
         4 for EXIT
    """)
while True:
    n=int(input("choose Option : "))
    if n==1:
        pv = input('Enter physical volume name : ')
        os.system('pvcreate {}'.format(pv)) 
        os.system('pvdisplay')
    elif n==2:
        pv = input('Enter physical volume name : ')
        os.system('pvcreate {}'.format(pv))
        vg = input('Enter volume group name: ')
        os.system('vgcreate {} {}'.format(vg, pv))
        os.display('vgdisplay')
    elif n==3:
        pv = input('Enter physical volume name : ') #name_format=/dev/sdb
        os.system('pvcreate {}'.format(pv)) 
        vg = input('Enter volume group name: ')    #name_format=anyname
        os.system('vgcreate {} {}'.format(vg, pv))
        size = input('Enter the size of the partition : ')
        name = input('Enter the name of the partition: ') #name_format=anyname
        os.system('lvcreate --size {} --name {} {}'.format(size,name,vg))
        os.system('lvdisplay')
        mount=input("enter name to format and mount:") #name_format=/dev/vg_name/lv_name
        os.system('mkfs.ext4 {}'.format(mount))  
        os.system('mkdir \dn1')
        os.system('mount {} /dn1'.format(mount))
        os.system('fdisk -l')
    else:
        break