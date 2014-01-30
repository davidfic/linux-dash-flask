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
    # sbin may not always be in the path
    cmd = "/sbin/ifconfig | grep -B1 'inet addr' | grep -v '^--$' | sed 's/^\([a-zA-Z0-9]\+\) .*/\\1/g' | cut -d':' -f 2 | awk '{print $1}'"
    local_interfaces_linear = sub.check_output(cmd, shell=True).split()
    
    local_interfaces_linear.append("external")
    #  Didn't want to add a dependency on Requests, but the right way to do this would be the following:
    # local_interfaces_linear.push(requests.get("http://ipecho.net/plain").text)
    local_interfaces_linear.append(sub.check_output("curl http://ipecho.net/plain", shell=True))

    interfaces = []
    this_interface = []
    count = 0
    for token in local_interfaces_linear:
        if count % 2:
            # Odd items - IPs, the second of each inner array
            this_interface.append(token)
            interfaces.append(list(this_interface)) # copy the list
        else:
            # Even items - interface names, the first item
            this_interface = [token]
        count += 1
            
    return interfaces

def get_installed_software():
    pass

def get_inet_speed():
    pass

def get_running_processes():
    pass

