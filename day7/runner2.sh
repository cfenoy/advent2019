#!/bin/bash

max=0

seq=$1

out1=`echo -e "0\n0" | ./code1.py`
out2=`echo -e "1\n$out1" | ./code1.py`
out3=`echo -e "2\n$out2" | ./code1.py`
out4=`echo -e "3\n$out3" | ./code1.py`
out5=`echo -e "4\n$out4" | ./code1.py`
echo $out5
