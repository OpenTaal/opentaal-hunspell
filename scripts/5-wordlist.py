#!/usr/bin/env python3

from operator import itemgetter

chars = {}
for word in open('../../opentaal-wordlist/wordlist.txt'):
    word = word[:-1]
    for char in word:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1

descending = []
for char, count in sorted(chars.items(), key=itemgetter(1), reverse=True):
    print(count, char)
    descending.append(char)
print('total', len(descending))
print('descending order:', ''.join(descending))

    
if ' ' in descending:
    hunspell_try = ' '

lowers='abcdefghijklmnopqrstuvwxyz'
for char in descending:
    if char in lowers:
        hunspell_try += char

if '-' in descending:
    hunspell_try += '-'

if "'" in descending:
    hunspell_try += "'"
#    hunspell_try += '’' # only if this is in the word list

uppers='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for char in descending:
    if char in uppers:
        hunspell_try += char

for char in hunspell_try:
    if char in descending:
        descending.remove(char)

for char in descending:
    hunspell_try += char

print('total TRY', len(hunspell_try))
print('TRY', hunspell_try)
