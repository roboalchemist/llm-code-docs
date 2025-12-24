# Source: https://tigervnc.org/doc/x0vncserver.html

# X0VNCSERVER 

------------------------------------------------------------------------

## NAME []

x0vncserver − TigerVNC server for X displays

## SYNOPSIS []

**x0vncserver** \[*options*\] **\
x0vncserver -version**

## DESCRIPTION []

**x0vncserver** is a TigerVNC server which makes any X display remotely accessible via VNC, TigerVNC or compatible viewers. Unlike **Xvnc**(1), it does not create a virtual display. Instead, it just shares an existing X server (typically, that one connected to the physical screen).

XDamage will be used if the existing X server supports it. Otherwise **x0vncserver** will fall back to polling the screen for changes.

## OPTIONS []

**x0vncserver** interprets the command line as a list of parameters with optional values. Running **x0vncserver −h** will show a list of all valid parameters with short descriptions. All parameters are optional, but normally you would have to use the **PasswordFile** parameter (see its description below).

There are several forms of specifying parameters in the command line (here we use '*SomeParameter*' as an example parameter name): **\
-***SomeParameter*

Enable the parameter, turn the feature on. This form can be used with parameters that simply enable or disable some feature.

**-***SomeParameter***=0**

Disable the parameter, turn the feature off.

**-***SomeParameter***=***value*

Assign the specified *value* to the parameter. The leading dash can be omitted, or it can be doubled if desired (like in GNU-style long options).

Parameter names are case-insensitive, their order in the command line can be arbitrary.

## PARAMETERS []

**−AcceptKeyEvents**

Accept key press and release events from clients. Default is on.

**−AcceptPointerEvents**

Accept pointer movement and button events from clients. Default is on.

**−AcceptSetDesktopSize**

Accept requests to resize the size of the desktop. Default is on.

**−AlwaysShared**

Always treat incoming connections as shared, regardless of the client-specified setting. Default is off.

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

**−display** *display*

The X display name. If not specified, it defaults to the value of the DISPLAY environment variable.

**−FrameRate** *fps*

The maximum number of updates per second sent to each client. If the screen updates any faster then those changes will be aggregated and sent in a single update to the client. Note that this only controls the maximum rate and a client may get a lower rate when resources are limited. Default is **60**.

**−Geometry** *geometry*

This option specifies the screen area that will be shown to VNC clients. The format is *width***x***height***+***xoffset***+***yoffset* , where '+' signs can be replaced with '−' signs to specify offsets from the right and/or from the bottom of the screen. Offsets are optional, +0+0 is assumed by default (top left corner). If the argument is empty, full screen is shown to VNC clients (this is the default).

**−GnuTLSPriority** *priority*

GnuTLS priority string that controls the TLS sessionâs handshake algorithms. See the GnuTLS manual for possible values. Default is **NORMAL**.

**−HostsFile** *filename*

This parameter allows to specify a file name with IP access control rules. The file should include one rule per line, and the rule format is one of the following: +*address*/*prefix* (accept connections from the specified address group), -*address*/*prefix* (reject connections) or ?*address*/*prefix* (query the local user). The first rule matching the IP address determines the action to be performed. Rules that include only an action sign (+, - or ?) will match any IP address. *Prefix* is optional and is specified as a number of bits (e.g. /24). Default is to accept connections from any IP address.

**−IdleTimeout** *seconds*

The number of seconds after which an idle VNC connection will be dropped. Default is 0, which means that idle connections will never be dropped.

**−ImprovedHextile**

Use improved compression algorithm for Hextile encoding which achieves better compression ratios by the cost of using slightly more CPU time. Default is on.

**−interface** *IP address*

Listen on interface. By default x0vncserver listens on all available interfaces.

**−localhost**

Only allow connections from the same machine. Useful if you use SSH and want to stop non-SSH connections from any other hosts.

**−Log** *logname***:***dest***:***level***\[, \...\]**

Configures the debug log settings. *dest* can currently be **stderr**, **stdout** or **syslog**, and *level* is between 0 and 100, 100 meaning most verbose output. *logname* is usually **\*** meaning all, but you can target a specific source file if you know the name of its \"LogWriter\". Default is **\*:stderr:30**.

**−MaxConnectionTime** *seconds*

Terminate when a client has been connected for *N* seconds. Default is 0.

**−MaxDisconnectionTime** *seconds*

Terminate when no client has been connected for *N* seconds. Default is 0.

**−MaxIdleTime** *seconds*

Terminate after *N* seconds of user inactivity. Default is 0.

**−MaxProcessorUsage** *percent*

Maximum percentage of CPU time to be consumed when polling the screen. Default is 35.

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

**−PollingCycle** *milliseconds*

Milliseconds per one polling cycle. Actual interval may be dynamically adjusted to satisfy **MaxProcessorUsage** setting. Default is 30.

**−Protocol3.3**

Always use protocol version 3.3 for backwards compatibility with badly-behaved clients. Default is off.

**−QueryConnect**

Prompts the user of the desktop to explicitly accept or reject incoming connections. Default is off.

**−QueryConnectTimeout** *seconds*

Number of seconds to show the Accept connection dialog before rejecting the connection. Default is **10**.

**−RawKeyboard**

Send keyboard events straight through and avoid mapping them to the current keyboard layout. This effectively makes the keyboard behave according to the layout configured on the server instead of the layout configured on the client. Default is off.

**−AcceptCutText**

Accept clipboard updates from clients. Default is on.

**−SetPrimary**

Set the PRIMARY as well as the CLIPBOARD selection. Default is on.

**−MaxCutText** *bytes*

The maximum permitted size of an incoming clipboard update. Default is **262144**.

**−SendCutText**

Send clipboard changes to clients. Default is on.

**−SendPrimary**

Send the PRIMARY as well as the CLIPBOARD selection to clients. Default is on.

**−RemapKeys** *mapping*

Sets up a keyboard mapping. *mapping* is a comma-separated string of character mappings, each of the form *char*-\>*char*, or *char*\<\>*char*, where *char* is a hexadecimal keysym. For example, to exchange the \" and @ symbols you would specify the following:

RemapKeys=0x22\<\>0x40

**−RequireUsername**

Require username for the RSA-AES security types. Default is off.

**−rfbport** *port*

Specifies the TCP port on which x0vncserver listens for connections from viewers (the protocol used in VNC is called RFB - \"remote framebuffer\"). Specify **-1** to disable listening on a TCP port. The default port is 5900 when started directly, and -1 when activated by a systemd socket.

**−rfbunixmode** *mode*

Specifies the mode of the Unix domain socket. The default is 0600.

**−rfbunixpath** *path*

Specifies the path of a Unix domain socket on which x0vncserver listens for connections from viewers. Default is to not listen to any Unix domain socket.

**−RSAKey** *path*

Path to the RSA key for the RSA-AES security types (**RA2**, **RA2ne**, **RA2_256** and **RA2ne_256**) in PEM format.

**−SecurityTypes** *sec-types*

Specify which security scheme to use for incoming connections. Valid values are a comma separated list of **None**, **VncAuth**, **Plain**, **TLSNone**, **TLSVnc**, **TLSPlain**, **X509None**, **X509Vnc**, **X509Plain**, **RA2**, **RA2ne**, **RA2_256** and **RA2ne_256**. Default is **TLSVnc,VncAuth**.

**−UseBlacklist**

Temporarily reject connections from a host if it repeatedly fails to authenticate. Default is on.

**−UseIPv4**

Use IPv4 for incoming and outgoing connections. Default is on.

**−UseIPv6**

Use IPv6 for incoming and outgoing connections. Default is on.

**−UseSHM**

Use MIT-SHM extension if available. Using that extension accelerates reading the screen. Default is on.

**−X509Cert** *path*

Path to a X509 certificate in PEM format to be used for all X509 based security types (X509None, X509Vnc, etc.).

**−X509Key** *path*

Private key counter part to the certificate given in **X509Cert**. Must also be in PEM format.

## SEE ALSO []

**Xvnc**(1), **vncpasswd**(1),\
https://www.tigervnc.org/

## AUTHOR []

Constantin Kaplinsky and others.

VNC was originally developed by the RealVNC team while at Olivetti Research Ltd / AT&T Laboratories Cambridge. TightVNC additions were implemented by Constantin Kaplinsky. Many other people have since participated in development, testing and support. This manual is part of the TigerVNC software suite.

------------------------------------------------------------------------