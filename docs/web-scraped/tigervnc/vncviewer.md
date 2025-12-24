# Source: https://tigervnc.org/doc/vncviewer.html

# vncviewer 

------------------------------------------------------------------------

## NAME []

vncviewer − VNC viewer for X

## SYNOPSIS []

**vncviewer** \[*options*\] \[*host*\]\[:*display#*\] **\
vncviewer** \[*options*\] \[*host*\]\[::*port*\] **\
vncviewer** \[*options*\] \[*unix socket*\] **\
vncviewer** \[*options*\] **−listen** \[*port*\] **\
vncviewer** \[*options*\] \[*.tigervnc file*\]

## DESCRIPTION []

**vncviewer** is a viewer (client) for Virtual Network Computing. This manual page documents version 4 for the X window system.

If you run the viewer with no arguments it will prompt you for a VNC server to connect to. Alternatively, specify the VNC server as an argument, e.g.:

vncviewer snoopy:2

where 'snoopy' is the name of the machine, and '2' is the display number of the VNC server on that machine. Either the machine name or display number can be omitted. So for example \":1\" means display number 1 on the same machine, and \"snoopy\" means \"snoopy:0\" i.e. display 0 on machine \"snoopy\".

As another quick way to start a connection to a VNC server, specify a .tigervnc configuration file as an argument to the viewer, e.g.:

vncviewer ./some.tigervnc

where './some.tigervnc' is an existing and valid TigerVNC configuration file. The file name needs to include a path separator. Additional options may be given too, but the given configuration file will overwrite any conflicting parameters.

If the VNC server is successfully contacted, you will be prompted for a password to authenticate you. You can also add 'VNC_USERNAME' and 'VNC_PASSWORD' to environment variables. If the password is correct, a window will appear showing the desktop of the VNC server.

## AUTOMATIC PROTOCOL SELECTION []

The viewer tests the speed of the connection to the server and chooses the encoding and pixel format (color level) appropriately. This makes it much easier to use than previous versions where the user had to specify arcane command line arguments.

The viewer normally starts out assuming the link is slow, using the encoding with the best compression. If it turns out that the link is fast enough it switches to an encoding which compresses less but is faster to generate, thus improving the interactive feel.

The viewer normally starts in full-color mode, but switches to low-color mode if the bandwidth is insufficient. However, this only occurs when communicating with servers supporting protocol 3.8 or newer, since many old servers do not support color mode changes safely.

Automatic selection can be turned off by setting the **AutoSelect** parameter to false, or from the options dialog.

## POPUP MENU []

The viewer has a popup menu containing entries which perform various actions. It is usually brought up by pressing F8, but this can be configured with the MenuKey parameter. Actions which the popup menu can perform include:

  -- ---- -- -------------------------------------------------------- --
     \*      switching in and out of full-screen mode                 
     \*      quitting the viewer                                      
     \*      generating key events, e.g. sending ctrl-alt-del         
     \*      accessing the options dialog and various other dialogs   
  -- ---- -- -------------------------------------------------------- --

By default, key presses in the popup menu get sent to the VNC server and dismiss the popup. So to get an F8 through to the VNC server simply press it twice.

## FULL-SCREEN MODE []

A full-screen mode is supported. This is particularly useful when connecting to a remote screen which is the same size as your local one. If the remote screen is bigger, you can scroll by bumping the mouse against the edge of the screen.

## OPTIONS (PARAMETERS) []

You can get a list of parameters by giving **−h** as a command-line option to vncviewer. Parameters can be turned on with -*param* or off with -*param*=0. Parameters which take a value can be specified as -*param value*. Other valid forms are *param***=***value* -*param*=*value* \--*param*=*value*. Parameter names are case-insensitive.

Many of the parameters can also be set graphically via the options dialog box. This can be accessed from the popup menu or from the \"Connection details\" dialog box. **\
−AcceptClipboard**

Accept clipboard changes from the server. Default is on.

**−AlertOnFatalError**

Display a dialog with any fatal error before exiting. Default is on.

**−AlwaysCursor**

Show a local cursor when the server sends an invisible cursor. Default is off.

**−AutoSelect**

Use automatic selection of encoding and pixel format (default is on). Normally the viewer tests the speed of the connection to the server and chooses the encoding and pixel format appropriately. Turn it off with **-AutoSelect=0**.

**−CompressLevel** *level*

Use specified lossless compression level. 0 = Low, 9 = High. Default is 2.

**−CursorType** *type*

Specify which cursor type to use when a local cursor is shown. It should be either \"Dot\", or \"System\". Ignored if AlwaysCursor is off. The default is \"Dot\".

**−CustomCompressLevel**

Use custom compression level. Default if **CompressLevel** is specified.

**−DesktopSize** *width***x***height*

Instead of keeping the existing remote screen size, the client will attempt to switch to the specified since when connecting. If the server does not support the SetDesktopSize message then the screen will retain the original size.

**−display** *Xdisplay*

Specifies the X display on which the VNC viewer window should appear.

**−DotWhenNoCursor (DEPRECATED)**

Show the dot cursor when the server sends an invisible cursor. Replaced by **-AlwaysCursor** and **-CursorType=Dot**

**−EmulateMiddleButton**

Emulate middle mouse button by pressing left and right mouse buttons simultaneously. Default is off.

**−FullColor, −FullColour**

Tells the VNC server to send full-color pixels in the best format for this display. This is default.

**−FullScreen**

Start in full-screen mode.

**−FullScreenAllMonitors (DEPRECATED)**

Use all local monitors and not just the current one when switching to full-screen mode. Replaced by **-FullScreenMode=all**

**−FullScreenMode** *mode*

Specify which monitors to use when in full screen. It should be either \"Current\", \"Selected\" (specified by **-FullScreenSelectedMonitors**) or \"All\". The default is \"Current\".

**−FullScreenSelectedMonitors** *monitors*

This option specifies the monitors to use with **-FullScreenMode=selected**. Monitors are ordered according to the system configuration from left to right, and in case of a conflict, from top to bottom. So, for example, \"1,2,3\" means that the first, second and third monitor counting from the left should be used. The default is \"1\".

**−FullscreenSystemKeys**

Pass special keys (like Alt+Tab) directly to the server when in full-screen mode.

**−geometry** *geometry*

Initial position of the main VNC viewer window. The format is *width***x***height***+***xoffset***+***yoffset* , where '+' signs can be replaced with '−' signs to specify offsets from the right and/or from the bottom of the screen. Offsets are optional and the window will be placed by the window manager by default.

**−GnuTLSPriority** *priority*

GnuTLS priority string that controls the TLS sessionâs handshake algorithms. See the GnuTLS manual for possible values. Default is **NORMAL**.

**−listen** *\[port\]*

Causes vncviewer to listen on the given port (default 5500) for reverse connections from a VNC server. WinVNC supports reverse connections initiated using the 'Add new client' menu option or the '−connect' command-line option. Xvnc supports reverse connections with a helper program called **vncconfig.**

**−Log** *logname***:***dest***:***level***\[, \...\]**

Configures the debug log settings. *dest* can currently be **stderr** or **stdout**, and *level* is between 0 and 100, 100 meaning most verbose output. *logname* is usually **\*** meaning all, but you can target a specific source file if you know the name of its \"LogWriter\". Default is **\*:stderr:30**.

**−LowColorLevel, −LowColourLevel** *level*

Selects the reduced color level to use on slow links. *level* can range from 0 to 2, 0 meaning 8 colors, 1 meaning 64 colors (the default), 2 meaning 256 colors. Note that decision if reduced color level is used is made by vncviewer. If you would like to force vncviewer to use reduced color level use **-AutoSelect=0** parameter.

**−MaxCutText** *bytes*

The maximum size of a clipboard update that will be accepted from a server. Default is **262144**.

**−Maximize**

Maximize viewer window.

**−MenuKey** *keysym-name*

This option specifies the key which brings up the popup menu. The currently supported list is: F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, Pause, Scroll_Lock, Escape, Insert, Delete, Home, Page_Up, Page_Down). Default is F8.

**−NoJpeg**

Disable lossy JPEG compression in Tight encoding. Default is off.

**−passwd, −PasswordFile** *password-file*

If you are on a filesystem which gives you access to the password file used by the server, you can specify it here to avoid typing it in. It will usually be *\$XDG_CONFIG_HOME/tigervnc/passwd*, or *˜/.config/tigervnc/passwd* if the former is unset.

**−PointerEventInterval** *time*

Time in milliseconds to rate-limit successive pointer events. Default is 17 ms (60 Hz).

**−PreferredEncoding** *encoding*

This option specifies the preferred encoding to use from one of \"Tight\", \"ZRLE\", \"hextile\" or \"raw\".

**−QualityLevel** *level*

JPEG quality level. 0 = Low, 9 = High. May be adjusted automatically if **-AutoSelect** is turned on. Default is 8.

**−ReconnectOnError**

Display a dialog with any error and offer the possibility to retry establishing the connection. In case this is off no dialog to re-connect will be offered. Default is on.

**−RemoteResize**

Dynamically resize the remote desktop size as the size of the local client window changes. Note that this may not work with all VNC servers.

**−SecurityTypes** *sec-types*

Specify which security schemes to attempt to use when authenticating with the server. Valid values are a comma separated list of **None**, **VncAuth**, **Plain**, **TLSNone**, **TLSVnc**, **TLSPlain**, **X509None**, **X509Vnc**, **X509Plain**, **RA2**, **RA2ne**, **RA2_256** and **RA2ne_256**. Default is to attempt every supported scheme.

**−SendClipboard**

Send clipboard changes to the server. Default is on.

**−SendPrimary**

Send the primary selection to the server as well as the clipboard selection. Default is on.

**−SetPrimary**

Set the primary selection as well as the clipboard selection. Default is on.

**−Shared**

When you make a connection to a VNC server, all other existing connections are normally closed. This option requests that they be left open, allowing you to share the desktop with someone already using it.

**−UseIPv4**

Use IPv4 for incoming and outgoing connections. Default is on.

**−UseIPv6**

Use IPv6 for incoming and outgoing connections. Default is on.

**−via** *gateway*

Automatically create encrypted TCP tunnel to the *gateway* machine before connection, connect to the *host* through that tunnel (TigerVNC−specific). By default, this option invokes SSH local port forwarding, assuming that SSH client binary can be accessed as /usr/bin/ssh. Note that when using the **−via** option, the host machine name should be specified as known to the gateway machine, e.g. \"localhost\" denotes the *gateway*, not the machine where vncviewer was launched. The environment variable *VNC_VIA_CMD* can override the default tunnel command of **/usr/bin/ssh −f −L \"\$L\":\"\$H\":\"\$R\" \"\$G\" sleep 20**. The tunnel command is executed with the environment variables *L*, *H*, *R*, and *G* taking the values of the local port number, the remote host, the port number on the remote host, and the gateway machine respectively.

**−ViewOnly**

Specifies that no keyboard or mouse events should be sent to the server. Useful if you want to view a desktop without interfering; often needs to be combined with **−Shared.**

**−X509CA** *path*

Path to CA certificate to use when authenticating remote servers using any of the X509 security schemes (X509None, X509Vnc, etc.). Must be in PEM format. Default is *\$XDG_CONFIG_HOME/tigervnc/x509_ca.pem*, or *˜/.config/tigervnc/x509_ca.pem*.

**−X509CRL** *path*

Path to certificate revocation list to use in conjunction with **-X509CA**. Must also be in PEM format. Default is *\$XDG_CONFIG_HOME/tigervnc/x509_crl.pem*, or *˜/.config/tigervnc/x509_crl.pem*.

## FILES []

*\$XDG_CONFIG_HOME/tigervnc/default.tigervnc\
\$HOME/.config/tigervnc/default.tigervnc*

Default configuration options. This file must have a \"magic\" first line of \"TigerVNC Configuration file Version 1.0\" (without quotes), followed by simple \<setting\>=\<value\> pairs of your choosing. The available settings are those shown in this man page.

*\$XDG_CONFIG_HOME/tigervnc/x509_ca.pem\
\$HOME/.config/tigervnc/x509_ca.pem*

Default CA certificate for authenticating servers.

*\$XDG_CONFIG_HOME/tigervnc/x509_crl.pem\
\$HOME/.config/tigervnc/x509_crl.pem*

Default certificate revocation list.

*\$XDG_DATA_HOME/tigervnc/x509_known_hosts\
\$HOME/.local/share/tigervnc/x509_known_hosts*

Known hosts database for certificate-based authentication.

*\$XDG_STATE_HOME/tigervnc/tigervnc.history\
\$HOME/.local/state/tigervnc/tigervnc.history*

History file for hostnames that have been recently connected to.

## SEE ALSO []

**Xvnc**(1), **vncpasswd**(1), **vncconfig**(1), **vncsession**(8)\
https://www.tigervnc.org

## AUTHOR []

Tristan Richardson, RealVNC Ltd. and others.

VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite.

------------------------------------------------------------------------