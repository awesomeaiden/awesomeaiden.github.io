#!/bin/sh

echo Building and pushing website
python3 app.py build
git subtree push --prefix build github master
