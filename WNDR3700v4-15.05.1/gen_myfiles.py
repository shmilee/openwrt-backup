#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
from myfiles_secret import *

outdir = './myfiles_for_image'
templatedir = './myfiles_templates'

print('==> Templates:\n%s' % all_templates)
print('==> Files TODO:\n')
for k in sorted(all_myfiles.keys()):
    print(k.replace('_d_', '.').replace('_', '/'))

print('\n==> BEGIN\n')

if os.path.exists(outdir):
    shutil.rmtree(outdir)
os.makedirs(outdir)


def read_file(infile):
    try:
        with open(infile) as file:
            data = file.read()
    except Exception as err:
        print('\033[31m[Error]\033[0m %s' % err)
    return data

for k in sorted(all_myfiles.keys()):
    template = '%s/%s' % (templatedir, k.replace('_d_', '.').replace('_', '/'))
    outfile = '%s/%s' % (outdir, k.replace('_d_', '.').replace('_', '/'))
    filedir = os.path.split(outfile)[0]
    if not os.path.exists(filedir):
        os.makedirs(filedir)
    print('==> %s -> %s' % (template, outfile))
    temp = read_file(template)

    for task in all_myfiles[k]:
        action = task[0]
        print(' -> %s' % action)

        if action == 'ADD':
            temp = temp + task[1]
        elif action == 'REPLACE':
            olddata = task[1][0]
            newdata = task[1][1]
            temp = temp.replace(olddata, newdata)
        elif action == 'ADDFILE':
            infile = task[1]
            olddata = task[2][0]
            newdata = task[2][1]
            indata = read_file(infile)
            temp = temp + indata.replace(olddata, newdata)
        else:
            print(' -> Unknown ACTION %s.' % action)

    try:
        with open(outfile, "w") as file:
            file.write(temp)
    except Exception as err:
        print('\033[31m[Error]\033[0m %s' % err)

print('\n==> Done.')
