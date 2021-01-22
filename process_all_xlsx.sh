#!/bin/sh

if [ -z "$1" ]
then
  OUTPUT_DIR="/github/workspace/grupoetra"
else
  OUTPUT_DIR="$1"
fi

mkdir -p ${OUTPUT_DIR}

INPUT_DIR="/excel2xml/excel2xml-input/excel-use-cases"

find $INPUT_DIR -type f -name '*.xlsx' -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  INPUT_DIR="$2"
  BASENAME=$(basename "$FILE" .xlsx | tr '[:blank:]' '_')
  NO_PREFIX="${FILE##$INPUT_DIR}"
  BASEPATH=$(dirname "$NO_PREFIX")
  DIRNAME=$(echo "${BASEPATH}" | tr '[:blank:]' '_')
  mkdir -p ${OUTPUT_DIR}/${DIRNAME}
  OUTPUT_FILE_NAME="${OUTPUT_DIR}${DIRNAME}/${BASENAME}.xml"
  echo "$OUTPUT_FILE_NAME"
  python3 /excel2xml/xlsx2xml.py "$FILE" > "$OUTPUT_FILE_NAME"
' {} ${OUTPUT_DIR} ${INPUT_DIR} ';'
