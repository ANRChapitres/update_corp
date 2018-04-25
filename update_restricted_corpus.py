
# coding: utf-8
# author: odysseuspolymetis


import sys
import os
import os.path
import fnmatch
from lxml import etree
from lxml.etree import tostring
import re
from collections import defaultdict
from collections import OrderedDict
from shutil import copyfile
import argparse


print('This software updates the restricted corpus from the global corpus \nusage: --glob path/to/your/global/dir --rest path/to/your/restricted/dir/ --out path/to/your/target/dir/')
parser = argparse.ArgumentParser()
parser.add_argument('--glob', help= '/your/directory/to/global/dir/')
parser.add_argument('--rest', help= '/your/directory/to/restricted/dir/')
parser.add_argument('--out', help= '/your/directory/to/your/target/dir/')
args = parser.parse_args()


restreint = args.rest
romans = args.glob
path_out = args.out


files_restreint=fnmatch.filter(os.listdir(restreint), '*.xml')
files_romans=fnmatch.filter(os.listdir(romans), '*.xml')

count=0
for bigger in files_restreint:
    if any(bigger[4:] in s for s in files_romans):
        copyfile(romans+bigger, path_out+bigger)
        count+=1
    else:
        print(bigger)
print(count+" files have been updated")

