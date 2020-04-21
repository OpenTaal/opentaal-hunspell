set -e
cd ..

if [ ! -e comparisons ]; then
	mkdir comparisons
fi

grep -v ^# nl.aff | sed -e 's/\s#.*//g' | sed -e '/^\s*$/d' > comparisons/new.aff
grep -v ^# downloads/nl.aff | sed -e 's/\s#.*//g' | sed -e '/^\s*$/d' > comparisons/prv.aff

# omit first line with total number of words
tail -n +2 nl.dic | sort > comparisons/new.dic
tail -n +2 downloads/nl.dic | sort > comparisons/prv.dic

cd comparisons
diff -ub prv.aff new.aff > aff_prv_new.diff
# next lines open a web browser!
diff2html -s side -F aff_prv_new.html -i file -- aff_prv_new.diff &

#TODO only later with less differences, too heavy now
#diff -ub prv.dic new.dic > dic_prv_new.diff
#diff2html -s side -F dic_prv_new.html -i file -- dic_prv_new.diff &

cd ../scripts
