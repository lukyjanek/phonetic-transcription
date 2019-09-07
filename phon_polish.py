#!/usr/bin/env python3
# coding: utf-8

"""Phonetic transcription of Polish text to IPA."""

import re
import sys


# function for the phonetic transcription of Polish language to IPA
def ipa_polish(text):
    """Phonetic transcription to IPA of given Polish text or word."""
    # set transription table (IPA)
    vowels = {'a': 'a', 'ą': 'ɔ', 'e': 'ɛ', 'ę': 'ɛ', 'i': 'i', 'o': 'ɔ',
              'u': 'u', 'ó': 'u', 'y': 'ɨ'}

    sonors = {'j': 'j', 'm': 'm', 'n': 'n', 'ń': 'ɲ', 'ni': 'ɲ', 'r': 'r',
              'l': 'l', 'ł': 'w'}

    voice_voice = {'b': 'b', 'd': 'd', 'g': 'ɡ', 'w': 'v', 'z': 'z',
                   'dź': 'd͡ʑ', 'dzi': 'd͡ʑ', 'ź': 'ʑ', 'zi': 'ʑ', 'dz': 'd͡z',
                   'dż': 'd͡ʐ', 'ż': 'ʐ', 'rz': 'ʐ', 'h': 'ɣ', 'ch': 'ɣ',
                   'v': 'v', 'q': 'kv', 'x': 'ks'}

    voice_voiceless = {'b': 'p', 'd': 't', 'g': 'k', 'w': 'f', 'z': 's',
                       'dź': 't͡ɕ', 'dzi': 't͡ɕ', 'ź': 'ɕ', 'zi': 'ɕ',
                       'dz': 't͡s', 'dż': 'd͡ʐ', 'ż': 'ʂ', 'rz': 'ʂ', 'h': 'x',
                       'ch': 'x', 'v': 'f', 'q': 'kf', 'x': 'ks'}

    voiceless_voiceless = {'p': 'p', 't': 't', 'k': 'k', 'f': 'f', 's': 's',
                           'ć': 't͡ɕ', 'ci': 't͡ɕ', 'ś': 'ɕ', 'si': 'ɕ',
                           'c': 't͡s', 'cz': 't͡ʂ', 'sz': 'ʂ'}

    voiceless_voice = {'p': 'b', 't': 'd', 'k': 'ɡ', 'f': 'v', 's': 'z',
                       'ć': 'd͡ʑ', 'ci': 'd͡ʑ', 'ś': 'ʑ', 'si': 'ʑ',
                       'c': 'd͡z', 'cz': 'd͡ʐ', 'sz': 'ʐ'}

    # exceptions
    n_nasals = ('d', 'g', 'dz', 'c', 'k', 't', 'cz', 'dż')
    w_nasals = ('w', 'z', 'ź', 'zi', 'rz', 'ż', 'ś', 'si', 'ch',
                'h', 'f', 's', 'sz')
    m_nasals = ('b', 'p')
    ni_nasals = ('dź', 'dzi', 'ci', 'ć')
    consonants_soft = ('dzi', 'zi', 'ci', 'si', 'ni')

    # TODO: foreign words

    # split on clauses
    text = text.replace('...', '.')
    parts = re.split(r'[,;\.\!\?\"\-\–$]', text)
    delimiters = [l for l in text if l in ',;.!?"-–']

    # transcript clauses
    transcripted_parts = list()
    for part in parts:
        # check input
        if not part:
            transcripted_parts.append('')
            continue

        # prepare text to list of letters to transcript
        part = part.lower().strip()
        part = part.replace('dzi', 'A').replace('dź', 'B').replace('rz', 'C')
        part = part.replace('dż', 'D').replace('ch', 'E').replace('sz', 'F')
        part = part.replace('cz', 'G').replace('dz', 'H').replace('zi', 'I')
        part = part.replace('ci', 'J').replace('si', 'K').replace('ni', 'L')
        digraphs = {'A': 'dzi', 'B': 'dź', 'C': 'rz', 'D': 'dż', 'E': 'ch',
                    'F': 'sz', 'G': 'cz', 'H': 'dz', 'I': 'zi', 'J': 'ci',
                    'K': 'si', 'L': 'ni'}
        part = list(part)
        for l in range(len(part)):
            if part[l] in digraphs:
                part[l] = digraphs[part[l]]

        # transcripted input
        ipa = [l for l in part]

        # find out intervals for neutralization and assimilation
        posit_vowel = [-1] + [i for i in range(len(part)) if part[i] in vowels]
        posit_sonor = [i for i in range(len(part)) if part[i] in sonors]

        # neutralization
        j = posit_vowel[-1]
        if posit_sonor and posit_sonor[-1] > posit_vowel[-1]:
            j = posit_sonor[-1]

        i = len(part) - 1
        while i > j:
            if part[i] in voice_voiceless:
                ipa[i] = voice_voiceless[part[i]]
            elif part[i] in voiceless_voiceless:
                ipa[i] = voiceless_voiceless[part[i]]
            elif part[i] in sonors:
                ipa[i] = sonors[part[i]]
            i -= 1

        # transctiption and assimilation
        while posit_vowel:
            i, k = j, j
            j = posit_vowel.pop()
            voice = None  # assimil. type (N=uknown, T=voice, F=voiceless)
            while i > j:
                # transcription of soft consonants
                if part[i] in consonants_soft:
                    # dzi, zi
                    if part[i] in ('dzi', 'zi'):
                        voice = True
                        if i < len(part) - 1 and part[i+1] in vowels:
                            ipa[i] = voice_voice[part[i]]
                        else:
                            ipa[i] = voice_voice[part[i]] + ' i'
                    # ci, si
                    elif i < len(part) - 1 and part[i] in ('ci', 'si'):
                        voice = False
                        if part[i+1] in vowels:
                            ipa[i] = voiceless_voiceless[part[i]]
                        else:
                            ipa[i] = voiceless_voiceless[part[i]] + ' i'
                    # ni
                    else:
                        voice = None
                        if i < len(part) - 1 and part[i+1] in vowels:
                            ipa[i] = sonors[part[i]]
                        else:
                            ipa[i] = sonors[part[i]] + ' i'
                # transcription of vowels
                elif part[i] in vowels:
                    # initial of word (glotal plosive)
                    if i == 0 or part[i-1] == ' ':
                        ipa[i] = 'ʔ ' + vowels[part[i]]
                    # ii
                    elif (part[i] == 'i' and i < len(part) - 1
                          and part[i+1] == 'i'):
                        ipa[i] = 'j'
                    # ą, ę
                    elif part[i] in 'ąę':
                        if i is len(part) - 1:
                            if part[i] == 'ą':
                                ipa[i] = vowels[part[i]] + ' u̯'
                            else:
                                ipa[i] = vowels[part[i]]
                        elif part[i+1] in n_nasals:
                            ipa[i] = vowels[part[i]] + ' ŋ'
                        elif part[i+1] in m_nasals:
                            ipa[i] = vowels[part[i]] + ' m'
                        elif part[i+1] in w_nasals:
                            ipa[i] = vowels[part[i]] + ' u̯'
                        elif part[i+1] in ni_nasals:
                            ipa[i] = vowels[part[i]] + ' ɲ'
                        else:
                            ipa[i] = vowels[part[i]]
                    # otherwise
                    else:
                        ipa[i] = vowels[part[i]]

                # transcription of sonors and consonants
                elif k != i:
                    # sonors
                    if part[i] in sonors:
                        voice = None
                        ipa[i] = sonors[part[i]]
                    # choose type of assimilation
                    elif voice is None:
                        # regression or progression of w
                        if part[i] in 'w' and i > 0:
                            if part[i-1] in 'tks':
                                ipa[i] = voice_voiceless[part[i]]
                                voice = False
                            else:
                                ipa[i] = voice_voice[part[i]]
                                voice = True
                        # regression or progression of ż and rz
                        elif part[i] in ('ż', 'rz') and i > 0:
                            if part[i-1] in 'ae':
                                ipa[i] = voice_voiceless[part[i]]
                                voice = False
                            else:
                                ipa[i] = voice_voice[part[i]]
                                voice = True
                        # voiced
                        elif part[i] in voice_voice:
                            ipa[i] = voice_voice[part[i]]
                            voice = True
                        # voiceless
                        elif part[i] in voiceless_voiceless:
                            ipa[i] = voiceless_voiceless[part[i]]
                            voice = False
                    # assimilation
                    else:
                        # voiced group
                        if voice is True and part[i] in voice_voice:
                            ipa[i] = voice_voice[part[i]]
                        elif voice is True and part[i] in voiceless_voice:
                            ipa[i] = voiceless_voice[part[i]]
                        # voiceless group
                        elif voice is False and part[i] in voice_voiceless:
                            ipa[i] = voice_voiceless[part[i]]
                        elif voice is False and part[i] in voiceless_voiceless:
                            ipa[i] = voiceless_voiceless[part[i]]

                i -= 1

        # clean empty cells and save transcripted clauses
        ipa = list(filter(None, ipa))
        transcripted_parts.append(ipa)

    # return transcripted text
    transcripted_parts = [' '.join(part) for part in transcripted_parts]
    transcripted = ''
    i = 0
    while i < len(delimiters):
        transcripted += transcripted_parts[i] + delimiters[i]
        i += 1
    if i < len(transcripted_parts):
        transcripted += transcripted_parts[-1]

    transcripted = re.sub(r'\.|\?|\!|\;|\"', '   ||   ', transcripted)
    transcripted = re.sub(r'\,|\-|\–', '   |   ', transcripted)
    return transcripted


# running script if it is used in shell (with stdin or path to file)
if __name__ == '__main__':

    if not sys.stdin.isatty():  # read from stdin
        for line in sys.stdin:
            print(ipa_polish(line.strip()), sep='\t')

    else:  # read from file
        if len(sys.argv) == 2:
            with open(sys.argv[1], mode='r', encoding='utf-8') as f:
                for line in f:
                    print(ipa_polish(line.strip()), sep='\t')
        else:
            print('Error: Use script in pipeline or give the path '
                  'to the relevant file in the first argument.')
