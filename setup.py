#!/usr/bin/python3.6
# coding=utf-8
# *******************************************************************
# *** (EX-818-M) Exploit 818 Mikrotik ***
# * Version:
#   v1.0
# * Date:
#   19 - 08 - 2019 { Mon 19 Aug 2019 }
# * Facebook:
#   http://fb.com/mhm.hack
# * Author:
#   Hathem Ahmed
# *******************************************************************

from setuptools import setup, find_packages

setup(
    name='ex818m',
    packages=find_packages(),
    version='1.0',
    scripts=['ex818m.py'],
    description="Advanced Networking Test for Passwords for Web Applications",
    long_description="A tool that pulls all cards or passwords in the network " +
                     "( Mikrotik ) without entering any pearls from the system.",
    author='Hathem Ahmed',
    url='https://github.com/HathemAhmed/ex818m',
    keywords=['Mikrotik', 'checker', 'web scanner',
              'Wifi scanner', 'EXploit 818', "ex818"],
    install_requires=['argparse', 'requests', 'requests[socks]'],
    license='GPL-3.0'
)

