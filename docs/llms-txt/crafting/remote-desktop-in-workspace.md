# Source: https://docs.sandboxes.cloud/docs/remote-desktop-in-workspace.md

# Remote Desktop in Workspace

A workspace in a sandbox is a Linux environment which also supports running X-Window based desktop applications. Crafting provides the easy experience setting up the remote desktop in a workspace with a single command.

### Requirements

Crafting Remote Desktop support requires the workspace running a Ubuntu/Debian based system.

To access the desktop remotely, a Remote Desktop Client support Microsoft RDP protocol must be installed on your local desktop machine. Some well known clients are:

* Mac OS: Microsoft Remote Desktop Client
* Linux: Remmina

### Setup Guide

Run the following command **inside** a sandbox workspace:

```shell
cs addon install remote-desktop
```

It may interactively ask for setting up keyboard configuration during the process.

This setup can be saved by [base snapshot](workspaces-setup#persist-packages-and-libraries-setup-with-snapshots) so that it doesn't have to be done manually every time for a new sandbox.

### Access Remote Desktop

From your local machine, make sure you have installed the CLI (see the [Download Page](https://sandboxes.cloud/download)). Then run the following command:

```shell
cs remote-desktop  # or "cs rd" for short
```

After selecting a workspace, it will display a local-forwarded address that a RDP client can connect to, like:

```
rdp://127.0.0.1:3389
```

The CLI will attempt to launch well know RDP client (Microsoft Remote Desktop Client for Mac OS, and Remmina for Linux) with correct configuration, however if the attempt failed, or you want specific configuration, please read the following sections.

Note: regarding Microsoft Remote Desktop Client for Mac OS, the `dynamic resolution` (resizing the desktop when the client window is resized) can't be supported during command line launch. To enable `dynamic resolution`, a profile must be created from the UI and explicitly enable that feature.

#### Microsoft Remote Desktop Client for Mac OS

According to the URL printed by the CLI, from its UI, add a PC with "PC name" of "localhost" (or "localhost:PORT" if PORT is not 3389) and save. Double click to connect. The client will always prompt for a username/password (this can be suppressed by specifying an account when saving the configuration), just enter anything as the connection is already authenticated and secured by the "cs rdp" command. It may warn about certificate, dismiss it.

When editing the configuration, more parameters can be configured in the "Display" tab, like color-depth. If the performance is not ideal, try to lower color-depth.

#### Remmina

On most desktop Ubuntu, Remmina is pre-installed and registered to handle "rdp://" URL, so the command "cs rdp" will be able to launch Remmina automatically (or other software registered with "rdp://" URL schema). However, the default configuration of Remmina may not provide the best experience:

* Scale mode not enabled by default. Click the button "Toggle Scale Mode" on the left bar to enable it, so the desktop will auto resize when the client window is resized;
* The display quality may not be ideal. Click the button "Settings" on the left bar to adjust the quality and color-depth accordingly.

### Use of Remote Desktop

Enabling Remote Desktop turns a workspace as a desktop environment on the cloud. From there, developers can:

* Run full-featured desktop IDEs, even they don't support remote development capabilities as provided by VSCode or JetBrains Gateway;
* Run desktop browser and desktop apps local to your development environment, without concerning about network latency.