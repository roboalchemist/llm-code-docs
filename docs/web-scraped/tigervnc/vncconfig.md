# Source: https://tigervnc.org/doc/vncconfig.html

# vncconfig 

------------------------------------------------------------------------

## NAME []

vncconfig − configure and control a VNC server

## SYNOPSIS []

**vncconfig** \[*parameters*\] **\
vncconfig** \[*parameters*\] **−connect** \[**-view-only**\] *host*\[:*port*\] **\
vncconfig** \[*parameters*\] **−disconnect\
vncconfig** \[*parameters*\] \[**-set**\] *Xvnc-param*=*value* \... **\
vncconfig** \[*parameters*\] **−list\
vncconfig** \[*parameters*\] **−get** *Xvnc-param* **\
vncconfig** \[*parameters*\] **−desc** *Xvnc-param*

## DESCRIPTION []

***vncconfig*** is used to configure and control a running instance of Xvnc, or any other X server with the VNC extension. Note that it cannot be used to control VNC servers prior to version 4.

When run with no options, it runs as a kind of \"helper\" application for Xvnc. Its main purpose when run in this mode is to query the user how new connections should be handled (provided this feature is enabled). The **-nowin** flag can be used if you always want the query support but don't wish to clutter the desktop with the settings window - alternatively the **-iconic** option can be used to make it iconified by default.

When run in any other mode, **vncconfig** is a one-shot program used to configure or control Xvnc as appropriate. It can be used to tell Xvnc to connect or disconnect from listening viewers, and to set and retrieve Xvnc's parameters.

Note that the DISPLAY environment variable or the **−display** option must be set as appropriate to control Xvnc. If you run it on an ordinary X server (or on a version 3 Xvnc) you will get an error message saying that there is no VNC extension.

## OPTIONS []

**−connect** \[**-view-only**\] *host*\[:*port*\]

Tells an Xvnc server to make a \"reverse\" connection to a listening VNC viewer (normally connections are made the other way round - the viewer connects to the server). *host* is the host where the listening viewer is running. If it's not listening on the default port of 5500, you can specify *host:port* instead. The **-view-only** option specifies that the server must ignore all keyboard or mouse events sent by the client.

**−desc** *Xvnc-param*

Prints a short description of the given Xvnc parameter.

**−disconnect**

This causes Xvnc to disconnect from all viewers so that the VNC desktop is not displayed anywhere.

**−get** *Xvnc-param*

Prints the current value of the given Xvnc parameter.

  -- ----------- -- --------------------------------------------- --
     **−list**      Lists all the parameters supported by Xvnc.   
  -- ----------- -- --------------------------------------------- --

\[**-set**\] *Xvnc-param*=*value*

Sets an Xvnc parameter to the given value. Note that some of Xvnc's parameters are read only once at startup so that changing them in this way may not have any effect.

## PARAMETERS []

**vncconfig** also has parameters of its own which can be set on the command line. These should not be confused with Xvnc's parameters which are manipulated with the **-set**, **-get**, **-list** and **-desc** options.

Parameters can be turned on with -*param* or off with -*param*=0. Parameters which take a value can be specified as -*param value*. Other valid forms are *param***=***value* -*param*=*value* \--*param*=*value*. Parameter names are case-insensitive. **\
−display** *Xdisplay*

Specifies the Xvnc server to control.

**−iconic**

When run as a \"helper\" app, make the window iconified at startup.

  -- ------------ -- ------------------------------------------------------ --
     **−nowin**      When run as a \"helper\" app, don't put up a window.   
  -- ------------ -- ------------------------------------------------------ --

## SEE ALSO []

**vncpasswd**(1), **vncviewer**(1), **Xvnc**(1), **vncsession**(8)\
https://www.tigervnc.org

## AUTHOR []

Tristan Richardson, RealVNC Ltd. and others.

VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite.

------------------------------------------------------------------------