
INPUT_DIR=$1
OUTPUT_DIR=$2

find $INPUT_DIR -type f -not -name '*.xlsx' -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  FILE_NO_SPACES=$(basename "${FILE}" | tr '[:blank:]' '_')
  cp "$FILE" "$OUTPUT_DIR/$FILE_NO_SPACES"
' {} ${OUTPUT_DIR} ';'
