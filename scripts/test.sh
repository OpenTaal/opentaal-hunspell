if [ -z $(which hunspell) ]; then
	echo 'Please, install Hunspell with sudo apt-get install hunspell'
	exit 1
fi

echo Pre
wc -l *.txt

hunspell -d ../nl -l -1 ../elements/stress.tsv > stress-hunspell-failed.txt
hunspell -d ../nl -G -1 ../elements/excluded.tsv > excluded-hunspell-failed.txt
hunspell -d ../nl -l -1 ../../opentaal-wordlist/elements/wordparts.tsv > wordparts-hunspell-failed.txt
hunspell -d ../nl -G -1 ../../opentaal-wordlist/elements/corrections.tsv > corrections-hunspell-failed.txt
sort ../../opentaal-wordlist/wordlist.txt > tmp1
awk -F '\t' '{print $1}' ../elements/excluded.tsv | sort > tmp2
/usr/bin/diff tmp1 tmp2 | /bin/grep \< | sed -e 's/^..//' > tmp3
hunspell -d ../nl -L tmp3 > wordlist-hunspell-failed.txt
rm -f tmp?

if [ -z $(which nuspell) ]; then
	echo 'Please, install Nuspell (from their PPA) with sudo apt-get install nuspell'
fi

awk -F '\t' '{print $1}' ../elements/stress.tsv > tmp && nuspell -d ../nl -l tmp > stress-nuspell-failed.txt 2> /dev/null
awk -F '\t' '{print $1}' ../elements/excluded.tsv > tmp && nuspell -d ../nl -G tmp > excluded-nuspell-failed.txt 2> /dev/null
#awk -F '\t' '{print $1}' ../../opentaal-wordlist/elements/wordparts.tsv > tmp && nuspell -d ../nl -L tmp > wordparts-nuspell-failed.txt 2> /dev/null
#awk -F '\t' '{print $1}' ../../opentaal-wordlist/elements/corrections.tsv > tmp && nuspell -d ../nl -G tmp > corrections-nuspell-failed.txt 2> /dev/null
#nuspell -d ../nl -l    ../../opentaal-wordlist/wordlist.txt > wordlist-nuspell-failed.txt 2> /dev/null
rm -f tmp

echo Post
wc -l *.txt
