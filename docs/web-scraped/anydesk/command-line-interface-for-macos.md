# Source: https://support.anydesk.com/docs/command-line-interface-for-macos

The following commands can be used on macOS to install and configure the AnyDesk client using the [Command-Line Interface]. These are useful for automated deployment, licensing, and configuring [Unattended Access]. Commands can be executed directly in the Terminal or integrated into scripts as part of device management workflows.

------------------------------------------------------------------------

## Installation 

As of **AnyDesk 6.3.0**, macOS custom clients can be deployed using a `.pkg` installer.  This method is suitable for scripted or automated deployments. The installer command must be executed with administrative privileges.

``` 
sudo installer -pkg AnyDesk.pkg -target /
```

Installs the AnyDesk application on the system.

> ::: blockquote-title
> 🚨 [**IMPORTANT**]
> :::
>
> This command installs the application, but does **not** automatically start the AnyDesk client or its background service. After installation, you must manually launch AnyDesk before using any of the commands listed below.

------------------------------------------------------------------------

## AnyDesk client 

These command-line instructions allow administrators to automate the configuration and management of the AnyDesk macOS client. This is particularly useful in enterprise environments or when deploying AnyDesk across multiple devices. All commands must be executed from the Terminal and some may require administrative privileges.

### Client commands 

Below are examples of commonly used commands to perform specific actions such as license registration and configuring unattended access. Each command should be executed as shown, and adapted with the correct license key or password values where applicable.

#### Run general commands 

``` 
/Applications/AnyDesk.app/Contents/MacOS/AnyDesk <parameter>
```

Executes a client-specific command. See [Client command parameters](/v1/docs/command-line-interface-for-macos#client-command-parameters) below for available options.

#### Register a license key 

``` 
echo <license_key> | /Applications/AnyDesk.app/Contents/MacOS/AnyDesk --register-license
```

Registers the specified license key with the AnyDesk client.

#### Set an unattended access password 

``` 
echo <password> | sudo /Applications/AnyDesk.app/Contents/MacOS/AnyDesk --set-password
```

Sets the unattended access password for the client. This action requires administrative privileges.

### Client command parameters 

The following parameters can be used with the AnyDesk macOS client to retrieve various types of information.

  ------------------------------------------------------------------ ----------------------------------------------------------------------
  [**Command**]   [**Description**]
  **\--get-alias**                                                   Returns the AnyDesk Alias.
  **\--get-id**                                                      Returns the AnyDesk ID.
  **\--get-status**                                                  Returns the current online status of the client.
  **\--version**                                                     Returns the installed AnyDesk version.
  ------------------------------------------------------------------ ----------------------------------------------------------------------

A tool that allows administrators and advanced users to automate installation, configuration, and client management tasks using command-line commands.

A feature that allows connections to a remote device without requiring manual approval on the other end, enabling access using just a password.