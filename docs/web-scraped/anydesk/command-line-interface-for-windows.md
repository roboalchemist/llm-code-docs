# Source: https://support.anydesk.com/docs/command-line-interface-for-windows

The AnyDesk [Command-Line Interface] (CLI) allows administrators and advanced users to automate installation, configuration, client and [Session Management], and network settings. This article explains how to use AnyDesk commands in the Windows Command Prompt or within scripts such as batch files to streamline deployments and administration.

> ::: blockquote-title
> 🚨 [**IMPORTANT**]
> :::
>
> All commands must be run from the directory where `AnyDesk.exe` is located, or the full executable path must be specified.

The location of the AnyDesk executable depends on the client type:

-   **Standard clients downloaded from** [**anydesk.com**](https://anydesk.com/en/downloads/windows) are typically installed to:\
    `C:\Program Files (x86)\AnyDesk\AnyDesk.exe`

-   **Custom clients generated via** [**my.anydesk.com**](http://my.anydesk.com/v2) are typically installed to:\
    `C:\Program Files (x86)\AnyDesk-<prefix>\AnyDesk-<prefix>.exe`\
    The `<prefix>` is a unique identifier for your account. You can find it in [my.anydesk](http://my.anydesk.com/v2) \> **Builds** tab \> select desired build \> in the **General** section, check the **Prefix** field.

------------------------------------------------------------------------

## Installation 

This section provides instructions for installing or updating the AnyDesk Windows client using command-line. You can use these commands in scripts, system deployment processes, or during manual setup. Installation parameters allow you to define specific installation behaviors, such as shortcut creation, silent mode, and update preferences.

### Installation commands 

To install or update AnyDesk using the CLI, use the following command format:

``` 
anydesk.exe --install <location> <additional_parameters>
```

For example:

``` 
anydesk.exe --install  “C:\Program Files (x86)\AnyDesk” --start-with-win --create-desktop-icon
```

For MSI-based deployments:

``` 
anydesk.msi (optional: INSTALL="<location>")
```

### **Installation parameters** 

  -------------------------------------------------------------------- -------------------------------------------------------------------------------------------
  [**Parameter**]   [**Description**]
  **\--install \<location\>**                                          Installs AnyDesk in the specified location (e.g., `C:\Program Files (x86)\AnyDesk`).
  **\--start-with-win**                                                Configures AnyDesk to launch automatically with Windows.
  **\--create-shortcuts**                                              Adds a Start Menu shortcut.
  **\--create-desktop-icon**                                           Adds a desktop shortcut.
  **\--remove-first**                                                  Uninstalls the current version before installing a new one. Useful for manual updates.
  **\--silent**                                                        Runs the installation without user interface and error prompts.
  **\--update-manually**                                               Enables manual updates (default for custom client).
  **\--update-disabled**                                               Disables AnyDesk updates.
  **\--update-auto**                                                   Enables automatic updates (default for standard clients; not available for custom clients
  -------------------------------------------------------------------- -------------------------------------------------------------------------------------------

------------------------------------------------------------------------

## AnyDesk client 

The AnyDesk executable (`anydesk.exe`) offers a wide range of commands that allow administrators to control and configure the client. These commands can be used individually or within automation scripts to streamline administrative tasks across multiple systems.

### Client commands 

The examples below demonstrate how to use key client commands, such as registering a license key or setting an [Unattended Access] password. These commands are frequently used during initial setup or when automating client configuration.

  ------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [**Command**]   [**Description**]
  **anydesk.exe \<parameter\>**                                      For a full list of available options, see [Client command parameters](/v1/docs/command-line-interface-for-windows#client-command-parameters).
  **echo \<license_key\> \| anydesk.exe \--register-license**        Registers the specified license key. Requires administrator privileges.
  **echo \<my_password\> \| anydesk.exe \--set-password**            Sets the specified password for Unattended Access.
  ------------------------------------------------------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### **Client command parameters** 

This table lists individual command-line parameters available for the AnyDesk client. These parameters can be used with `anydesk.exe` to configure or control the client directly, and are commonly used in scripts or administrative setups.

+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [**Parameter**] | [**Description**]                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--uninstall**                                                   | Uninstalls AnyDesk with a graphical prompt.                                                                                                                                                                                                                                                                                         |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--remove**                                                      | Uninstalls AnyDesk silently without any prompt or UI.                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--start**                                                       | Starts the AnyDesk background service.                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--stop-service**                                                | Stops the AnyDesk background service.                                                                                                                                                                                                                                                                                               |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--restart-service**                                             | Restarts the AnyDesk background service.                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--remove-password**                                             | Deletes the Unattended Access password (admin rights required). **Note:** This cannot remove preset passwords from custom clients.                                                                                                                                                                                                  |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--remove-license**                                              | Removes the license key from the client. **Note:** This does not sign out users signed in via their account.                                                                                                                                                                                                                        |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--get-alias**                                                   | Displays the AnyDesk Alias. Typically used in scripts.                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--get-id**                                                      | Displays the AnyDesk ID. Typically used in scripts.                                                                                                                                                                                                                                                                                 |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--get-status**                                                  | Displays the client's online status.                                                                                                                                                                                                                                                                                                |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--version**                                                     | Displays the installed AnyDesk version.                                                                                                                                                                                                                                                                                             |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--settings**                                                    | Opens the default (local) settings page.                                                                                                                                                                                                                                                                                            |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--admin-settings**                                              | Opens the global (admin-level) settings page.                                                                                                                                                                                                                                                                                       |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--settings:\<viable_parameter\>**                               | Opens the specified settings section.                                                                                                                                                                                                                                                                                               |
|                                                                    |                                                                                                                                                                                                                                                                                                                                     |
|                                                                    | Supported parameters: `ui`, `security`, `alias`, `privacy`, `video`, `capture`, `audio`, `connection`, `file_transfer`, `recording`, `printer`, `wol`, `license`, `about` |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--admin-settings:\<viable_parameter\>**                         | Opens the specified section of the global settings.\                                                                                                                                                                                                                                                                                |
|                                                                    | Supported parameters: `capture`, `security`, `connection`, `recording`                                                                                                                                                                                                                  |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **\--disclaimer**                                                  | Displays the custom disclaimer message. Only works for custom clients with this option enabled.                                                                                                                                                                                                                                     |
+--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Example batch script to get AnyDesk ID:**

``` 
@echo off
for /f "delims=" %%i in ('"C:\Program Files (x86)\AnyDesk\AnyDesk.exe" --get-id') do set ID=%%i 
echo AnyDesk ID is: %ID%
pause
```

------------------------------------------------------------------------

## Permission profile commands (AnyDesk 7+) 

Permission profiles allow administrators to define custom access control settings for remote sessions. These profiles can be created, configured, and managed via the command line. This is supported in AnyDesk version 7 and later.

### Create a permission profile 

``` 
anydesk.exe --add-profile <name> +<permission> +<permission> ...
```

Creates a new permission profile named `<name>`. By default, all permissions are disabled. Use `+<permission>` to enable specific permissions, separated by spaces.

Supported permissions:

-   `audio`

-   `input`

-   `clipboard`

-   `clipboard_files`

-   `block_input`

-   `sas (CTRL+ALT+DEL action)`

-   `restart`

-   `file_manager`

-   `lock_desk`

-   `sysinfo`

-   `whiteboard`

-   `tcp_tunnel`

-   [`VPN`]

-   `user_pointer`

-   `privacy_feature`

-   `record_session`

### Create a profile with unattended access password 

``` 
echo <password> | anydesk.exe --add-profile <name> +<permission> +<permission> ...
```

Creates a permission profile named `<name>` with the specified unattended access password. Permissions must be defined the same way as above.

### Set a password for an existing profile 

``` 
echo <password> | anydesk.exe --set-password <profile>
```

Assigns or updates the unattended access password for the specified profile.

-   For custom profiles: use the permission profile name.

-   For default profiles, use:

    -   `_default` -- Default

    -   `_full_access` -- Full Access

    -   `_screen_sharing` -- Screen Sharing

    -   `_unattended_access` -- [Unattended Access](/v1/docs/permission-profiles)

### Remove a password from a profile 

``` 
anydesk.exe --remove-password <profile>
```

Removes the unattended access password from the specified profile.

> ::: blockquote-title
> 💡 **NOTE**
> :::
>
> This command cannot remove preset passwords from custom client configurations.

------------------------------------------------------------------------

## Start sessions via command-line 

You can initiate remote sessions directly from the command line using the `anydesk.exe` executable.

### Connection commands 

This can be useful for integrating AnyDesk with scripts, management tools, or automation processes.

**Connect to a client**

``` 
anydesk.exe <ID/Alias> <additional parameters>
```

Starts a remote session to the specified AnyDesk ID or Alias.

-   `<ID_or_Alias>` - the AnyDesk address of the remote client.

-   `<additional_parameters>` - optional parameters to customize the session. For additional parameters, see [Optional session parameters](/v1/docs/command-line-interface-for-windows#optional-session-parameters).

**Connect using a password**

``` 
echo <password> | anydesk.exe <ID/Alias> --with-password
```

Starts a session to the specified client and submits the given password for Unattended Access.

### Optional session parameters 

You can add the following parameters to session commands to modify how the session starts:

  ------------------------------------------------------------------ ----------------------------------------------------------------------
  [**Command**]   [**Description**]
  **\--file-transfer**                                               Starts a File Transfer session.
  **\--full-screen**                                                 Starts a session in fullscreen mode.
  **\--plain**                                                       Starts a session in a window without borders and menu options.
  ------------------------------------------------------------------ ----------------------------------------------------------------------

------------------------------------------------------------------------

## Proxy commands 

You can configure AnyDesk's HTTP proxy settings using command-line parameters. This is especially useful for environments with strict network policies or where proxy authentication is required.

> 🦉[ For more details on proxy settings, see ][[**this article**]](/docs/settings)[. ]

### Disable proxy usage 

``` 
anydesk.exe --proxy --set-host never
```

Sets the proxy mode to **No proxy** under **Settings \> Connection \> HTTP-Proxy**. AnyDesk will not attempt to connect via a proxy.

### Detect proxy automatically 

``` 
anydesk.exe --proxy --set-host detect
```

Sets the proxy mode to **Detect proxy**. AnyDesk will attempt to detect a proxy. If none is found, it will proceed without one.

### Set up a manual proxy 

``` 
anydesk.exe --proxy --set-host <proxy_type> <address> <port> [<force_proxy>] [--reconnect]
```

Configures a manual proxy under **Settings \> Connection \> HTTP-Proxy**.

-   `<proxy_type>`: `http`, `https`, or `socks`

-   `<address>`: Proxy server address (IP or URL)

-   `<port>`: Port used to connect to the proxy

-   `[+force-proxy]`: Try proxy, fallback to normal connection if it fails (optional)

-   `[-force-proxy]`: Force proxy; disconnect if the proxy is unavailable (optional)

-   `[--reconnect]`: Restarts the connection to apply the new settings (optional)

### Disable proxy authentication 

``` 
anydesk.exe --proxy --set-auth disable
```

Disables authentication. Sets **HTTP-Proxy** authentication to **No authentication required**.

### Use Windows credentials 

``` 
anydesk.exe --proxy --set-auth auto
```

Uses Windows account credentials for proxy authentication (NTLM). Sets **HTTP-Proxy** authentication to **NTLM**.

### Specify username and password 

``` 
echo <password> | anydesk.exe --proxy --set-auth simple <username>
```

Uses the configured username and password for authentication. Sets the proxy authentication method to **Set up username and password**.

A tool that allows administrators and advanced users to automate installation, configuration, and client management tasks using command-line commands.

The process of overseeing and controlling remote sessions, including starting, ending, and monitoring connections.

A feature that allows connections to a remote device without requiring manual approval on the other end, enabling access using just a password.

A built-in feature that creates a secure, private connection between local and remote devices. It enhances security by linking only the two devices directly, without allowing access to other devices on either network.