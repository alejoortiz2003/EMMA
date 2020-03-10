#!/bin/bash

ini=1
fin=1501
path1=/home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/chest_xray/train/PNEUMONIA
path2=/home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/chest_xray/train/PNEUMONIA1500
cd $path1

ls -1 *.jpeg > /home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/lista

while [ $ini != $fin ]
do 
    file=`cat /home/davidalejandro/Desktop/transfer-learning-for-diagnostic-images-spanish-/lista | awk '{if (NR=='$ini') print $1}'`
    echo "$path1 .... $ini"
    echo "traferring $file...... to $file $path2/$file"
    cp $path1/$file $path2/$file
    pwd

    let ini=$ini+1
done
