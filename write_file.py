# -*- coding: utf-8 -*-
import time
import sys

fp = open("a.txt", "w")

for i in range(10):
    fp.write(sys.argv[1]+"\n")
    time.sleep(0.5)
fp.close()
