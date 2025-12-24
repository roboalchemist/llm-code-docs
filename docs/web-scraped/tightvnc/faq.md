# Source: https://www.tightvnc.com/faq.php

## Contents

-   [What Windows versions does TightVNC support?](#OS)
-   [How would I connect from the Internet to a machine in the internal network which is behind a router?](#portfwd)
-   [How secure is TightVNC?](#howsecure)
-   [How to exit full screen TightVNC Viewer?](#exitfullscreen)
-   [How can I hide the tray icon of my TightVNC Server?](#hideicon)
-   [Does TightVNC work on Mac OS X?](#macosx)
-   [How can I uninstall TightVNC?](#uninstall)

------------------------------------------------------------------------

[]

## What Windows versions does TightVNC support?

TightVNC runs basically on any version of Windows (both 32-bit and 64-bit systems are supported):

-   Windows XP / Vista / 7 / 8 / 8.1 / 10 / 11,
-   corresponding versions of Windows Server.

On Windows XP, you should have the latest Service Pack installed. Windows CE systems are not supported.

There are no minimum disk space or RAM requirements. TightVNC uses so little space and memory that it can run anywhere Windows is running.

Previous TightVNC version 1.2 and 1.3 have some limitations, however. It is not possible to use TightVNC Server as a system service on Windows Vista / Windows 7 in this case.

------------------------------------------------------------------------

[]

## How would I connect from the Internet to a machine in the internal network which is behind a router?

You should enable \"port forwarding\" in your router\'s configuration. Port forwarding allows passing external connections to computers in the internal network. Almost all routers support this type of redirection.

For example, to access VNC or TightVNC server running on default ports, a router can be configured such way that TCP connections to ports 5900 and 5800 would be passed to the same ports of a particular machine with a specified private IP address (typically 192.168.x.x).

Here is an example of configuring port forwarding, assuming that TightVNC Server is running on default ports 5900 and 5800, on the machine with IP 192.168.1.100:

  -----------------------------------------------------------------------------
  Application   Start\      End\        Protocol    IP Address      Enable
                Port        Port                                    
  ------------- ----------- ----------- ----------- --------------- -----------
  TightVNC      5900        5900        TCP         192.168.1.100   yes

  TightVNC      5800        5800        TCP         192.168.1.100   yes
  -----------------------------------------------------------------------------

When port forwarding is set up, you can connect to the router\'s IP address such way as if it was your target machine\'s IP address, but you should specify those port numbers on which port forwarding was activated.

See also:

-   [www.portforward.com](http://www.portforward.com/) (help on setting up port forwarding on various routers and firewalls)

------------------------------------------------------------------------

[]

## How secure is TightVNC?

Although TightVNC encrypts VNC passwords sent over the net, the rest of the traffic is sent as is, unencrypted (for password encryption, VNC uses a DES-encrypted challenge-response scheme, where the password is limited by 8 characters, and the effective DES key length is 56 bits). So using TightVNC over the Internet can be a security risk. To solve this problem, we have plans to implement built-in encryption in future versions of TightVNC.

In the mean time, if you need *real* security, we recommend installing an SSH server, and using SSH tunneling for all TightVNC connections from untrusted networks.

------------------------------------------------------------------------

[]

## How to exit full screen TightVNC Viewer?

To exit full-screen mode in TightVNC Viewer for Windows, you can use the Ctrl-Alt-Shift-F keyboard combination.

The reason for the complex keyboard combination is that we should use a hotkey that is unlikely to be used by normal applications. If a combination is used as a TightVNC Viewer hotkey, it will be processed locally in the viewer and thus will not be passed to the VNC server, so there may be problems with remote applications where the same keyboard shortcut is used.

In our modern applications such as [Remote Ripple](https://remoteripple.com/) and [MightyViewer](https://mightyviewer.com/), exiting full-screen mode is much easier. Simply move the mouse pointer to the upper border of the screen, and a floating toolbar will appear where you can choose to exit full screen.

------------------------------------------------------------------------

[]

## How can I hide the tray icon of my TightVNC Server?

### Answer for TightVNC versions 1.x:

To disable the tray icon, you should start the \"regedit\" utility from the command line, go to the HKEY_LOCAL_MACHINE\\Software\\ORL\\WinVNC3\\ folder, and create a DWORD parameter with the name \"DisableTrayIcon\" and the value \"1\". Then, after restarting TightVNC Server, the icon will not be shown anymore.

But please note that hiding the icon is usually not a good idea. For example, if you want to restrict users from changing the server Properties, it might be better to use the AllowProperties setting. For more information, see the description of \"AllowProperties\", \"AllowShutdown\" and \"AllowEditClients\" options in the [VNC documentation](http://www.realvnc.com/products/free/3.3.7/winvnc.html).

### Answer for TightVNC versions 2.x:

Open TightVNC configuration, choose Server tab, uncheck \"Show icon in the notification area\", press Ok.

To show the icon again, use one of Control Interface or Offline Configuration shortcuts found under the TightVNC group under Start\\All Programs.

------------------------------------------------------------------------

[]

## Does TightVNC work on Mac OS X?

Currently, we do not offer a version for Mac OS X. It\'s very likely that TightVNC will include one in the future, but not in the nearest days. Currently, our team is busy working on the Windows version.

If you need viewer part on Mac OS X, try TightVNC Java Viewer. It\'s cross-platform and should work fine in any system where Java environment can be installed, including MacOS X.

Also note that recent versions of Mac OS X include built-in VNC-compatible server which is compatible with TightVNC as well. In other words, you can connect to any modern Mac OS X system with TightVNC Viewer.

------------------------------------------------------------------------

[]

## How do I uninstall TightVNC?

Normally, TightVNC can be removed just like any other software, from the Control Panel (Add/Remove Programs). But if something goes wrong, or TightVNC was installed manually, you can always remove it manually using step-by-step procedures below.

### Uninstall procedure for TightVNC versions 1.x:

1.  Log in as an Administrator (or as a user with similar permissions).
2.  If TightVNC Server is running, close it. If it is running but not showing the tray icon, choose Process Manages, locate WinVNC.exe process and shutdown it.
3.  If TightVNC Server was registered as a system service, unregister it. To do that, locate WinVNC.exe file under \\Program Files\\TightVNC (or wherever TightVNC was installed), and type in the command line: WinVNC.exe -remove
4.  Remove the whole \\Program Files\\TightVNC directory (or wherever TightVNC was installed).
5.  Remove all TightVNC shortcuts from the Start\\All Programs menu.
6.  Remove the settings from the registry if desired. The settings can be found in HKEY_LOCAL_MACHINE\\Software\\ORL and/or HKEY_CURRENT_USER\\Software\\ORL.

### Uninstall procedure for TightVNC versions 2.x:

1.  Log in as an Administrator (or as a user with similar permissions).
2.  If TightVNC Server is running, close it. If it is running but not showing the tray icon, choose Process Manages, locate all tvnserver.exe process and shutdown each one of them.
3.  If TightVNC Server was registered as a system service, unregister it. To do that, locate tvnserver.exe file under \\Program Files\\TightVNC (or wherever TightVNC was installed), and type in the command line: tvnserver.exe -remove
4.  Remove the whole \\Program Files\\TightVNC directory (or wherever TightVNC was installed).
5.  Remove all TightVNC shortcuts from the Start\\All Programs menu.
6.  Remove the settings from the registry if desired. The settings can be found in HKEY_LOCAL_MACHINE\\Software\\TightVNC and/or HKEY_CURRENT_USER\\Software\\TightVNC