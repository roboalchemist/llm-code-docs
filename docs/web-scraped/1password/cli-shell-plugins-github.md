# Source: https://developer.1password.com/docs/cli/shell-plugins/github

On this page

# Use 1Password to securely authenticate the GitHub CLI

The GitHub shell plugin allows you to use 1Password to securely authenticate [the GitHub CLI ](https://cli.github.com/) with your fingerprint, Apple Watch, or system authentication, rather than storing your credentials in plaintext.

Follow the instructions to configure your default credentials and source the `plugins.sh` file, then you\'ll be prompted to authenticate the GitHub CLI with biometrics.

## Requirements[â€‹](#requirements "Direct link to Requirements") 

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  Install and sign in to 1Password for [Mac](https://1password.com/downloads/mac) or [Linux](https://1password.com/downloads/linux).
3.  Install [1Password CLI](https://app-updates.agilebits.com/product_history/CLI2) 2.9.0 or later.\
    [If you\'ve already installed 1Password CLI, learn how to [update your installation](/docs/cli/reference/update/).]
4.  [Integrate 1Password CLI with the 1Password app](/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration).
5.  Install [the GitHub CLI ](https://github.com/cli/cli#installation).

The following shells are supported:

- Bash
- Zsh
- fish

## Before you begin: Create and save a GitHub personal access token[â€‹](#before-you-begin-create-and-save-a-github-personal-access-token "Direct link to Before you begin: Create and save a GitHub personal access token") 

Before you can use 1Password to authenticate the GitHub CLI, you\'ll need to [create a GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). 1Password authenticates the GitHub CLI with your personal access token instead of a username and password.

If you\'ve already created a personal access token, [skip to step 1](#step-1-configure-your-default-credentials).

If you haven\'t created a personal access token yet, you can create one and use the [1Password browser extension](https://support.1password.com/getting-started-browser/) to quickly save it in 1Password:

1.  Open and unlock [1Password in your browser](https://support.1password.com/getting-started-browser/).
2.  [Follow the steps](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a GitHub personal access token.
3.  Select **Save item** when 1Password asks if you want to save an item for the GitHub personal access token.
4.  Choose the vault where you want to save the item, edit the item\'s name and details, then select **Save item**.

![The pop-up screen to save your GitHub personal access token in 1Password.](/img/shell-plugins/github-save.png)![The pop-up screen to save your GitHub personal access token in 1Password.](/img/shell-plugins/github-save-dark.png)

## Step 1: Configure your default credentials[â€‹](#step-1-configure-your-default-credentials "Direct link to Step 1: Configure your default credentials") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]If you use multiple GitHub accounts

If you want to use the GitHub shell plugin with more than one GitHub account, like your personal and work accounts, [learn how to set up your plugin to use multiple accounts](/docs/cli/shell-plugins/multiple-accounts/).

To get started with the GitHub shell plugin:

1.  Sign in to the 1Password account you want to use with the GitHub plugin:

    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::
2.  If you only want to configure the plugin in a specific directory, change to that directory
3.  Run the command to set up the plugin:

    :::::: container_wh0u
    ::::: wrapper_Ok5U
    ::: 
    :::

    ::: 
    [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]
    :::
    :::::
    ::::::

You\'ll be prompted to import your GitHub credentials into 1Password or select an existing 1Password item where your credentials are saved, then configure when the credentials should be used.

![A terminal window displaying the op plugin init command and options to import or select an item.](/img/shell-plugins/gh-1.png)![A terminal window displaying the op plugin init command and options to import or select an item.](/img/shell-plugins/gh-1.png)

### Step 1.1: Import or select an item

#### Import a new item

If you haven\'t saved your GitHub credentials in 1Password yet, select **Import into 1Password**. Enter your credentials, choose a name for the new 1Password item, and select the vault where you want to save it.

If 1Password detects your credentials in your local development environment, you\'ll be prompted to import them automatically.

![A terminal window showing the fields available to import an item, including the token, item name, and vault.](/img/shell-plugins/gh-2.png)![A terminal window showing the fields available to import an item, including the token, item name, and vault.](/img/shell-plugins/gh-2.png)

#### Select an existing item

If you\'ve already saved your GitHub credentials in 1Password, select **Search in 1Password**.

You\'ll see a list of related items and the vaults where they\'re saved. If you don\'t see your credentials, select **Expand search** to browse all items in your account.

![A terminal window showing the option to search for an existing item in your 1Password account.](/img/shell-plugins/gh-3.png)![A terminal window showing the option to search for an existing item in your 1Password account.](/img/shell-plugins/gh-3.png)

### Step 1.2: Set default credential scope

After you select or import your credentials, you\'ll be prompted to configure when to use the item to authenticate GitHub.

![A terminal window showing the options for configuring when the credentials should be used.](/img/shell-plugins/gh-4.png)![A terminal window showing the options for configuring when the credentials should be used.](/img/shell-plugins/gh-4.png)

- **\"Prompt me for each new terminal session\"** will only configure the credentials for the duration of the current terminal session. Once you exit the terminal, the default will be removed.
- **\"Use automatically when in this directory or subdirectories\"** will make the credentials the default in the current directory and all of its subdirectories, as long as no other directory-specific defaults are set in them. A terminal-session default takes precedence over a directory-specific one.
- **\"Use as global default on my system\"** will set the credentials as the default in all terminal sessions and directories. A directory-specific default takes precedence over a global one.

If you use a single GitHub account, select **Use as global default on my system**. This will set your personal access token as the default in all terminal sessions and directories.

If you use multiple GitHub accounts, [learn how to use directory-specific defaults for context switching](/docs/cli/shell-plugins/multiple-accounts/).

## Step 2: Source the plugins.sh file[â€‹](#step-2-source-the-pluginssh-file "Direct link to Step 2: Source the plugins.sh file") 

To make the plugin available, source your `plugins.sh` file. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

The file path for your `op` folder may vary depending on your [configuration directory](/docs/cli/config-directories/). `op plugin init` will output a source command with the correct file path.

If this is your first time installing a shell plugin, you\'ll also need to add the source command to your RC file or shell profile to persist the plugin beyond the current terminal session. For example:

- Bash
- Zsh
- fish

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 3: Use the CLI[â€‹](#step-3-use-the-cli "Direct link to Step 3: Use the CLI") 

The next time you enter a command with GitHub, you\'ll be prompted to authenticate with biometrics or system authentication.

![A CLI being authenticated using 1Password CLI biometric unlock.](/img/shell-plugins/gh-5.png)![A CLI being authenticated using 1Password CLI biometric unlock.](/img/shell-plugins/gh-5.png)

## Step 4: Remove imported credentials from disk[â€‹](#step-4-remove-imported-credentials-from-disk "Direct link to Step 4: Remove imported credentials from disk") 

After saving your GitHub credentials in 1Password, you can remove all local copies you previously had stored on disk.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Next steps[â€‹](#next-steps "Direct link to Next steps") 

1Password Shell Plugins support [more than 60 third-party CLIs](/docs/cli/shell-plugins#get-started). To see a list of supported CLIs:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To choose another plugin to get started with:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To use shell plugins for seamless context switching, learn how to configure a plugin in [multiple environments](/docs/cli/shell-plugins/environments/) or with [multiple accounts.](/docs/cli/shell-plugins/multiple-accounts/)

## Get help[â€‹](#get-help "Direct link to Get help") 

### Inspect your configuration

To inspect your current GitHub configuration:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

1Password CLI will return a list of the credentials you\'ve configured to use with GitHub and their default scopes, as well as a list of aliases configured for GitHub.

![A terminal window showing the results of the command op plugin inspect.](/img/shell-plugins/gh-6.png)![A terminal window showing the results of the command op plugin inspect.](/img/shell-plugins/gh-6.png)

### Clear your credentials

To reset the credentials used with GitHub:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can clear one configuration at a time, in this order of precedence:

1.  Terminal session default
2.  Directory default, from the current directory to `$HOME`
3.  Global default

For example, if you\'re in the directory `$HOME/projects/awesomeProject` and you have a terminal session default, directory defaults for `$HOME` and `$HOME/projects/awesomeProject`, and a global default credential configured, you would need to run `op plugin clear gh` four times to clear all of your defaults.

To clear your global default credentials, terminal session default, and the defaults for your current directory at the same time, run `op plugin clear gh --all`.

## Reference[â€‹](#reference "Direct link to Reference") 

1Password authenticates with GitHub by injecting environment variables with the credentials required by the plugin commands directly from your 1Password account.

If you saved your GitHub credentials in 1Password manually rather than using `op plugin` to import a new item, make sure that your field names match the table below.

If the item doesn\'t contain a field with the required name, you\'ll be prompted to rename one of the existing fields.

  1Password field names   Environment variables
  ----------------------- -----------------------
  Token                   `GH_TOKEN`
  Host (optional)         `GH_HOST`

## Learn more

- [Use shell plugins to switch between multiple environments](/docs/cli/shell-plugins/environments/)
- [Use shell plugins with multiple accounts](/docs/cli/shell-plugins/multiple-accounts/)
- [Build your own shell plugins](/docs/cli/shell-plugins/contribute/)