#!/usr/bin/python3
"""deployer"""
from fabric.api import *


env.hosts = ['100.25.159.254', '54.144.128.184']
env.user = "ubuntu"


def do_clean(number=0):
    """cleares our of date archives"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
