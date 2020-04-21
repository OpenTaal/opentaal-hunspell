cd ../downloads
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

# affix file
cp -f ../parts/header.aff ../nl.aff

echo >> ../nl.aff
echo '# replacements for improving suggestions' >> ../nl.aff
echo REP $(cat replacements.tsv | wc -l) >> ../nl.aff
awk -F '\t' '{print "REP "$1" "$2"\t# "$3}' replacements.tsv | sed -e 's/\t# $//g' >> ../nl.aff

echo >> ../nl.aff
cat ../parts/compounds.aff >> ../nl.aff

echo >> ../nl.aff
cat ../parts/affixes.aff >> ../nl.aff

#TODO rest of this script to create .dic file
# dictionary file
rm -f ../nl.dic
for i in $(cat stress.tsv|awk -F '\t' '{print $2}'); do
	echo $i/NS >> ../nl.dic
done
cat ../parts/numbers.dic >> ../nl.dic
cat ../parts/romannumbers.dic >> ../nl.dic

IFS=$SAVEIFS
cd ../scripts
