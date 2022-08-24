#!/bin/sh -l

res=$(python deploy.py $1 $2)
echo "::set-output name=time::$res"
