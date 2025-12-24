# Source: https://support.anydesk.com/docs/remote-restart

**Remote Restart** is an AnyDesk feature that lets you restart a remote device during a session. It also allows you to reconnect automatically after the restart or restart the device in Safe mode with networking.

Before proceeding, ensure that:

-   Remote restart is enabled in the remote client's [security settings](https://support.anydesk.com/knowledge/settings#security).

------------------------------------------------------------------------

## Restarting the remote device 

To restart a device remotely:

1.  Start a remote session with the device you want to restart.

2.  In the session toolbar, click **Actions**.

3.  Select **Remote Restart** from the dropdown menu.

4.  Select one of the following options:

    -   **Restart** -- to perform a standard reboot.

    -   **Restart in safe mode** -- to reboot into Safe Mode with networking.

Once the device restarts, the session will reconnect automatically if supported.

------------------------------------------------------------------------

## Limitations 

-   Some wireless adapters may not function in Safe Mode. It\'s recommended to use an **Ethernet connection** on the remote device.

-   **Automatic reconnection** works only for the client that initiated the remote restart.

-   When connecting to a macOS device with FileVault enabled from a non-macOS device, the **Remote Restart** option is unavailable.