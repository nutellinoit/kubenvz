#!/bin/bash

echo "Switching $1 to $2 version"

filepath="$HOME/.kubenvz/$1_$2"

if [ -f "$filepath" ]; then
    echo "$1 to $2 version exist, relinking..."
    rm /usr/local/bin/$1
    ln -s $filepath /usr/local/bin/$1
    chmod +x /usr/local/bin/$1
    echo "done!"

else
    echo "$1 to $2 version is not installed. run kubenvz $1 install $2 . Run kubenvz $1 list remote for the correct version to use"
fi

