#!/bin/bash -

SCRIPT_PATH=$(dirname $(readlink -f $BASH_SOURCE))

export PYTHONPATH=$SCRIPT_PATH/src:$PYTHONPATH
# Defer control.
python $SCRIPT_PATH/src/byby/main.py 12321 132 1
read -p "something here ..."