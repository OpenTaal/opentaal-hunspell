hunspell -d ../nl -G -1 ../elements/obsolete.tsv > obsolete-failed.txt
hunspell -d ../nl -G -1 ../elements/outdated.tsv > outdated-failed.txt
hunspell -d ../nl -L -1 ../elements/stress.tsv > stress-failed.txt
hunspell -d ../nl -L -1 ../../opentaal-wordlist/wordparts.tsv > wordparts-failed.txt
hunspell -d ../nl -G -1 ../../opentaal-wordlist/corrections.tsv > corrections-failed.txt
hunspell -d ../nl -L    ../../opentaal-wordlist/wordlist.txt > wordlist-failed.txt
#TODO remove excluded from last file
