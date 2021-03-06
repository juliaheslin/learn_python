# -*- coding: utf-8 -*-
"""
module_0.py

Introduction to modules
=======================

This module serves as an example for how everything should
look in a typical module. You can copy this module and use it as a template.

To run the tests, open a command prompt in the root directory (the one that
contains setup.py: 'learn_python') and type `python setup.py tests`
This will find and run all of the tests in this project.

To only run the tests for this module (this is not the typical way of doing
things, but it might be more convenient under these circumstances), simply
run this module and the script at the bottom will automatically run the tests
for this module.

Alternatively, you can run the tests for this module directly from the command
line:
    `python -m unittest tests/test_module_0.py
"""


def hello_world():
    """
    Print 'Hello World' to the screen.

    Args:
    ----
        none

    Returns:
    -------
        True
    """
    print("Hello World!")
    return True

if __name__ == '__main__':

    import unittest

    testsuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testsuite)
