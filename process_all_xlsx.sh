#!/bin/sh

if [ -z "$1" ]
then
  INPUT_DIR="/excel2xml/excel2xml-input/excel-use-cases"
  export PYTHON_SCRIPT="/excel2xml/xlsx2xml.py"
else
  INPUT_DIR="$1"
  export PYTHON_SCRIPT="xlsx2xml.py"
fi

if [ -z "$2" ]
then
  OUTPUT_DIR="/github/workspace/grupoetra"
else
  OUTPUT_DIR="$2"
fi

mkdir -p ${OUTPUT_DIR}

find $INPUT_DIR -type f -name '*.xlsx' -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  INPUT_DIR="$2"
  BASENAME=$(basename "$FILE" .xlsx | tr '[:blank:]' '_')
  NO_PREFIX="${FILE##$INPUT_DIR}"
  BASEPATH=$(dirname "$NO_PREFIX")
  DIRNAME=$(echo "${BASEPATH}" | tr '[:blank:]' '_')
  mkdir -p ${OUTPUT_DIR}/${DIRNAME}
  sh process_images.sh ${INPUT_DIR}/${BASEPATH} $OUTPUT_DIR/$DIRNAME
  OUTPUT_FILE_NAME="${OUTPUT_DIR}${DIRNAME}/${BASENAME}.xml"
  echo "$OUTPUT_FILE_NAME"
  python3 ${PYTHON_SCRIPT} "$FILE" > "$OUTPUT_FILE_NAME"
' {} ${OUTPUT_DIR} ${INPUT_DIR} ';'
