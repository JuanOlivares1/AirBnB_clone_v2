#!/usr/bin/python3
""" Module for testing file storage PASO"""
import unittest
from models.base_model import BaseModel
import os
import pep8


class test_fileStorage(unittest.TestCase):
    """ Class to test the file storage method """

    def test_file_storage_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0)
