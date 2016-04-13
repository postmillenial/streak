#!/bin/bash


lines=$(ps -ef | grep streak.py | wc -l)

if [ $lines -ne 2 ]; then
    python /var/streak/streak.py 2>&1 | logger &
fi
git add _*
git commit -m $(date +%s)
git push
