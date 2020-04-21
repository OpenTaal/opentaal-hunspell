cd ..
if [ ! -e downloads ]; then
	mkdir downloads
fi
cd downloads
rm -rf *.txt *.tsv *.deb usr var nl.aff nl.dic dutch

# files new version
scp zaph:database-tools/release-hunspell/* .
wget https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/wordlist.txt
wget https://raw.githubusercontent.com/OpenTaal/opentaal-wordlist/master/corrections.tsv

# files previous version
apt-get download hunspell-nl wdutch
for i in *.deb; do
	dpkg -x $i .
done
cp -f  usr/share/hunspell/nl.* usr/share/dict/dutch .

cd ../scripts
