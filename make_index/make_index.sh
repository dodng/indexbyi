#!/bin/bash

url='url.seed'
url_here='url.seed.here'

#url is exist ?
if [ ! -f "$url_here" ]; then 
    touch $url_here 
fi 

i=`wc -l $url_here | awk -F ' ' '{print $1;}'`

cat $url | while read line
do
    haveurl=`cat $url_here | grep -F "$line" | awk -F ' ' '{print $1;}'`
    if [ "$haveurl" =  "" ]; then
        i=`expr $i + 1`
#0 download url
        wget -t2 --timeout=30 -nv "$line" -O $i".html"
#1 parse_html
        python parse_html.py $i".html"
#2 seg_words content -> index.one_url
        python seg_word.py $i".html.content" $i
#3 merge index
        python merge_index.py
#4 dump breif
        python dump_brief.py $i $i".html" $line `date "+%Y-%m-%d/%H:%M:%S"`
#5 clear file
        rm -f ${i}.html*
#6 add url
        echo $line >> $url_here
    fi
done
