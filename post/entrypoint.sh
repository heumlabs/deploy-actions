#!/bin/sh -l

REPO="$1"
SHA="$2"

cd /code
fab post-deploy -r "$REPO" -s "$SHA"
