#!/usr/bin/env python

from setuptools import setup

setup(
  name="recceiver",
  version="1.5",
  description="resync server",
  author="Michael Davidsaver",
  author_email="mdavidsaver@gmail.com",
  url="https://github.com/mdavidsaver/recsync",
  packages=[
    "recceiver",
    "twisted.plugins",
  ],
  package_data={
    "twisted": ["plugins/recceiver_plugin.py"],
  },
)
