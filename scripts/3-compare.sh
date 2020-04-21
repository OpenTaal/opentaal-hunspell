set -e
cd ..

if [ ! -e comparisons ]; then
	mkdir comparisons
fi

# remove lines with only comments and empty lines
grep -v ^# nl.aff | grep -v ^$ > comparisons/new.aff
grep -v ^# downloads/nl.aff | grep -v ^$ > comparisons/prv.aff

# omit first line with total number of words
#tail -n +2 nl.dic | sort > comparisons/new.dic
#tail -n +2 downloads/nl.dic | sort > comparisons/prv.dic

cd comparisons
diff -ub prv.aff new.aff > aff_prv_new.diff
diff2html -s side -o stdout -i file -- aff_prv_new.diff > aff_prv_new.html

#TODO only later with less differences, too heavy now
#diff -ub prv.dic new.dic > dic_prv_new.diff
#diff2html -s side -F dic_prv_new.html -i file -- dic_prv_new.diff &

cd ../scripts
