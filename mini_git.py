import argparse
import configparser
import grp, pwd
import os
import hashlib
import sys
from datetime import datetime
from fnmatch import fnmatch
from math import ceil
import re
import zlib


parser = argparse.ArgumentParser()
config = configparser.ConfigParser()


class commit:
    date = datetime.now()
    message = ''
    id = '' 
    parents = []
    def __init__(self,message,id,parents):
        self.message = message
        self.id = id
        self.parents = parents


class branche:
    commits = set()
    def __init__(self,commits):
        self.commits.add(commits)
        

class git:
    startnode = ''
    adjlist = []
    def __init__(self,startnode, adjlist):
        self.startnode = startnode
        self.adjlist = adjlist
    
    def insert(value):