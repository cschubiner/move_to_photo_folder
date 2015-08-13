#!/usr/bin/env python
import os
filePath = str(os.environ["KMVAR_Path"]) # assuming the KM variable is named "path"
os.system('cp "' + filePath + '" photo_folder')
print 'Photo moved!?'
