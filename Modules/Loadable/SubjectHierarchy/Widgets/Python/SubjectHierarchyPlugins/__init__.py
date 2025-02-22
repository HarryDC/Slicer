"""This package contains plugins for Subject Hierarchy implemented in Python."""

import os
import traceback
import logging
import sys

from . import parameterNodeWrapper  # Required to ensure parameterNodeWrapper plugins are registered

currentDir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentDir)
for fileName in os.listdir(currentDir):
    fileNameNoExtension = os.path.splitext(fileName)[0]
    fileExtension = os.path.splitext(fileName)[1]
    if fileExtension == ".py" and fileNameNoExtension != "__init__":
        importStr = f"from {fileNameNoExtension} import *"
        try:
            exec(importStr)
        except Exception as e:
            logging.error("Failed to import " + fileNameNoExtension + ": " + traceback.format_exc())
