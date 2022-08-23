#!/bin/sh -l

res=$(python deploy.py)
echo "::set-output name=time::$res"
