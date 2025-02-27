#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive from
the contents of the web_static folder of your AirBnB Clone repo,
"""
from fabric.api import *
import os.path
import tarfile
from datetime import datetime


def do_pack():
    """The function that generates the .tgz file"""
    local("mkdir -p versions")
    date = str(datetime.now()).replace("-", "")\
                              .replace(":", "")\
                              .replace(" ", "")\
                              .replace(".", "")
    output_name = "web_static_" + date + ".tgz"

    tar = local('tar -cvzf versions/{} web_static'.format(output_name))

    if os.path.exists("./versions/{}".format(output_name)):
        return os.path.normpath("/versions/{}.tgz".format(output_name))
    else:
        return None
