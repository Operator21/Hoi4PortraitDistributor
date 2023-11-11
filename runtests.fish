#!/usr/bin/env fish
# activate env
source ./venv/bin/activate

# run tests
python3 -m unittest src/test/filehelper_test.py