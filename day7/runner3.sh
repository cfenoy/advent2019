#!/bin/bash

max=0

seq=$1

#for i in `seq 0 4`;do
for i in `seq 5 9`;do
  for j in `seq 5 9`;do
    if [[ $j -eq $i ]];then
            continue
    fi
    for k in `seq 5 9`;do
      if [ $k -eq $j -o $k -eq $i ];then
              continue
      fi
      for l in `seq 5 9`;do
        if [ $l -eq $k -o $l -eq $j -o $l -eq $i ];then
                continue
        fi
        for m in `seq 5 9`;do
          if [ $m -eq $l -o $m -eq $k -o $m -eq $j -o $m -eq $i ];then
                  continue
          fi
          echo run 
          ./code1.py < f1 >f2& echo -e "$i\n0" >f1
          ./code1.py < f2 >f3& echo "$j" > f2
          ./code1.py < f3 >f4& echo "$k" > f3
          ./code1.py < f4 >f5& echo "$l" > f4
          out5=`./code1.py < f5 | tee f1 | awk -v max=0 '{if($1>max){max=$1}}END{print max}' & echo "$m" > f5`
          if [[ $out5 -gt $max ]];then
                  max=$out5
          fi
          wait
        done
      done
    done
  done
done
echo $max
