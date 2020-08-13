#!/usr/bin/python3
""" Module for testing file storage"""
import unittest
import pep8


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
