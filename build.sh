#!/bin/sh

echo Building and pushing website
python app.py build
git subtree push --prefix build github master
