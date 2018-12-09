#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tempfile
import pytest
import os
from shutil import rmtree
from pathlib import Path
from folder_monitor.monitor import monitor_the_folder

__author__ = "Benjamin Broadaway"
__copyright__ = "Benjamin Broadaway"
__license__ = "mit"



def test_monitor(tmpdir):
    srcDir = Path(tmpdir.mkdir("srcDir"))
    dstDir = Path(tmpdir.mkdir("dstDir"))

    # Create three files
    Path(srcDir.joinpath('fileA.txt')).touch()
    Path(srcDir.joinpath('fileB.txt')).touch()
    Path(srcDir.joinpath('fileC.txt.part')).touch()
    assert len(os.listdir(srcDir)) == 3
    assert len(os.listdir(dstDir)) == 0

    print("srcDir:")
    print(os.listdir(srcDir))
    print("dstDir:")
    print(os.listdir(dstDir))

    # sync 'em
    monitor_the_folder(srcDir, dstDir, ".part")
    
    # one file shouldn't have been copied
    assert len(os.listdir(srcDir)) == 1
    assert len(os.listdir(dstDir)) == 2

    # remove .part
    os.rename(Path(srcDir.joinpath('fileC.txt.part')), Path(srcDir.joinpath('fileC.txt')))

    # sync again
    monitor_the_folder(srcDir, dstDir, ".part")
    
    # now the files should be in the destination folder
    assert len(os.listdir(srcDir)) == 0
    assert len(os.listdir(dstDir)) == 3

    print("srcDir:")
    print(os.listdir(srcDir))
    print("dstDir:")
    print(os.listdir(dstDir))


    print("\nsrcDir: %s" % srcDir.absolute())
    print("dstDir: %s" % dstDir.absolute())


    
    # clean up
    rmtree(srcDir)
    rmtree(dstDir)

def test_another_thing():
    assert 6 < 500
