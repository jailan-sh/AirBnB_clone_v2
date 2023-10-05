#!/usr/bin/python3
""" a Fabric script that generates a .tgz archive """
import os
from fabric.api import *


env.hosts = ['54.196.48.32', '34.229.255.108']

def do_deploy(archive_path):
    """
    Fabric script that distributes an archive to your web servers
    """
    if os.path.isfile(archive_path) is False:
        return False
    
    
    
