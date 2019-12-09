#!/bin/bash

max=0

seq=$1

mkfifo f1 f2 f3 f4 f5

#for i in `seq 0 4`;do
for i in $seq;do
  out1=`echo -e "$i\n0" | ./code1.py`
  for j in `seq 0 4`;do
    if [[ $j -eq $i ]];then
            continue
    fi
    out2=`echo -e "$j\n$out1" | ./code1.py`
    for k in `seq 0 4`;do
      if [ $k -eq $j -o $k -eq $i ];then
              continue
      fi
      out3=`echo -e "$k\n$out2" | ./code1.py`
      for l in `seq 0 4`;do
        if [ $l -eq $k -o $l -eq $j -o $l -eq $i ];then
                continue
        fi
        out4=`echo -e "$l\n$out3" | ./code1.py`
        for m in `seq 0 4`;do
          if [ $m -eq $l -o $m -eq $k -o $m -eq $j -o $m -eq $i ];then
                  continue
          fi
          out5=`echo -e "$m\n$out4" | ./code1.py`
          if [[ $out5 -gt $max ]];then
                  max=$out5
          fi
          echo $i $j $k $l $m $out5
        done
      done
    done
  done
done
echo $max
rm f1 f2 f3 f4 f5
