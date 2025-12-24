# Source: https://help.realvnc.com/hc/en-us/articles/360002253878-Configuring-RealVNC-Connect-Using-Parameters

# Configuring RealVNC Connect Using Parameters 

[Follow](/hc/en-us/articles/360002253878-Configuring-RealVNC-Connect-Using-Parameters/subscription.html "Opens a sign-in dialog")

![Avatar](https://help.realvnc.com/system/photos/360022267298/MicrosoftTeams-image__3_.png)

**[Tegan](/hc/en-us/profiles/366602748777-Tegan)**

Updated September 17, 2025 12:59

RealVNC Server, RealVNC Viewer and supporting programs are controlled by parameters, set to suitable default values for most users out-of-the-box.

For a list of all supported parameters, please refer to the below links:

[RealVNC Viewer Parameter Reference](/hc/en-us/articles/360002254618)

[RealVNC Server Parameter Reference](/hc/en-us/articles/360002251297)

You can configure a program by specifying new values for parameters either:

-   Before the program starts.
-   On the command line at start-up.
-   While the program is running, and connections are in progress.

For more information on RealVNC Server modes, see [Understanding RealVNC Server Modes](/hc/en-us/articles/360002253238).

[]

# Configuring programs before they start 

You can specify parameters yourself:

-   Under Windows, in the Registry.
-   Under Linux or macOS, in configuration files.

Note that if you have a subscription which includes Group Policy, it might be easier to use [policy](/hc/en-us/articles/360002250797) to deploy parameters remotely. This has the additional benefit of locking down programs so they cannot be changed by users.

[]

## Populating the Windows Registry with parameters 

Under Windows, if you have permission to edit the Windows Registry, you can specify parameters as values for particular Registry keys.

The following table lists the Registry keys to create or edit for each program, and the order in which parameters are applied. Parameters specified using policy override parameters specified at the command line, which in turn override parameters specified manually in the Registry.

+--------------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Program                                          | Order parameters are applied\                        | Notes                                                                                                          |
|                                                  | (lowest takes precedence)                            |                                                                                                                |
+--------------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                  |     HKLM\Software\RealVNC\vncserver                  | The **Options** dialog for a program updates a particular Registry key; see *Using the Options dialog* below.\ |
| **[*(Service Mode)*]** |     HKLM\Software\Policies\RealVNC\vncserver         | \                                                                                                              |
|                                                  |                                                      | Note it is not possible to specify parameters at the command line for RealVNC Server in Service Mode.          |
+--------------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                  |     HKCU\Software\RealVNC\vncserver                  |                                                                                                                |
| **[*(User Mode)*]**    |     <parameters at the command line>                 |                                                                                                                |
|                                                  |     HKCU\Software\Policies\RealVNC\vncserver         |                                                                                                                |
+--------------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| RealVNC Viewer                                   |     HKCU\Software\RealVNC\vncviewer                  |                                                                                                                |
|                                                  |     <parameters at the command line>                 |                                                                                                                |
|                                                  |     <per-connection settings from Address Book entry |                                                                                                                |
|                                                  |     /.vnc file>                                      |                                                                                                                |
|                                                  |     HKCU\Software\Policies\RealVNC\vncviewer         |                                                                                                                |
|                                                  |     HKLM\Software\Policies\RealVNC\vncviewer         |                                                                                                                |
+--------------------------------------------------+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

For example, to specify the `Log` parameter for RealVNC Server in Service Mode:

1.  Using Registry Editor, navigate to `HKEY_LOCAL_MACHINE\Software\RealVNC\vncserver`.
2.  Select **New \> String Value** from the shortcut menu, and create `Log`.
3.  Select **Modify** from the shortcut menu, and specify appropriate **Value data**, for example `*:file:100`.

**\*All parameters take string values, even boolean parameters.**

[]

## Populating configuration files with parameters 

Under Linux and Mac, each program has a number of configuration files, and additionally a number shared between all programs and user accounts on the computer.

The following tables list the files you can create or edit for each, and the order in which parameters are applied. Note that parameters specified using policy override parameters specified at the command line, which in turn override parameters specified manually in configuration files.

### Linux 

+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Program                                                       | Order parameters are applied\               | Notes                                                                                                                                                                                                                                                                                              |
|                                                               | (lowest takes precedence)                   |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                               |     /etc/vnc/config.d/common.custom         | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below.\                                                                                                                                                                                             |
| **[*(Service Mode)*]**              |     /etc/vnc/config.d/vncserver-x11         | \                                                                                                                                                                                                                                                                                                  |
|                                                               |     /root/.vnc/config.d/common              | Parameters specified in `/etc/vnc/*/vncserver-x11` are applied to RealVNC Server in User Mode too.                                                                                                                                                                                                 |
|                                                               |     /root/.vnc/config.d/vncserver-x11       |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/vncserver-x11         |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                               |     /etc/vnc/config.d/common.custom         | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below\                                                                                                                                                                                              |
| ***[(User Mode)]***                 |     /etc/vnc/config.d/vncserver-x11         | \                                                                                                                                                                                                                                                                                                  |
|                                                               |     ~/.vnc/config.d/common                  | Parameters specified in `/etc/vnc/*/vncserver-x11` are applied to RealVNC Server in Service Mode too.                                                                                                                                                                                              |
|                                                               |     ~/.vnc/config.d/vncserver-x11           |                                                                                                                                                                                                                                                                                                    |
|                                                               |     <parameters at the command line>        |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/vncserver-x11         |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                               |     /etc/vnc/config.d/common.custom         | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below                                                                                                                                                                                               |
| ***[(Virtual Mode - SystemXorg)]*** |     /etc/vnc/config.d/vncserver-x11-virtual |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/common                  |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/vncserver-x11-virtual   |                                                                                                                                                                                                                                                                                                    |
|                                                               |     <parameters at the command line>        |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/vncserver-x11-virtual |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                               |     /etc/vnc/config.d/common.custom         | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below                                                                                                                                                                                               |
| ***[(Virtual Mode - Xvnc)]***       |     /etc/vnc/config.d/Xvnc                  |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/common                  |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/Xvnc                    |                                                                                                                                                                                                                                                                                                    |
|                                                               |     <parameters at the command line>        |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/Xvnc                  |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server\                                               |     /etc/vnc/config.d/common.custom         | The daemon only accepts a subset of parameters; run `vncserver-virtuald -help` for a list. The daemon then launches the `vncserver-x11 -virtual` or `Xvnc` process for each connecting user, at which point its configuration files are applied to it (see RealVNC Server in Virtual Mode, above). |
| ***[(Virtual Mode daemon)]***       |     /etc/vnc/config.d/vncserver-virtuald    |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /root/.vnc/config.d/common              | Note the daemon does not have an **Options** dialog.                                                                                                                                                                                                                                               |
|                                                               |     /root/.vnc/config.d/vncserver-virtuald  |                                                                                                                                                                                                                                                                                                    |
|                                                               |     <parameters at the command line>        |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/vncserver-virtuald    |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Viewer                                                |     /etc/vnc/config.d/common.custom         | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below.                                                                                                                                                                                              |
|                                                               |     /etc/vnc/config.d/vncviewer             |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/common                  |                                                                                                                                                                                                                                                                                                    |
|                                                               |     ~/.vnc/config.d/vncviewer               |                                                                                                                                                                                                                                                                                                    |
|                                                               |     <parameters at the command line>        |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/common                |                                                                                                                                                                                                                                                                                                    |
|                                                               |     /etc/vnc/policy.d/vncviewer             |                                                                                                                                                                                                                                                                                                    |
+---------------------------------------------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]

### macOS 

+--------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Program                        | Order parameters are applied\                                    | Notes                                                                                                                           |
|                                | (lowest takes precedence)                                        |                                                                                                                                 |
+--------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server in Service Mode | [`/etc/vnc/config.d/common.custom`]\   | Parameters specified in [`/etc/vnc/*.d/vncserver`] are applied to RealVNC Server in User Mode too.    |
|                                | [`/etc/vnc/config.d/vncserver`]\       |                                                                                                                                 |
|                                | [`/var/root/.vnc/config.d/common`]\    | The **Options** dialog updates a particular configuration file; see *Using the Options dialog* below.                           |
|                                | [`/var/root/.vnc/config.d/vncserver`]\ |                                                                                                                                 |
|                                | [`/etc/vnc/policy.d/common`]\          | Note it is not possible to specify parameters at the command line.                                                              |
|                                | [`/etc/vnc/policy.d/vncserver`]        |                                                                                                                                 |
+--------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Server in User Mode    | [`/etc/vnc/config.d/common.custom`]\   | Parameters specified in [`/etc/vnc/*.d/vncserver`] are applied to RealVNC Server in Service Mode too. |
|                                | [`/etc/vnc/config.d/vncserver`]\       |                                                                                                                                 |
|                                | [`~/.vnc/config.d/common`]\            | The **Options** dialog updates the configuration file; see *Using the Options dialog* below                                     |
|                                | [`~/.vnc/config.d/vncserver`]\         |                                                                                                                                 |
|                                | \<parameters at the command line\>\                              |                                                                                                                                 |
|                                | [`/etc/vnc/policy.d/common`]\          |                                                                                                                                 |
|                                | [`/etc/vnc/policy.d/vncserver`]        |                                                                                                                                 |
+--------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| RealVNC Viewer                 | [`/etc/vnc/config.d/common.custom`]\   | The **Options** dialog updates the configuration file. See *Using the Options dialog* below.                                    |
|                                | [`/etc/vnc/config.d/vncviewer`]\       |                                                                                                                                 |
|                                | [`~/.vnc/config.d/common`]\            |                                                                                                                                 |
|                                | [`~/.vnc/config.d/vncviewer`]\         |                                                                                                                                 |
|                                | \<parameters at the command line\>\                              |                                                                                                                                 |
|                                | [`/etc/vnc/policy.d/common`]\          |                                                                                                                                 |
|                                | [`/etc/vnc/policy.d/vncviewer`]        |                                                                                                                                 |
+--------------------------------+------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

### Sharing configuration files between programs and user accounts 

When RealVNC Connect is installed, [`/etc/vnc/config.d/common`] is created. Note this file is reserved for use by RealVNC.

To specify parameters for all programs for all user accounts on the computer, create [`/etc/vnc/config.d/common.custom`].

To specify parameters for all programs for a particular user account, create [`~/.vnc/config.d/common`].

**[`*~`] is the [`root`] user account for certain programs; see the tables above.**

Other configuration files are program-specific. For example, to specify parameters for RealVNC Server in User Mode for all user accounts on a Linux computer, create [`/etc/vnc/config.d/vncserver-x11`].

To specify parameters for RealVNC Server in User Mode for a particular user account, create [`~/.vnc/config.d/vncserver-x11`]. Note this is the file updated by the Options dialog.

[]

#### Format of a configuration file 

Each parameter in a configuration file should be on a separate line; leading and trailing white space and comments are skipped, and environment variables expanded for parameters that accept them. For example:

    #This is a comment
    Desktop=Build machine
    Encryption=AlwaysOn
    Authentication=SystemAuth
    RsaPrivateKeyFile=$HOME/secure/vnc
    Permissions=admin:f,vncusers:d,guests:v

[]

# Configuring programs on the command line at start-up 

Under any platform, for most programs, you can pass parameters in at the command line when you start that app, each preceded by a dash ([`-`]). This enables you to configure a particular instance of the program, rather than every time it runs. For example:

[`vncserver-x11`]` `[`-Desktop="Debug`]` `[`machine"`]` `[`-Authentication=VncAuth`]

**\*You cannot configure RealVNC Server in Service Mode at the command line. For the RealVNC Server in Virtual Mode daemon, you *can* specify command line parameters in the [`/etc/init.d/<daemon>`] script or in [`/etc/systemd/system/<daemon>.service`], but it is recommended you use configuration files instead.**

Parameters specified at the command line override the same parameters specified in the Windows Registry (see *Populating the Windows Registry with parameters* for the exact order) or in configuration files (see *Populating configuration files with parameters*), except for those set by policy.

Note there are disadvantages to specifying parameters at the command line:

-   The **Options** dialog does not reflect your choices, which may confuse users.
-   Under Linux and Mac, parameters may be overridden if a running program is reloaded. See *Reloading parameters* below.

**\*RealVNC recommends specifying parameters *either* in the Windows Registry/configuration files *or* at the command line, but not both.**

For convenience, if you have many command line parameters to specify, you can populate a text file (one parameter per line; omit the dash) and reference it using the [`-vncconfigfile`] option, for example:

[`vncserver-x11`]` `[`-vncconfigfile`]` `[`/my/command/line/parameter/file`]

[]

# Reconfiguring running programs 

You can reconfigure:

-   Any running program using its Options dialog, if it has one. See *Using the Options dialog*.
-   RealVNC Server only by reloading parameters. See *Reloading parameters* below.

Note that most changes take effect immediately. Changes to a few parameters, however, require all connections to be terminated, and changes to a very small minority require the program to be restarted.

[]

## Using the Options dialog 

Most programs have an **Options** dialog, providing a user-friendly interface to the parameter mechanism. An **Options** dialog typically consists of several tabs or pages devoted to particular topics such as security or connectivity, and an **Expert** tab or page enabling users to edit parameters directly.

Note the following:

-   The **Options** dialog for RealVNC Server in Service Mode requires elevated privileges.
-   The **Options** dialog for RealVNC Server in Virtual Mode is only available to connected users.
-   The **Options** dialog can be hidden from users. See [Preventing Users Configuring RealVNC Connect](/hc/en-us/articles/360002250757)
-   Parameters set by policy are disabled in the **Options** dialog.

Changes made in an **Options** dialog automatically update a particular Registry key or configuration file; see the tables below. When the **OK** or **Apply** button is clicked, *all* Registry keys or configuration files for that program are then reloaded.

[]

### Windows 

  -------------------------------- ---------------------------------------------------------------
  Program                          The Options dialog updates\...
  RealVNC Server in Service Mode   [`HKLM\Software\RealVNC\vncserver`]
  RealVNC Server in User Mode      [`HKCU\Software\RealVNC\vncserver`]
  RealVNC Viewer                   [`HKCU\Software\RealVNC\vncviewer`]
  -------------------------------- ---------------------------------------------------------------

See *Populating the Windows Registry with parameters* for a complete list of Registry keys and the order in which they are applied.

[]

### Linux 

  --------------------------------- ---------------------------------------------------------------------
  Program                           The Options dialog updates\...

  RealVNC Server in Service Mode    [`/root/.vnc/config.d/vncserver-x11`]

  RealVNC Server in User Mode       [`~/.vnc/config.d/vncserver-x11`]

  RealVNC Server in Virtual Mode\   [`~/.vnc/config.d/vncserver-x11-virtual`]
  (SystemXorg)                      

  RealVNC Server in Virtual Mode\   [`~/.vnc/config.d/Xvnc`]
  (Xvnc)                            

  RealVNC Viewer                    [`~/.vnc/config.d/vncviewer`]
  --------------------------------- ---------------------------------------------------------------------

See *Populating configuration files with parameters* for a complete list of configuration files and order in which they are applied.

[]

### macOS 

  -------------------------------- -----------------------------------------------------------------
  Program                          The Options dialog updates\...
  RealVNC Server in Service Mode   [`/var/root/.vnc/config.d/vncserver`]
  RealVNC Server in User Mode      [`~/.vnc/config.d/vncserver`]
  RealVNC Viewer                   [`~/.vnc/config.d/vncviewer`]
  -------------------------------- -----------------------------------------------------------------

See *Populating configuration files with parameters* for a complete list of configuration files and order in which they are applied.

[]

## Reloading parameters 

You can reconfigure a running instance of RealVNC Server without downtime by editing Registry keys (Windows) or configuration files (other platforms) and then running the [`-reload`] command to re-apply *all* Registry keys or configuration files to that instance of RealVNC Server. For example, to reload RealVNC Server in User Mode under Linux:

[`vncserver-x11`]` `[`-reload`]

Note that:

-   The [`-reload`] command also re-applies license keys.
-   The [`-reload`] command does *not* re-apply:
    -   Parameters specified at the command line (see *Configuring programs on the command line at start-up*) under Linux and Mac. If these parameters have subsequently changed, the original command line values will be overridden.
    -   [X options](/hc/en-us/articles/360002253918), for RealVNC Server in Virtual Mode under Linux.
-   To reload all running instances of RealVNC Server for the current user, in any mode, run the command [`vnclicense`]` `[`-reload`]. To reload all running instances of RealVNC Server in any mode for all users, run the same command with elevated privileges.