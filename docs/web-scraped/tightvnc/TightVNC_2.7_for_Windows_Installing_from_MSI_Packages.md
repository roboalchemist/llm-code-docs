# Source: https://www.tightvnc.com/doc/win/TightVNC_2.7_for_Windows_Installing_from_MSI_Packages.pdf

TightVNC for Windows: Installing from MSI Packages
                                        TightVNC Version 2.7
                                  Copyright © 2012 GlavSoft LLC.

TightVNC is distributed as a Microsoft Windows Installer (MSI) file. These files can be installed in
two ways.
   •   Using the installation wizard
       Simply double-click an MSI file in the file explorer and follow the on-screen instructions.
   •   Silent (unattended) installation
       With this option, you can automate TightVNC installation on one or multiple computers as it
       does not require user input. Simply create a script that automatically installs TightVNC, or
       install it through a terminal connection (for example, Telnet).
All available options for silent installation are found below.

System Requirements
TightVNC runs basically on any version of Windows:
   •   Windows XP / Vista / 7 / 8
   •   Windows Server 2003 / 2008 / 2008 R2 / 2012
Both 32-bit (x86) and 64-bit (x64) systems are supported.
There are no minimum disk space or RAM requirements. TightVNC uses so little space and
memory that it can run anywhere Windows is running.

32-bit and 64-bit Packages
For Windows, separate TightVNC versions are available for 32-bit and 64-bit systems. These are
(2.7.1 matches a version number):
   •   tightvnc-2.7.1-setup-32bit.msi
   •   tightvnc-2.7.1-setup-64bit.msi
Please check My Computer > Properties to download and install the correct version for your
system. (It is not recommended to run a 32-bit version on a 64-bit system, as it can cause lower
performance.)

Silent Installation
To install an MSI package silently from the command line, you should run the msiexec tool with /i
and /quiet options (where /i stands for install, /quiet sets silent mode). For TightVNC, it would be a
good idea to add the /norestart option, to prevent rebooting the system after installing the software.
If everything is good, TightVNC installation should not require restart even if its previous version is
running as a service. The installer should upgrade the system correctly, by shutting down old
service, installing the files and then starting new service.
Here is the simplest example of installing TightVNC in a silent mode:
   •   msiexec /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
This command should install TightVNC with default settings. However, MSI allows you to
customize installation via so called MSI properties. The general syntax is the following:
    •      msiexec /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
           PROPERTY1=value1 PROPERTY2=value2 PROPERTY3=value3
There is a number of standard properties which are supported by every package (e.g. ADDLOCAL
for selecting components to be installed). Also, each package can add its own MSI properties to
perform some package-dependent customization. In next sections, all TightVNC-specific MSI
properties will be documented.

Components to Install
If you would like to install a specific component of TightVNC, use the standard MSI property
named ADDLOCAL. The following three commands install only the server part, only the client part
and both parts, correspondingly:
    •      msiexec /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
           ADDLOCAL=Server
    •      msiexec /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
           ADDLOCAL=Viewer
    •      msiexec /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
           ADDLOCAL="Server,Viewer"

Properties, Part 1: Installation Options
All available installation options listed below work only in the silent mode (with /quiet option).
Properties which are related to the TightVNC Viewer installation configuration begin with
VIEWER_ prefix, and server installation properties begin with SERVER_ prefix. Notice that a
property will have an effect only if you install the component associated with it.
Property                           Value

VIEWER_ASSOCIATE_VNC_EXTENSION     0 – do not associate the ".vnc" file extension with tvnviewer.exe
                                   1 – associate the ".vnc" file extension with tvnviewer.exe
                                   Default value: 1
SERVER_REGISTER_AS_SERVICE         0 – do not register the server as a service
                                   1 – register the server as a service
                                   Default value: 1
SERVER_ADD_FIREWALL_EXCEPTION      0 – do not add firewall exception for the TightVNC Server
                                   1 – add firewall exception for the TightVNC Server
                                   Default value: 1
VIEWER_ADD_FIREWALL_EXCEPTION      0 – do not add firewall exception for the TightVNC Viewer
                                   1 – add firewall exception for the TightVNC Viewer
                                   Default value: 1
SERVER_ALLOW_SAS                   0 – do not allow generating the "Ctrl+Alt+Del" combination (also known as SAS)
                                   programmatically
                                   1 – allow generating the "Ctrl+Alt+Del" combination programmatically
                                   Default value: 1

Table 1: Installation options

Properties, Part 2: TightVNC Server Configuration (Service Mode)
You can preconfigure your TightVNC Server during installation, by specifying configuration-
related properties in the command line. This will affect service mode only, it will not alter settings
of application-mode TightVNC Server.
Each configuration option (e.g. ALLOWLOOPBACK) is controlled via a pair of MSI properties
with different prefixes (SET_ALLOWLOOPBACK and VALUE_OF_ALLOWLOOPBACK in this
example).
SET_* properties control if the respective option should be modified. They accept the following
values:
   •    1 – set the configuration option (you should provide the corresponding VALUE_OF_*
        property);
   •    0 – do not change the option;
   •    −1 – remove the option from the server configuration (this should result in resetting the
        option to its default value).
VALUE_OF_* properties provide actual values for the configuration options, but they take effect
only if the corresponding SET_* properties have been set to 1. Thus, to set each individual
configuration option XXX, you must specify both SET_XXX and VALUE_OF_XXX properties. For
example, to disable incoming connections in your newly installed server, you should install
TightVNC with a command like this:
   •    msiexec.exe /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
          SET_ACCEPTRFBCONNECTIONS=1 VALUE_OF_ACCEPTRFBCONNECTIONS=0
Here is a list of all server options configurable via MSI properties:
MSI Property Names                       Option Value (for VALUE_* Properties)                       Configuration Window
SET_ACCEPTHTTPCONNECTIONS                Enables Java Viewer (on HTTP connections)                   Server/Web Access
                                         0 – do not serve Java Viewer to Web clients
VALUE_OF_ACCEPTHTTPCONNECTIONS
                                         1 – serve Java Viewer to Web clients
                                         Default value: 1

SET_ACCEPTRFBCONNECTIONS                 0 – do not accept incoming connections                      Server/Incoming Viewer
                                         1 – accept incoming connections                             Connections
VALUE_OF_ACCEPTRFBCONNECTIONS
                                         Default value: 1
SET_ALLOWLOOPBACK                        0 – do not allow loopback connections                       Access Control/Loopback
                                         1 – allow loopback connections                              connections
VALUE_OF_ALLOWLOOPBACK
                                         Default value: 0

SET_ALWAYSSHARED                         Defines server behaviors on a new connection                Administration/Session
                                         0 – allow non-shared connections                            Sharing
VALUE_OF_ALWAYSSHARED
                                         1 – always treat new connections as shared
                                         Default value: 0

                                         If both ALWAYSHARED and NEVERSHARED are false
                                         then the type of connection is determined by client
                                         settings

                                         Note: this option is described further in the section
                                         "Properties, Part 3: Server behavior on new connections"
SET_BLOCKLOCALINPUT                      0 – allow local input during client sessions                Server/Web Access
                                         1 – block local input during client sessions
VALUE_OF_BLOCKLOCALINPUT
                                         Default value: 0
SET_BLOCKREMOTEINPUT                     0 – allow remote input events                               Server/Input Handling
                                         1 – block remote input events
VALUE_OF_BLOCKREMOTEINPUT
                                         Default value: 0
SET_DISCONNECTACTION                     Defines an action that will be performed when last client   Administration/When Last
                                         disconnects:                                                Client Disconnects
VALUE_OF_DISCONNECTACTION
                                         0 – do nothing
                                         1 – lock desktop
                                         2 – log off current user
                                         Default value: 0
MSI Property Names                   Option Value (for VALUE_* Properties)                        Configuration Window
SET_DISCONNECTCLIENTS                Defines server behaviors on a new connection                 Administration/Session
                                     0 – disconnect existing clients on new non-shared            Sharing
VALUE_OF_DISCONNECTCLIENTS
                                     connection
                                     1 – block new non-shared connection if someone is
                                     already connected
                                     Default value: 1

                                     DISCONNECTCLIENTS does not work if
                                     ALWAYSSHARED is set to 1

                                     Note: this option is described further in this section
                                     "Properties, Part 3: Server behavior on new connections"
SET_EXTRAPORTS                       Mapping of additional listening TCP ports to selected        Extra ports/Extra ports
                                     screen area
VALUE_OF_EXTRAPORTS
                                     Type: string in format
                                     "PORT:WIDTHxHEIGHT+LEFT+TOP"
                                     For example:
                                     "5901:1280x1024+0+0,5902:1280x1080+1280+0"
                                     Default value: ""
SET_GRABTRANSPARENTWINDOWS           0 – do not grab transparent windows                          Server/Update Handling
                                     1 – grab transparent windows
VALUE_OF_GRABTRANSPARENTWINDOWS
                                     Default value: 0
SET_HTTPPORT                         Web access port                                              Server/Web Access
                                     Type: DWORD
VALUE_OF_HTTPPORT
                                     Default value: 5800
SET_IPACCESSCONTROL                  Set rules for IP ranges                                      Access Control/Rules
                                     Type: string in format "IP1-IP2:{0|1|2}", where:
VALUE_OF_IPACCESSCONTROL
                                     0 – allow connections
                                     1 – deny connections
                                     2 – set query action
                                     Multiple rules should be separated with commas.

                                     For example:
                                     "0.0.0.0-255.255.255.255:2" – set the query action for all
                                     incoming connections.
                                     Default value: ""
SET_LOCALINPUTPRIORITY               0 – allow remote input on local activity                     Server/Input Handling
                                     1 – block remote input on local activity
VALUE_OF_LOCALINPUTPRIORITY
                                     Default value: 0
SET_LOCALINPUTPRIORITYTIMEOUT        Allows to change inactivity time (in seconds) belonged       Server/Input Handling
                                     with the option "Block remote input on local activity"
VALUE_OF_LOCALINPUTPRIORITYTIMEOUT
                                     Type: DWORD
                                     Default value: 3
SET_LOGLEVEL                         Log verbosity level                                          Administration/Logging
                                     Value range: 0-9 (0 – disable logging)
VALUE_OF_LOGLEVEL
                                     Default value: 0
SET_LOOPBACKONLY                     0 – allow                                                    Access Control/Loopback
                                     1 – allow only loopback connections                          Connections
VALUE_OF_LOOPBACKONLY
                                     Default value: 0
SET_NEVERSHARED                      Defines server behaviors on a new connection                 Administration/Session
                                     0 – allow shared connections                                 Sharing
VALUE_OF_NEVERSHARED
                                     1 – never treat new connection as shared
                                     Default value: 0

                                     If both ALWAYSHARED and NEVERSHARED are false
                                     then the type of connection is determined by the client's
                                     setting

                                     Note: this option is described further in this section
                                     "Properties, Part 3: Server behavior on new connections"
SET_POLLINGINTERVAL                  Screen polling cycle time (in milliseconds)                  Server/Update Handling
                                     Type: DWORD
VALUE_OF_POLLINGINTERVAL
                                     Default value: 1000
SET_QUERYACCEPTONTIMEOUT             The setting is effective only for IP-addresses with access   Access Control/Query
                                     rule action "Query local user":                              Settings
VALUE_OF_QUERYACCEPTONTIMEOUT
                                     0 – reject connection on timeout
                                     1 – accept connection on timeout
                                     Default value: 0
MSI Property Names                                Option Value (for VALUE_* Properties)                         Configuration Window
SET_QUERYTIMEOUT                                  Query timeout (in seconds)                                    Access Control/Query
                                                  Type: DWORD                                                   Settings
VALUE_OF_QUERYTIMEOUT
                                                  Default value: 30
SET_REMOVEWALLPAPER                               0 – show wallpaper                                            Server/Miscellaneous
                                                  1 – hide desktop wallpaper
VALUE_OF_REMOVEWALLPAPER
                                                  Default value: 1
SET_REPEATCONTROLAUTHENTICATION                   0 – ask for administrative password only once (for this       Administration/Control
                                                  control interface)                                            Interface
VALUE_OF_REPEATCONTROLAUTHENTICATION
                                                  1 – ask for administrative password for each server
                                                  operation
                                                  Default: 0
SET_RFBPORT                                       Main server port                                              Server/Incoming Viewer
                                                  Type: DWORD                                                   Connections
VALUE_OF_RFBPORT
                                                  Default value: 5900
SET_RUNCONTROLINTERFACE                           0 – do not show service icon in the notification area         Server/Miscellaneous
                                                  1 – show service icon in the notification area
VALUE_OF_RUNCONTROLINTERFACE
                                                  Default value: 1
SET_SAVELOGTOALLUSERSPATH                         0 – make log file private for each user                       Administration/Logging
                                                  1 – make log file available to all users
VALUE_OF_SAVELOGTOALLUSERSPATH
                                                  Default value: 0
SET_USEMIRRORDRIVER                               0 – do not use mirror driver                                  Server/Update Handling
                                                  1 – use mirror driver if available
VALUE_OF_USEMIRRORDRIVER
                                                  Default value: 1

Table 2: Server configuration options

Properties, Part 3: Server Behavior on New Connections
Server behavior and connection types are controlled by ALWAYSHARED, NEVERSHARED and
DISCONNECTCLIENTS options and their combinations. The meaningful combinations are shown
in the following table.
ALWAYSSHARED NEVERSHARED DISCONNECTCLIENTS                                                        Description
0                    0             0                              Block new non-shared connection if someone is already connected
0                    0             1                              Disconnect existing clients on new non-shared connection
0                    1             0                              Never treat connections as shared, disable new clients if there is one
                                                                  already
0                    1             1                              Never treat connections as shared, disconnect existing client on new
                                                                  connections
1                    0             0, 1 (not significant)         Always treat connection as shared, add new clients and keep old
                                                                  connections

Table 3: Server session sharing options
In the first two examples the resulting connection type is determined by the client setting (the check
box "Request shared session" in the "Connection options" window). In the remaining cases that
client setting is ignored.

Properties, Part 4: Password Protection (Service Mode)
The server settings in the table 2 work in any installation mode, but there are some server options
concerned with password settings which are effective only during silent installation.
To protect your TightVNC Server, you can set passwords for control interface and VNC client
authentication. Settings responsible for enabling authentication are
USECONTROLAUTHENTICATION and USEVNCAUTHENTICATION.
If USECONTROLAUTHENTICATION option is set to 1, the server will require the authentication
for most of control operations. The USEVNCAUTHENTICATION option is responsible for
requiring VNC authentication of incoming connections, which can have view-only or full-control
access type. You can set passwords for both of them.
To add a password, first you need to set "use corresponding authentication" property to 1 and then
add necessary passwords. All available password options are presented in the table 4. Do not forget
to use SET_/VALUE_OF_ pair.
MSI Property Names                     Option Value (for VALUE_* Properties)                          Configuration Window
SET_USECONTROLAUTHENTICATION           0 – do not protect control operations with an administrative   Administration/Control
                                       password                                                       Interface
VALUE_OF_USECONTROLAUTHENTICATION
                                       1 – protect control operations with an administrative
                                       password
                                       Default value: 0
SET_USEVNCAUTHENTICATION               0 – do not require VNC authentication on establishing          Server/Incoming Viewer
                                       connection                                                     Connections
VALUE_OF_USEVNCAUTHENTICATION
                                       1 – require VNC authentication on establishing connection
                                       Default value: 1
SET_CONTROLPASSWORD                    Password required to run the server control interface          [Administration/Control
                                       Type: string                                                   Interface]Password
VALUE_OF_CONTROLPASSWORD
                                       Default value: ""
                                       Requires USECONTROLAUTHENTICATION to be set to 1
SET_PASSWORD                           Password used as primary for incoming connections              [Server/Incoming Viewer
                                       Type: string                                                   Connections]Primary
VALUE_OF_PASSWORD
                                       Default value: ""                                              password
                                       Requires USEVNCAUTHENTICATION to be set to 1
SET_VIEWONLYPASSWORD                   Password used as "view-only" for incoming connections          [Server/Incoming Viewer
                                       Type: string                                                   Connection]View-only
VALUE_OF_VIEWONLYPASSWORD
                                       Default value: ""                                              password
                                       Requires USEVNCAUTHENTICATION to be set to 1

Table 4: Password protection options
The specific examples of setting passwords are considered in the next section.

Sample Command Line to Preset All Passwords
Here we explore specific examples of setting passwords with MSI properties.
To set a main password for VNC authentication, you should use following commands:
    •   SET_USEVNCAUTHENTICATION=1
        VALUE_OF_USEVNCAUTHENTICATION=1
        SET_PASSWORD=1
        VALUE_OF_PASSWORD=PASS
Also, you can set view-only password:
    •   SET_VIEWONLYPASSWORD=1
        VALUE_OF_VIEWONLYPASSWORD=VIEWPASS
And if you would like to configure the administrative password (protect the user interface of the
TightVNC Server), set the following values as well:
    •   SET_USECONTROLAUTHENTICATION=1
        VALUE_OF_USECONTROLAUTHENTICATION=1
        SET_CONTROLPASSWORD=1
        VALUE_OF_CONTROLPASSWORD=ADMNPASS
Finally, lets set all the passwords in one command line:
    •   msiexec.exe /i tightvnc-2.7.1-setup-64bit.msi /quiet /norestart
             SET_USEVNCAUTHENTICATION=1
             VALUE_OF_USEVNCAUTHENTICATION=1
             SET_PASSWORD=1
             VALUE_OF_PASSWORD=mainpass
             SET_VIEWONLYPASSWORD=1
             VALUE_OF_VIEWONLYPASSWORD=viewpass
             SET_USECONTROLAUTHENTICATION=1
VALUE_OF_USECONTROLAUTHENTICATION=1
SET_CONTROLPASSWORD=1
VALUE_OF_CONTROLPASSWORD=admpass