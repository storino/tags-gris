#!usr/bin/env bash

for line in $(cat $filename); do
    #echo $line
    nome=echo $line | awk -F ',' '{print $1}'
    idade=echo $line | awk -F ',' '{print $2}'
    if (( $idade >= 16)); then
        echo $nome
    fi
done
