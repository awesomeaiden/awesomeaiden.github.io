#!/bin/sh

echo Building and pushing website
rm -r docs/*
python3 app.py build
git add docs
git commit -m "Docs build update"
git push
