#!/bin/bash

find /excel2xml -type f -name '*.xlsx' -exec sh -c '
  file="$0"
  python3 /excel2xml/xlsx2xml.py "$file"
' {} ';'
