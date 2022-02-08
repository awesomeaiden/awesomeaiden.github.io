#!/bin/sh

echo Building and pushing website
rm -r build/*
python3 app.py build
git add build
git commit -m "Build update"
git push
