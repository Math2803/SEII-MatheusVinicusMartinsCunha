#!/bin/bash

echo Hello Word > hello.txt
echo Good day to you! >> hello.txt
cat hello.txt

wc -w < hello.txt
cat << EOF
inicio do texto
meio do texto
fim do texto
EOF

wc -w <<< "HELLO HOW ARE YOU?"
