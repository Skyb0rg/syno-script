syno-script
===========

Manage operations on the diskstation by cgi-website 

Projekt Status: Alpha ... but works like a charm

The CGI-Script can:
- show processlist 
- poweroff the diskstation
... more will comming soon

Installation:

create directory on the Diskstation

DS412> mkdir /usr/syno/synoman/webman/3rdparty/Syno-Script

DS412> cd /usr/syno/synoman/webman/3rdparty/Syno-Script

DS412> cat >syno-script

Past the Code into this Window
Quit with Ctrl + D

You can also copy the file to folder, if you know how ;)

give the file the right permission, need execute rights on the Diskstation

DS412> chmod oug+x syno-script.cgi

Now you can open the URL in you Browser:

http://<yourDS>:5000/webman/3rdparty/Syno-Script/test1.cgi?<command>

Commands:

processlist - list all prozessen on the Diskstation

synodown - shuts the Diskstation down


Examples:

http://DS412:5000/webman/3rdparty/Syno-Script/syno-script.cgi?processlist

http://192.168.1.1:5000/webman/3rdparty/Syno-Script/syno-script.cgi?synodown

http://DS412:5000/webman/3rdparty/Syno-Script/syno-script.cgi?<command>

