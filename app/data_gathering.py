import os
import subprocess as sub
from subprocess import PIPE
import requests

import utility

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
    # sbin may not always be in the path
    cmd = "/sbin/ifconfig | grep -B1 'inet addr' | grep -v '^--$' | sed 's/^\([a-zA-Z0-9]\+\) .*/\\1/g' | cut -d':' -f 2 | awk '{print $1}'"
    local_interfaces_linear = sub.check_output(cmd, shell=True).split()
    
    local_interfaces_linear.append("external")
    local_interfaces_linear.append(requests.get("http://ipecho.net/plain").text)
    

    interfaces = []
    this_interface = []
    for count, token in enumerate(local_interfaces_linear):
        if count % 2:
            # Odd items - IPs, the second of each inner array
            this_interface.append(token)
            interfaces.append(list(this_interface)) # copy the list
        else:
            # Even items - interface names, the first item
            this_interface = [token]
            
    return interfaces

def get_installed_software():
    pass

def get_inet_speed():
    pass

def get_running_processes():
    pass

def get_uptime():
    seconds_up = sub.check_output("cat /proc/uptime | cut -d' ' -f1", shell=True)
    time_units = ["seconds", "minutes", "hours", "days", "years"]
    time_string = ""
    for quantity, unit in zip(utility.split_seconds(seconds_up), time_units):
        time_string = "{0} {1} {2}".format(quantity, unit, time_string)
    return time_string
