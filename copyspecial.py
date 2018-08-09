#!/usr/bin/env python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import argparse

"""Copy Special exercise
"""


# Collects all paths for files user inputs to command line
def collect_paths(path):
    if not os.path.exists(path):
        return ["empty"]
    files = os.listdir(path)
    list_of_paths = []
    for f in files:
        match = re.search('__\w+__', f)
        if match:
            list_of_paths.append(os.path.abspath(f))
    return list_of_paths


# Copies all files user inputs to a specified directory
def copy_files(path, files):
    current_dir = os.getcwd()
    if not os.path.exists(path):
        p = 'mkdir -p {0}'.format(path)
        os.system(p)
    else:
        print "Path exists"
    for f in files:
        match = re.search('__\w+__', f)
        if match:
            os.chdir(current_dir)
            shutil.copy(f, path)


# Creates a zip file with any file user inputs
def zip_files(zipname, paths):
    file_names = ''
    for i in paths:
        file_names += i + " "
    cmd = "zip -j {0} {1}".format(str(zipname), str(file_names))
    print "\n Command I'm going to do: ", cmd, "\n"
    os.system(cmd)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('dirs', help='sends all file paths')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)

    # This grabs file paths everytime the program runs
    all_paths = collect_paths(args.dirs)

    if args.todir:
        copy_files(args.todir, all_paths)
    elif args.tozip:
        zip_files(args.tozip, all_paths)
    else:
        print "\n".join(all_paths)

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing)
    # with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions

if __name__ == "__main__":
    main()
