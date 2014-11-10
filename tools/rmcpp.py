#rm all cpp files in current dir and child dirs.

import os
import sys
import re

rootdir = os.getcwd()
for dirpath, dirnames, files in os.walk(rootdir):
    for file in files:
        pattern = re.compile(r'.*\.cpp$')
        matchObj = re.match( pattern,file, 0)
        if (matchObj):
             filepath= os.path.join(dirpath, file) 
             print filepath 
             os.remove(filepath) 
    
         
   

