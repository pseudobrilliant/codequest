#! /usr/bin/bash

dir_name=${1//[-]/_}
mkdir -p $dir_name
top_dir=$PWD
cd $dir_name
wget "https://lmcodequestacademy.com/api/static/problems/$1" -O "$dir_name.pdf"
cp "$top_dir/template.py" "$dir_name.py"
touch "input.txt"
cd $top_dir
