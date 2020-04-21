#!/usr/bin/env python3

#from difflib import ndiff

def oconv(word):
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

# self-check
for option in options_general:
    if option in options_suggest:
        print('ERROR: Overlap general and suggest')
        exit(1)
    if option in options_compounding:
        print('ERROR: Overlap general and compounding')
        exit(1)
    if option in options_affix:
        print('ERROR: Overlap general and affix')
        exit(1)
    if option in options_other:
        print('ERROR: Overlap general and other')
        exit(1)
    if option in options_deprecated:
        print('ERROR: Overlap general and deprecated')
        exit(1)
    if option in options_undocumented:
        print('ERROR: Overlap general and undocumented')
        exit(1)
for option in options_suggest:
    if option in options_compounding:
        print('ERROR: Overlap suggest and compounding')
        exit(1)
    if option in options_affix:
        print('ERROR: Overlap suggest and affix')
        exit(1)
    if option in options_affix:
        print('ERROR: Overlap suggest and other')
        exit(1)
    if option in options_deprecated:
        print('ERROR: Overlap suggest and deprecated')
        exit(1)
    if option in options_undocumented:
        print('ERROR: Overlap suggest and undocumented')
        exit(1)
for option in options_compounding:
    if option in options_affix:
        print('ERROR: Overlap compounding and affix')
        exit(1)
    if option in options_other:
        print('ERROR: Overlap compounding and other')
        exit(1)
    if option in options_deprecated:
        print('ERROR: Overlap compounding and deprecated')
        exit(1)
    if option in options_undocumented:
        print('ERROR: Overlap compounding and undocumented')
        exit(1)
for option in options_affix:
    if option in options_other:
        print('ERROR: Overlap affix and other')
        exit(1)
    if option in options_deprecated:
        print('ERROR: Overlap affix and deprecated')
        exit(1)
    if option in options_undocumented:
        print('ERROR: Overlap affix and undocumented')
        exit(1)
for option in options_other:
    if option in options_deprecated:
        print('ERROR: Overlap other and deprecated')
        exit(1)
    if option in options_undocumented:
        print('ERROR: Overlap other and undocumented')
        exit(1)
for option in options_deprecated:
    if option in options_undocumented:
        print('ERROR: Overlap deprecated and undocumented')
        exit(1)

flags_all = set()
oconvs = {}
sfxs = {}
pfxs = {}
comment = None
in_oconv = 0
in_sfx = 0
in_pfx = 0
in_compoundrule = 0
in_checkcompoundpattern = 0
flag = None
flag_prev = ''
line_nr = 0
keepcase = None
warn = None
forceucase = None
forbiddenword = None
nosuggest = None
compoundbegin = None
compoundmiddle = None
compoundend = None
compoundpermitflag = None
onlyincompound = None
unused_flags = ('C0', 'CQ')

lang = 'nl'

for line in open('../2.1/{}.aff'.format(lang)):
    line_nr += 1
    line = line.replace('\t', ' ').strip()
    if line == '':
        continue
    if line.startswith('#'):
        comment = line
        continue
# 	while '  ' in line:  # TODO
# 		line = line.replace('  ', ' ')
# 	while '\t' in line:  # TODO report?
# 		line = line.replace('\t', ' ')
    fields = line.split(' ')
    option = fields[0]
    if option not in options_general and option not in options_suggest and option not in options_compounding and option not in options_affix and option not in options_other and option not in options_undocumented and option not in options_deprecated:
        print('ERROR: Unknown option {} found in line {}'.format(option, line_nr))
        exit(1)

    if option == 'KEEPCASE':
        flag = fields[1]
        flags_all.add(flag)
        keepcase = flag
        continue
    if option == 'WARN':
        flag = fields[1]
        flags_all.add(flag)
        warn = flag
        continue
    if option == 'FORCEUCASE':
        flag = fields[1]
        flags_all.add(flag)
        forceucase = flag
        continue
    if option == 'FORBIDDENWORD':
        flag = fields[1]
        flags_all.add(flag)
        forbiddenword = flag
        continue
    if option == 'NOSUGGEST':
        flag = fields[1]
        flags_all.add(flag)
        nosuggest = flag
        continue
    if option == 'COMPOUNDBEGIN':
        flag = fields[1]
        flags_all.add(flag)
        compoundbegin = flag
        continue
    if option == 'COMPOUNDMIDDLE':
        flag = fields[1]
        flags_all.add(flag)
        compoundmiddle = flag
        continue
    if option == 'COMPOUNDEND':
        flag = fields[1]
        flags_all.add(flag)
        compoundend = flag
        continue
    if option == 'COMPOUNDPERMITFLAG':
        flag = fields[1]
        flags_all.add(flag)
        compoundpermitflag = flag
        continue
    if option == 'ONLYINCOMPOUND':
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
                pass # print('__', fields[1])
            else:
                in_pfx = int(fields[3])
#                if comment:
#                    print('PFX {} {} {}'.format(flag, in_pfx, comment))
#                else:
#                    print('PFX {} {}'.format(flag, in_pfx))
            if flag in pfxs:
                if len(fields) == 4:
                    fields.append('.')  # workaround
                pfxs[flag][fields[4]] = fields[2], fields[3]
            else:
                pfxs[flag] = {}
        else:
            in_pfx = 0
    else:
        if option == 'PFX':
            in_pfx = int(fields[3])
            flag = fields[1]
            flags_all.add(flag)
#            if comment:
#                print('PFX {} {} {}'.format(flag, in_pfx, comment))
#            else:
#                print('PFX {} {}'.format(flag, in_pfx))
            if flag in pfxs:
                pfxs[flag][fields[4]] = fields[2], fields[3]
            else:
                pfxs[flag] = {}
        else:
            pass

    if in_sfx:
        if option == 'SFX':
            flag_prev = flag
            flag = fields[1]
            flags_all.add(flag)
            if flag == flag_prev:
                pass # print('__', fields[1])
            else:
                in_sfx = int(fields[3])
#                if comment:
#                    print('SFX {} {} {}'.format(flag, in_sfx, comment))
#                else:
#                    print('SFX {} {}'.format(flag, in_sfx))
            if flag in sfxs:
                if len(fields) == 4:
                    fields.append('.')  # workaround
                sfxs[flag][fields[4]] = fields[2], fields[3]
            else:
                sfxs[flag] = {}
        else:
            in_sfx = 0
    else:
        if option == 'SFX':
            in_sfx = int(fields[3])
            flag = fields[1]
            flags_all.add(flag)
#            if comment:
#                print('SFX {} {} {}'.format(flag, in_sfx, comment))
#            else:
#                print('SFX {} {}'.format(flag, in_sfx))
            if flag in sfxs:
                sfxs[flag][fields[4]] = fields[2], fields[3]
            else:
                sfxs[flag] = {}
        else:
            pass
        comment = None
   

expansions = {}   
for line in open('../2.1/{}.dic'.format(lang)):
    line_nr += 1 
    line = line.strip().split('\t')[0]
    if line == '' or line.startswith('#'):
        continue
    flags = None
    if '/' in line and '\/' not in line:  # can be improved for 'km\/h/Xx'
        words = set()
        word, flags = line.split('/')
        flags = [flags[i:i + 2] for i in range(0, len(flags), 2)]
        if word == 'melodieus':
            print('XXXXX', flags)
        for flag in flags:
#            if flag not in flags_all and flag not in unused_flags:
#                print('WARNING: Unknown flag {} for word {}'.format(flag, word))
#                continue
            if flag in sfxs and flag[0] == 'A':
                print(flag)
                for condition, values in sfxs[flag].items():
                    strip, append = values
                    if (condition == '.' or word.endswith(condition)) and word.endswith(strip): #uitsplitsen
                        if flag not in expansions:
                            expansions[flag] = {}
                        if condition not in expansions[flag]:
                            expansions[flag][condition] = []
                        expansion = word
                        if condition != '.':
                            expansion = expansion[:-len(strip)]
#                            word = '{}<strong>{}</strong>'.format(word[:-len(strip)], word[-len(strip):])
                        expansion += '<strong>{}</strong>'.format(append)
                        word = word.replace('</strong><strong>', '')
                        expansion = expansion.replace('</strong><strong>', '')
                        expansions[flag][condition].append((word, expansion))
    else:
        if '\/' in line:
            word = line.replace('\/', '/')
        else:
            word = line
# 		print(word)


header = '''<!DOCTYPE html>
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
<h1>{0}</h1>'''
            
footer = '''</html>'''

html = open('adjectives.html', 'w')
html.write(header.format('Adjectives'))
for flag, conditions in sorted(expansions.items()):
    html.write('<h2>Flag "{}"</h2>\n'.format(flag))
    for condition, pairs in sorted(conditions.items()):
        html.write('<h3>Flag "{}" with condition "{}"</h3>\n'.format(flag, condition))
        html.write('<table>\n<tr><th>word</th><th>expansion</th><th>spell check</th></tr>\n')
        first = True
        exps = []
        for pair in sorted(pairs):
            exps.append(oconv(pair[1].replace('<strong>', '').replace('</strong>', '')))
        exps = '\n'.join(exps)
        for pair in sorted(pairs):
            if first:
                first = False
                html.write('<tr><td>{}</td><td>{}</td><td rowspan="{}"><textarea data-lt-active="false" cols="50" rows="{}">{}</textarea></td></tr>\n'.format(oconv(pair[0]), oconv(pair[1]), len(pairs), len(pairs), exps))
            else:
                html.write('<tr><td>{}</td><td>{}</td></tr>\n'.format(oconv(pair[0]), oconv(pair[1])))
            
        html.write('</table>\n')
html.write(footer)
    
    
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

