#!/bin/sh
exec xvfb-run /usr/bin/diff-pdf "$@"
