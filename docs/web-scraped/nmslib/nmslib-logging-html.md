# Source: https://nmslib.github.io/nmslib/logging.html

Title: Configuring Logging for NMSLIB — nmslib 2.0.5 documentation

URL Source: https://nmslib.github.io/nmslib/logging.html

Markdown Content:
[nmslib](https://nmslib.github.io/nmslib/index.html)

This library logs to a Python logger named `nmslib`. This lets you fully control the log messages produced by nmslib in Python.

For instance, to log everything produced by nmslib to a default python logger:

# setup basic python logging
import logging
logging.basicConfig(level=logging.DEBUG)

# importing nmslib logs some debug messages on startup, that
# that will be output to the python log handler created above
import nmslib

To quiet these messages you can just set the level for nmslib as appropiate:

# setup basic python logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Only log WARNING messages and above from nmslib
logging.getLogger('nmslib').setLevel(logging.WARNING)

import nmslib
