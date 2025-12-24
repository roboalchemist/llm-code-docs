# Source: https://uvnc.com/docs/documentation/134-ultravnc-virtual-displays.html

# Virtual display

**\*\* UltraVNC Server need to be started as Administrator or Service to be able to use the Virtual monitors**\
**\*\* OS of the Server Windows 10 \>= 1903**\
**\*\* Both Server and Viewer need to be 1.3.0 \>=  to support it\
\*\* DDEngine capture must be used to be able to select seperated monitors**

 

-   1\. When activated the Server display resolution can be changed.
-   2\. You can manual select a resolution you want.
-   3\. The Viewer resolutions of all displays are send to the server
-   4\. Extend display: an extra display(s) are added\
    Use only virtual: The display is extended, but the server local displays are disabled
-   5\. Allow multi monitor spanning: When you select 3) and 4) The fullscreen mode cover\
    all your monitors. When not selected, fullscreen is on the selected monitor.
-   6\. Fit to screen: The screen is auto resize to the selected window/fullscreen size
-   7. The Viewer auto show the extended display.\
    [https://www.uvnc.eu/download/130/virtual2.mp4](https://www.uvnc.eu/download/130/virtual2.mp4)\

If 1, 2 and 4 set to extend, each viewer connect to a separate virtual display. Each viewer that connect create his own extended display and when disconnect he also remove that display.\
The normal behavior is that extended displays are only removed when the last viewer disconnect.\
\

Sample usage:

-   Assume you have a desktop PC with one screen (let\'s say 1920x1080) and a laptop (let\'s say 1366x768). So you sit at your desk and work on the desktop machine and your laptop is just sitting on the desk and not being used. You can now start your laptop, put it next to your desktop screen. Launch UltraVNC Viewer on it, connect to your desktop extending the screen.\
    Now your desktop has a virtual dual-screen setup with one 1920x1080 display and a 1366x768 display. The VNC client on the laptop will show you all activities on this virtual screen. So you can continue to work on your desktop machine but actually you can use the laptop as a screen extension.\
    \
-   You want to remote screen to be invisible. Settings 4. to \"Use only virtual displays\" shutdown the remote monitor.

 

 

Local Server screen is disabled and the 2 viewer screens are added. Options set to 1 , 3 and 4 to \"use only virtual displays\"\
\

 

Viewer button to switch between displays 1/2/multiple

**If ddengine is not used, you can not select each seperate screen !!!!**

 

Technical\
A vncviewer connection that request a virtual display is like plugging a usb monitor.\
When the viewers disconnect it\'s like unplugging the monitor.\
Is something goes wrong and the vnc server doesn\'t detect the disconnect, a reboot will reset the displays\
in all cases.\
\

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