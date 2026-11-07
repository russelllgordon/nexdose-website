#!/bin/sh
# Regenerates every page from the Python templates in this folder.
cd "$(dirname "$0")" && for f in home plus howto support rest; do python3 "$f.py" || exit 1; done
