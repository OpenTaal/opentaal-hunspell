SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

cd ../download

# afix file
cp -f ../2.2/nl_head.aff ../2.2/nl.aff

echo >> ../2.2/nl.aff
echo '# replacements for improving suggestions' >> ../2.2/nl.aff
echo REP `cat rep.tsv | wc -l` >> ../2.2/nl.aff
awk -F '\t' '{print "REP "$1" "$2"\t# "$3}' rep.tsv | sed -e 's/\t# $//g' >> ../2.2/nl.aff

# dictionary file
rm -f ../2.2/nl.dic
for i in `cat woorden-met-klemtoonteken.txt`; do
	echo $i/NS >> ../2.2/nl.dic
done

cd ../tools

IFS=$SAVEIFS
