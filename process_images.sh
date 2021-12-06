
INPUT_DIR=$1
OUTPUT_DIR=$2

set -x

find $INPUT_DIR -type f -not -name '*.xlsx' -exec sh -c '
  FILE="$0"
  OUTPUT_DIR="$1"
  cp "$FILE" "$OUTPUT_DIR/"
' {} ${OUTPUT_DIR} ';'
