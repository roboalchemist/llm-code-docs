# Source: https://uvnc.com/docs/ultravnc-viewer/52-ultravnc-viewer-commandline-parameters.html

# UltraVNC Viewer Commandline Parameters 

[-help, -? or -h\
Print a help message.\
-listen \[port\]\
Start the UltraVNC Viewer in listen mode. If port is specified, the Viewer listens on that port instead of 5900 default port.\
example UltraVNC Viewer listen non standard port 80\
vncviewer.exe -listen 80\
][[**-dsmplugin filename.dsm**\
]example1: vncviewer.exe host -dsmplugin msrc4plugin.dsm\
example2: vncviewer.exe host -dsmplugin securevncplugin.dsm\
\
**-proxy** host:port\
the proxy is not your office proxy, is UltraVNC Repeater proxy.\
\
the proxy/repeater mode I (distributor) Repeater must be on your lan\
\"%:\\programfiles%\\UltraVNC\\vncviewer.exe\" -proxy host:5901 -connect hostname\
\"%programfiles%\\UltraVNC\\vncviewer.exe\" -proxy distributor:5901 -connect host -dsmplugin filename.dsm\
\
proxy/repeater mode II (with ID number)\
\"%:\\programfiles%\\UltraVNC\\vncviewer.exe\" -proxy host:5901 ID:1234\
\"%programfiles%\\UltraVNC\\vncviewer.exe\" -proxy host:5901 ID:1234 -dsmplugin filename.dsm\"]

[[-autoacceptincoming\
]Auto  Accept Incoming connection (no SC Server info)\
][[-autoacceptnodsm\
]Server connection set without encryption, there no message is NOT encrypted while UltraVNC Viewer listen with dsmplugin\
][[-autoreconnect \[DelayInSeconds\]\
]-autoreconnect (default value 3 seconds)\
example: autoreconnect after 15 seconds\
vncviewer.exe -autoreconnect 15 -connect hostname\
commandline autoreconnect\
default=3\
value is number of seconds between reconnects This allow to set a bigger timeout between reconnect intervals this function is blocked by Repeater for Viewer.\
\"%programfiles%\\ultravnc\\vncviewer.exe\" -autoreconnect 30 -connect hostname::5900 -quickoption 3 -dsmplugin SecureVNCPlugin.dsm\
**-reconnect** x (warning) not yet available by command line) only gui\
This is the number of times a reconnect is made before the Viewer close the connection.\
][[**-disablesponsor**\
]remove the sponsor of UltraVNC Viewer message error\
[-fttimeout] sec\
Filetransfer timeout sec \[1-60\]\
[-keepalive] sec\
Interval to send a keepalive message\
[-askexit]\
Open a dialogbox on exit \" do you realy want to quit\"\
[-restricted]\
remove options from system menu ( Filetransfer, chat \....)\
[-viewonly ]\
Do not send local keyboard or mouse events to the remote computer.\
][[-nostatus\
]Don\'t show the status window while connecting.\
][[-nohotkeys\
]Do not enable hot keys (like CTRL+ALT+F9 for full screen mode etc.). Can be useful in case of conflict with other installed software hotkeys.\
][[-notoolbar\
]Do not display the toolbar.\
[-autoscaling]\
Automatically scale the Viewer window so that the remote screen fits at best your local screen size.\
][[-fullscreen\
]Display Viewer in full screen mode.\
[-noauto]\
Disable auto mode. Required for using the color options below or saving a custom configuration (otherwise the settings from quick options always override).\
][[-8bit, -256colors, -64colors, -8colors, -8greycolors, -4greycolors, -2greycolors\
]Set the color depth. Fewer colors can significantly reduce the required bandwidth.\
Note: Grey colors only work with 32 bits color screen resolution. 16 or 24 bits color resolutions just don\'t work with grey colors.\
][[-shared\
]Share the Server with other Viewers, i.e. allow several Viewers to connect simultaneously to the Server.\
][[-swapmouse\
]Swap left and right button of the mouse.\
][[-nocursor\
]Do not display any local dot mouse cursor.\
][[-dotcursor\
]Display the local dot mouse cursor.\
][[-normalcursor\
]Display the normal local mouse cursor.\
][[-belldeiconify\
]not used\
][[-emulate3\
]Emulate a 3-button mouse.\
][[-noemulate3\
]Do not emulate a 3-button mouse.\
][[-nocursorshape\
]don\'t change cursor chapes\
][[-noremotecursor\
]\".\" is used as remote cursor\
][[-scale A/B\
]Scale the display by the factor A/B.\
][[-emulate3timeout Timeout\
]emulate 3 button mouse with 2 buttons\
][[-emulate3fuzz Emul3Fuzz\
]emulate 3 button mouse with 2 buttons\
][[-disableclipboard\
]Do not transfer clipboard content.\
][[-delay delay\
]debug option\
[-loglevel] loglevel\
Set the loglevel. This can range from 0 (minimal) to 10 (maximum logging).\
[-console]\
Open a console window for log output.\
[-logfile] filename\
Log to the file specified by filename.\
[-config] filename\
Read the configuration from filename.\
[-register ]\
Record the path to the VNC Viewer and the type of the .vnc files in the registry\
[-encoding] encoding\
Encoding is either raw, rre, corre, hextile, zlib, zlibhex, tight or ultra. Encodings are described here.\
[-compresslevel] level\
Use specified compression level (0..9) for \"tight\" and \"zlib\" encodings (Tight encoding specific). Level 1 uses minimum of CPU time and achieves weak compression ratios, while level 9 offers best compression but is slow in terms of CPU time consumption on the Server side. Use high levels with very slow network connections, and low levels when working over high-speed LANs. It\'s not recommended to use compression level 0, reasonable choices start from the level 1.\
[-quality] quality\
Use the specified JPEG quality (0..9) for the \"tight\" encoding (Tight encoding specific). Quality level 0 denotes bad image quality but very impressive compression ratios, while level 9 offers very good image quality at lower compression ratios. Note that the \"tight\" encoder uses JPEG to encode only those screen areas that look suitable for lossy compression, so quality level 0 does not always mean unacceptable image quality.\
[-user ]msuser\
MS-Logon (NTLM1) username set at Server (not Viewer side)\
\
[-password ]password\
Use the specified password for \"classic\" VNC authentication.\
-serverscale scale\
Scale the display on the Server side by 1/scale. For instance scale = 2 means that the remote screen dimensions are reduced by 2 (\"half screen size\"), reducing at the same time the amount of graphical data received by a factor 4 (2\^2).\
-quickoption n\
Select a quickoption. Modem option is default\
1 = AUTO (auto select best settings, this never use ultra experimental maybe \"forever\")\
2 = LAN (\> 1Mbit/s) Max Colors\
3 = MEDIUM (\> 128Kbit/s )- 256 Colors\
4 = MODEM (19K - 128Kbit/s) - 64 Colors\
5 = SLOW (\< 19Kbit/s) 8 Colors\
6 = (custom ?) N/A (not available and fail)\
7 = ULTRA (\> 2Mbit/s) - Experimental (still experimental after 2 years)]

[-position x y w h\
\
REMARK\
Commandline options are Merged with the default saved settings.\
Sample:\
if you save viewonly as default -\> a Viewer started with a commandline option will always be \"viewonly\".]

 

  --
  --

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