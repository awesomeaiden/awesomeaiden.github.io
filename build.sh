#!/bin/sh

echo Building and pushing website
rm -r docs/*
pip install -r requirements.txt
python app.py build
cp CNAME docs
git add docs
git commit -m "Docs build update"
git push
