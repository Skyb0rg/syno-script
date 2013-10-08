#!/bin/sh
# syno-script
# Version 0.1
# https://github.com/Skyb0rg/syno-script
# First running code

header="Content-type: text/html\n\n<html><head><title>Syno-Script</title></head><body>"
footer="</body></html>"
case $1 in
        "processlist")
                        echo -e $header'<pre>'
                        ps
                        echo -e '</pre>'$footer
;;
        "test2")
;;
        "synodown")
                        echo -e $header
                        poweroff
                        echo -e $footer
;;
        *)
                        echo -e $header
                        echo -e '<b>unknown command '$1' <br>\n you may use one of the following:</b>\n<br>'
                        echo -e 'Commands:\n<br>'
                        echo -e 'processlist - list all processes on the Diskstation\n<br>'
                        echo -e 'synodown - shuts the Diskstation down\n<br>'

                        echo -e $footer
;;
esac
