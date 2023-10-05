#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive """
from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    dt = datetime.now().strftime('%Y%m%d%H%M%S')
    if os.path.isdir("versions") is False:
        local('mkdir versions')
    file = "versions/web_static_{}.tgz".format(dt)
    if local('tar -czvf {} web_static'.format(file)).failed is True :
        return None
    return file
