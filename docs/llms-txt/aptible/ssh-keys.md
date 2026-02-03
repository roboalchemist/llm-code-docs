# Source: https://www.aptible.com/docs/core-concepts/security-compliance/authentication/ssh-keys.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSH Keys

> Learn about using SSH Keys to authenticate with Aptible

## Overview

Public Key Authentication is a secure method for authentication, and how Aptible authenticates deployments initiated by pushing to an [App](/core-concepts/apps/overview)'s [Git Remote](/how-to-guides/app-guides/deploy-from-git#git-remote). You must provide a public SSH key to set up Public Key Authentication.

<Warning> If SSO is enabled for your Aptible organization, attempts to use the git remote will return an `App not found or not accessible` error. Users must be added to the [allowlist](/core-concepts/security-compliance/authentication/sso#exempt-users-from-sso-requirement) to access your Organization's resources via Git. </Warning>

## Supported SSH Key Types

Aptible supports the following SSH key types:

* ssh-rsa

* ssh-ed25519

* ssh-dss

## Adding/Managing SSH Keys

<Frame><img src="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8049809963310cde5e0c0b0fb25bc15c" alt="" data-og-width="5120" width="5120" data-og-height="2560" height="2560" data-path="images/1-SSHKeys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=280&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=363296fedd3f6463825930b97fa99eb5 280w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=560&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=f6cd832c428dba8ce9baa6d3c0c9e4bc 560w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=840&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8f0f69f5d5527139aa571199a864b762 840w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=1100&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=c04585e2fccd9329b01f487354e4fbf7 1100w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=1650&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=8e30eff247ff5e0c06f17c604d1cfce0 1650w, https://mintcdn.com/aptible/MtH_goy23rOUOZd7/images/1-SSHKeys.png?w=2500&fit=max&auto=format&n=MtH_goy23rOUOZd7&q=85&s=0fa540f326fdd5c7c267a6c87a4bf33f 2500w" /></Frame>

If you [don't already have an SSH Public Key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys), generate a new SSH key using this command:

```
ssh-keygen -t ed25519 -C "your_email@example.com"
```

If you are using a legacy system that doesn't support the Ed25519 algorithm, use the following:

```
shell ssh-keygen -t rsa -b 4096 -C "you@example.com"
```

Once you have generated your SSH key, follow these steps:

1. In the Aptible dashboard, select the Settings option on the bottom left.

2. Select the SSH Keys option under Account Settings.

3. Reconfirm your credentials by entering your password on the page that appears.

4. Follow the instructions for copying your Public SSH Key in Step 1 listed on the page.

5. Paste your Public SSH Key in the text box located in Step 2 listed on the page.

# Featured Troubleshooting Guides

<Card title="git Push Permission Denied" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/permission-denied-git-push" />
