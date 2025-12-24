# Source: https://tigervnc.org/doc/Xvnc.html

# Xvnc 

------------------------------------------------------------------------

## NAME []

Xvnc − the X VNC server

## SYNOPSIS []

**Xvnc** \[*options*\] :*display#*

## DESCRIPTION []

***Xvnc*** is the X VNC (Virtual Network Computing) server. It is based on a standard X server, but it has a \"virtual\" screen rather than a physical one. X applications display themselves on it as if it were a normal X display, but they can only be accessed via a VNC viewer - see **vncviewer**(1).

So Xvnc is really two servers in one. To the applications it is an X server, and to the remote VNC users it is a VNC server. By convention we have arranged that the VNC server display number will be the same as the X server display number, which means you can use eg. snoopy:2 to refer to display 2 on machine \"snoopy\" in both the X world and the VNC world.

The best way of starting **Xvnc** is via **vncsession**. This sets up the environment appropriately and starts a desktop environment. See the manual page for **vncsession**(8) for more information.

## OPTIONS []

**Xvnc** takes lots of options - running **Xvnc -help** gives a list. Many of these are standard X server options, which are described in the **Xserver**(1) manual page. In addition to options which can only be set via the command-line, there are also \"parameters\" which can be set both via the command-line and through the **vncconfig**(1) program. **\
−depth** *depth*

Specify the pixel depth in bits of the desktop to be created. Default is 24, other possible values are 16 and 32. Anything else is likely to cause strange behaviour by applications and may prevent the server from starting at all.

**−geometry** *width***x***height*

Specify the size of the desktop to be created. Default is 1024x768.

  -- ------------ -- -------------------------------------------------------------------------------------------------------------------------------
     **−help**       List all the options and parameters
     **−inetd**      This significantly changes Xvnc's behaviour so that it can be launched from inetd. See the section below on usage with inetd.
  -- ------------ -- -------------------------------------------------------------------------------------------------------------------------------

**−pixelformat** *format*

Specify pixel format for server to use (BGRnnn or RGBnnn). The default for depth 16 is RGB565 and for depth 24 and 32 is RGB888.

**−rendernode** *path*

DRM render node to use for DRI3 GPU acceleration. Specify an empty path to disable DRI3. Default is **auto** which makes **Xvnc** pick a suitable available render node.

## PARAMETERS []

VNC parameters can be set both via the command-line and through the **vncconfig**(1) program, and with a VNC-enabled Xorg server via Options entries in the xorg.conf file.

Parameters can be turned on with -*param* or off with -*param*=0. Parameters which take a value can be specified as -*param value*. Other valid forms are *param***=***value* -*param*=*value* \--*param*=*value*. Parameter names are case-insensitive. **\
−AcceptCutText**

Accept clipboard updates from clients. Default is on.

**−AcceptKeyEvents**

Accept key press and release events from clients. Default is on.

**−AcceptPointerEvents**

Accept pointer movement and button events from clients. Default is on.

**−AcceptSetDesktopSize**

Accept requests to resize the size of the desktop. Default is on.

**−AllowOverride**

Comma separated list of parameters that can be modified using VNC extension. Parameters can be modified for example using **vncconfig**(1) program from inside a running session.

**−AlwaysShared**

Always treat incoming connections as shared, regardless of the client-specified setting. Default is off.

**−AvoidShiftNumLock**

Key affected by NumLock often require a fake Shift to be inserted in order for the correct symbol to be generated. Turning on this option avoids these extra fake Shift events but may result in a slightly different symbol (e.g. a Return instead of a keypad Enter).

**−BlacklistThreshold** *count*

The number of unauthenticated connection attempts allowed from any individual host before that host is black-listed. Default is 5.

**−BlacklistTimeout** *seconds*

The initial timeout applied when a host is first black-listed. The host cannot re-attempt a connection until the timeout expires. Default is 10.

**−CompareFB** *mode*

Perform pixel comparison on framebuffer to reduce unnecessary updates. Can be either **0** (off), **1** (always) or **2** (auto). Default is **2**.

**−desktop** *desktop-name*

Each desktop has a name which may be displayed by the viewer. It defaults to \"\<user\>@\<hostname\>\".

**−DisconnectClients**

Disconnect existing clients if an incoming connection is non-shared. Default is on. If **DisconnectClients** is false, then a new non-shared connection will be refused while there is a client active. When combined with **NeverShared** this means only one client is allowed at a time.

**−FrameRate** *fps*

The maximum number of updates per second sent to each client. If the screen updates any faster then those changes will be aggregated and sent in a single update to the client. Note that this only controls the maximum rate and a client may get a lower rate when resources are limited. Default is **60**.

**−GnuTLSPriority** *priority*

GnuTLS priority string that controls the TLS sessionâs handshake algorithms. See the GnuTLS manual for possible values. For GnuTLS \< 3.6.3 the default value will be **NORMAL** to use upstream default. For newer versions of GnuTLS system-wide crypto policy will be used.

**−IdleTimeout** *seconds*

The number of seconds after which an idle VNC connection will be dropped. Default is 0, which means that idle connections will never be dropped.

**−ImprovedHextile**

Use improved compression algorithm for Hextile encoding which achieves better compression ratios by the cost of using slightly more CPU time. Default is on.

**−interface** *IP address*

Listen on interface. By default Xvnc listens on all available interfaces.

**−localhost**

Only allow connections from the same machine. Useful if you use SSH and want to stop non-SSH connections from any other hosts.

**−Log** *logname***:***dest***:***level***\[, \...\]**

Configures the debug log settings. *dest* can currently be **stderr**, **stdout** or **syslog**, and *level* is between 0 and 100, 100 meaning most verbose output. *logname* is usually **\*** meaning all, but you can target a specific source file if you know the name of its \"LogWriter\". Default is **\*:stderr:30**.

**−MaxConnectionTime** *seconds*

Terminate when a client has been connected for *N* seconds. Default is 0.

**−MaxCutText** *bytes*

The maximum size of a clipboard update that will be accepted from a client. Default is **262144**.

**−MaxDisconnectionTime** *seconds*

Terminate when no client has been connected for *N* seconds. Default is 0.

**−MaxIdleTime** *seconds*

Terminate after *N* seconds of user inactivity. Default is 0.

**−NeverShared**

Never treat incoming connections as shared, regardless of the client-specified setting. Default is off.

**−pam_service** *name***, −PAMService** *name*

PAM service name to use when authentication users using any of the \"Plain\" security types. Default is **vnc**.

**−Password** *password*

Obfuscated binary encoding of the password which clients must supply to access the server. Using this parameter is insecure, use **PasswordFile** parameter instead.

**−PasswordFile** *passwd-file***, −rfbauth** *passwd-file*

Password file for VNC authentication. There is no default, you should specify the password file explicitly. Password file should be created with the **vncpasswd**(1) utility. The file is accessed each time a connection comes in, so it can be changed on the fly.

**−PlainUsers** *user-list*

A comma separated list of user names that are allowed to authenticate via any of the \"Plain\" security types (Plain, TLSPlain, etc.). Specify **\*** to allow any user to authenticate using this security type. Specify **%u** to allow the user of the server process. Default is to deny all users.

**−Protocol3.3**

Always use protocol version 3.3 for backwards compatibility with badly-behaved clients. Default is off.

**−QueryConnect**

Prompts the user of the desktop to explicitly accept or reject incoming connections. Default is off.

The **vncconfig**(1) program must be running on the desktop in order for QueryConnect to be supported.

**−QueryConnectTimeout** *seconds*

Number of seconds to show the Accept connection dialog before rejecting the connection. Default is **10**.

**−RawKeyboard**

Send keyboard events straight through and avoid mapping them to the current keyboard layout. This effectively makes the keyboard behave according to the layout configured on the server instead of the layout configured on the client. Default is off.

**−RemapKeys** *mapping*

Sets up a keyboard mapping. *mapping* is a comma-separated string of character mappings, each of the form *char*-\>*char*, or *char*\<\>*char*, where *char* is a hexadecimal keysym. For example, to exchange the \" and @ symbols you would specify the following:

RemapKeys=0x22\<\>0x40

**−RequireUsername**

Require username for the RSA-AES security types. Default is off.

**−rfbport** *port*

Specifies the TCP port on which Xvnc listens for connections from viewers (the protocol used in VNC is called RFB - \"remote framebuffer\"). The default is 5900 plus the display number. Specify **-1** to disable listening on a TCP port.

**−rfbunixmode** *mode*

Specifies the mode of the Unix domain socket. The default is 0600.

**−rfbunixpath** *path*

Specifies the path of a Unix domain socket on which Xvnc listens for connections from viewers.

**−RSAKey** *path*

Path to the RSA key for the RSA-AES security types (**RA2**, **RA2ne**, **RA2_256** and **RA2ne_256**) in PEM format.

**−SecurityTypes** *sec-types*

Specify which security scheme to use for incoming connections. Valid values are a comma separated list of **None**, **VncAuth**, **Plain**, **TLSNone**, **TLSVnc**, **TLSPlain**, **X509None**, **X509Vnc**, **X509Plain**, **RA2**, **RA2ne**, **RA2_256** and **RA2ne_256**. Default is **TLSVnc,VncAuth**.

**−SendCutText**

Send clipboard changes to clients. Default is on.

**−SendPrimary**

Send the primary selection and cut buffer to the server as well as the clipboard selection. Default is on.

**−SetPrimary**

Set the primary selection as well as the clipboard selection. Default is on.

**−UseBlacklist**

Temporarily reject connections from a host if it repeatedly fails to authenticate. Default is on.

**−UseIPv4**

Use IPv4 for incoming and outgoing connections. Default is on.

**−UseIPv6**

Use IPv6 for incoming and outgoing connections. Default is on.

**−X509Cert** *path*

Path to a X509 certificate in PEM format to be used for all X509 based security types (X509None, X509Vnc, etc.).

**−X509Key** *path*

Private key counter part to the certificate given in **X509Cert**. Must also be in PEM format.

Allowing override of parameters such as **PAMService** or **PasswordFile** can negatively impact security if Xvnc runs under different user than the programs allowed to override the parameters.

When **NoClipboard** parameter is set, allowing override of **SendCutText** and **AcceptCutText** has no effect.

Default is **desktop,AcceptPointerEvents,SendCutText,AcceptCutText,SendPrimary,SetPrimary**.

## USAGE WITH INETD []

By configuring the **inetd**(1) service appropriately, Xvnc can be launched on demand when a connection comes in, rather than having to be started manually. When given the **-inetd** option, instead of listening for TCP connections on a given port it uses its standard input and standard output. There are two modes controlled by the wait/nowait entry in the inetd.conf file.

In the nowait mode, Xvnc uses its standard input and output directly as the connection to a viewer. It never has a listening socket, so cannot accept further connections from viewers (it can however connect out to listening viewers by use of the vncconfig program). Further viewer connections to the same TCP port result in inetd spawning off a new Xvnc to deal with each connection. When the connection to the viewer dies, the Xvnc and any associated X clients die. This behaviour is most useful when combined with the XDMCP options -query and -once. An typical example in inetd.conf might be (all on one line):

5950 stream tcp nowait nobody /usr/local/bin/Xvnc Xvnc -inetd -query localhost -once securitytypes=none

In this example a viewer connection to :50 will result in a new Xvnc for that connection which should display the standard XDM login screen on that machine. It is usually OK to accept connections without a VNC password, since the user still needs to log in via XDM in this case.

In the wait mode, when the first connection comes in, inetd gives the listening socket to Xvnc. This means that for a given TCP port, there is only ever one Xvnc at a time. Further viewer connections to the same port are accepted by the same Xvnc in the normal way. Even when the original connection is broken, the Xvnc will continue to run. If this is used with the XDMCP options -query and -once, the Xvnc and associated X clients will die when the user logs out of the X session in the normal way. It is important to use a VNC password in this case. A typical entry in inetd.conf might be:

5951 stream tcp wait james /usr/local/bin/Xvnc Xvnc -inetd -query localhost -once passwordFile=/home/james/.config/tigervnc/passwd

In fact typically, you would have one entry for each user who uses VNC regularly, each of whom has their own dedicated TCP port which they use. In this example, when user \"james\" connects to :51, he enters his VNC password, then gets the XDM login screen where he logs in in the normal way. However, unlike the previous example, if he disconnects, the session remains persistent, and when he reconnects he will get the same session back again. When he logs out of the X session, the Xvnc will die, but of course a new one will be created automatically the next time he connects.

## SEE ALSO []

**vncconfig**(1), **vncpasswd**(1), **vncviewer**(1), **vncsession**(8), **Xserver**(1), **inetd**(1)\
https://www.tigervnc.org

## AUTHOR []

Tristan Richardson, RealVNC Ltd. and others.

VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite.

------------------------------------------------------------------------