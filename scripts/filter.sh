grep ^[A-Z] wordlist-hunspell-failed.txt\
|grep -v ^CD|grep -v ^CI|grep -v ^CL|grep -v ^CM|grep -v ^CV|grep -v ^CX\
|grep -v ^DC|grep -v ^DI|grep -v ^DL|grep -v ^DV|grep -v ^DX\
|grep -v ^LI|grep -v ^LV|grep -v ^LX\
|grep -v ^MC|grep -v ^MD|grep -v ^MI|grep -v ^ML|grep -v ^MM|grep -v ^MV|grep -v ^MX\
>/tmp/a
grep ^[^A-Z] wordlist-hunspell-failed.txt>>/tmp/a

