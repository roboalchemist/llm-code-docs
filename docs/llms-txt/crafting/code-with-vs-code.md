# Source: https://docs.sandboxes.cloud/docs/code-with-vs-code.md

# Code with VS Code

In this page, we cover the common topics regarding using VS Code to work on code inside the Crafting Sandbox.

### Launch desktop VS Code and connect to sandbox

The Web IDE come with Crafting Sandbox is the open-source version of VS Code, which offers a near native experience like the desktop VS Code. But if you prefer, you can use the desktop version of VS Code you have already installed on your local machine to directly code in sandbox.

Simply run `cs vscode`, and select the workspace you want to connect to, it will launch the VS code and establish a remote coding environment via SSH.

```shell
$ cs vscode
```

Keep in mind that for this feature to work, the `code` command to launch VS Code needs to be in your `PATH`, which may not be default for **MacOS** users.

```shell
export PATH="$PATH:/Applications/Visual Studio Code.app/Contents/Resources/app/bin"
```

With native IDE on your local machine, all the convenient settings and customizations are already set, and the extensions are already installed. So you can get a more familiar coding environment to have best productivity.

The VS Code supports remote coding by splitting the IDE functionality into frontend and backend. With `cs vscode`, the IDE frontend (such as editor) runs on your local machine, while the IDE backend (such as language index, code analytics, etc.) runs on the sandbox. The SSH connection is used in between. The embedded terminal on the IDE is also on the remote sandbox, which is convenient for you to run `git` commands at where the code is. Some features in VS Code require remote settings, and some extensions require remote installation, please see [below](#setup-appropriate-extensions-on-sandbox) for more information.

#### How to set up WSL to enable launching VS Code from WSL and connect to sandbox?

Windows Subsystem of Linux (WSL) is a new platform to provide Ubuntu experience on Windows 10/11 platform. It is getting more and more popular with developers. Visual Studio Code supports WSL seamlessly by running the IDE in windows while using "remote development support" to connect to code in Linux subsystem.

Although the CLI `cs` works normally in WSL, it does not work with native Windows platform yet, therefore `cs vscode` does not work out-of-the-gate directly in WSL. However, with minimal configuration, it can be setup properly. The reason for the problem is that **since VS Code launched in WSL is running in native Windows, it will use the default ssh client in Windows and configurations there to connect to Sandbox, thus making the setup done by`cs` ineffective**. To work around it, we need to **let VS Code use ssh config in WSL itself**.

To do that, we need to do following steps

1. First, do `cs ssh` in WSL to connect to the target workspace for the proper ssh setup to be created in WSL.
2. Create a `ssh.bat` executable batch file and put it somewhere in the Windows File System, e.g. `C:\Users\<Your User Name>\.ssh` with one line content `C:\Windows\system32\wsl.exe ssh %*`
3. Install "Remote - SSH" (ms-vscode-remote.remote-ssh) plugin in the VS Code if not already done so.
4. Edit settings in VS Code, "Settings" -> "Extensions" -> "Remote - SSH" -> "Remote.SSH: Path", set it to your `ssh.bat` location, e.g. `C:\Users\<Your User Name>\.ssh\ssh.bat`. Or if you prefer to directly modify settings in JSON, add: `"remote.SSH.path": "C:\\Users\\<Your User Name>\\.ssh\\ssh.bat"` in the json config.

After that, the `cs vscode` in the WSL will connect properly to sandbox, remember to select `Linux` as the remote platform.

### Setup appropriate extensions on sandbox

To have best productivity, we usually need to config the extensions properly for our IDE. No matter using Web IDE or desktop VS Code, sometimes the extensions need to be installed on IDE backend, at where the code is. It means that sometimes even if you have installed the extension locally on your desktop VS Code, you may need to reinstall it on as remote extension on sandbox.

The VS Code extensions you installed on sandbox are located under your home directory in the workspace

* Desktop VS Code extensions: `~/.vscode-server/`
* Web IDE extensions: `~/.vscode-remote/`

To avoid the effort of reinstalling it manually every time for a new sandbox, you can include these directories in `Home Snapshot` for the team to share (see [here](https://docs.sandboxes.cloud/docs/workspaces-setup#home-snapshots)) or your `Personal Snapshot` just for yourself (see [here](https://docs.sandboxes.cloud/docs/personalize))