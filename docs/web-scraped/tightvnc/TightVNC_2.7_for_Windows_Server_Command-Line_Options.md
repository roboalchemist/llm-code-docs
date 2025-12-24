# Source: https://www.tightvnc.com/doc/win/TightVNC_2.7_for_Windows_Server_Command-Line_Options.pdf

TightVNC for Windows: Server Command-Line Options
                                       TightVNC Version 2.7
                                 Copyright © 2013 GlavSoft LLC.
TightVNC Server can be fully configured, started or stopped purely via the command line.
All settings found in the user interface can be changed via CLI options listed below. Besides that,
the command line interface makes it possible to share only a specific window or display, rather than
showing the whole desktop.

How To Execute Command via Command-Line Interface
Command-line options are accepted by the tvnserver.exe file. The default path to this file is
“C:\Program Files\TightVNC\tvnserver.exe”.
Program options specified on the command line follow these general rules:
   •   The server receives only one command at a time.
   •   A command name begins with a dash, e.g. -help.
   •   If any, command parameters are separated from a command by whitespace.
   •   Parameters that contain spaces must be quoted.
   •   Command names and parameters are case insensitive.

Command Description
Below the following command formatting is used:
   •   Options in curly braces “{}” and separated by a vertical line “ | “ represent a set of choices
       for a user. Choose one and run the command.
       For example, tvnserver.exe { -controlservice | -controlapp } can be run
       as:
           •    tvnserver.exe -controlservice
           •    tvnserver.exe -controlapp
   •   Optional arguments are specified in brackets “ [] “.
       For example, tvnserver.exe -install [ -silent ] can be run as:
            •   tvnserver.exe -install
            •   tvnserver.exe -install -silent

Command Usage
tvnserver.exe -help
tvnserver.exe [ -run ]
tvnserver.exe { -install | -reinstall | -remove | -start | -stop }
         [ -silent ]
tvnserver.exe { -controlservice | -controlapp }
tvnserver.exe { -controlservice | -controlapp }
         { -connect HOST | -disconnectall | -reload | -shutdown |
         -sharefull | -shareprimary |
         -sharedisplay DISPLAY_NUMBER |
         -sharerect WIDTHxHEIGHT+LEFT+TOP |
         -sharewindow CAPTION |
         -shareapp PROCESS_ID }
         [ -passfile FILE ]
tvnserver.exe { -configservice | -configapp }

Command-Line Options

tvnserver.exe -help
Displays TightVNC Server help message with available command-line options.

tvnserver.exe [ -run ]
Runs TightVNC Server in application mode.

tvnserver.exe { -install | -reinstall | -remove | -start | -stop } [ -silent ]
Manages launching TightVNC Server in service mode. If you don't want TightVNC Server to show
any message, add -silent option.
Command           Parameters Description

-install                        Registers TightVNC Server as a system service.

-reinstall                      Unregisters TightVNC Server as a system service and then
                                registers it again.

-remove                         Unregisters TightVNC Server as a system service.

-start                          Starts TightVNC Server as a system service.

-stop                           Stops TightVNC Server as a system service.

tvnserver.exe { -controlservice | -controlapp }
Opens configuration window of the running TightVNC Server. Changes in the server configuration
take effect immediately after approval.
Command           Parameters Description

-controlservice                 Opens TightVNC Server configuration window (service mode).

-controlapp                     Opens TightVNC Server configuration window (application
                                mode).

tvnserver.exe { -controlservice | -controlapp } COMMAND [ -passfile FILE ]
Executes a command on the running TightVNC Server. Since you may launch TightVNC Server as
an application and as a service simultaneously, you have to to clarify what server should execute the
command. Use -controlservice, if you send a command to TightVNC Server running in service
mode, and -controlapp option, if you send a command to TightVNC Server running as application.
Also notice that the server doesn't report the status of the operations it executes.
If the server is protected by an administrative password, and tvnserver.exe can not access the
Windows registry where this password is stored, you need to add -passfile option. As a parameter,
this option takes a path to a file with the required password. The password stored in this file should
be in ASCII (7-bit) characters.
Command             Parameters                         Description

-connect            HOST[:PORT]                        Connects to a viewer started in the "listening"
                                                       mode (so-called “reversed connection”).
                                                       If port is not specified, the server
                                                       automatically connects to host on 5500 port.
                                                       Note: there is no notification, if connection
                                                       can not be established.

-disconnectall                                         Disconnects all viewers from the server.

-reload                                                Updates settings of running TightVNC
                                                       Server from the Windows registry.

-shutdown                                              Quits the server.

-sharefull                                             Shares virtual desktop, which consists of all
                                                       physical displays of the machine where
                                                       TightVNC Server runs. Shared screen area
                                                       updates automatically, if the configuration of
                                                       virtual desktop has been modified.
                                                       Note: this is the default behavior of
                                                       TightVNC Server when it is started.

-shareprimary                                          Shares primary display (display 1).

-sharedisplay       DISPLAY_NUMBER                     Shares display with the specified number. If
                                                       the display with given number does not exist,
                                                       a screen with zero dimensions will be sent.
Command          Parameters                      Description

-sharerect       WIDTHxHEIGHT+LEFT+TOP Shares a rectangular region of the desktop
                                       with given parameters. If a region overhangs
                                       the virtual desktop, the shared area will be
                                       limited by the bounds of the virtual desktop.
                                                 The point (0, 0) is the top left corner of the
                                                 primary display. Therefore, if a region is
                                                 placed on the left or above the origin, you
                                                 need to use negative values.
                                                 For example, if you have the following
                                                 display configuration:

                                                                                ,
                                                 and you want to share the second display
                                                 with 1280x1024 resolution, use
                                                 “1280x1024+−1280+0” string as a
                                                 parameter.
                                                 Shared screen area updates automatically, if
                                                 the configuration of virtual desktop has been
                                                 modified.

-sharewindow     CAPTION                         Shares the first window with the caption that
                                                 matches or partially matches the specified
                                                 value. Other windows placed above shared
                                                 one also become visible to a viewer.
                                                 If the window with this caption does not exist
                                                 or has been minimized, a viewer will receive
                                                 a screen with zero dimensions. And
                                                 conversely, if the window with specified
                                                 caption appears on the desktop, it will be
                                                 shared automatically.

-shareapp        PROCESS_ID                      Shares all windows of the application with
                                                 the specified process ID (PID). The size of
                                                 the shared screen area is equal to the size of
                                                 virtual desktop. Nevertheless, all regions that
                                                 are not relevant to the application, including
                                                 the windows placed above shared ones and
                                                 the taskbar, will be darkened.
                                                 If the application with the given PID does not
                                                 exist or has been closed, a viewer will
                                                 receive a darkened virtual desktop screen. If
                                                 an application with the given PID appears in
                                                 the system again, it won't be shared.
-reload, -sharefull, -shareprimary, -sharedisplay, -sharewindow, -shareapp commands have no
analogues in graphical user interface. They can be executed only by using command-line interface.

tvnserver.exe { -configservice | -configapp }
Opens offline TightVNC Server configuration. It makes no difference whether the server is running,
since the changes are written directly to the Windows registry, bypassing TightVNC Server. The
server updates its configuration on start up or by the -reload command.
Command          Parameters Description

-configservice                Opens TightVNC Server offline configuration window (service
                              mode). This operation requires administrator privilege.

-configapp                    Opens TightVNC Server offline configuration window (application
                              mode).