#!/usr/bin/env python3
# coding: utf-8

import sys
import unittest

sys.path.append('../')
from phon_polish import ipa_polish


class TestIpaCzech(unittest.TestCase):
    def test_rz(self):
        self.assertEqual(ipa_polish('przemek'), 'p ʂ ɛ m ɛ k')


if __name__ == '__main__':
    unittest.main()
