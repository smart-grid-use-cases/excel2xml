
INPUT_DIR=$1
OUTPUT_DIR=$2

find $INPUT_DIR -type f -not \( -name '*.xlsx' -o -name '*.pdf' \) -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  FILE_NO_SPACES=$(basename "${FILE}" | tr '[:blank:]' '_')
  cp "$FILE" "$OUTPUT_DIR/$FILE_NO_SPACES"
' {} ${OUTPUT_DIR} ';'

find $INPUT_DIR -type f -name '*.pdf' -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  FILE_NO_SPACES=$(basename "${FILE}" | tr '[:blank:]' '_')
  pdftoppm -png -singlefile "$FILE" "$OUTPUT_DIR/$FILE_NO_SPACES"
  echo "Converting $FILE to $OUTPUT_DIR/${FILE_NO_SPACES}.png"
' {} ${OUTPUT_DIR} ';'
