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
    try:
        localpath = archive_path.split('/')[1]
        newpath = localpath.split('.')[0]
        rempath = "/data/web_static/releases/"

        put(archive_path, "/tmp/".format(localpath))
        sudo("mkdir -p {}{}".format(rempath, newpath))
        sudo("tar -xzf /tmp/{} -C {}{}".format(localpath, rempath, newpath))
        sudo("rm /tmp/{}".format(localpath))
        sudo("cp -r {0}{1}/web_static/* {0}{1}/".format(rempath, newpath))
        sudo("rm -rf {}{}/web_static".format(rempath, newpath))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {}{}/ /data/web_static/current".format(rempath, newpath))
        return True
    except:
        return False
