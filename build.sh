#!/bin/sh

echo Building and pushing website
rm -r docs/*
pip install -r requirements.txt || pip3 install -r requirements.txt
python app.py build || python3 app.py build
cp CNAME docs
git add docs
git commit -m "Docs build update"
git push
