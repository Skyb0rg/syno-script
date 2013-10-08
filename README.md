syno-script
===========

Manage operations on the diskstation by cgi-website 

Projekt Status: Alpha ... but works like a charm

The CGI-Script can:
- show processlist 
- poweroff the diskstation
... more will comming soon

Installation:
------------
create directory on the Diskstation

Option1:

`DS412> mkdir /usr/syno/synoman/webman/3rdparty/Syno-Script`  
`DS412> cd /usr/syno/synoman/webman/3rdparty/Syno-Script`  
`DS412> cat >syno-script`  


Past the Code into this Window  
quit with Ctrl + D  
 
Option2:
you can also copy the file to folder, if you know how ;)  

Give the file the right permission, need execute rights on the Diskstation  
`DS412> chmod oug+x syno-script.cgi`

Now you can open the URL in you Browser:  
`http://<yourDS>:5000/webman/3rdparty/Syno-Script/test1.cgi?<command>`

Commands:
------------

processlist - list all processes on the Diskstation  
synodown - shuts the Diskstation down  


Examples:  
http://DS412:5000/webman/3rdparty/Syno-Script/syno-script.cgi?processlist  
http://192.168.1.1:5000/webman/3rdparty/Syno-Script/syno-script.cgi?synodown  
http://DS412:5000/webman/3rdparty/Syno-Script/syno-script.cgi?<command>  



#Addons:

Homematic CCU1 & CCU2  
------------

Little Script for shutting down the Diskstation

you can copy it to the `/usr/local/addons/cuxd/extra` Directory  
and start it by using CUXD:  
`sh /usr/local/addons/cuxd/extra/syno-shutdown.sh <ip> <port>`  

Example:
`sh /usr/local/addons/cuxd/extra/syno-shutdown.sh 192.168.1.100 5000`  
