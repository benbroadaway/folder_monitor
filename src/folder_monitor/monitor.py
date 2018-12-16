#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
[options.entry_points] section in setup.cfg:

    console_scripts =
         fibonacci = folder_monitor.skeleton:run
         fibonacci = folder_monitor.monitor:run

Then run `python setup.py install` which will install the command `fibonacci`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""

import argparse
import sys
import logging

from pathlib import Path
from shutil import copyfile
from logging.handlers import RotatingFileHandler
import re
import os
from folder_monitor import __version__

__author__ = "Benjamin Broadaway"
__copyright__ = "Benjamin Broadaway"
__license__ = "mit"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """Parse command line parameters

    Args:
      args ([str]): command line parameters as list of strings

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(
        description="Folder monitor and syncer")
    parser.add_argument(
        '--version',
        action='version',
        version='folder_monitor {ver}'.format(ver=__version__))
    parser.add_argument(
        '-monitor',
        '--monitor_dir',
        dest="monitor_dir",
        help="Directory to monitor",
        required=True,
        type=str,
        metavar="SRC")
    parser.add_argument(
        '-dest',
        '--dest_dir',
        dest="destination_dir",
        help="Directory to send files",
        required=True,
        type=str,
        metavar="DST")
    parser.add_argument(
        '-ignore',
        '--ignore_pattern',
        dest="ignore_pattern",
        help="File pattern to ignore",
        required=True,
        type=str,
        metavar="PTRN")
    parser.add_argument(
        '-v',
        '--verbose',
        dest="loglevel",
        help="set loglevel to INFO",
        action='store_const',
        const=logging.INFO)
    parser.add_argument(
        '-vv',
        '--very-verbose',
        dest="loglevel",
        help="set loglevel to DEBUG",
        action='store_const',
        const=logging.DEBUG)
    return parser.parse_args(args)

def monitor_the_folder(src, dst, ignore):
    """Monitor a folder and sync non-ignored files

        Args:
            src (str): source directory,
            dst (str): destination directory,
            ignore (str): pattern to ignore

    """

    pattern = re.compile(ignore)

    for p in Path(src).iterdir():
        # should we ignore?
        if pattern.search(p.name):
            _logger.info("ignoring: {}".format(p.name))
            continue

        if p.is_dir():
            # recurse
            _logger.info("Recursing into: {}".format(p.absolute()))
            monitor_the_folder(p.absolute(), dst, ignore)
            if len(os.listdir(p)) == 0:
                os.rmdir(p)
        else:
            # copy to destination
            copied_file = copyfile(p, Path(dst).joinpath(p.name))
            _logger.info("{} -> {}".format(p.name, copied_file))
            if Path(copied_file).exists() and (Path(copied_file).__sizeof__() == p.__sizeof__()):
                # okay, we can delete
                _logger.info("Deleting {}".format(p.absolute()))
                os.remove(p.absolute())
            else:
                _logger.info("Something isn't matching between files!")
            





def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    #logging.basicConfig(level=loglevel, stream=sys.stdout,
    #                    format=logformat, datefmt="%Y-%m-%d %H:%M:%S")

    logFile = '/tmp/folder_monitor.log'

    logging_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                    backupCount=2, encoding=None, delay=0)
    logging_handler.setFormatter(logging.Formatter(logformat))
    logging_handler.setLevel(loglevel)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logging.Formatter(logformat))


    _logger.addHandler(logging_handler)
    _logger.addHandler(consoleHandler)
    _logger.setLevel(loglevel)


def main(args):
    """Main entry point allowing external calls

    Args:
      args ([str]): command line parameter list
    """
    args = parse_args(args)
    setup_logging(args.loglevel)
    monitor_the_folder(args.monitor_dir, args.destination_dir, args.ignore_pattern)
    _logger.info("#### done with monitoring run ####")


def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
