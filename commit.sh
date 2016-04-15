#!/bin/bash

cd /var/streak
git add _*
git commit -m $(date +%s)
git push
