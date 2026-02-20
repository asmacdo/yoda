#!/bin/sh
set -eu
if [ $# -eq 0 ]; then
    exec xvfb-run diff-pdf --help
fi
exec xvfb-run "$@"
