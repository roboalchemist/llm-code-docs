# Source: https://uvnc.com/docs/documentation/132-ultravnc-connections.html

# Connections

## Direct

localhost can be any dns name or IP address. \
Local IP/names ony works within your LAN, for WAN you need to use official IP addresses.

## Using a Repeater

 

## What"s a repeater ?

\
When your Viewer or Server is behind a nat router he has a local IP address.  Usual this is something like (192.168..., 10.0...). This is unreachable from the internet as you need an official IP address for it.\
A Repeater is a software that you run on a Server with an official IP address, somewhere on the net.\
The Server and Viewer announce themselves to the Repeater and when the Repeater find 2 identical ID\'s he connect the stream. You always need to use encryption + password in combination with ID\'s, the ID on his own doesn\'t offer any security.

Repeater.exe

When you start the repeater.exe it run in the tray and you access the option with a webbrowser. \
\
<http://localhost>:80  (if port 80 is in use the portnumber is added 1 (80,81,82..) until an open port is found. The default login \"admin\" with password \"adminadmi2\".

 

After you connect the Viewer to the Repeater, he is visible in the Repeater Stat page.

 

 UltraVNC Server systray: \"Add New Client\" Allow you can make a connection to the Repeater

5500 is the Repeater Server listen port

 

#####  

This result in a connection

 

#####  

## Can I use the Repeater when UltraVNC Server is running as Service ?

Yes

-autoreconnect ID:123456789 -connect localhost:5500

The service connects the Server in a loop to the Repeater.

#####  

#####  

[](# "Menu")

[](#)

-   [Home](https://uvnc.com/)
-   [Products[]](https://uvnc.com/products/ultravnc.html)
    -   [UltraVNC](https://uvnc.com/products/ultravnc.html)
    -   [UltraVNC Repeater](https://uvnc.com/products/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/products/ultravnc-sc.html)
    -   [UltraVNC Mirror Driver](https://uvnc.com/products/mirror-driver.html)
    -   [PcHelpWare](https://uvnc.com/products/pchelpware.html)
    -   [PcHelpWareV2](https://uvnc.com/products/pchelpwarev2.html)
-   [Downloads[]](https://uvnc.com/downloads/ultravnc.html)
    -   [UltraVNC](https://uvnc.com/downloads/ultravnc.html)
    -   [UltraVNC Repeater](https://uvnc.com/downloads/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/downloads/ultravnc-sc.html)
    -   [UltraVNC VNC Secure](https://uvnc.com/downloads/encryption.html)
    -   [UltraVNC Mirror Driver](https://uvnc.com/downloads/mirror-driver.html)
    -   [PcHelpWare](https://uvnc.com/downloads/pchelpware.html)
    -   [UltraVNC ScreenRecorder](https://uvnc.com/downloads/ultravnc-screenrecorder.html)
-   [Documentation[]](https://uvnc.com/docs/ultravnc-server.html)
    -   [UltraVNC Server](https://uvnc.com/docs/ultravnc-server.html)
    -   [UltraVNC Viewer](https://uvnc.com/docs/ultravnc-viewer.html)
    -   [UltraVNC Repeater](https://uvnc.com/docs/ultravnc-repeater.html)
    -   [UltraVNC Single Click (SC)](https://uvnc.com/docs/ultravnc-sc.html)
    -   [Documentation 1.3.x +](https://uvnc.com/docs/documentation.html)
    -   [General Knowledge](https://uvnc.com/docs/general-knowledge.html)
    -   [PcHelpWare](https://uvnc.com/docs/pchelpware.html)
-   [Forum](https://forum.uvnc.com)
-   [Git](https://github.com/ultravnc/ultravnc)
-   [Bluesky](https://bsky.app/profile/ultravnc.bsky.social)
-   [OpenHub](https://openhub.net/p/ultravnc)

-   [[]](https://www.facebook.com/UltraVNC1)
-   [[]](https://twitter.com/ultravnc1)
-   [[]](https://www.reddit.com/r/ultravnc/)
-   [[]](https://mastodon.social/@ultravnc)
-   [[]](https://github.com/ultravnc)

[[]](#)

**JavaScript is currently disabled.**Please enable it for a better experience of [Jumi](http://2glux.com/projects/jumi).