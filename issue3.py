import unittest
from one_hot_encoder import fit_transform


class TestFT(unittest.TestCase):
    def test_empty_args(self):
        self.assertRaises(TypeError, fit_transform)

    def test_empty_list_arg(self):
        categories = []
        exp_transformed_cats = []
        transformed_cats = fit_transform(categories)
        self.assertEqual(transformed_cats, exp_transformed_cats)

    def test_one_category(self):
        categories = ['Moscow', 'Moscow', 'Moscow']
        exp_transformed_cats = [
            ('Moscow', [1]),
            ('Moscow', [1]),
            ('Moscow', [1]),
        ]
        transformed_cats = fit_transform(categories)
        self.assertEqual(transformed_cats, exp_transformed_cats)

    def test_empty_category(self):
        categories = ["", "text2"]
        exp_cat = ("", [0, 1])
        transformed_cats = fit_transform(categories)
        self.assertIn(exp_cat, transformed_cats)

    def test_strings_as_args(self):
        categories = ['Moscow', 'London', 'New-York']
        exp_transformed_cats = [
            ('Moscow', [0, 0, 1]),
            ('London', [0, 1, 0]),
            ('New-York', [1, 0, 0]),
        ]
        transformed_cats = fit_transform(*categories)
        self.assertEqual(transformed_cats, exp_transformed_cats)
