# Source: https://headscale.net/stable/usage/connect/windows/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/usage/connect/windows.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/usage/connect/windows.md "View source of this page")

# Connecting a Windows client[¶](#connecting-a-windows-client "Permanent link")

This documentation has the goal of showing how a user can use the official Windows [Tailscale](https://tailscale.com) client with headscale.

Instructions on your headscale instance

An endpoint with information on how to connect your Windows device is also available at `/windows` on your running instance.

## Installation[¶](#installation "Permanent link")

Download the [Official Windows Client](https://tailscale.com/download/windows) and install it.

## Configuring the headscale URL[¶](#configuring-the-headscale-url "Permanent link")

Open a Command Prompt or Powershell and use Tailscale\'s login command to connect with your headscale instance (e.g `https://headscale.example.com`):

    tailscale login --login-server <YOUR_HEADSCALE_URL>

Follow the instructions in the opened browser window to finish the configuration.

## Troubleshooting[¶](#troubleshooting "Permanent link")

### Unattended mode[¶](#unattended-mode "Permanent link")

By default, Tailscale\'s Windows client is only running when the user is logged in. If you want to keep Tailscale running all the time, please enable \"Unattended mode\":

- Click on the Tailscale tray icon and select `Preferences`
- Enable `Run unattended`
- Confirm the \"Unattended mode\" message

See also [Keep Tailscale running when I\'m not logged in to my computer](https://tailscale.com/kb/1088/run-unattended)

### Failing node registration[¶](#failing-node-registration "Permanent link")

If you are seeing repeated messages like:

    [GIN] 2022/02/10 - 16:39:34 | 200 |    1.105306ms |       127.0.0.1 | POST     "/machine/redacted"

in your headscale output, turn on `DEBUG` logging and look for:

    2022-02-11T00:59:29Z DBG Machine registration has expired. Sending a authurl to register machine=redacted

This typically means that the registry keys above was not set appropriately.

To reset and try again, it is important to do the following:

1.  Shut down the Tailscale service (or the client running in the tray)
2.  Delete Tailscale Application data folder, located at `C:\Users\<USERNAME>\AppData\Local\Tailscale` and try to connect again.
3.  Ensure the Windows node is deleted from headscale (to ensure fresh setup)
4.  Start Tailscale on the Windows machine and retry the login.