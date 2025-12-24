# Source: https://www.tightvnc.com/doc/win/TightVNC_for_Windows-Installation_and_Getting_Started.pdf

TightVNC for Windows: Installation and Getting Started
                                       TightVNC Version 2.6
                                  Copyright © 2012 GlavSoft LLC.

Introduction to TightVNC
TightVNC is a remote desktop software application. It lets you connect to another computer and
display its live remote desktop or control the remote computer with your mouse and keyboard, just
like you do it sitting in front of that computer. Since it is designed to work out of a box, TightVNC
can be very handy not only for system administrators and support service, but for all users who
want to benefit from TightVNC.
Like other VNC systems, it consists of two parts: the Server, which shares the screen of the
machine it's running on, and the Viewer, which shows the remote screen received from the server.
So to get started, you just need to run a server on the machine you want to access remotely, and
connect to it with a viewer. TightVNC distribution for Windows includes both the server and the
viewer parts available under GNU GPL license v.2 and commercial license [HTML].

Installation
Starting from the version 2.5, TightVNC comes in the form of MSI-packages. They can be easily
installed using standard Windows Installer. Just select the package matching a type of your
operating system (32-bit or 64-bit), run it and follow the installation wizard. The TightVNC Setup
Wizard lets you choose the components to install (TightVNC Server and/or TightVNC Viewer) and
adjust some installation settings.
The default settings suit most users needs. However, if you want to change them, a few check boxes
on "Select additional tasks" step may require an explanation.
   ✔   Register TightVNC Server as a system service (recommended)
       By default, TightVNC Server is installed as a Windows service and starts immediately after
       installation. At the end of the installation you will be asked about passwords for TightVNC
       Server as a service, in order to protect it from unauthorized access. If you uncheck this
       check box, TightVNC Server will be available only as a normal Windows application, but
       you can always register it as service later. See the "TightVNC Server" chapter for more
       information.
   ✔   Configure system to allow services simulate Ctrl-Alt-Del
       When TightVNC server runs as a Windows service, it can simulate "Ctrl-Alt-Del" key
       combination. If you want to disable this combination to prevent access to task manager and
       system reboot, uncheck this check box.
After you install TightVNC, we also recommend you to download and set up DFMirage mirror
display driver [EXE]. It allows TightVNC to gain the best performance under Windows. With
DFMirage, TightVNC Server can detect screen updates and grab pixel data in a very efficient way,
which decreases CPU consumption.
Also some administrators may wish to install TightVNC using silent installation mode. A silent
installation runs on its own without any intervention so that administrators are freed from the task
of monitoring the installation and providing input to dialog boxes. This method also lets you to
preconfigure your TightVNC server settings. Silent installation is described in detail in the
documentation on TightVNC MSI installer [PDF].
In case you are curious, the table below shows where TightVNC keeps its files. Note that TightVNC
does not install anything into the system directory.
TightVNC files                 Location

Default destination            Program Files\TightVNC

"Start" menu entry             Start->Programs->TightVNC

Registry keys                  HKEY_LOCAL_MACHINE\Software\TightVNC
                               HKEY_CURRENT_USER\Software\TightVNC

Table 1: TightVNC data

Getting Started

TightVNC Server
TightVNC Server is designed to run in two modes:
    •   application mode (personal server for a current user);
    •   service mode (system-wide server running in the background).
In application mode, the server, just like any other desktop software, can be running only during the
current user session and quits on the logout. Each user has his/her personal settings and passwords.
To make a machine accessible even while there is no user logged in, and to make the server start
automatically on reboot, the TightVNC Server should be running as a system service. Service mode
is configured independently of application mode; the settings and passwords of TightVNC Server as
a service are global for all users.
The distinctions between these modes are illustrated in the table below.
                             TightVNC Server (application mode)        TightVNC Server (service mode)
"Start" menu entry           Programs\TightVNC\TightVNC Server         Programs\TightVNC\TightVNC Server
                             (Application Mode)                        (Service Mode)
Tray icon label              TightVNC Server                           TightVNC Service
Starts automatically         No                                        Yes
Server activity              Runs only for current user (quits when    Runs in the background as long as Windows
                             the user logs out)                        is running

Server settings              Personal settings for each user           Global settings common for all Windows
                                                                       users
Allows "Ctrl+Alt+Delete" No                                            Yes
combination

Table 2: The differences between application and service modes of TightVNC Server

Running TightVNC Server in Application Mode
To start TightVNC Server in the application mode, choose:
Start->Programs->TightVNC->TightVNC Server (Application Mode)->Run TightVNC Server.
If you want to quit the TightVNC server, right-click the TightVNC tray icon and choose "Shutdown
TightVNC Server".
Running TightVNC Server in Service Mode
To run TightVNC Server as a system service, follow these instructions:
   1. If you unchecked the recommended option "Register TightVNC Server as a system service"
      during installation, first, you need to register TightVNC Server as a service. Click:
       Start->Programs->TightVNC->TightVNC Server (Service Mode)->Register TightVNC
       Service.
   2. To start TightVNC Server as a service, click:
       Start->Programs->TightVNC->TightVNC Server (Service Mode)->Start TightVNC Service
       or type in the command line:
       net start tvnserver
   3. If you want the server to show its tray icon, click:
       Start->Programs->TightVNC->TightVNC Server (Service Mode)->TightVNC Server –
       Control Interface
To stop TightVNC Server in service mode, use one of two ways:
   •   click Start->Programs->TightVNC->TightVNC Server (Service Mode)->Stop TightVNC
       Service
   •   type in the command line:
       net stop tvnserver

Using TightVNC Server
Despite the differences mentioned above, TightVNC server modes are configured and used in the
same way.
On successful startup, TightVNC will add a small icon to the tray in the system task bar
(notification area). Moving the mouse over this icon shows the server mode and the IP address of
the machine (which can be entered in the remote viewer to access this server).

Mouse over the icon shows TightVNC Server mode (as a service) and the IP address

Mouse over the icon shows TightVNC Server mode (as an application) and the IP address
When you launch TightVNC Server for the first time, it will ask the passwords for control interface
and VNC authentications. For security reasons, the server will not accept incoming connections,
until you specify required passwords or intentionally cancel VNC authentication. The last option is
not safe, and TightVNC Server will notify you about it:
Hint is warning that no authorization is being used
To protect the machine from unauthorized access, you should set passwords for VNC
authentication. Follow these instructions:
   1. Click the TightVNC Server/Service tray icon.
   2. In the "Server" tab, check "Require VNC authentication".
   3. Set passwords for full-control access (Primary password) and view-only access (View-only
      password).
Also you may wish to set a control interface password. In Configuration window, click the
"Administration" tab, check "Protect control operations with an administrative password" and set
desirable password.
The passwords for TightVNC Server in a service mode are set similarly using its own control
interface (click the TightVNC Service tray icon). If you want to set passwords for TightVNC
Service while it is not running, use Offline Configuration (Start->Programs->TightVNC-
>TightVNC Server (Service Mode)->TightVNC Service – Offline Configuration).

TightVNC Server Status
The TightVNC Server/Service tray icon indicates you about server status. It has white background
if the server is ready but there is no viewer connected, and inverted colors when at least one viewer
has accessed the desktop.

Icon shows that server is running and ready to accept new client connections

Icon is shown in inverted colors when viewers are connected
Red border around TightVNC Server tray icon means that the server does not accept client
connections. It may happen in case you forbid incoming connection in the TightVNC control
interface or for some other reasons, which will be shown in the tray icon hint.

Red border indicates that new client connections are disabled
If you right-click the TightVNC Server/Service tray icon, you will see TightVNC Server menu:

TightVNC Server menu
Lets take a look at the TightVNC Server menu:
   •   Configuration... – Displays TightVNC configuration window (Control Interface), which
       allows the user to change various parameters of the TightVNC Server. This window is also
       displayed on click the tray icon.
   •   Attach Listening Viewer... – Connects from the TightVNC server to a viewer started in the
       "listening" mode. The name of the target viewer machine and port are entered in the dialog.
       This so called "reverse connection" is treated as shared.
   •   Attach to Dispatcher... – This is a future extension that will allow to connect a server and a
       viewer from different networks using a mediator, or Dispatcher.
   •   Disconnect All Viewers – Disconnects all currently connected viewers from the server.
   •   About... – Shows information about the software.
   •   Shutdown TightVNC Server – Quits.
Now, when you run TightVNC Server and set all required passwords, the server is accessible for
incoming connections.

Running TightVNC Viewer
To view and control a remote desktop where a TightVNC Server is running, you need to run the
TightVNC Viewer. To run the viewer, choose:
Start->Programs->TightVNC->TightVNC Viewer.
You will see a window allowing to choose a server to connect to.
                 "New Connection" dialog window
To connect to remote server, enter its host name or IP address in the field "Remote Host" and click
"Connect". Port number is optional; you need to specify it only if it differs from the default value
(5900). On successful connection, you will be prompted for the server password, if there is one.
After you provide a correct password, you will see the remote desktop.
When you're not able to connect to a remote server (e.g. when the server is "hidden" in local
network behind a router), you may try a reverse connection. In this case, you connect from a server
to a client, not vice versa. To set the viewer to listening more, click "Listening mode" button. After
you do so, the viewer's icon will appear in the system tray area, and the viewer will be able to
accept incoming connections from a TightVNC server (see the description of "Attach Listening
Viewer..." TightVNC Server menu item).

Using Web Browser as a Viewer (TightVNC Java Viewer)
TightVNC Server contains a small web server as well. This server listens for incoming HTTP
connections on 5800 port (by default). If you connect to the server with a web browser, it will send
you back a Java applet – TightVNC Java Viewer. The applet allows you to connect to this remote
server and control its desktop directly from your web browser.
In order to connect to the remote machine "myhost", you should point your web browser at:
http://myhost:5800/. The applet will prompt you for a TightVNC authentication password, and then
display the remote desktop. Obviously, the browser must support Java applets. Also you should
enable "Serve Java Viewer to Web clients" option in the TightVNC Server configuration.

Uninstalling TightVNC
TightVNC can be uninstalled using the Add/Remove Programs utility under the Control Panel.

References
For additional information on installation and configuration see the main documentation page and
the TightVNC FAQ.
If you want to compile the source yourself, please, read instructions in the BUILDING.txt file
included in the source archive.