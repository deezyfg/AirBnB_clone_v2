#!/usr/bin/python3
"""
Deletes out-of-date archives from both local and remote servers.

Usage: fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

# Define the host servers
env.hosts = ['54.167.187.16', '54.172.159.27']

# Set the username for SSH connection
env.user = "ubuntu"


def do_clean(number=0):
    """
    Delete out-of-date archives.

    Args:
        number (int): The number of archives to keep. If number is 0 or 1,
        keeps only the most recent archive. If number is 2, keeps the most
        and second-most recent archives, etc.
    """

    # Convert number to integer
    number = 1 if int(number) == 0 else int(number)

    # Remove out-of-date archives locally
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Remove out-of-date archives remotely
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
