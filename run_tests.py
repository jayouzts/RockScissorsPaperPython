#!/usr/bin/env python3

import os
import sys
import unittest

# Add src/ to sys.path so imports work
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
sys.path.insert(0, SRC_DIR)

# Manually import your test modules
from tests import test_rules  # import your test file as a module

# Load all tests from the module(s)
loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(test_rules))

# Run the test suite
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Exit with success/fail code
sys.exit(0 if result.wasSuccessful() else 1)
