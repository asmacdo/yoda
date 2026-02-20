#!/bin/sh
# Start a virtual display for diff-pdf (needs GTK+/Cairo to render).
# Using Xvfb directly is more reliable in containers than xvfb-run.
set -eu

Xvfb :99 -screen 0 1024x768x24 -nolisten tcp &
export DISPLAY=:99

# Wait for Xvfb to be ready
for _ in 1 2 3 4 5; do
    if xdpyinfo -display :99 >/dev/null 2>&1; then break; fi
    sleep 0.2
done

if [ $# -eq 0 ]; then
    exec diff-pdf --help
fi
exec "$@"
