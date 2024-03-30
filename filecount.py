#!/usr/bin/env python3

import os, sys

list_of_files = os.listdir()
for i, j in enumerate(list_of_files):
    print(i, j)