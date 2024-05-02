#!/usr/bin/python3
"""
Fabric script to generate a tgz archive
Usage: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    Create a compressed archive of the web_static folder
    """

    # Generate timestamp for the archive name
    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'

    # Create versions directory if it doesn't exist
    local('mkdir -p versions')

    # Create the tgz archive
    create = local('tar -cvzf versions/{} web_static'.format(archive))

    # Return the archive name if successful, otherwise return None
    if create is not None:
        return archive
    else:
        return None
