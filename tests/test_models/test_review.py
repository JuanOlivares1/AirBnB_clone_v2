#!/usr/bin/python3
"""test review"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pep8


class test_review(test_basemodel):
    """test_review"""

    def test_Review_pep8(self):
        """ tests pep8 compliance """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['./models/review.py'])
        self.assertEqual(result.total_errors, 0)

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
