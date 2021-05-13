#!/usr/bin/env python3
# coding: utf-8

import sys
import unittest

sys.path.append('../')
from phon_czech import ipa_czech


class TestIpaCzech(unittest.TestCase):
    def test_ch(self):
        self.assertEqual(ipa_czech('všechno'), 'f ʃ ɛ x n ɔ')
        self.assertEqual(ipa_czech('střecha'), 's t r̝̊ ɛ x a')
        self.assertEqual(ipa_czech('prachbídný'), 'p r a ɣ b iː d n iː')

    def test_x(self):
        self.assertEqual(ipa_czech('text'), 't ɛ k s t')
        self.assertEqual(ipa_czech('exil'), 'ʔ ɛ ɡ z ɪ l')
        self.assertEqual(ipa_czech('latexu'), 'l a t ɛ k s u')
        self.assertEqual(ipa_czech('exot'), 'ʔ ɛ ɡ z ɔ t')
        self.assertEqual(ipa_czech('exemplář'), 'ʔ ɛ ɡ z ɛ m p l aː r̝̊')
        self.assertEqual(ipa_czech('boxovat'), 'b ɔ k s ɔ v a t')
        self.assertEqual(ipa_czech('pexeso'), 'p ɛ k s ɛ s ɔ')
        self.assertEqual(ipa_czech('mexiko'), 'm ɛ k s ɪ k ɔ')
        self.assertEqual(ipa_czech('exboxer'), 'ʔ ɛ ɡ z b ɔ k s ɛ r')
        self.assertEqual(ipa_czech('export'), 'ʔ ɛ k s p ɔ r t')


if __name__ == '__main__':
    unittest.main()
