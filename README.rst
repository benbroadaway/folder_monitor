==============
folder_monitor
==============


Monitor a folder and move files to another!

Description
===========

A longer description of your project goes here...

Get Started
===========
Create a virtual environment::

   # use your python executable here >=3.7
   python3 -m venv ./venv
   # start the environment
   source ./venv/bin/activate

Build
=====
Building is run through ``setup.py``::

   python setup.py build

Testing
===========
Run a test::

   python -m pytest -s test_monitor.py::test_monitor

Run all tests::

   python setup.py test

Install
=======
This will build the egg, and install it to your system::

   python setup.py install

Uninstall
==========
This takes a little more work::

   # looks for package info
   pip show folder_monitor | grep Location
   # outputs...
   # Location: /usr/local/lib/python3.7/site-packages/folder_monitor-0.1.0-py3.7.egg

   # remove egg from site-packages (you may have different versions here)
   rm -rf /usr/local/lib/python3.7/site-packages/folder_monitor-0.1.0-py3.7.egg

   # remove main script
   rm /usr/local/bin/monitor_a_directory
   
Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
