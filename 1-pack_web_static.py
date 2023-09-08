#!/usr/bin/python3
"""generates an archive of web_static folder"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """function to generate the archive"""
    try:
        local("mkdir -p versions")
        res = local("tar -cvzf versions/web_static_{}.tgz web_static"
                    .format(datetime.now().strftime("%Y%m%d%H%M%s")),
                    capture=True)
        return res
    except Exception:
        return None
