#!/bin/sh

echo Building and pushing website
rm -r docs/*
python3 app.py build
cp CNAME docs
git add docs
git commit -m "Docs build update"
git push
