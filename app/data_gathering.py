import os
import subprocess as sub
from subprocess import PIPE

def get_os():
    return sub.check_output('uname -a',shell=True)

def get_disk_usage():
    cmd = "df -hP"  

    disk_usage = sub.check_output(cmd, shell=True)
    disk_list = []
    
    for line in disk_usage.splitlines():
        # We don't want to split the last header on a space, or we will have
        #  one extra column.
        line = line.replace("Mounted on", "Mountpoint")
        disk_list.append(line.split())
    
    return disk_list

def get_users():
    pass

def get_ip():
    pass

def get_installed_software():
    pass

def get_inet_speed():
    pass

def get_running_processes():
    pass

