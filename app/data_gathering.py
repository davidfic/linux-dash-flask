import os
import subprocess as sub
from subprocess import PIPE

def get_os():
    return sub.check_output('uname -a',shell=True)

def get_disk_usage():
    cmd = "df -h |awk '{print $1, $2, $3, $4, $5, $6, $7, $9}'"  

    disk_usage = sub.check_output(cmd, shell=True)
    disk_list = []
    
    for s in disk_usage.splitlines():
        disk_list.append(s)
    
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