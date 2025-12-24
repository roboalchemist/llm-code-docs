# Source: https://help.realvnc.com/hc/en-us/articles/360002313518-vncserver-x11-man-page

# vncserver-x11 man page 

[Follow](/hc/en-us/articles/360002313518-vncserver-x11-man-page/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360032675571/admin-settings-male-filled.png)

**[RealVNC Support Agent](/hc/en-us/profiles/361957203312-RealVNC-Support-Agent)**

Updated March 22, 2024 15:02

# vncserver-x11 

## Name 

**vncserver-x11** - VNC® Server in User Mode

## Synopsis 

**vncserver-x11** \[*OPTION*\...\]

**vncserver-x11** \[*MODE*\] \[*OPTION*\...\] *COMMAND*

## Description 

**vncserver-x11** starts VNC Server in User Mode, to allow the desktop of the currently-logged on user to be remoted to VNC Viewer on another computer. When this user is logged out, VNC Server automatically stops; all VNC Viewer users are disconnected, and cannot reconnect. Note that a suitable offline license is required; see [vnclicense](https://help.realvnc.com/hc/en-us/articles/360002310657).

Run **vncserver-x11** to start VNC Server and wait for connections. A user interface consisting of a status dialog and, if supported by the window manager, a status icon is displayed, providing connectivity information and convenient access to features such as file transfer and chat. The status dialog shows information about how to connect and authenticate from VNC Viewer on another computer.

Note that an instance of **vncserver-x11** is automatically started (as the root user) by VNC Server in Service Mode; see [vncserver-x11-serviced](https://help.realvnc.com/hc/en-us/articles/360002310857).

**vncserver-x11** consumes one computer \'desktop\' from your subscription. See [vnclicense](https://help.realvnc.com/hc/en-us/articles/360002310657) for how to check licensing details.

## Commands 

Applying a command to **vncserver-x11** performs an auxiliary operation instead of starting VNC Server.

To see a list of valid commands, run [`vncserver-x11`]` `[`-help`].

## Mode 

To apply a *COMMAND* to the privileged instance of **vncserver-x11** started by VNC Server in Service Mode, run the command as root and specify **-service**.

Otherwise, commands apply automatically to VNC Server in User Mode.

## OPTIONS 

Options are parameters, used to configure VNC Server, and also the following:

[`-iconnect`]` `[`HOST[::PORT]`]
:   Establishes a reverse connection to a Listening VNC Viewer on HOST at PORT (5500 by default). See [vncviewer](https://help.realvnc.com/hc/en-us/articles/360002310477).

[`-newinstance`]
:   Starts a new instance of VNC Server, providing your subscription permits; see [vnclicense](https://help.realvnc.com/hc/en-us/articles/360002310657). By default, running **vncserver-x11** a second time interacts with the first instance.

[`-showstatus`]
:   Displays the status dialog and status icon. This may be useful to force display in some desktop environments.

[`-vncconfigfile`]` FILE`
:   For convenience, if you have many parameters to specify at the command line, populate a text file (one parameter per line; omit the dash) and reference it using this flag.

To see a list of valid parameters, run [`vncserver-x11`]` `[`-help`].

## VNC configuration files 

Parameters can be specified as command line *OPTIONS*, but preferably in VNC configuration files. VNC configuration files are available for:

-   All programs, or just VNC Server
-   All users of the computer, or just the user starting VNC Server
-   Policy, in order to lock down VNC Server

When VNC Server starts, parameters are applied in the following order:

1.  System-wide VNC configuration files
2.  Per-user VNC configuration files
3.  Command line *OPTIONS*
4.  Policy VNC configuration files

This means that a particular parameter specified at the command line overrides the same parameter specified in a per-user or in a system-wide VNC configuration file, but is itself overridden by the same parameter specified in a policy VNC configuration file. Policy cannot be changed by users.

Note there is a disadvantage to specifying parameters at the command line: parameters cannot be reloaded while VNC Server is running. VNC configuration files *can* be reloaded, however, which means that VNC Server can be reconfigured without downtime.

For a full list of available VNC configuration files, visit [Configuring VNC Connect Using Parameters](https://help.realvnc.com/hc/en-us/articles/360002253878).

## Logging 

By default, **vncserver-x11** logs basic activity to file at *\$HOME/.vnc/vncserver-x11.log*.

To change the log quality, quantity, or destination, specify the **Log**, **LogDir**, and **LogFile** parameters.

## See also 

[vncserver-x11-serviced](https://help.realvnc.com/hc/en-us/articles/360002310857), [vnclicense](https://help.realvnc.com/hc/en-us/articles/360002310657), [vncinitconfig](https://help.realvnc.com/hc/en-us/articles/360002313458), [vncpasswd](https://help.realvnc.com/hc/en-us/articles/360002313698), [vncviewer](https://help.realvnc.com/hc/en-us/articles/360002310477)