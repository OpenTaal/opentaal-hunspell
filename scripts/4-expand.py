#!/usr/bin/env python3
'''Expand TODO'''

__author__ = 'Sander van Geloven'

# from difflib import ndiff
from datetime import datetime
from re import match
import sys


def oconv(word):
    """Convert output."""
    for key, value in oconvs.items():
        word = word.replace(key, value)
    return word


# followings list are manually obtained from $ man -K 5 hunspell
options_general = ('SET',
                   'FLAG',
                   'COMPLEXPREFIXES',
                   'LANG',
                   'IGNORE',
                   'AF',
                   'AM',)
options_suggest = ('KEY',
                   'TRY',
                   'NOSUGGEST',
                   'MAXCPDSUGS',
                   'MAXNGRAMSUGS',
                   'MAXDIFF',
                   'ONLYMAXDIFF',
                   'NOSPLITSUGS',
                   'SUGSWITHDOTS',
                   'REP',
                   'MAP',
                   'PHONE',
                   'WARN',
                   'FORBIDWARN',)
options_compounding = ('BREAK',
                       'COMPOUNDRULE',
                       'COMPOUNDMIN',
                       'COMPOUNDFLAG',
                       'COMPOUNDBEGIN',
                       'COMPOUNDLAST',
                       'COMPOUNDEND',
                       'COMPOUNDMIDDLE',
                       'ONLYINCOMPOUND',
                       'COMPOUNDPERMITFLAG',
                       'COMPOUNDFORBIDFLAG',
                       'COMPOUNDMORESUFFIXES',
                       'COMPOUNDROOT',
                       'COMPOUNDWORDMAX',
                       'CHECKCOMPOUNDDUP',
                       'CHECKCOMPOUNDREP',
                       'CHECKCOMPOUNDCASE',
                       'CHECKCOMPOUNDTRIPLE',
                       'SIMPLIFIEDTRIPLE',
                       'CHECKCOMPOUNDPATTERN',
                       'FORCEUCASE',
                       'COMPOUNDSYLLABLE',
                       'SYLLABLENUM',)
options_affix = ('PFX',
                 'SFX',)
options_other = ('CIRCUMFIX',
                 'FORBIDDENWORD',
                 'FULLSTRIP',
                 'KEEPCASE',
                 'ICONV',
                 'OCONV',
                 'NEEDAFFIX',
                 'SUBSTANDARD',
                 'WORDCHARS',
                 'CHECKSHARPS',)
options_undocumented = ('VERSION',
                        'CHECKNUM',
                        'NONGRAMSUGGEST',)
options_deprecated = ('LEMMA_PRESENT',
                      'PSEUDOROOT',)


def self_check():  # pylint: disable=R0912,R0915
    """Perform self-check."""
    for option in options_general:
        if option in options_suggest:
            print('ERROR: Overlap general and suggest')
            sys.exit(1)
        if option in options_compounding:
            print('ERROR: Overlap general and compounding')
            sys.exit(1)
        if option in options_affix:
            print('ERROR: Overlap general and affix')
            sys.exit(1)
        if option in options_other:
            print('ERROR: Overlap general and other')
            sys.exit(1)
        if option in options_deprecated:
            print('ERROR: Overlap general and deprecated')
            sys.exit(1)
        if option in options_undocumented:
            print('ERROR: Overlap general and undocumented')
            sys.exit(1)
    for option in options_suggest:
        if option in options_compounding:
            print('ERROR: Overlap suggest and compounding')
            sys.exit(1)
        if option in options_affix:
            print('ERROR: Overlap suggest and affix')
            sys.exit(1)
        if option in options_affix:
            print('ERROR: Overlap suggest and other')
            sys.exit(1)
        if option in options_deprecated:
            print('ERROR: Overlap suggest and deprecated')
            sys.exit(1)
        if option in options_undocumented:
            print('ERROR: Overlap suggest and undocumented')
            sys.exit(1)
    for option in options_compounding:
        if option in options_affix:
            print('ERROR: Overlap compounding and affix')
            sys.exit(1)
        if option in options_other:
            print('ERROR: Overlap compounding and other')
            sys.exit(1)
        if option in options_deprecated:
            print('ERROR: Overlap compounding and deprecated')
            sys.exit(1)
        if option in options_undocumented:
            print('ERROR: Overlap compounding and undocumented')
            sys.exit(1)
    for option in options_affix:
        if option in options_other:
            print('ERROR: Overlap affix and other')
            sys.exit(1)
        if option in options_deprecated:
            print('ERROR: Overlap affix and deprecated')
            sys.exit(1)
        if option in options_undocumented:
            print('ERROR: Overlap affix and undocumented')
            sys.exit(1)
    for option in options_other:
        if option in options_deprecated:
            print('ERROR: Overlap other and deprecated')
            sys.exit(1)
        if option in options_undocumented:
            print('ERROR: Overlap other and undocumented')
            sys.exit(1)
    for option in options_deprecated:
        if option in options_undocumented:
            print('ERROR: Overlap deprecated and undocumented')
            sys.exit(1)


oconvs = {}


def main(args):  # pylint: disable=R0912,R0914,R0915
    """Expand dictionary words accoring to affix flags."""
    wordlist = set()
    for word in open('../../opentaal-wordlist/wordlist.txt'):
        wordlist.add(word[:-1])
    for word in open('../../opentaal-wordlist/wordparts.tsv'):
        wordlist.add(word.split('\t')[0])
    datetimeversion = ''
    for line in open('../../opentaal-wordlist/datetimeversion.txt'):
        datetimeversion = line.strip()

    wordlist_new_l = set()
    wordlist_new_i = {}
    no_strip = set()

    flags_all = set()
    sfxs = {}
    pfxs = {}
    comment_line = None
    in_oconv = 0
    in_sfx = 0
    in_pfx = 0
    in_compoundrule = 0
    in_checkcompoundpattern = 0
    flag = None
    flag_prev = ''
    line_nr = 0
    keepcase = None  # pylint: disable=W0612
    warn = None  # pylint: disable=W0612
    forceucase = None  # pylint: disable=W0612
    forbiddenword = None  # pylint: disable=W0612
    nosuggest = None  # pylint: disable=W0612
    compoundmin = None  # pylint: disable=W0612
    compoundbegin = None  # pylint: disable=W0612
    compoundmiddle = None  # pylint: disable=W0612
    compoundend = None  # pylint: disable=W0612
    compoundpermitflag = None  # pylint: disable=W0612
    onlyincompound = None  # pylint: disable=W0612
    flags_undefined = {}

    for line in open(f'{args}.aff'):
        line_nr += 1
        line = line[:-1]
        if line == '':
            continue
        stripped = line.strip()
        if line != stripped:
            print('WARNING: Found leading or trailing whitespace in line'
                  f' {line_nr}: {line}')
        if '  ' in line or ' \t' in line or '\t ' in line or '\t\t' in line:
            print('WARNING: Found duplicate whitespace in line'
                  f' {line_nr}: {line}')
        if line == '':
            continue
        if line.startswith('#'):
            comment_line = line
            continue
        data = line
        comment = None
        if '\t' in line:
            data, comment = line.split('\t')
        fields = data.split(' ')
        option = fields[0]
        if option not in options_general \
            and option not in options_suggest \
            and option not in options_compounding \
            and option not in options_affix \
            and option not in options_other \
            and option not in options_undocumented \
            and option not in options_deprecated:
            print(f'ERROR: Unknown option {option} in line {line_nr}:'
                  f' {line}')
            sys.exit(1)

        if option == 'KEEPCASE':
            if keepcase is not None:
                print(f'ERROR: Duplicate KEEPCASE in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            keepcase = flag
            continue
        if option == 'WARN':
            if warn is not None:
                print(f'ERROR: Duplicate WARN in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            warn = flag
            continue
        if option == 'FORCEUCASE':
            if forceucase is not None:
                print(f'ERROR: Duplicate FORCEUCASE in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            forceucase = flag
            continue
        if option == 'FORBIDDENWORD':
            if forbiddenword is not None:
                print(f'ERROR: Duplicate FORBIDDENWORD in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            forbiddenword = flag
            continue
        if option == 'NOSUGGEST':
            if nosuggest is not None:
                print(f'ERROR: Duplicate NOSUGGEST in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            nosuggest = flag
            continue
        if option == 'COMPOUNDMIN':
            if compoundmin is not None:
                print(f'ERROR: Duplicate COMPOUNDMIN in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            compoundmin = flag
            continue
        if option == 'COMPOUNDBEGIN':
            if compoundbegin is not None:
                print(f'ERROR: Duplicate COMPOUNDBEGIN in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            compoundbegin = flag
            continue
        if option == 'COMPOUNDMIDDLE':
            if compoundmiddle is not None:
                print(f'ERROR: Duplicate COMPOUNDMIDDLE in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            compoundmiddle = flag
            continue
        if option == 'COMPOUNDEND':
            if compoundend is not None:
                print(f'ERROR: Duplicate COMPOUNDEND in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            compoundend = flag
            continue
        if option == 'COMPOUNDPERMITFLAG':
            if compoundpermitflag is not None:
                print(f'ERROR: Duplicate COMPOUNDPERMITFLAG in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            compoundpermitflag = flag
            continue
        if option == 'ONLYINCOMPOUND':
            if onlyincompound is not None:
                print(f'ERROR: Duplicate ONLYINCOMPOUND in line {line_nr}:'
                      f' {line}')
                continue
            flag = fields[1]
            flags_all.add(flag)
            onlyincompound = flag
            continue
        if option == 'COMPOUNDRULE':
            if in_compoundrule:
                flags = fields[1].split('\t')[0][1:-1].split(')(')
                for flag in flags:
                    flags_all.add(flag)
                in_compoundrule -= 1
            else:
                in_compoundrule = int(fields[1])
            continue

        if option == 'CHECKCOMPOUNDPATTERN':
            if in_checkcompoundpattern:
                flag1 = fields[1]
                flag2 = fields[2].split('\t')[0]
                if flag1[0] == '/':
                    flags_all.add(flag1[1:])
                if flag2[0] == '/':
                    flags_all.add(flag2[1:])
                in_checkcompoundpattern -= 1
            else:
                in_checkcompoundpattern = int(fields[1])
            continue

        if option == 'OCONV':
            if in_oconv:
                oconvs[fields[1]] = fields[2]
                in_oconv -= 1
            else:
                in_oconv = int(fields[1])
            continue

        if in_pfx:
            if option == 'PFX':
                flag_prev = flag
                flag = fields[1]
                flags_all.add(flag)
                if flag == flag_prev:
                    pfxs[flag][fields[4]] = fields[2], fields[3].split('-/')[0].split('/')[0]
                else:
                    flags_all.add(flag)
                    pfxs[flag] = {}
                    in_pfx = int(fields[3])
            else:
                in_pfx = 0
        else:
            if option == 'PFX':
                flag = fields[1]
                flags_all.add(flag)
                pfxs[flag] = {}
                in_pfx = int(fields[3])

        if in_sfx:
            if option == 'SFX':
                flag_prev = flag
                flag = fields[1]
                flags_all.add(flag)
                if flag == flag_prev:
                    sfxs[flag][fields[4]] = fields[2], fields[3].split('-/')[0].split('/')[0]
                else:
                    flags_all.add(flag)
                    sfxs[flag] = {}
                    in_sfx = int(fields[3])
            else:
                in_sfx = 0
        else:
            if option == 'SFX':
                flag = fields[1]
                flags_all.add(flag)
                sfxs[flag] = {}
                in_sfx = int(fields[3])

    expansions = {}
    for line in open(f'{args}.dic'):  # pylint: disable=R1702
        line_nr += 1
        line = line.strip().split('\t')[0]
        if line == '' or line.startswith('#'):
            continue
        flags = None
        if '/' in line and '\\/' not in line:  # can be improved for 'km\/h/Xx'
            words = set()  # pylint: disable=W0612
            word, flags = line.split('/')
            if len(flags) % 2 != 0:
                print(f'ERROR: Uneven characters for flags {flags} on line {line_nr}: {line}')
            flags = [flags[i:i + 2] for i in range(0, len(flags), 2)]
            for flag in flags:
                if flag not in flags_all:
                    if flag not in flags_undefined:
                        flags_undefined[flag] = 1
                    flags_undefined[flag] += 1
                    continue
                if flag in pfxs:
                    for condition, values in pfxs[flag].items():
                        strip, append = values
                        if match('^' + condition + '.*', word):
                            if flag not in expansions:
                                expansions[flag] = {}
                            if condition not in expansions[flag]:
                                expansions[flag][condition] = []
                            expansion = word
                            if strip != '0':
                                if expansion.startswith(strip):
                                    expansion = expansion[len(strip):]
                                else:
                                    no_strip.add(f'WARNING: For prefix of {oconv(word)} with flag {flag} and condition {condition}, could not strip {strip}')
                                # word = '{}<strong>{}</strong>'.format(word[:-len(strip)], word[-len(strip):])  # pylint: disable=C0301
                            bare = f'{append}{expansion}'
                            expansion = '<strong>{}</strong>{}'.format(append, expansion)
                            blue = 0
                            obare = oconv(bare)
                            if obare not in wordlist:
                                if obare not in wordlist_new_i:
                                    wordlist_new_i[obare] = set()
                                wordlist_new_i[obare].add(word)
                                blue = 2
                            oword = oconv(word)
                            if oword not in wordlist and oword not in wordlist_new_l:
                                wordlist_new_l.add(oword)
                                if blue == 0:
                                    blue = 1
                                else:
                                    blue = 3
                            # word = word.replace('</strong><strong>', '')
                            expansion = expansion.replace('</strong><strong>', '')
                            expansions[flag][condition].append((word, expansion, blue))
                elif flag in sfxs:
                    for condition, values in sfxs[flag].items():
                        strip, append = values
                        if match('.*' + condition + '$', word):
                            if flag not in expansions:
                                expansions[flag] = {}
                            if condition not in expansions[flag]:
                                expansions[flag][condition] = []
                            expansion = word
                            if strip != '0':
                                if expansion.endswith(strip):
                                    expansion = expansion[:-len(strip)]
                                else:
                                    no_strip.add(f'WARNING: For suffix of {oconv(word)} with flag {flag} and condition {condition}, could not strip {strip}')
                                # word = '{}<strong>{}</strong>'.format(word[:-len(strip)], word[-len(strip):])  # pylint: disable=C0301
                            bare = f'{expansion}{append}'
                            expansion += '<strong>{}</strong>'.format(append)
                            blue = 0
                            obare = oconv(bare)
                            if obare not in wordlist:
                                if obare not in wordlist_new_i:
                                    wordlist_new_i[obare] = set()
                                wordlist_new_i[obare].add(word)
                                blue = 2
                            oword = oconv(word)
                            if oword not in wordlist and oword not in wordlist_new_l:
                                wordlist_new_l.add(oword)
                                if blue == 0:
                                    blue = 1
                                else:
                                    blue = 3
                            # word = word.replace('</strong><strong>', '')
                            expansion = expansion.replace('</strong><strong>', '')
                            expansions[flag][condition].append((word, expansion, blue))
        else:
            if '\\/' in line:
                word = line.replace('\\/', '/')
            else:
                word = line
            # print(word)

    now = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now())

    header = '''\
<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8" />
<title>{0}</title>
<style>
* {{font-family: monospace, monospace;}}
textarea {{line-height: 150%;}}
</style>
</head>
<body>
<h1>{0}</h1>
{1} {2} against word list of {3} words, datetimeversion {4}'''

    footer = '''</html>'''

    html_ind = open('index.html', 'w')
    html_ind.write(header.format('Index', now, args, len(wordlist), datetimeversion))

    html_com = open('compounds.html', 'w')
    html_com.write(header.format('Compounds', now, args, len(wordlist), datetimeversion))

    html_adj = open('adjectives.html', 'w')
    html_adj.write(header.format('Adjectives', now, args, len(wordlist), datetimeversion))

    html_ver = open('verbs.html', 'w')
    html_ver.write(header.format('Verbs', now, args, len(wordlist), datetimeversion))

    html_nou = open('nouns.html', 'w')
    html_nou.write(header.format('Nouns', now, args, len(wordlist), datetimeversion))

    html_pro = open('proper-nouns.html', 'w')
    html_pro.write(header.format('Proper Nouns', now, args, len(wordlist), datetimeversion))

    html = None
    for flag, conditions in sorted(expansions.items()):
        if flag[0] == 'C':
            html = html_com
        elif flag[0] == 'A':
            html = html_adj
        elif flag[0] == 'V':
            html = html_ver
        elif flag[0] in ('Y', 'Z') or flag[0] in ('P') and flag.upper() != flag:
            html = html_nou
        elif flag[0] in ('P') and flag.upper() == flag:
            html = html_pro
        else:
            print(f'TODO report on flag {flag}')
            continue
        html.write('<h2>Flag "{}"</h2>\n'.format(flag))
        if flag[0] == 'C':
            continue
        for condition, triples in sorted(conditions.items()):
            html.write('<h3>Flag "{}" with condition "{}"</h3>\n'.format(flag, condition))
            html.write('<table>\n<tr><th>word</th><th>expansion</th><th>spell check</th></tr>\n')
            first = True
            exps = []
            for triple in sorted(triples):
                exps.append(oconv(triple[1].replace('<strong>', '').replace('</strong>', '')))
            exps = '\n'.join(exps)
            for triple in sorted(triples):
                if first:
                    first = False
                    if triple[2] == 1:
                        html.write('<tr><td><font color="blue">{}</font></td><td><font color="blue">{}</font></td><td rowspan="{}">'
                                       '<textarea data-lt-active="false" cols="50"'
                                       ' rows="{}">{}</textarea></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1]),
                                               len(triples), len(triples), exps))
                    elif triple[2] == 2:
                        html.write('<tr><td>{}</td><td>{}</td><td rowspan="{}">'
                                       '<textarea data-lt-active="false" cols="50"'
                                       ' rows="{}">{}</textarea></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1]),
                                               len(triples), len(triples), exps))
                    elif triple[2] == 3:
                        html.write('<tr><td><font color="blue">{}</font></td><td><font color="blue">{}</font></td><td rowspan="{}">'
                                       '<textarea data-lt-active="false" cols="50"'
                                       ' rows="{}">{}</textarea></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1]),
                                               len(triples), len(triples), exps))
                    else:
                        html.write('<tr><td>{}</td><td>{}</td><td rowspan="{}">'
                                       '<textarea data-lt-active="false" cols="50"'
                                       ' rows="{}">{}</textarea></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1]),
                                               len(triples), len(triples), exps))
                else:
                    if triple[2] == 1:
                        html.write('<tr><td><font color="blue">{}</font></td><td>{}</td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1])))
                    elif triple[2] == 2:
                        html.write('<tr><td>{}</td><td><font color="blue">{}</font></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1])))
                    elif triple[2] == 3:
                        html.write('<tr><td><font color="blue">{}</font></td><td><font color="blue">{}</font></td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1])))
                    else:
                        html.write('<tr><td>{}</td><td>{}</td></tr>\n'
                                       .format(oconv(triple[0]),
                                               oconv(triple[1])))

            html.write('</table>\n')
            
    html_com.write(footer)
    html_adj.write(footer)
    html_ver.write(footer)
    html_nou.write(footer)
    html_pro.write(footer)

    html_ind.write('<h2>Missing lemmas from wordlist</h2>\n')
    html_ind.write(f'{len(wordlist_new_l)} lemmas')
    html_ind.write('<pre>')
    first = True
    for word in sorted(wordlist_new_l):
        if first:
            first = False
        else:
            html_ind.write('\n')
        html_ind.write(f'{word}')
    html_ind.write('</pre>\n')

    html_ind.write('<h2>Missing inflections from wordlist</h2>\n')
    html_ind.write(f'{len(wordlist_new_i)} inflections')
    html_ind.write('<pre>')
    outer_first = True
    for word, bases in sorted(wordlist_new_i.items()):
        if outer_first:
            outer_first = False
        else:
            html_ind.write('\n')
        html_ind.write(f'{word}\t')
        inner_first = True
        for base in sorted(bases):
            if inner_first:
                inner_first = False
            else:
                html_ind.write(';')
            html_ind.write(f'{oconv(base)}')
    html_ind.write('</pre>\n')

    html_ind.write('<h2>Undefined flags</h2>\n')
    html_ind.write('<pre>')
    first = True
    for key, value in sorted(flags_undefined.items()):
        if first:
            first = False
        else:
            html_ind.write('\n')
        html_ind.write(f'WARNING: Undefined flag {key} found {value} times')
    html_ind.write('</pre>\n')

    html_ind.write('<h2>Could not strip</h2>\n')
    html_ind.write('<pre>')
    first = True
    for message in sorted(no_strip):
        if first:
            first = False
        else:
            html_ind.write('\n')
        html_ind.write(message)
    html_ind.write('</pre>\n')

    html_ind.write(footer)

    #        w = ''
    #        e = ''
    #        for i, s in enumerate(ndiff(word, expansion)):
    #            if s[0] == ' ':
    #                w += s[-1]
    #                e += s[-1]
    #            elif s[0] == '-':
    #                w += '**{}**'.format(s[-1])
    #            else:
    #                e += '**{}**'.format(s[-1])


if __name__ == "__main__":
    main('/var/tmp/nl')
