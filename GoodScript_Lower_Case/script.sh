#!/bin/bash

# Directory to process (default to current directory if not provided)
DIR=${1:-.}

# Iterate through all files in the directory
for FILE in "$DIR"/*; do
  # Check if it's a file (not a directory)
  if [ -f "$FILE" ]; then
    # Get the lowercase version of the filename
    LOWERCASE_FILE="$(dirname "$FILE")/$(basename "$FILE" | tr '[:upper:]' '[:lower:]')"

    # Rename the file only if the names are different
    if [ "$FILE" != "$LOWERCASE_FILE" ]; then
      mv "$FILE" "$LOWERCASE_FILE"
      echo "Renamed: $FILE -> $LOWERCASE_FILE"
    fi
  fi
done

echo "All files processed."
