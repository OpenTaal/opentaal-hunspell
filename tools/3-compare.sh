cd ..
for i in ?.?; do
	echo $i
	cd $i
	grep -v ^# nl.aff | sed -e 's/\s#.*//g' | sed -e '/^\s*$/d' > nl_stripped.aff
	cd ..
done
if [ -n `which diff2html` ]; then
	diff -ub 2.1/nl_stripped.aff 2.2/nl_stripped.aff | diff2html -s side --sc enabled -i stdin -F differences_2.1_2.2.html &
fi
diff -b 2.1/nl_stripped.aff 2.2/nl_stripped.aff | more
