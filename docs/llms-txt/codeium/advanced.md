# Source: https://docs.windsurf.com/windsurf/advanced.md

# Advanced

All advanced configurations can be found in Windsurf Settings which can be accessed by the top right dropdown → Windsurf Settings or Command Palette (Ctrl/⌘+Shift+P) → Open Windsurf Settings Page.

# Enabling Cascade access to .gitignore files

To provide Cascade with access to files that match patterns in your project's .gitignore , go to your Windsurf Settings and go to "Cascade Gitignore Access". By default, it is turned off. To provide access, turn it on by clicking the toggle.

# SSH Support

The usual SSH support in VSCode is licensed by Microsoft, so we have implemented our own just for Windsurf. It does require you to have [OpenSSH](https://www.openssh.com/) installed, but otherwise has minimal dependencies, and should "just work" like you're used to. You can access SSH under `Remote-SSH` in the Command Palette, or via the `Open a Remote Window` button in the bottom left.
This extension has worked great for our internal development, but there are some known caveats and bugs:

* We currently only support SSHing into Linux-based remote hosts.

* The usual Microsoft "Remote - SSH" extension (and the [open-remote-ssh](https://github.com/jeanp413/open-remote-ssh) extension) will not work—please do not install them, as they conflict with our support.

* We don't have all the features of the Microsoft SSH extension right now. We mostly just support the important thing: connecting to a host. If you have feature requests, let us know!

* Connecting to a remote host via SSH then accessing a devcontainer on that remote host won't work like it does in VSCode. (We're working on it!) For now, if you want to do this, we recommend instead manually setting up an SSH daemon inside your devcontainer. Here is the set-up which we've found to work, but please be careful to make sure it's right for your use-case.

  1. Inside the devcontainer, run this once (running multiple times may mess up your `sshd_config`):

  ```
  sudo -s -- <<HERE
  sed -i '/SSO SSH Config START/Q' /etc/ssh/sshd_config
  echo "Port 2222" >> /etc/ssh/sshd_config
  ssh-keygen -A
  HERE
  ```

  2. Inside the devcontainer, run this in a terminal you keep alive (e.g. via tmux):

  ```
  sudo /usr/sbin/sshd -D
  ```

  3. Then just connect to your remote host via SSH in windsurf, but using the port 2222.

* SSH agent-forwarding is on by default, and will use Windsurf's latest connection to that host. If you're having trouble with it, try reloading the window to refresh the connection.

* On Windows, you'll see some `cmd.exe` windows when it asks for your password. This is expected—we'll get rid of them soon.

* If you have issues, please first make sure that you can ssh into your remote host using regular `ssh` in a terminal. If the problem persists, include the output from the `Output > Remote SSH (Windsurf)` tab in any bug reports!

# Dev Containers

Windsurf supports Development Containers on Mac, Windows, and Linux for both local and remote (via SSH) workflows.

Prerequisites:

* Local: Docker must be installed on your machine and accessible from the Windsurf terminal.
* Remote over SSH: Connect to a remote host using Windsurf Remote-SSH. Docker must be installed and accessible on the remote host (from the remote shell). Your project should include a `devcontainer.json` or equivalent config.

Available commands (in both local and remote windows):

1. `Dev Containers: Open Folder in Container`
   * Open a new workspace using a specified `devcontainer.json`.
2. `Dev Containers: Reopen in Container`
   * Reopen the current workspace in a new container defined by your `devcontainer.json`.
3. `Dev Containers: Attach to Running Container`
   * Attach to an existing Docker container and connect your current workspace to it. If the container does not follow the [Development Container Specificaton](https://containers.dev/implementors/spec/), Windsurf will attempt best-effort detection of the remote user and environment.
4. `Dev Containers: Reopen Folder Locally`
   * When connected to a development container, disconnect and reopen the workspace on the local filesystem.
5. `Dev Containers: Show Windsurf Dev Containers Log`
   * Open the Dev Containers log output for troubleshooting.

These commands are available from the Command Palette and will also appear when you click the `Open a Remote Window` button in the bottom left (including when you are connected to a remote host via SSH).

Related:

* `Remote Explorer: Focus on Dev Containers (Windsurf) View` — quickly open the Dev Containers view.

# WSL (Beta)

As of version 1.1.0, Windsurf has beta support for Windows Subsystem for Linux. You must already have WSL set up and configured on your Windows machine.

You can access WSL by clicking on the `Open a Remote Window` button in the bottom left, or under `Remote-WSL` in the Command Palette.

# Extension Marketplace

You can change the marketplace you use to download extensions from. To do this, go to `Windsurf Settings` and modify the Marketplace URL settings under the `General` section.

<Frame>
  <img src="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=6c7f06982ae1e5792aa12b1f1970b667" data-og-width="3420" width="3420" data-og-height="2130" height="2130" data-path="assets/windsurf/marketplace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=280&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=79dd7846d8b8a335db5332a58b4c9d69 280w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=560&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=cecf49e3ff27f3b5395a0c6edb8f5586 560w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=840&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=b00c825189ed8984c9d5ffb0b804abce 840w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=1100&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=afee6fa94e68a56b6adeb0b57c19d8a9 1100w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=1650&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=1bc7c733c51537a85bc6b7aec1cc5153 1650w, https://mintcdn.com/codeium/bVGscI7v3lPUsThV/assets/windsurf/marketplace.png?w=2500&fit=max&auto=format&n=bVGscI7v3lPUsThV&q=85&s=fb79355a10c6c82a57f6506f7843ac54 2500w" />
</Frame>

## Windsurf Plugins

<AccordionGroup>
  <Accordion title="Windsurf Pyright">
    Search "Windsurf Pyright" or paste in `@id:codeium.windsurfPyright` in the extensions search bar.
  </Accordion>
</AccordionGroup>
