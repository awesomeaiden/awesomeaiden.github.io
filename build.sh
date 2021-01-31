#!/bin/sh

echo Building and pushing website
python app.py build
git add build
git commit -m "Build update"
git push
git subtree push --prefix build github master --force
