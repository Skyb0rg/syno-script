#!/bin/bash
# syno-shutdown
# Version 0.1
# https://github.com/Skyb0rg/syno-script
# First running code
# ----------------------------------------------------------------------
LD_LIBRARY_PATH=/usr/local/addons/cuxd /usr/local/addons/cuxd/curl -s "http://$1:$2/webman/3rdparty/Syno-Script/syno-script.cgi?synodown"