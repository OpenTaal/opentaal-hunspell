#!/usr/bin/env python3
'''Find dictionary entries what can be replaced by a flag.'''

# flag
# remove
# add
# match
# description
# capital

repls = (
    # ('Ya', '', 'tje', '.', 'diminutive singular', False),
    # ('Ya', '', 'tjes', '.', 'diminutive', False),

    # ('Yb', '', 'je', '[^m]', 'diminutive singular', False),
    # ('Yb', '', 'jes', '[^m]', 'diminutive plural', False),
    # ('Yb', '', 'pje', '[m]', 'diminutive singular', False),
    # ('Yb', '', 'pjes', '[m]', 'diminutive plural', False),

    # ('Yc', 'g', 'kje', '.', 'diminutive singular', False),
    # ('Yc', 'g', 'kjes', '.', 'diminutive plural', False),

    # ('Yd', '', 'etje', '.', 'diminutive singular', False),
    # ('Yd', '', 'etjes', '.', 'diminutive plural', False),

    # ('Ye', '', 'atje','a', 'diminutive singular', False),
    # ('Ye', '', 'utje','u', 'diminutive singular', False),
    # ('Ye', '', 'otje','o', 'diminutive singular', False),
    # ('Ye', '', 'etje','i', 'diminutive singular', False),
    # ('Ye', 'é', 'eetje', 'é', 'diminutive singular', False),
    # ('Ye', '', 'atjes', 'a', 'diminutive plural', False),
    # ('Ye', '', 'utjes', 'u', 'diminutive plural', False),
    # ('Ye', '', 'otjes', 'o', 'diminutive plural', False),
    # ('Ye', '', 'etjes', 'i', 'diminutive plural', False),
    # ('Ye', 'é', 'eetjes', 'é', 'diminutive plural', False),

    # ('Yf', '', 'betje', 'b', 'diminutive singular', False),
    # ('Yf', '', 'getje', 'g', 'diminutive singular', False),
    # ('Yf', '', 'ketje', 'k', 'diminutive singular', False),
    # ('Yf', '', 'letje', 'l', 'diminutive singular', False),
    # ('Yf', '', 'metje', 'm', 'diminutive singular', False),
    # ('Yf', '', 'netje', 'n', 'diminutive singular', False),
    # ('Yf', '', 'petje', 'p', 'diminutive singular', False),
    # ('Yf', '', 'retje', 'r', 'diminutive singular', False),
    # ('Yf', '', 'setje', 's', 'diminutive singular', False),
    # ('Yf', '', 'betjes', 'b', 'diminutive plural', False),
    # ('Yf', '', 'getjes', 'g', 'diminutive plural', False),
    # ('Yf', '', 'ketjes', 'k', 'diminutive plural', False),
    # ('Yf', '', 'letjes', 'l', 'diminutive plural', False),
    # ('Yf', '', 'metjes', 'm', 'diminutive plural', False),
    # ('Yf', '', 'netjes', 'n', 'diminutive plural', False),
    # ('Yf', '', 'petjes', 'p', 'diminutive plural', False),
    # ('Yf', '', 'retjes', 'r', 'diminutive plural', False),
    # ('Yf', '', 'setjes', 's', 'diminutive plural', False),

    # ('Yg', '', '\'tje', '.', 'diminutive singular', False),
    # ('Yg', '', '\'tjes', '.', 'diminutive plural', False),

    # ('Za', '', 's', '.', 'plural', False),

    # ('Zu', '', 's', 'ium', 'plural', False),
    # ('Zu', 'ium', 'ia', 'ium', 'plural', False),
    # ('Zu', 'icus', 'ici', 'icus', 'plural', False),
    # ('Zu', 'icus', 'ica', 'icus', 'plural', False),

    # ('Zx', 'um', 'a', 'um', 'plural', False),
    # ('Zx', 'us', 'i', 'us', 'plural', False),

    ('Zb', '', 'en', '[^eo]', 'plural', False),
    ('Zb', '', 'ën', '[eo]', 'plural', False),

    ('Zc', '', '\'s', '.', 'plural', False),

    # ('Zd', 'heid', 'heden', '.', 'plural', False),

    # ('Ze', '', 'ben', 'b', 'plural', False),
    # ('Ze', '', 'den', 'd', 'plural', False),
    # ('Ze', '', 'fen', 'f', 'plural', False),
    # ('Ze', '', 'gen', 'g', 'plural', False),
    # ('Ze', '', 'ken', 'k', 'plural', False),
    # ('Ze', '', 'len', 'l', 'plural', False),
    # ('Ze', '', 'men', 'm', 'plural', False),
    # ('Ze', '', 'nen', 'n', 'plural', False),
    # ('Ze', '', 'pen', 'p', 'plural', False),
    # ('Ze', '', 'sen', 's', 'plural', False),
    # ('Ze', '', 'ren', 'r', 'plural', False),
    # ('Ze', '', 'ten', 't', 'plural', False),
    # ('Ze', '', 'zen', 'z', 'plural', False),

    # ('Zf', 'al', 'len', 'l', 'plural', False),
    # ('Zf', 'ar', 'ren', 'r', 'plural', False),
    # ('Zf', 'an', 'nen', 'n', 'plural', False),
    # ('Zf', 'ad', 'den', 'd', 'plural', False),
    # ('Zf', 'ak', 'ken', 'k', 'plural', False),
    # ('Zf', 'ap', 'pen', 'p', 'plural', False),
    # ('Zf', 'as', 'zen', 's', 'plural', False),
    # ('Zf', 'af', 'ven', 'f', 'plural', False),
    # ('Zf', 'am', 'men', 'm', 'plural', False),
    # ('Zf', 'at', 'ten', 't', 'plural', False),
    # ('Zf', 'ag', 'gen', 'g', 'plural', False),
    # ('Zf', 'el', 'len', 'l', 'plural', False),
    # ('Zf', 'er', 'ren', 'r', 'plural', False),
    # ('Zf', 'en', 'nen', 'n', 'plural', False),
    # ('Zf', 'ed', 'den', 'd', 'plural', False),
    # ('Zf', 'ek', 'ken', 'k', 'plural', False),
    # ('Zf', 'ep', 'pen', 'p', 'plural', False),
    # ('Zf', 'es', 'zen', 's', 'plural', False),
    # ('Zf', 'ef', 'ven', 'f', 'plural', False),
    # ('Zf', 'em', 'men', 'm', 'plural', False),
    # ('Zf', 'et', 'ten', 't', 'plural', False),
    # ('Zf', 'eg', 'gen', 'g', 'plural', False),
    # ('Zf', 'ol', 'len', 'l', 'plural', False),
    # ('Zf', 'or', 'ren', 'r', 'plural', False),
    # ('Zf', 'on', 'nen', 'n', 'plural', False),
    # ('Zf', 'od', 'den', 'd', 'plural', False),
    # ('Zf', 'ok', 'ken', 'k', 'plural', False),
    # ('Zf', 'op', 'pen', 'p', 'plural', False),
    # ('Zf', 'os', 'zen', 's', 'plural', False),
    # ('Zf', 'of', 'ven', 'f', 'plural', False),
    # ('Zf', 'om', 'men', 'm', 'plural', False),
    # ('Zf', 'ot', 'ten', 't', 'plural', False),
    # ('Zf', 'og', 'gen', 'g', 'plural', False),
    # ('Zf', 'ul', 'len', 'l', 'plural', False),
    # ('Zf', 'ur', 'ren', 'r', 'plural', False),
    # ('Zf', 'un', 'nen', 'n', 'plural', False),
    # ('Zf', 'ud', 'den', 'd', 'plural', False),
    # ('Zf', 'uk', 'ken', 'k', 'plural', False),
    # ('Zf', 'up', 'pen', 'p', 'plural', False),
    # ('Zf', 'us', 'zen', 's', 'plural', False),
    # ('Zf', 'uf', 'ven', 'f', 'plural', False),
    # ('Zf', 'um', 'men', 'm', 'plural', False),
    # ('Zf', 'ut', 'ten', 't', 'plural', False),
    # ('Zf', 'ug', 'gen', 'g', 'plural', False),

    # ('Zg', 'af', 'fen', '.', 'plural', False),
    # ('Zg', 'of', 'fen', '.', 'plural', False),
    # ('Zg', 'es', 'sen', '.', 'plural', False),

    # ('Zh', 's', 'zen', 's', 'plural', False),
    # ('Zh', 'f', 'ven', 'f', 'plural', False),

    ('Zi', '', 'n', '.', 'plural, see also Zj', False),

    ('Zj', '', 'n', '.', 'plural, see also Zi', False),

    ('PN', '', '\'', '[hsxz]', 'possessive proper name', True),
    #TODO PN
    ('PN', '', 's', '[bcdefghjklmnpqrtuüvwxzéëâïóçà]', 'possessive proper name', True),
    #TODO PN
    ('PN', '', '\'s', 'che', 'possessive proper name', True),
    ('PN', '', '\'s', 'dge', 'possessive proper name', True),

    # ('PI', '', 'se', '.', 'female inhabitant', True),
    #TODO missing rule plural

    # ('PJ', '', 'aar', 'en', 'male inhabitant singular', True),
    # ('PJ', '', 'mer', 'm', 'male inhabitant singular', True),

    # ('PK', '', 'er', '[^r]', 'male inhabitant singular', True),
    # ('PK', '', 'der', 'r', 'male inhabitant singular', True),
    # ('PK', '', 'ers', '[^r]', 'male inhabitant plural', True),
    # ('PK', '', 'ders', 'r', 'male inhabitant plural', True),

    ('Zk', '', 'en', '.', 'noun from adjective plural', False),
    ('Zk', '', 'e', '.', 'noun from adjective singular', False),

    # ('Zm', '', 'heid', '.', 'noun from adjective singular', False),
    # ('Zm', '', 'heden', '.', 'noun from adjective plural', False),

     # ('Xe', '', 'e', '.', 'female noun singular', False),
#    #TODO missing rule plural

    ('V3', '', 't', '[^ao]', 'verb third person', False),
    ('V3', '', 'at', 'a', 'verb third person', False),
    ('V3', '', 'ot', 'o', 'verb third person', False),

    ('Vp', '', 'de', '.', 'verb past tense', False),
    ('Vp', '', 'den', '.', 'verb past tense', False),

    ('Vq', '', 'te', '.', 'verb past tense', False),
    ('Vq', '', 'ten', '.', 'verb past tense', False),

    ('Va', 't', 'de', 't', 'verb past tense', False),
    ('Va', 't', 'den', 't', 'verb past tense', False),

    ('Vb', 't', 'te', 't', 'verb past tense', False),
    ('Vb', 't', 'ten', 't', 'verb past tense', False),

    ('Vi', '', 'd', '.', 'verb past tense', False),
    ('Vi', '', 'de', '.', 'verb past tense', False),

    ('Ve', '', 'e', '.', 'verb past tense', False),

    ('Aa', '', 'e', '[^e]', 'adjective', False),
    ('Aa', '', 'ë', '[e]', 'adjective', False),

    ('Ab', '', 'er', '[^r]', 'adjective', False),
    ('Ab', '', 'der', 'r', 'adjective', False),

    # ('Ac', '', 'ere', '[^r]', 'adjective', False),
    # ('Ac', '', 'dere', 'r', 'adjective', False),

    ('Ad', '', 'st', '[^s]', 'adjective', False),
    ('Ad', '', 't', 's', 'adjective', False),

    ('Ae', '', 'ste', '[^s]', 'adjective', False),
    ('Ae', '', 'te', 's', 'adjective', False),

    ('Ai', '', 's', '.', 'adjective', False),

    ('Al', 'ob', 'be', 'oob', 'adjective', False),
    ('Al', 'ad', 'de', 'aad', 'adjective', False),
    ('Al', 'ed', 'de', 'eed', 'adjective', False),
    ('Al', 'od', 'de', 'ood', 'adjective', False),
    ('Al', 'af', 've', 'aaf', 'adjective', False),
    ('Al', 'of', 've', 'oof', 'adjective', False),
    ('Al', 'ag', 'ge', 'aag', 'adjective', False),
    ('Al', 'eg', 'ge', 'eeg', 'adjective', False),
    ('Al', 'og', 'ge', 'oog', 'adjective', False),
    ('Al', 'ak', 'ke', 'aak', 'adjective', False),
    ('Al', 'ek', 'ke', 'eek', 'adjective', False),
    ('Al', 'ok', 'ke', 'ook', 'adjective', False),
    ('Al', 'al', 'le', 'aal', 'adjective', False),
    ('Al', 'el', 'le', 'eel', 'adjective', False),
    ('Al', 'ol', 'le', 'ool', 'adjective', False),
    ('Al', 'am', 'me', 'aam', 'adjective', False),
    ('Al', 'om', 'me', 'oom', 'adjective', False),
    ('Al', 'um', 'me', 'uum', 'adjective', False),
    ('Al', 'an', 'ne', 'aan', 'adjective', False),
    ('Al', 'en', 'ne', 'een', 'adjective', False),
    ('Al', 'on', 'ne', 'oon', 'adjective', False),
    ('Al', 'ar', 're', 'aar', 'adjective', False),
    ('Al', 'or', 're', 'oor', 'adjective', False),
    ('Al', 'es', 'se', 'ees', 'adjective', False),
    ('Al', 'at', 'te', 'aat', 'adjective', False),
    ('Al', 'et', 'te', 'eet', 'adjective', False),
    ('Al', 'ot', 'te', 'oot', 'adjective', False),
    ('Al', 'os', 'ze', 'oos', 'adjective', False),
    ('Al', 'us', 'se', 'uus', 'adjective', False),
    ('Al', 'ut', 'te', 'uut', 'adjective', False),
    ('Al', 'ur', 're', 'uur', 'adjective', False),
    ('Al', 'er', 're', 'eer', 'adjective', False),
    ('Al', 'op', 'pe', 'oop', 'adjective', False),
    ('Al', 'un', 'ne', 'uun', 'adjective', False),
    ('Al', 'em', 'me', 'eem', 'adjective', False),
    ('Al', 'ul', 'le', 'uul', 'adjective', False),
    ('Al', 'as', 'se', 'aas', 'adjective', False),
    ('Al', 'uk', 'ke', 'uuk', 'adjective', False),

    ('Am', 'eel', 'ële', 'ieel', 'adjective', False),

# zwak => zwakke
    ('An', '', 'de', 'd', 'adjective', False),
    ('An', '', 'fe', 'f', 'adjective', False),
    ('An', '', 'ge', 'g', 'adjective', False),
    ('An', '', 'ke', 'k', 'adjective', False),
    ('An', '', 'le', 'l', 'adjective', False),
    ('An', '', 'me', 'm', 'adjective', False),
    ('An', '', 'ne', 'n', 'adjective', False),
    ('An', '', 'pe', 'p', 'adjective', False),
    ('An', '', 're', 'r', 'adjective', False),
    ('An', '', 'se', 's', 'adjective', False),
    ('An', '', 'te', 't', 'adjective', False),

# zwak => zwakker
    ('Ao', '', 'der', 'd', 'adjective', False),
    ('Ao', '', 'fer', 'f', 'adjective', False),
    ('Ao', '', 'ger', 'g', 'adjective', False),
    ('Ao', '', 'ker', 'k', 'adjective', False),
    ('Ao', '', 'ler', 'l', 'adjective', False),
    ('Ao', '', 'mer', 'm', 'adjective', False),
    ('Ao', '', 'ner', 'n', 'adjective', False),
    ('Ao', '', 'per', 'p', 'adjective', False),
    ('Ao', '', 'rer', 'r', 'adjective', False),
    ('Ao', '', 'ser', 's', 'adjective', False),
    ('Ao', '', 'ter', 't', 'adjective', False),

# zwak => zwakkere
    ('Ap', '', 'dere', 'd', 'adjective', False),
    ('Ap', '', 'fere', 'f', 'adjective', False),
    ('Ap', '', 'gere', 'g', 'adjective', False),
    ('Ap', '', 'kere', 'k', 'adjective', False),
    ('Ap', '', 'lere', 'l', 'adjective', False),
    ('Ap', '', 'mere', 'm', 'adjective', False),
    ('Ap', '', 'nere', 'n', 'adjective', False),
    ('Ap', '', 'pere', 'p', 'adjective', False),
    ('Ap', '', 'rere', 'r', 'adjective', False),
    ('Ap', '', 'sere', 's', 'adjective', False),
    ('Ap', '', 'tere', 't', 'adjective', False),

# kwaad => kwader, boos=> bozer
    ('Aq', 'ob', 'ber', 'oob', 'adjective', False),
    ('Aq', 'ad', 'der', 'aad', 'adjective', False),
    ('Aq', 'ed', 'der', 'eed', 'adjective', False),
    ('Aq', 'od', 'der', 'ood', 'adjective', False),
    ('Aq', 'af', 'ver', 'aaf', 'adjective', False),
    ('Aq', 'of', 'ver', 'oof', 'adjective', False),
    ('Aq', 'ag', 'ger', 'aag', 'adjective', False),
    ('Aq', 'eg', 'ger', 'eeg', 'adjective', False),
    ('Aq', 'og', 'ger', 'oog', 'adjective', False),
    ('Aq', 'ak', 'ker', 'aak', 'adjective', False),
    ('Aq', 'ek', 'ker', 'eek', 'adjective', False),
    ('Aq', 'ok', 'ker', 'ook', 'adjective', False),
    ('Aq', 'al', 'ler', 'aal', 'adjective', False),
    ('Aq', 'el', 'ler', 'eel', 'adjective', False),
    ('Aq', 'ol', 'ler', 'ool', 'adjective', False),
    ('Aq', 'am', 'mer', 'aam', 'adjective', False),
    ('Aq', 'om', 'mer', 'oom', 'adjective', False),
    ('Aq', 'um', 'mer', 'uum', 'adjective', False),
    ('Aq', 'an', 'ner', 'aan', 'adjective', False),
    ('Aq', 'en', 'ner', 'een', 'adjective', False),
    ('Aq', 'on', 'ner', 'oon', 'adjective', False),
    ('Aq', 'es', 'ser', 'ees', 'adjective', False),
    ('Aq', 'at', 'ter', 'aat', 'adjective', False),
    ('Aq', 'et', 'ter', 'eet', 'adjective', False),
    ('Aq', 'ot', 'ter', 'oot', 'adjective', False),
    ('Aq', 'os', 'zer', 'oos', 'adjective', False),
    ('Aq', 'us', 'ser', 'uus', 'adjective', False),
    ('Aq', 'ut', 'ter', 'uut', 'adjective', False),

    # ('Gs', '', 'straat', '.', 'geography', True),

    # ('Gl', '', 'laan', '.', 'geography', True),

    # ('Gh', '', 'hof', '.', 'geography', True),

    # ('Gi', '', 'singel', '.', 'geography', True),

    # ('Gp', '', 'plein', '.', 'geography', True),

    # ('Gk', '', 'kanaal', '.', 'geography', True),

    # ('Ga', '', 'kade', '.', 'geography', True),

    # ('Gw', '', 'weg', '.', 'geography', True),

    # ('GL', 'straat', 'laan', 'straat', 'geography', True),

    # ('GW', 'straat', 'weg', 'straat', 'geography', True),

    )

#TODO support flag
exceps = ('Maaskant', 'Maaskantje', )

def row(word, letters):
    '''True if word does not ends with one of the letters.'''
    for letter in letters:
        if word[-1] == letter:
            return True
    return False

def nonrow(word, letters):
    '''True if word does not end with any of the letters.'''
    for letter in letters:
        if word[-1] == letter:
            return False
    return True

def check(number, word, flags, word_prev, flags_prev):
    '''Check if previous word is conjugation of word.'''
    if word is None or word_prev is None:
        return
    # if word in exceps:
    #     return
    if flags is not None or flags_prev is not None:
        return #TODO Remove this later, is to keep it simple for now.
    for repl in repls:
        if repl[5] and word[0] == word[0].lower():
            continue
        if not repl[5] and word[0] == word[0].upper():
            continue
        if repl[3] != '.':
            if repl[3][0] == '[' and repl[3][-1] == ']':
                if repl[3][1] == '^':
                    if not nonrow(word, repl[3][1:-1]):
                        continue
                else:
                    if not row(word, repl[3][1:-1]):
                        continue
            else:
                if not word.endswith(repl[3]):
                    continue
        proc = word
        length = len(repl[1])
        if length > 0:
            if proc[-length:] == repl[1]:
                proc = proc[:-length] + repl[2]
        else:
            proc += repl[2]
        if proc == word_prev:
            if flags is None:
                if flags_prev is None:
                    print(f'line {number:06d} type {repl[4]} word {word} '
                          f'might need flag {repl[0]} to include '
                          f'{word_prev}')
                else:
                    print(f'line {number:06d} type {repl[4]} word {word} flags '
                          f'{flags} might need flag {repl[0]} to include '
                          f'{word_prev}')
            else:
                if flags_prev is None:
                    print(f'line {number:06d} type {repl[4]} word {word} flags '
                          f'{flags} might need flag {repl[0]} to include '
                          f'{word_prev}')
                else:
                    print(f'line {number:06d} type {repl[4]} word {word} flags '
                          f'{flags} might need flag {repl[0]} to include '
                          f'{word_prev} flags {flags_prev}')

def main():
    '''Loop over dictionary file.'''
    with open('../nl.dic') as dic:
        prev_word = None
        prev_flags = None
        prev_prev_word = None
        prev_prev_flags = None
        prev_prev_prev_word = None
        prev_prev_prev_flags = None
        number = 0
        for line in dic:
            line = line[:-1]
            number += 1
            this_word = None
            this_flags = None
            if '/' in line:
                pos = line.find('/')
                if line[pos-1] != '\\':
                    this_word = line[:pos]
                    this_flags = line[pos+1:]
            else:
                this_word = line

            check(number, this_word, this_flags, prev_word, prev_flags)
            check(number, prev_word, prev_flags, this_word, this_flags)
            check(number, this_word, this_flags, prev_prev_word, prev_prev_flags)
            check(number, prev_prev_word, prev_prev_flags, this_word, this_flags)
            check(number, this_word, this_flags, prev_prev_prev_word, prev_prev_prev_flags)
            check(number, prev_prev_prev_word, prev_prev_prev_flags, this_word, this_flags)

            prev_prev_prev_word = prev_prev_word
            prev_prev_prev_flags = prev_prev_flags
            prev_prev_word = prev_word
            prev_prev_flags = prev_flags
            prev_word = this_word
            prev_flags = this_flags

if __name__ == "__main__":
    main()
