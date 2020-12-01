import pytest
from one_hot_encoder import fit_transform


def test_empty_args():
    with pytest.raises(TypeError):
        fit_transform()


def test_empty_list_arg():
    categories = []
    exp_transformed_cats = []
    transformed_cats = fit_transform(categories)
    assert transformed_cats == exp_transformed_cats


def test_one_category():
    categories = ['Moscow', 'Moscow', 'Moscow']
    exp_transformed_cats = [
        ('Moscow', [1]),
        ('Moscow', [1]),
        ('Moscow', [1]),
    ]
    transformed_cats = fit_transform(categories)
    assert transformed_cats == exp_transformed_cats


def test_with_empty_category():
    categories = ["", "text2"]
    exp_cat = ("", [0, 1])
    transformed_cats = fit_transform(categories)
    assert exp_cat in transformed_cats


def test_strings_as_args():
    categories = ['Moscow', 'London', 'New-York']
    exp_transformed_cats = [
        ('Moscow', [0, 0, 1]),
        ('London', [0, 1, 0]),
        ('New-York', [1, 0, 0]),
    ]
    transformed_cats = fit_transform(*categories)
    assert transformed_cats == exp_transformed_cats
