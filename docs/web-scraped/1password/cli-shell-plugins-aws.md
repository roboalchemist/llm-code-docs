# Source: https://developer.1password.com/docs/cli/shell-plugins/aws

On this page

# Use 1Password to securely authenticate the AWS CLI

The AWS shell plugin allows you to use 1Password to securely authenticate [the AWS CLI ](https://aws.amazon.com/cli/) with your fingerprint, Apple Watch, or system authentication, rather than storing your credentials in plaintext.

Follow the instructions to configure your default credentials and source the `plugins.sh` file, then you\'ll be prompted to authenticate the AWS CLI with biometrics.

If you use `cdk`, you can also set up the [AWS CDK Toolkit shell plugin](/docs/cli/shell-plugins/aws-cdk-toolkit/).

## Requirements[â€‹](#requirements "Direct link to Requirements") 

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  Install and sign in to 1Password for [Mac](https://1password.com/downloads/mac) or [Linux](https://1password.com/downloads/linux).
3.  Install [1Password CLI](https://app-updates.agilebits.com/product_history/CLI2) 2.9.0 or later.\
    [If you\'ve already installed 1Password CLI, learn how to [update your installation](/docs/cli/reference/update/).]
4.  [Integrate 1Password CLI with the 1Password app](/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration).
5.  Install [the AWS CLI. ](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)

After you install the AWS CLI, make sure you have an AWS config file at `~/.aws/config` on Mac or Linux, or `C:\Users\USERNAME\.aws\config` on Windows. If you don\'t have a config file:

1.  Use [`aws configure` ](https://docs.aws.amazon.com/cli/latest/reference/configure/) to create one.
2.  When prompted, skip entering your AWS access key pair to avoid writing your credentials on disk in the `.aws/credetials` file.

The following shells are supported:

- Bash
- Zsh
- fish

## Before you begin: Create and save an AWS access key[â€‹](#before-you-begin-create-and-save-an-aws-access-key "Direct link to Before you begin: Create and save an AWS access key") 

If you\'ve already created an AWS access key, [skip to step 1](#step-1-configure-your-default-credentials).

If you haven\'t created an access key yet, you can create one and use the [1Password browser extension](https://support.1password.com/getting-started-browser/) to quickly save it in 1Password:

1.  Open and unlock [1Password in your browser](https://support.1password.com/getting-started-browser/).
2.  [Follow the steps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html?icmpid=docs_iam_console#Using_CreateAccessKey) to create an access key for the AWS CLI.
3.  On the \"Retrieve access keys\" page, select **Show** to reveal the secret access key.
4.  Select **Save item** when 1Password asks if you want to save an item for the AWS access key.
5.  Choose the vault where you want to save the item, edit the item\'s name and details, then select **Save item**.

![The pop-up screen to save your AWS access key in 1Password.](/img/shell-plugins/aws-save.png)![The pop-up screen to save your AWS access key in 1Password.](/img/shell-plugins/aws-save-dark.png)

## Step 1: Configure your default credentials[â€‹](#step-1-configure-your-default-credentials "Direct link to Step 1: Configure your default credentials") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]If you use AWS in multiple environments

If you want to use the AWS shell plugin in multiple environments, like production and development, [learn how to set up your plugin for seamless context switching](/docs/cli/shell-plugins/environments/).

To get started with the AWS shell plugin:

1.  Sign in to the 1Password account you want to use with the AWS plugin:

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

You\'ll be prompted to import your AWS credentials into 1Password or select an existing 1Password item where your credentials are saved, then configure when the credentials should be used.

![A terminal window displaying the op plugin init command and options to import or select an item.](/img/shell-plugins/aws-1.png)![A terminal window displaying the op plugin init command and options to import or select an item.](/img/shell-plugins/aws-1.png)

### Step 1.1: Import or select an item

#### Import a new item

If you haven\'t saved your AWS credentials in 1Password yet, select **Import into 1Password**. Enter your credentials, choose a name for the new 1Password item, and select the vault where you want to save it.

If 1Password detects your credentials in your local development environment, you\'ll be prompted to import them automatically.

![A terminal window showing the fields available to import an item, including the token, item name, and vault.](/img/shell-plugins/aws-2.png)![A terminal window showing the fields available to import an item, including the token, item name, and vault.](/img/shell-plugins/aws-2.png)

#### Select an existing item

If you\'ve already saved your AWS credentials in 1Password, select **Search in 1Password**.

You\'ll see a list of related items and the vaults where they\'re saved. If you don\'t see your credentials, select **Expand search** to browse all items in your account.

![A terminal window showing the option to search for an existing item in your 1Password account.](/img/shell-plugins/aws-3.png)![A terminal window showing the option to search for an existing item in your 1Password account.](/img/shell-plugins/aws-3.png)

### Step 1.2: Set default credential scope

After you select or import your credentials, you\'ll be prompted to configure when to use the item to authenticate AWS.

![A terminal window showing the options for configuring when the credentials should be used.](/img/shell-plugins/aws-4.png)![A terminal window showing the options for configuring when the credentials should be used.](/img/shell-plugins/aws-4.png)

- **\"Prompt me for each new terminal session\"** will only configure the credentials for the duration of the current terminal session. Once you exit the terminal, the default will be removed.
- **\"Use automatically when in this directory or subdirectories\"** will make the credentials the default in the current directory and all of its subdirectories, as long as no other directory-specific defaults are set in them. A terminal-session default takes precedence over a directory-specific one.
- **\"Use as global default on my system\"** will set the credentials as the default in all terminal sessions and directories. A directory-specific default takes precedence over a global one.

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

The next time you enter a command with AWS, you\'ll be prompted to authenticate with biometrics or system authentication.

![A CLI being authenticated using 1Password CLI biometric unlock.](/img/shell-plugins/aws-5.png)![A CLI being authenticated using 1Password CLI biometric unlock.](/img/shell-plugins/aws-5.png)

## Step 4: Remove imported credentials from disk[â€‹](#step-4-remove-imported-credentials-from-disk "Direct link to Step 4: Remove imported credentials from disk") 

After you save your AWS credentials in 1Password, you can remove all local copies you currently have stored on disk.

Plaintext access keys are commonly stored in your AWS [shared credentials file ](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/creds-file.html) (default location: `~/.aws/credentials`). If you remove your credentials from this file, make sure to configure shell plugins for any other tools that use the file to authenticate to AWS, like [Terraform](/docs/cli/shell-plugins/terraform/).

## Optional: Assume multiple roles[â€‹](#optional-assume-multiple-roles "Direct link to Optional: Assume multiple roles") 

You can use the AWS shell plugin to assume multiple roles in the same way you\'d assume roles with the AWS CLI, by defining role profiles [in your AWS config file. ](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html#cli-role-prepare) For example:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)\~/.aws/config

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Then include the `--profile` flag to call an AWS command using a role. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If you want to always use the same profile, you can set the `AWS_PROFILE` environment variable. In that case, the `--profile` flag would only be needed to override the default set in the environment. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Optional: Set up multi-factor authentication[â€‹](#optional-set-up-multi-factor-authentication "Direct link to Optional: Set up multi-factor authentication") 

If you use [multi-factor authentication ](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa.html) with AWS, you can configure the AWS shell plugin to provide your one-time password.

You can do this in two ways:

- [Add the ARN for your multi-factor authentication device to a profile in your AWS config file. ](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html#cli-configure-role-mfa)
- Add the one-time password code and ARN to the item in 1Password where your AWS credentials are stored. If you choose this option, your multi-factor authentication information will be treated as your `default` profile and used globally with every other profile.

### Save your one-time password and ARN in 1Password

#### Step 1: Save your QR code

2.  Open and unlock the 1Password app.
3.  Select the item where your AWS credentials are saved, then select **Edit**.
4.  Select **Add More** \> **One-Time Password**.
5.  [Follow the steps to enable a virtual multi-factor authentication device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_enable_virtual.html) for your AWS account.
6.  Select **Show secret key** in the AWS wizard, then copy the string of characters into the One-Time Password field on your item.
7.  Select **Save**.

Your item will now show a one-time password that you can use to finish the AWS multi-factor authentication device set-up flow.

Your edited item must include the `one-time password` and `mfa serial` fields:

![The AWS item in 1Password with MFA credentials added.](/img/shell-plugins/aws-mfa.png)![The AWS item in 1Password with MFA credentials added.](/img/shell-plugins/aws-mfa-dark.png)

#### Step 2: Save the ARN for your multi-factor authentication device

1.  Find the [ARN for your multi-factor authentication device](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_checking-status.html) and copy it.
2.  Open and unlock the 1Password app.
3.  Select the item where you saved your AWS credentials then select **Edit**.
4.  Select **Add More** \> **Text**.
5.  Paste the ARN as the value of the field.
6.  Title the field `mfa serial`.
7.  Select **Save**.

1Password CLI will detect your multi-factor authentication credentials if they\'re saved in fields titled `one-time password` and `mfa serial`. If your one-time password isn\'t detected, make sure your fields are titled correctly.

1Password CLI will then set the `AWS_SECRET_ACCESS_KEY`, `AWS_ACCESS_KEY_ID` and `AWS_SESSION_TOKEN` provisional environment variables to specify the temporary multi-factor authentication session values.

## Next steps[â€‹](#next-steps "Direct link to Next steps") 

1Password Shell Plugins support [more than 60 third-party CLIs](/docs/cli/shell-plugins#get-started). To see a list of supported CLIs:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To choose another plugin to get started with:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To use shell plugins for seamless context switching, learn how to configure a plugin in [multiple environments](/docs/cli/shell-plugins/environments/) or with [multiple accounts.](/docs/cli/shell-plugins/multiple-accounts/)

## Get help[â€‹](#get-help "Direct link to Get help") 

### Inspect your configuration

To inspect your current AWS configuration:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

1Password CLI will return a list of the credentials you\'ve configured to use with AWS and their default scopes, as well as a list of aliases configured for AWS.

![A terminal window showing the results of the command op plugin inspect.](/img/shell-plugins/aws-6.png)![A terminal window showing the results of the command op plugin inspect.](/img/shell-plugins/aws-6.png)

### Clear your credentials

To reset the credentials used with AWS:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can clear one configuration at a time, in this order of precedence:

1.  Terminal session default
2.  Directory default, from the current directory to `$HOME`
3.  Global default

For example, if you\'re in the directory `$HOME/projects/awesomeProject` and you have a terminal session default, directory defaults for `$HOME` and `$HOME/projects/awesomeProject`, and a global default credential configured, you would need to run `op plugin clear aws` four times to clear all of your defaults.

To clear your global default credentials, terminal session default, and the defaults for your current directory at the same time, run `op plugin clear aws --all`.

## Reference[â€‹](#reference "Direct link to Reference") 

1Password authenticates with AWS by injecting environment variables with the credentials required by the plugin commands directly from your 1Password account.

If you saved your AWS credentials in 1Password manually rather than using `op plugin` to import a new item, make sure that your field names match the table below.

If the item doesn\'t contain a field with the required name, you\'ll be prompted to rename one of the existing fields.

  1Password field names       Environment variables
  --------------------------- -------------------------
  Access Key ID               `AWS_ACCESS_KEY_ID`
  Secret Access Key           `AWS_SECRET_ACCESS_KEY`
  Default region (optional)   `AWS_DEFAULT_REGION`

## Learn more

- [Use shell plugins to switch between multiple environments](/docs/cli/shell-plugins/environments/)
- [Use shell plugins with multiple accounts](/docs/cli/shell-plugins/multiple-accounts/)
- [Build your own shell plugins](/docs/cli/shell-plugins/contribute/)