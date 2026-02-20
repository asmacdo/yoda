#!/bin/sh
# If invoked with no args or flags, treat as diff-pdf invocation.
# If first arg is diff-pdf, run it under xvfb-run.
# Otherwise, run the command as-is (e.g. a script that calls diff-pdf itself).
set -eu

if [ $# -eq 0 ]; then
    /usr/bin/diff-pdf --help 2>&1 || true
    exit 0
fi

case "$1" in
    diff-pdf)
        shift
        exec xvfb-run /usr/bin/diff-pdf "$@"
        ;;
    -*)
        # Flags like --help, --output-diff, etc. — treat as diff-pdf args
        exec xvfb-run /usr/bin/diff-pdf "$@"
        ;;
    *)
        exec "$@"
        ;;
esac
