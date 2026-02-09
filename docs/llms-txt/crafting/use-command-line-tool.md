# Source: https://docs.sandboxes.cloud/docs/use-command-line-tool.md

# Use command line tool

Crafting Sandbox CLI, `cs`, provides full-fledged access to the Crafting platform from your local machine, and it also pre-installed in all workspaces in any sandbox. Some advanced functionalities and configurations are only available via the CLI. In this page, we will go over some basics of CLI. For more details, please refer to our [Reference](https://docs.sandboxes.cloud/docs/command-line-tool).

### Download, install, and login

From our Web Console, the [Download page](https://sandboxes.cloud/download) provides a simple command with the link to download and install CLI to your system. It supports Linux and MacOS natively. For Windows users, please set up [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install) and use the Linux distribution in WSL. After downloading, please make sure it is in your `PATH` for convenient access.

The CLI has auto-update feature. It detects when a new version becomes available and updates itself automatically. Please use `cs version` to see its current version.

You need to login so that the CLI can operate on your behalf. You can use `cs login` to explicitly login to an account, or directly run a command which will prompt you to login when needed.

### SSH access to workspaces

Simply running `cs ssh` will get you the list of sandboxes in order to select where to login. You can also use the `--workspace` or `-W` option to specify which workspace to login to, in the format of `SANDBOX/WORKLOAD`. Just like normal SSH, you can also run a command remotely with it, or establish an SSH tunnel.

```shell
$ cs ssh
```

If the sandbox is suspended, the `cs ssh` command will first resume it, and then take you to the terminal of the workspace you SSHed into.

In the workspace, you will find the source code repository checked out under your home directory with your specified relative path. You can go edit the code or run any git commands to switch branch, push code, etc. In all the workspaces in Sandbox system, you will act as `owner` and have password-less `sudo` access, which enables you to install any packages via `apt install` or do other customizations for your development need.

### Commands to use inside workspaces

The CLI `cs` is made available inside each workspace, and you can use it via any terminal (from ssh, from Web IDE, or from your native IDE). You can use it to manage running processes, tail logs, and run automation such as building code, etc.

```shell
cs ps                 # List all processes(daemons)
cs up                 # Start all or specified daemons.
cs down               # Stop all or specified daemons.
cs restart            # Restart all or specified daemons.
cs log 	              # Tail workspace logs
cs build              # Run the build commands setup in repo manifest
```

### More commands

Other commonly used commands from your local machine includes:

```shell
cs vscode             # Launch local VS Code to directly edit code on sandbox
cs jetbrains          # Launch local Jetbrains IDE to directly edit code on sandbox
cs template           # Template related commands, create, edit, list, etc.
cs sandbox            # Sandbox related commands, create, list, etc.
cs portforward        # Start a port-forwarding session for hybrid development
cs scp                # Copy files between local and sandbox
cs rsync              # Run rsync between local and sandbox
cs mutagen            # Run two-way sync between local and sandbox
```

The CLI tool also provides management features for templates and sandboxes, as well as many other convenience or information features. Some are more for advanced usage cases, which will be covered later in this document. We will elaborate on them in corresponding topics later. Read the full [Reference](https://docs.sandboxes.cloud/docs/command-line-tool).