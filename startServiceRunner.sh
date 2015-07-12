#!/bin/sh
dirPath=$1
ip=$2
sh $dirPath/environmentSetup.sh $dirPath
source $dirPath/venv/bin/activate
pip install web.py
pip install schedule
#python $dirPath/serviceRunner.py $ip
nohup python -u $dirPath/serviceRunner.py $ip > pyModule-aaS.log &
