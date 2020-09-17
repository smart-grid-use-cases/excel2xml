from alpine:latest

run apk update
run apk add python3 py3-pip
run /usr/bin/pip3 install pyxb openpyxl
copy . /excel2xml
cmd sh /excel2xml/process_all_xlsx.sh
