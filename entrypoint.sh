#!/bin/sh -l

cd /code
fab create-r2m -r $1 -b $2 --target $3 --title "$4"
