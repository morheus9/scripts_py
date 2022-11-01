import glob
import os

pattern = "/home/pi/*.log"
files = glob.glob(pattern)

for file in files:
    os.remove(file)
