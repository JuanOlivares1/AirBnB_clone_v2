#!/usr/bin/python3
"""Modle - generates a .tar file"""
from fabric.api import local
import datetime
from os.path import getsize


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
