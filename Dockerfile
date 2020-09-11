from alpine:latest

run apk update
run apk add python3 py3-pip
run /usr/bin/pip3 install pyxb openpyxl
copy . /excel2xml
copy excel2xml-input/grupoetra/*.xlsx /excel2xml/
workdir /excel2xml
cmd ls /excel2xml && python3 /excel2xml/xlsx2xml.py
