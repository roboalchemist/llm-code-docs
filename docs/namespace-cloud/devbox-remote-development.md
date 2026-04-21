<!-- Source: https://namespace.so/docs/devbox/remote-development -->

# Remote Development

Connect to your devbox from your local environment using SSH, your preferred terminal, or a full IDE. All remote connections are tunneled securely through the Namespace API. No public IP addresses or open ports are required.

## Prerequisites

Before connecting, make sure you have completed [Getting Started](/docs/devbox#getting-started) — the Devbox CLI must be installed and authenticated. You'll also need a running devbox.

## Terminal Access

### Direct SSH

The fastest way to get a shell in your devbox:

```
$

```
devbox ssh main
```
```

This establishes an interactive SSH session directly to your devbox. Use the `-A` flag to forward your local SSH agent:

```
$

```
devbox ssh -A main
```
```

### Configure SSH

To use the standard `ssh` command (and enable any tool that relies on SSH config), run:

```
$

```
devbox configure-ssh main
```
```

This sets up your local `~/.ssh/config` with an `Include` directive pointing to `~/.namespace/ssh/`, writes the SSH key and a host config for your devbox. After running this, you can connect with:

```
$

```
ssh main.devbox.namespace
```
```

This also enables tools like `scp`, `rsync`, and any program that reads your SSH config.

### Port Forwarding

Forward ports from your devbox to localhost:

```
$

```
devbox port-forward main --ports 3000,8080
```
```

Remap ports with `local:remote` syntax:

```
$

```
devbox port-forward main --ports 4000:3000
```
```

If your devbox has configured port forwards in its blueprint, running `devbox port-forward main` without `--ports` will forward all of them automatically.

## IDEs

All IDE integrations connect over SSH. There are three ways to get started:

- **Dashboard:** Open VS Code or Cursor directly from the devbox dashboard.
- **Automatic:** `devbox open-ide` configures SSH and opens your IDE in one step. Available for VS Code, Cursor, Zed, and others.
- **Manual:** Run `devbox configure-ssh` first (see [Configure SSH](#configure-ssh)), then connect from your IDE using the SSH host. You may need to specify a working directory. Use `/workspaces/{repo-name}` if you created your devbox with `--checkout`.

### VS Code / Cursor

#### Open from the dashboard

1. In the Devbox dashboard, click **Open VSCode** and choose VS Code (desktop) or Cursor (desktop)

VS Code installs the Namespace Devbox extension automatically. On first use, the extension will open your browser to authenticate with Namespace. Once authenticated, it connects to your Devbox.

#### Open from the CLI

Open your devbox directly in VS Code or Cursor:

```
$

```
devbox open-ide main
```
```

```
$

```
devbox open-ide main --flavor cursor
```
```

This will:

1. Configure local SSH access to your devbox
2. Ensure the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) extension is installed (see the [VS Code Remote-SSH documentation](https://code.visualstudio.com/docs/remote/ssh) for more details)
3. Open a new window connected to your devbox

You can also use `--flavor vscode-insiders`, `--flavor codium`, `--flavor positron`, `--flavor windsurf`, or `--flavor zed`.

### JetBrains

JetBrains IDEs support remote development through [JetBrains Gateway](https://www.jetbrains.com/remote-development/gateway/) or the built-in remote development features in IDEs like IntelliJ IDEA, GoLand, PyCharm, and WebStorm. See the [JetBrains remote development documentation](https://www.jetbrains.com/help/idea/remote-development-starting-page.html) for more details.

1. Configure SSH access. This writes the SSH key and proxy config so Gateway can connect without manual setup:

```
$

```
devbox configure-ssh main
```
```

2. Open JetBrains Gateway and select **SSH Connection**
3. Create a new connection with the host `main.devbox.namespace` and username `devbox`
4. Select the IDE and project directory on the remote host

JetBrains Gateway installs the IDE backend on your devbox and streams the UI to your local machine.

### Zed

Open your devbox in Zed:

```
$

```
devbox open-ide main --flavor zed
```
```

This opens Zed with a remote SSH connection to your devbox. Zed connects using its [native SSH remote development](https://zed.dev/docs/remote-development) support.

## Next Steps

**[Sessions →](/docs/devbox/sessions)**
Persistent terminal sessions that survive disconnections and devbox restarts.

**[Managing Devboxes →](/docs/devbox/managing)**
Lifecycle operations, machine sizes, workspace defaults, and monitoring.

**[Custom Images →](/docs/devbox/images)**
Build custom base images with your tools and runtimes pre-installed.

Last updated April 1, 2026
