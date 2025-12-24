# Source: https://support.anydesk.com/docs/command-line-interface-for-linux

The AnyDesk [Command-Line Interface] (CLI) for Linux enables administrators and advanced users to automate installation, configuration, client management, and remote connections. This article outlines available CLI commands, including installation procedures, client interaction, and session control. These commands can be entered directly in the terminal or integrated into scripts for automated deployments and configurations.

------------------------------------------------------------------------

## Installation 

<div>

AnyDesk for Linux can be installed or updated using the terminal with support for `.deb` and `.rpm` repositories. Repository setup instructions are available here:

-   [DEB](http://deb.anydesk.com/howto.html)

-   [RPM](http://rpm.anydesk.com/howto.html)

</div>

------------------------------------------------------------------------

## AnyDesk client 

### Client commands 

These commands can be used to interact with the AnyDesk client through the terminal or scripts.

The following commands can be used to interact with the AnyDesk client via terminal. These commands are often incorporated into scripts to streamline client configuration.

  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [**Command**]   [**Description**]
  **anydesk \<parameter\>**                                          Executes the specified parameter. See [Client command parameters](/v1/docs/command-line-interface-for-linux#client-command-parameters).
  **echo \<password\> \| anydesk \--set-password**                   Sets the specified password for [Unattended Access] (requires `root`).
  **echo \<license_key\> \| anydesk \--register-license**            Registers the specified license key.
  ------------------------------------------------------------------ ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Client command parameters 

The table below lists available parameters for managing and querying the AnyDesk client:

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| [**Parameter**] | [**Description**]                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--get-alias**                                                   | Displays the AnyDesk Alias.                                                                            |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--get-id**                                                      | Displays the AnyDesk ID.                                                                               |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--get-status**                                                  | Displays the client's online status.                                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--version**                                                     | Displays the installed AnyDesk version.                                                                |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--settings**                                                    | Opens the default (local) settings page.                                                               |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--admin-settings**                                              | Opens the global (admin-level) settings page (requires `root`).                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| **\--admin-settings:\<viable_parameter\>**                         | Opens the specified section of the global settings (requires `root`).                                  |
|                                                                    |                                                                                                        |
|                                                                    | Supported:`capture`, `security`, `connection`, `recording` |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

------------------------------------------------------------------------

## Start sessions via command-line 

You can initiate a session to a remote client directly from the command line.

### Connection commands 

These commands can include optional parameters for session customization.

**Connect to a client**

``` 
anydesk <ID/Alias> <additional parameters>
```

Starts a remote session to the specified AnyDesk ID or Alias.

-   `<ID_or_Alias>` - the AnyDesk address of the remote client.

-   `<additional_parameters>` - optional parameters to customize the session. For additional parameters, see [Optional session parameters](/v1/docs/command-line-interface-for-linux#optional-session-parameters).

**Connect using a password**

``` 
echo <password> | anydesk <ID/Alias> --with-password
```

Starts a session to the specified client and submits the given password for Unattended Access.

### Optional session parameters 

You can add the following parameters to session commands to modify how the session starts:

  ------------------------------------------------------------------ ----------------------------------------------------------------------
  [**Command**]   [**Description**]
  **\--file-transfer**                                               Starts a File Transfer session.  
  **\--fullscreen**                                                  Starts a session in fullscreen mode.
  ------------------------------------------------------------------ ----------------------------------------------------------------------

A tool that allows administrators and advanced users to automate installation, configuration, and client management tasks using command-line commands.

A feature that allows connections to a remote device without requiring manual approval on the other end, enabling access using just a password.