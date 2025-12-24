# Source: https://uvnc.com/docs/ultravnc-server/49-ultravnc-server-configuration.html

# UltraVNC Server Configuration

[Admin Properties]

[The \"Admin Properties\" menu item in the system tray UltraVNC Server icon menu refers to Default Local System Properties (service mode) or Current User Properties (application mode) and allows for customizing several areas:]

[Configurations]

[Incoming connections\
][Accept Socket Connections\
][Should be activated for normal operation. The display number and ports to use can be configured or set to `Auto` which defaults to Display `0`, Port `5900` and JavaViewer port `5800`.\
The port is always Display No + 5900.\
\
][Display\
][Defaults to `0`.]

[Ports\
][Defaults to `5900` and `5800` for HTTP.]

[Enable JavaViewer (HTTP connect)\
][Allows to view a remote computer by opening a browser and go to ][`http://`*`remote-machine`*`:`*`http-port`*`/`].

[Allow Loopback Connections\
][Sometimes this could be helpful for tests. Normally it\'s not needed since the result is not very useful.]

[Loopback Only\
][Needed for tests. Connections from outside are not allowed.]

[When last client disconnects\
][In a helpdesk scenario, you normally \"Do Nothing\" when disconnecting. When administering Servers via remote control, you might wish to either \"Lock Workstation\" or \"Logoff Workstation\" for security reasons.]

[Query on incoming connection\
][If enabled, every time someone tries to connect via UltraVNC, a pop-up dialog informs the user and asks the user to either accept or refuse the attempt. Configure the timeout for the dialog window and what action should be taken if the user clicked no button until timeout.]

[Keyboard & Mouse\
][Some situations (e.g. presentations) require that either the Viewer or the remote computer don\'t input keyboard or mouse events. This can be configured by \"Disable Viewer inputs\" or \"Disable Local inputs\".]

[Multi Viewer connections\
][Here you can configure the behavior if multiple Viewers attempt to connect to the same UltraVNC Server. \"Disconnect all existing connections\" implies that only one Viewer can be connected at a time and the last one wins. \"Keep existing connections\" allows for several Viewers simultaneously. \"Refuse the new connection\" implies that only one Viewer can be connected at a time and the first one wins. \"Refuse all new connections\" ??]

[Authentication\
][\"VNC Password\" is a per-machine password and is required.]

[Require MS-Logon\
Activates MS-Logon I. Works on Windows 9x as well as Windows NT4 / Windows Server 2000 / Windows XP. Requires computer and user to be in the same domain.\
New MS-Logon\
Activates MS-Logon II. Allows for cross-domain authentication, i.e. computer is in domain A, user in domain B with a trust between A and B (typically in Active Directory). Works only on Windows NT4 / Windows Server 2000 / Windows XP.\
Configure MS-Logon Groups\
Opens the configuration dialog for MS-Logon authorization. For MS-Logon I there is a dialog allowing to configure 3 groups:][For MS-Logon II tere is the standard Windows Security property page:]\

[DSM Plugin\
][If there are any DSM (Data Stream Modification) Plugins available, their usage can be configured here. Currently there are several encryption plugins available.]

[Miscellaneous\
][Remove Wallpaper for Viewers\
][To reduce network traffic the wallpaper on the remote computer\'s desktop can be removed during the connection.]

[Enable Blank Monitor on Viewer Request\
][Allow Viewers to disable the monitor if they request so.]

[Enable File Transfer\
][Enable the UltraVNC File Transfer.]

[Log debug info to the WinVNC.log file\
][Enable logging. The log file is in C:\\WinNT\\system32 if winvnc runs as service. The logging level can be configured in the registry.]

[Disable Tray icon\
][The icon in the system tray can be disabled to disallow users to change any settings.]

[Forbid the user to close down WinVNC\
][Disallow users to close down WinVNC.]

[Disable clients options in tray icon menu\
][Disable the \"Properties\" menu item in the system tray icon menu.]

[Capture Alpha-Blending\
][Capture also semi transparent screens]

[Enable Alpha-Blending Screen Blanking\
][Enable another method to disable the monitor.]

[Default Server Screen Scale\
The Server screen can be scaled down here.\
Properties\
The \"Properties\" menu item in the system tray UltraVNC Server icon menu refers to per user settings:]

[System Hook Dll\
Provides DDI hooking, especially on Windows 9x.]

[Video Hook Driver\
The video hook driver provides high speed and low CPU load on Windows Server 2000 / Windows XP / Windows Server 2003.]

[Check the Video Hook Driver\
][Here you can test the video hook driver, see it\'s version and whether it\'s currently active:]\

[Low Accuracy\
][Get higher speed with reduced accuracy.]

[Share only the Server Window Named\
][Do not share the whole desktop but only the window with the specified name.\
]

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