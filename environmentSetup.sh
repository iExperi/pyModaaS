#!/bin/sh
projectDir=$1
sudo mkdir -p $1
sudo python $projectDir/get-pip.py
sudo pip install virtualenv
cd $projectDir
virtualenv venv
virtualenv -p /usr/bin/python venv
