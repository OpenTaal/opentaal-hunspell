hunspell -d ../nl -G -1 ../elements/obsolete.tsv > obsolete-hunspell-failed.txt
hunspell -d ../nl -G -1 ../elements/outdated.tsv > outdated-hunspell-failed.txt
hunspell -d ../nl -L -1 ../elements/stress.tsv > stress-hunspell-failed.txt
hunspell -d ../nl -L -1 ../../opentaal-wordlist/wordparts.tsv > wordparts-hunspell-failed.txt
hunspell -d ../nl -G -1 ../../opentaal-wordlist/corrections.tsv > corrections-hunspell-failed.txt
hunspell -d ../nl -L    ../../opentaal-wordlist/wordlist.txt > wordlist-hunspell-failed.txt
#TODO remove excluded from last file

#nuspell -d ../nl -G -1 ../elements/obsolete.tsv > obsolete-nuspell-failed.txt
#nuspell -d ../nl -G -1 ../elements/outdated.tsv > outdated-nuspell-failed.txt
#nuspell -d ../nl -L -1 ../elements/stress.tsv > stress-nuspell-failed.txt
#nuspell -d ../nl -L -1 ../../opentaal-wordlist/wordparts.tsv > wordparts-nuspell-failed.txt
#nuspell -d ../nl -G -1 ../../opentaal-wordlist/corrections.tsv > corrections-nuspell-failed.txt
nuspell -d ../nl -l    ../../opentaal-wordlist/wordlist.txt > wordlist-nuspell-failed.txt
#TODO remove excluded from last file
