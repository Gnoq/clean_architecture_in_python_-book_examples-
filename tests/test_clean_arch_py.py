#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_clean_arch_py
----------------------------------

Tests for `clean_arch_py` module.
"""

from clean_arch_py.calc import Calc

from clean_arch_py import clean_arch_py


# @pytest.fixture
# def response():
#     """Sample pytest fixture.
#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9


def test_add_three_numbers():
    c = Calc()

    res = c.add(4, 5, 6)

    assert res == 15
