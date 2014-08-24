#!/usr/bin/env python3
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
    name = "bridger",
    version = "0.1",
    packages = find_packages(),

    install_requires = [],

    include_package_data = True,

    author = "Sandro Covo",
    author_email = "sandro@covo.ch",
    description = "This is an app, that allows listenting from music\
                   that is streamed from torrents.",
    license = "GPLv3",
    keywords = "music torrent streaming",
)
