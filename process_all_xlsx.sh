#!/bin/sh

if [ -z "$1" ]
then
  OUTPUT_DIR="/github/workspace/grupoetra"
else
  OUTPUT_DIR="$1"
fi

mkdir -p ${OUTPUT_DIR}

find /excel2xml -type f -name '*.xlsx' -exec sh -c '
  file="$0"
  OUTPUT_DIR="$1"
  file_no_ext="${file%.xlsx}"
  DIRNAME=$(basename "${file_no_ext}" | tr '[:blank:]' '_')
  mkdir -p ${OUTPUT_DIR}/${DIRNAME}
  output_file_name="${OUTPUT_DIR}/${DIRNAME}/${DIRNAME}.xml"
  echo "$output_file_name"
  python3 /excel2xml/xlsx2xml.py "$file" > "$output_file_name"
' {} ${OUTPUT_DIR} ';'
