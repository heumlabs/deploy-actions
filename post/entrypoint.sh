#!/bin/sh -l

REPO="$1"
SHA="$2"

fab post-deploy -r "$REPO" -s "$SHA"
