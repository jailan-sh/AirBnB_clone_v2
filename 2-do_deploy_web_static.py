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
        file = archive_path.split('/')[-1].split('.')[0]
        zipt = archive_path.split('/')[-1]
        path = "/data/web_static/releases/{}".format(file)
        
        put(archive_path, '/tmp/')
        run("mkdir {}".format(path))
        run('tar -xzf /tmp/{} -c {}'.format(zipt, path))
        run('rm /tmp/{}'.format(zipt))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path))
        return True
    except:
        return False
