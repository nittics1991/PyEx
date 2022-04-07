#!/bin/bash

sudo apt install -y python3-pip python3-uno

pip install pyoo

if [[ ! -d ~/.config/libreoffice/4/user/python ]] ;
then
    mkdir -p ~/.config/libreoffice/4/user/python
    echo ..create script path
fi


