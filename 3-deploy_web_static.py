#!/usr/bin/python3
"""Modle - generates a .tar file"""
from fabric.api import *
from datetime import datetime
from os.path import isfile, getsize

env.hosts = ['35.243.167.75', '35.196.225.34']


def do_pack():
    """creates the pack .tar"""
    try:
        local("mkdir -p versions")
        fecha = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        nombre = "versions/web_static_" + fecha + ".tgz"
        local("tar -cvzf " + nombre + " web_static")
        print("web_static packed: {} -> {}Bytes".format(nombre,
              getsize(nombre)))
        return nombre
    except:
        return None

def do_deploy(archive_path):
    """send data to remote server"""
    if isfile(archive_path):
        pre_path = archive_path.split("/")[1]
        put(archive_path, "/tmp/")
        tmp_path = "/tmp/" + pre_path
        releases_path = "/data/web_static/releases/" + pre_path.split(".")[0]
        sudo("mkdir -p {:s}".format(releases_path))
        sudo("tar -xzf {:s} -C {:s}".format(tmp_path, releases_path))
        sudo("rm {:s}".format(tmp_path))
        all_path_w = releases_path + "/web_static/*"
        dictory_path = releases_path + "/web_static/"
        sudo("mv {:s} {:s}".format(all_path_w, releases_path))
        sudo("rm -rf {:s}".format(dictory_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {:s} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    else:
        return False

def deploy():
    """deploy"""
    fl = do_pack()
    if fl is None:
        return False
    else:
        return do_deploy(fl)
