cd ..
for i in ?.?; do
	echo $i
	cd $i
	grep -v ^# nl.aff | sed -e 's/\s#.*//g' | sed -e '/^\s*$/d' > nl_stripped.aff
	cd ..
done
diff -b 2.1/nl_stripped.aff 2.2/nl_stripped.aff | more
