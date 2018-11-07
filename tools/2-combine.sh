SAVEIFS=$IFS
IFS=$(echo -en "\n\b")

cd ../download

cp -f ../2.2/nl_head.aff ../2.2/nl.aff
awk -F '\t' rep.tsv '{print $1 $2\t#$3}' >> ../2.2/nl.aff

rm -f ../2.2/nl.dic
for i in `cat woorden-met-klemtoonteken.txt`; do
	echo $i/NS >> ../2.2/nl.dic
done

cd ../tools

IFS=$SAVEIFS
