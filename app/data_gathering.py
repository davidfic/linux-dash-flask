import os
import subprocess as sub
from subprocess import PIPE
import requests
from sys import platform as _platform
import time
import datetime
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
    if _platform.startswith("linux"): # linux, linux2, linux3 etc
        seconds_up = sub.check_output("cat /proc/uptime | cut -d' ' -f1", shell=True)
    elif _platform == "darwin":
        days_up = sub.check_output("uptime | cut -d' ' -f4", shell=True)
        hour_minute_up = sub.check_output("uptime | cut -d' ' -f6", shell=True)
        hm_up = hour_minute_up[:-2]+":00"
        seconds_from_days  = (60*60*24)*int(days_up)
        x = time.strptime(hm_up.split(',')[0],'%H:%M:%S')
        seconds = datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds()
        seconds_up = seconds + seconds_from_days
    elif _platform == "win32":
        pass
    else:
        return "Unexpected system type: " + _platform

    time_units = ["seconds", "minutes", "hours", "days", "years"]
    time_string = ""
    print "seconds up is:" , seconds_up
    for quantity, unit in zip(utility.split_seconds(seconds_up), time_units):
        time_string = "{0} {1} {2}".format(quantity, unit, time_string)
    return time_string
