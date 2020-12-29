if [ -z $(which hunspell) ]; then
	echo 'Please, install Hunspell with sudo apt-get install hunspell'
	exit 1
fi

wc -l *txt

hunspell -d ../nl -L -1 ../elements/stress.tsv > stress-hunspell-failed.txt
hunspell -d ../nl -G -1 ../elements/excluded.tsv > excluded-hunspell-failed.txt
hunspell -d ../nl -L -1 ../../opentaal-wordlist/elements/wordparts.tsv > wordparts-hunspell-failed.txt
#hunspell -d ../nl -L -1 ../elements/obsolete.tsv > obsolete-hunspell-failed.txt
#hunspell -d ../nl -G -1 ../elements/outdated.tsv > outdated-hunspell-failed.txt
hunspell -d ../nl -G -1 ../../opentaal-wordlist/elements/corrections.tsv > corrections-hunspell-failed.txt
hunspell -d ../nl -L    ../../opentaal-wordlist/wordlist.txt > wordlist-hunspell-failed.txt
#TODO remove excluded from last file

if [ -z $(which nuspell) ]; then
	echo 'Please, install Nuspell (from their PPA) with sudo apt-get install nuspell'
fi

#awk -F '\t' '{print $1}' ../elements/stress.tsv > tmp && nuspell -d ../nl -L tmp > stress-nuspell-failed.txt 2> /dev/null
#awk -F '\t' '{print $1}' ../elements/excluded.tsv > tmp && nuspell -d ../nl -L tmp > excluded-nuspell-failed.txt 2> /dev/null
#awk -F '\t' '{print $1}' ../../opentaal-wordlist/elements/wordparts.tsv > tmp && nuspell -d ../nl -L tmp > wordparts-nuspell-failed.txt 2> /dev/null
##awk -F '\t' '{print $1}' ../elements/obsolete.tsv > tmp && nuspell -d ../nl -L tmp > obsolete-nuspell-failed.txt 2> /dev/null
##awk -F '\t' '{print $1}' ../elements/outdated.tsv > tmp && nuspell -d ../nl -G tmp > outdated-nuspell-failed.txt 2> /dev/null
#awk -F '\t' '{print $1}' ../../opentaal-wordlist/elements/corrections.tsv > tmp && nuspell -d ../nl -G tmp > corrections-nuspell-failed.txt 2> /dev/null
#nuspell -d ../nl -l    ../../opentaal-wordlist/wordlist.txt > wordlist-nuspell-failed.txt 2> /dev/null
#TODO remove excluded from last file

#rm -f tmp

wc -l *txt
