# Source: https://developer.1password.com/docs/ssh/get-started

On this page

# Get started with 1Password for SSH

You can use 1Password to generate an SSH key and autofill your public key to your favorite Git platform. Then, set up the 1Password SSH agent and configure your SSH or Git client so you can use the 1Password SSH agent to authenticate your Git and SSH workflow.

The following examples use GitHub to illustrate the SSH workflow from start to finish, but you can modify the steps to use with your favorite Git or cloud platform.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

- Mac
- Windows
- Linux

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  [Install and sign in to 1Password for Mac.](https://1password.com/downloads/mac)
3.  [Install the 1Password browser extension](https://1password.com/downloads/browser-extension) (optional).\
    [Required to autofill SSH keys in your browser.]

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  [Install and sign in to 1Password for Windows.](https://1password.com/downloads/windows)
3.  [Install the 1Password browser extension](https://1password.com/downloads/browser-extension) (optional).\
    [Required to autofill SSH keys in your browser.]

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  [Install and sign in to 1Password for Linux.](https://1password.com/downloads/linux)
3.  [Install the 1Password browser extension](https://1password.com/downloads/browser-extension) (optional).\
    [Required to autofill SSH keys in your browser.]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

The 1Password SSH agent doesn\'t work with [Flatpak ](https://flatpak.org/) or Snap Store installations of 1Password. To use the SSH agent, choose a different method to [install 1Password for Linux](https://support.1password.com/install-linux/).

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

For the best experience when using the 1Password SSH agent, you can configure [Touch ID](https://support.1password.com/touch-id-mac/), [Apple Watch](https://support.1password.com/apple-watch-mac/), [Windows Hello](https://support.1password.com/windows-hello/), or [system authentication](https://support.1password.com/system-authentication-linux/) to unlock 1Password and authenticate SSH key requests.

## Step 1: Generate an SSH key[â€‹](#step-1-generate-an-ssh-key "Direct link to Step 1: Generate an SSH key") 

1.  Open and unlock the 1Password app, then navigate to your **Personal**, **Private**, or **Employee** vault. The name of this vault varies depending on your account type.
2.  Select **New Item** \> **SSH Key**.
3.  Select **Add Private Key** \> **Generate New Key**.
4.  Select an SSH key type: [Ed25519 or RSA](/docs/ssh/manage-keys#supported-ssh-key-types), then select **Generate**.
5.  When you\'re done, select **Save**.

1Password will generate your SSH key, which includes the private key, public key, and its fingerprint.

![Generating a new SSH Key item with the Ed25519 key type selected.](/img/ssh/github-generate-ssh-key.png)![Generating a new SSH Key item with the Ed25519 key type selected.](/img/ssh/github-generate-ssh-key.png)

Learn more about [generating or importing SSH keys](/docs/ssh/manage-keys/) and [which SSH keys you can use with the 1Password SSH agent](/docs/ssh/agent#eligible-keys).

## Step 2: Upload your public key[â€‹](#step-2-upload-your-public-key "Direct link to Step 2: Upload your public key") 

After you generate your SSH key, you can add the public key to your GitHub account. Visit the [GitHub SSH key settings page](https://github.com/settings/ssh/new) upload your public key using the 1Password browser extension or desktop app.

- Browser extension
- Desktop apps

1.  Select the **Title** or **Key** field on the GitHub settings page. If 1Password doesn\'t show a list of suggested items, select the 1Password icon in the field.
2.  Select the GitHub SSH key you just created. 1Password will automatically fill the public key and title in the corresponding fields.
3.  Select **Add SSH Key** on the settings page to save the key in your GitHub account.

Your SSH key can now be used to authenticate with GitHub.

For examples using other Git or cloud platforms, see [Autofill public keys](/docs/ssh/public-key-autofill/).

![The GitHub SSH key settings page in a browser, with the Key field selected on the page and the GitHub SSH key item selected in the 1Password popup.](/img/ssh/add-public-key-github.png)![The GitHub SSH key settings page in a browser, with the Key field selected on the page and the GitHub SSH key item selected in the 1Password popup.](/img/ssh/add-public-key-github.png)

1.  Navigate to the GitHub SSH key you just created in 1Password and select it.
2.  Copy your public key from the item details, then paste it into the **Key** field on the GitHub settings page.\
    [You can also use [Quick Access](https://support.1password.com/quick-access/) to find and copy your public key.]
3.  Then select **Add SSH Key** on the settings page to save the key in your GitHub account.

Your SSH key can now be used to authenticate with GitHub.

For examples using other Git or cloud platforms, see [Autofill public keys](/docs/ssh/public-key-autofill/).

![A GitHub SSH Key item selected in the 1Password desktop app, with the public key field selected and ready to copy.](/img/ssh/copy-public-key-github.png)![A GitHub SSH Key item selected in the 1Password desktop app, with the public key field selected and ready to copy.](/img/ssh/copy-public-key-github.png)

## Step 3: Turn on the 1Password SSH agent[â€‹](#step-3-turn-on-the-1password-ssh-agent "Direct link to Step 3: Turn on the 1Password SSH agent") 

The 1Password desktop app includes an SSH agent that, when turned on, runs in the background to handle authentication for your SSH clients.

Follow these steps to turn on the SSH agent:

- Mac
- Windows
- Linux

1.  Open the 1Password app and select **1Password** \> **Settings** from the menu bar, then select **Developer**.
2.  Select **Set Up SSH Agent**, then choose whether you want to display SSH key names when you authorize connections.
3.  (Optional) [Adjust the authorization options](#adjust-your-authorization-options) for when and how often the SSH agent will ask you to approve SSH requests.

![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)

If you previously turned off the SSH agent and would like to turn it back on, select the checkbox to **Use the SSH agent**.

When you choose to display SSH key names when authorizing connections, it\'s easier for you to identify which key 1Password is requesting access to when authenticating a request from an SSH client. To display key names in authorization prompts, 1Password needs to [save the titles of your SSH Key items in local storage](/docs/ssh/agent/security#local-storage). To turn off this feature, deselect the checkbox to **Display key names when authorizing connections** in the Security section.

To make sure the SSH agent keeps running, even when the 1Password app is closed:

1.  Open the 1Password app and select **1Password** \> **Settings** from the menu bar, then select **General**.
2.  Select the checkboxes to **Keep 1Password in the menu bar** and **Start at login**.

![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiIC8+PC9zdmc+)]caution

The 1Password SSH agent only works with SSH clients that support [Microsoft OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_overview). For more information, see [SSH client compatibility](/docs/ssh/agent/compatibility/).

#### Check if the OpenSSH Authentication Agent service is installed and running[â€‹](#check-if-the-openssh-authentication-agent-service-is-installed-and-running "Direct link to Check if the OpenSSH Authentication Agent service is installed and running") 

Before you can turn on the SSH agent in 1Password, you\'ll need to check if the OpenSSH Authentication Agent service is installed:

1.  Go to **Services** \> **OpenSSH Authentication Agent** (press [Win] + [R] on your keyboard to open the Run window, type `services.msc` and press [Enter] or select **OK**).

2.  Look for the **OpenSSH Authentication Agent** in the list of services.

    If you don\'t see the OpenSSH Authentication Agent in the list, skip ahead to the steps to [turn on the SSH agent in 1Password](/docs/ssh/get-started#turn-on-the-ssh-agent-in-1password).

    If you do see the OpenSSH Authentication Agent in the list, continue with these steps to disable it from startup and make sure it\'s not running:

3.  Select **OpenSSH Authentication Agent** in the list of services and press [Enter].

4.  In the \"Startup type\" menu, select **Disabled**. If the service status shows the agent is running, select **Stop**.

5.  Select **Apply** \> **OK**.

The 1Password SSH agent can then take over and listen on the system-wide pipe at `\\.\pipe\openssh-ssh-agent`.

![Stop the Windows OpenSSH Authentication Agent service](/img/ssh/windows-openssh-agent.png)![Stop the Windows OpenSSH Authentication Agent service](/img/ssh/windows-openssh-agent.png)

#### Turn on the SSH agent in 1Password[â€‹](#turn-on-the-ssh-agent-in-1password "Direct link to Turn on the SSH agent in 1Password") 

Follow these steps to turn on the SSH agent in 1Password:

1.  Open the 1Password app, then select your account or collection at the top of the sidebar and select **Settings** \> **Developer**.
2.  Select **Set Up SSH Agent**, then choose whether or not you want to display SSH key names when you authorize connections.
3.  (Optional) [Adjust the authorization options](#adjust-your-authorization-options) for when and how often the SSH agent will ask you to approve SSH requests.

![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)

If you previously turned off the SSH agent and would like to turn it back on, select the checkbox to **Use the SSH agent**.

When you choose to display SSH key names when authorizing connections, it\'s easier for you to identify which key 1Password is requesting access to when authenticating a request from an SSH client. To display key names in authorization prompts, 1Password needs to [save the titles of your SSH Key items in local storage](/docs/ssh/agent/security#local-storage). To turn off this feature, deselect the checkbox to **Display key names when authorizing connections** in the Security section.

To make sure the SSH agent keeps running, even when the 1Password app is closed:

1.  Open 1Password, then select your account or collection at the top of the sidebar and select **Settings** \> **General**.
2.  Select the checkbox to **Keep 1Password in the notification area**.

![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)

1.  Open the 1Password app, then select your account or collection at the top of the sidebar and select **Settings** \> **Developer**.
2.  Select **Set Up SSH Agent**, then choose whether or not you want to display SSH key names when you authorize connections.
3.  (Optional) [Adjust the authorization options](#adjust-your-authorization-options) for when and how often the SSH agent will ask you to approve SSH requests.

![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)![The SSH agent developer settings in the 1Password desktop app, with both checkboxes selected and a badge at the top that shows the agent is running.](/img/ssh/turn-on-ssh-agent.png)

If you previously turned off the SSH agent and would like to turn it back on, select the checkbox to **Use the SSH agent**.

When you choose to display SSH key names when authorizing connections, it\'s easier for you to identify which key 1Password is requesting access to when authenticating a request from an SSH client. To display key names in authorization prompts, 1Password needs to [save the titles of your SSH Key items in local storage](/docs/ssh/agent/security#local-storage). To turn off this feature, deselect the checkbox to **Display key names when authorizing connections** in the Security section.

To make sure the SSH agent keeps running, even when the 1Password app is closed:

1.  Open 1Password, then select your account or collection at the top of the sidebar and select **Settings** \> **General**.
2.  Select the checkbox to **Keep 1Password in the system tray**.

![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)![The general settings page in the 1Password desktop app, with the checkboxes selected for the settings to keep the SSH agent running.](/img/ssh/keep-1password-running-mac.png)

## Step 4: Configure your SSH or Git client[â€‹](#step-4-configure-your-ssh-or-git-client "Direct link to Step 4: Configure your SSH or Git client") 

After you turn on the SSH agent in 1Password, you\'ll need to configure your SSH client to use the agent for authentication.

- Mac
- Windows
- Linux

Add the `IdentityAgent` snippet to your `~/.ssh/config` file:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If your `~/.ssh` folder or `config` file doesn\'t exist yet, create it first.

You can also set the `SSH_AUTH_SOCK` environment variable in the shell where your SSH command runs:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

For an agent path that\'s easier to type, you can optionally run the following command to create a symlink for `~/.1password/agent.sock`:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Now your SSH clients will use the 1Password SSH agent for all hosts.

If you prefer to migrate to the 1Password SSH agent gradually, you can configure your SSH clients to only use the SSH agent for one or more specific hosts, instead of all hosts. Learn more about [gradual migration](/docs/ssh/agent/advanced#gradual-migration).

Some SSH clients don\'t support every configuration option that the `~/.ssh/config` file has to offer. Learn more about [SSH client compatibility](/docs/ssh/agent/compatibility/).

By default, OpenSSH servers are configured to limit the amount of authentication attempts for an incoming SSH connection. Learn more about how to avoid the [SSH server six-key limit](/docs/ssh/agent/advanced#ssh-server-six-key-limit).

Additional configuration to use the SSH agent for authentication with your SSH clients isn\'t required.

To use the SSH agent with Git, configure the [`core.sshCommand`](https://git-scm.com/docs/git-config#Documentation/git-config.txt-coresshCommand) variable in your Git config to use Microsoft OpenSSH:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can also manually edit your [`gitconfig` file](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup#:~:text=On%20Windows%20systems):

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

For the best Git experience with 1Password, install the latest version of [Git for Windows](https://gitforwindows.org/) (version `2.33` or later).

If you\'re using Windows Subsytem for Linux (WSL), you can [use the 1Password SSH agent with WSL](/docs/ssh/integrations/wsl).

By default, OpenSSH servers are configured to limit the amount of authentication attempts for an incoming SSH connection. Learn more about how to avoid the [SSH server six-key limit](/docs/ssh/agent/advanced#ssh-server-six-key-limit).

Add the `IdentityAgent` snippet to your `~/.ssh/config` file:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If your `~/.ssh` folder or `config` file doesn\'t exist yet, create it first.

You can also set the `SSH_AUTH_SOCK` environment variable in the shell where your SSH command runs:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Now your SSH clients will use the 1Password SSH agent for all hosts.

If you prefer to migrate to the 1Password SSH agent gradually, you can configure your SSH clients to only use the SSH agent for one or more specific hosts, instead of all hosts. Learn more about [advanced use cases](/docs/ssh/agent/advanced#gradual-migration).

Some SSH clients don\'t support every configuration option that the `~/.ssh/config` file has to offer. Learn more about [SSH client compatibility](/docs/ssh/agent/compatibility/).

By default, OpenSSH servers are configured to limit the amount of authentication attempts for an incoming SSH connection. Learn more about how to avoid the [SSH server six-key limit](/docs/ssh/agent/advanced#ssh-server-six-key-limit).

## Step 5: Run a command[â€‹](#step-5-run-a-command "Direct link to Step 5: Run a command") 

Now you\'re ready to start using the 1Password SSH agent with GitHub.

From your project directory, run:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If you don\'t have a project available on GitHub where you can run `git pull` now, you can run this command instead to quickly test your GitHub SSH setup:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 6: Authorize the SSH request[â€‹](#step-6-authorize-the-ssh-request "Direct link to Step 6: Authorize the SSH request") 

1Password will ask you to allow your terminal or other SSH client to use your SSH key. You can approve this request using the authentication option indicated on the prompt (for example, Touch ID, Windows Hello, or your account password). If 1Password is locked, you\'ll also be prompted to unlock the app so the SSH agent can access your private keys.

![Authorization prompt showing a Touch ID icon.](/img/ssh/auth-prompt-touch-id.png)![Authorization prompt showing a Touch ID icon.](/img/ssh/auth-prompt-touch-id.png)

![Authorization prompt showing that the 1Password account password needs to be entered.](/img/ssh/auth-prompt-account-password.png)![Authorization prompt showing that the 1Password account password needs to be entered.](/img/ssh/auth-prompt-account-password.png)

![Authorization prompt showing a Windows Hello icon.](/img/ssh/auth-prompt-windows-hello.png)![Authorization prompt showing a Windows Hello icon.](/img/ssh/auth-prompt-windows-hello.png)

After approving the request, you can continue using the same SSH key for that application without being prompted again until 1Password locks or quits. You can also [configure your authorization settings](#adjust-your-authorization-options) to prompt more or less frequently.

[Learn more about the 1Password SSH agent authorization model.](/docs/ssh/agent/security#authorization-model)

### Adjust your authorization options[â€‹](#adjust-your-authorization-options "Direct link to Adjust your authorization options") 

There are several options you can choose from to determine how long the agent remembers your SSH key approval and what usage you\'re approving for each key. These options determine when the SSH agent will ask you to approve SSH requests.

#### In the 1Password settings[â€‹](#in-the-1password-settings "Direct link to In the 1Password settings") 

Open 1Password, then select your account or collection at the top of the sidebar and select **Settings** \> **Developer**. In the security settings for the SSH agent, you can choose the options that best suit your needs. You can change your settings at any time.

![SSH agent security settings showing the menu with the two options for when 1Password will ask you to approve SSH requests.](/img/ssh/security-settings-ask-approval.png)

1Password can ask you to approve an SSH request:

- **For each new application** (default): You\'ll be asked to authorize SSH requests from each new application to use a specific SSH key.

- **For each new application and terminal session**: Similar to the first option, you\'ll be asked to authorize SSH requests from each new application to use a specific SSH key. If the application is a terminal emulator or an IDE with a built-in terminal, you\'ll also be asked to authorize requests for each new terminal tab in that application.

![SSH agent security settings showing the menu with the options for how long 1Password remembers your key approval.](/img/ssh/security-settings-remember-approval.png)

You can choose how long 1Password will remember your key approval.

- **Until 1Password locks** (default): Every time 1Password locks, your key approvals are wiped from the agent\'s memory and you\'ll be asked to reauthorize any previously approved SSH clients to use your keys. For example, if you approve the terminal application to use your SSH key for GitHub, then 1Password locks, you\'ll need to reapprove any new requests from the terminal to use your GitHub SSH key when 1Password unlocks.

  [Learn how to change your 1Password lock settings.](https://support.1password.com/auto-lock/)

- **Until 1Password quits**: Every time 1Password quits, your key approvals are wiped from the agent\'s memory. Any agent sessions and background processes will also end. To use the SSH agent to authorize any new requests to use your SSH keys, you\'ll need to reopen 1Password.

- **For a set amount of time**: You can choose from 4, 12, or 24 hours. If you select one of these options, your key approvals will remain in the agent\'s memory for that duration, even when 1Password is locked. You won\'t need to reauthorize new requests from the same applications to use the same SSH keys you\'ve already approved, but you\'ll be prompted to unlock 1Password so the SSH agent can access your private key.

#### In the authorization prompt[â€‹](#in-the-authorization-prompt "Direct link to In the authorization prompt") 

Every authorization prompt for a client to use an SSH key includes the option to approve the use of that key for all applications. To turn on this option, select the checkbox to **Approve for all applications**.

![An authorization prompt from 1Password with the allow all option checked, showing that all applications can use the GitHub SSH key.](/img/ssh/auth-prompt-allow-all.png)

This option can be selected for individual SSH keys. It temporarily authorizes all applications running in the current OS user account on your device to use that SSH key for the duration of the agent session (depending on [the options you\'ve selected in the developer settings](#in-the-1password-settings) in 1Password). You can use this option alongside your other settings.

[Learn more about the authorization options for the SSH agent.](/docs/ssh/agent/security#authorization-options)

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Manage SSH keys](/docs/ssh/manage-keys#generate-an-ssh-key)
- [Autofill public keys](/docs/ssh/public-key-autofill/)
- [SSH client compatibility](/docs/ssh/agent/compatibility/)
- [Advanced use cases](/docs/ssh/agent/advanced/)
- [About 1Password SSH Agent security](/docs/ssh/agent/security/)
- [Use the 1Password SSH agent with WSL](/docs/ssh/integrations/wsl)