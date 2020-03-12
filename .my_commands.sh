#!/bin/bash

function create() {
    cd
    source .env
    python3 create.py $1
    if [ $? -eq 0 ]
    then
        mkdir $FILEPATH$1
        cd $FILEPATH$1
        git init
        git remote add origin git@github.com:$USERNAME/$1.git
        touch README.md
        git add .
        git commit -m "Initial commit"
        git push -u origin master
        code .
    fi
}

function delete() {
    cd
    source .env
    python3 delete.py $1
}

function get() {
    cd
    source .env
    python3 get.py
}
