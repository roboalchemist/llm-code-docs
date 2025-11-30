# Source: https://developer.1password.com/docs/ssh/git-commit-signing

On this page

# Sign Git commits with SSH

Git version 2.34 and later supports signing commits and tags with SSH keys â€" no GPG key needed.

This means you can use the [1Password SSH integration](/docs/ssh/) to create new Git signing keys in seconds, and use them with your terminal apps and other [Git clients](/docs/ssh/agent/compatibility/) without the private key ever leaving 1Password. You can also automatically configure Git commit signing with SSH in the 1Password app.

When you sign your commits, they can be cryptographically verified using the SSH public keys associated with your [GitHub ](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification), [GitLab ](https://docs.gitlab.com/user/project/repository/signed_commits/ssh#configure-git-to-sign-commits-with-your-ssh-key), or [Bitbucket ](https://support.atlassian.com/bitbucket-cloud/docs/use-ssh-keys-to-sign-commits/) account. This ensures other people can verify that the changes were actually made by you. This is important because anyone with push rights to your repository can push new commits as any author, allowing them to impersonate others if commits aren\'t signed.

[Learn how easy it is to use 1Password to sign your Git commits.](https://blog.1password.com/git-commit-signing/)

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you get started, you\'ll need to:

1.  [Sign up for 1Password.](https://1password.com/pricing/password-manager)
2.  Install and sign in to 1Password for [Mac](https://1password.com/downloads/mac), [Windows](https://1password.com/downloads/windows), or [Linux](https://1password.com/downloads/linux).
3.  Update to Git 2.34.0 or later.
4.  [Import or generate SSH keys in 1Password.](/docs/ssh/manage-keys/)
5.  [Set up the 1Password SSH Agent.](/docs/ssh/get-started#step-3-turn-on-the-1password-ssh-agent)

## Step 1: Configure Git commit signing with SSH[â€‹](#step-1-configure-git-commit-signing-with-ssh "Direct link to Step 1: Configure Git commit signing with SSH") 

To automatically configure Git commit signing with SSH globally:

1.  Open the SSH key you want to use in your 1Password desktop app.
2.  Select \> **Configure Commit Signing**.
3.  In the next window, select **Edit Automatically**.\
    [Or select **Copy Snippet**, then paste the snippet into your `~/.gitconfig` file manually.]

![The Configure Git Commit Signing window showing options to edit your config file automatically or copy the configuration snippet manually.](/img/ssh/configure-git-commit-signing.png)![The Configure Git Commit Signing window showing options to edit your config file automatically or copy the configuration snippet manually.](/img/ssh/configure-git-commit-signing.png)

You can also [configure SSH signing in a single repository](#configure-commit-signing-in-a-single-repository).

1Password will make the following changes to your Git config file:

- Set `gpg.format` to `ssh`.
- Set `user.signingkey` to the public key you chose to sign commits with.
- Set `commit.gpgsign` to `true` so you don\'t need to include the `-S` flag with each commit. *(optional)*
- Set `gpg.ssh.program` to the SSH signer binary provided by 1Password, so you don\'t have to set `SSH_AUTH_SOCK` yourself. *(optional)*

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6IiAvPjwvc3ZnPg==)]tip

If you use WSL on a Windows machine, learn how to set up the [1Password WSL integration](/docs/ssh/integrations/wsl) to authenticate SSH and Git commands and [sign your Git commits within WSL](/docs/ssh/integrations/wsl#sign-git-commits-with-ssh).

## Step 2: Register your public key[â€‹](#step-2-register-your-public-key "Direct link to Step 2: Register your public key") 

Now that you\'ve configured SSH commit signing locally, you\'ll need to register your public key so that others can verify the authenticity of your commits.

- GitHub
- GitLab
- Bitbucket
- Locally

To allow GitHub to verify your commits, visit the [GitHub SSH key settings ](https://github.com/settings/ssh/new) to register your SSH key for commit signing. You can use the 1Password browser extension to automatically fill in the public key and key title.

Make sure you set the \"Key type\" to `Signing key` to allow your SSH key to be used for signing commits.

![The GitHub form to add a new SSH key, with signing key selected.](/img/ssh/github-add-ssh-key.png)![The GitHub form to add a new SSH key, with signing key selected.](/img/ssh/github-add-ssh-key.png)

To allow GitLab to verify your commits, visit the [GitLab SSH key settings ](https://gitlab.com/-/user_settings/ssh_keys) to register your SSH key for commit signing. You can use the 1Password browser extension to automatically fill in the public key and key title.

Make sure you set the \"Usage type\" to either `Authentication & Signing` or `Signing` to allow your SSH key to be used for signing commits.

![The GitLab form to add a new SSH key, with authentication and signing selected.](/img/ssh/gitlab-add-ssh-key.png)![The GitLab form to add a new SSH key, with authentication and signing selected.](/img/ssh/gitlab-add-ssh-key.png)

To allow Bitbucket to verify your commits, visit the [Bitbucket SSH key settings ](https://bitbucket.org/account/settings/ssh-keys/) to register your SSH key for commit signing. You can use the 1Password browser extension to automatically fill in the public key and key title.

![The Bitbucket form to add a new SSH key.](/img/ssh/bitbucket-add-ssh-key.png)![The Bitbucket form to add a new SSH key.](/img/ssh/bitbucket-add-ssh-key.png)

To verify SSH signatures locally, you\'ll need to create an [allowed signers file ](https://www.man7.org/linux/man-pages/man1/ssh-keygen.1.html#ALLOWED_SIGNERS) and configure Git to use it.

You can choose to configure this globally, for example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Or to tie it to a single repository, for example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

In the allowed signers file, add pairs of emails and public keys you\'d like to trust:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)allowed_signers

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You can share this file with others and could even consider checking it into Git, similar to a `CODEOWNERS` file.

## Step 3: Commit and push your code[â€‹](#step-3-commit-and-push-your-code "Direct link to Step 3: Commit and push your code") 

Now that you\'re all set up, you can commit some code:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You\'ll be prompted to authorize your SSH key the same way you unlock the 1Password app (for example, with Touch ID or Windows Hello).

![A Mac terminal showing a git commit command, overlaid with a 1Password prompt asking to authorize the use of a commit signing key with Touch ID.](/img/ssh/git-sign.png)

If you\'ve chosen to use the same key to sign as you do to push and pull, you can now also push without requiring additional authorization:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Step 4: Verify your commit signature[â€‹](#step-4-verify-your-commit-signature "Direct link to Step 4: Verify your commit signature") 

- GitHub
- GitLab
- Bitbucket
- Locally

If you look at your commit history on GitHub, you should see the `Verified` badge show up on your SSH-signed commits. If you select it, you can see the SSH key used to sign it.

![A GitHub commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/github-verified.png)![A GitHub commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/github-verified.png)

If you look at your commit history on GitLab, you should see the `Verified` badge show up on your SSH-signed commits. If you select it, you can see the SSH key used to sign it.

![A GitLab commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/gitlab-verified.png)![A GitLab commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/gitlab-verified.png)

If you look at your commit history on Bitbucket, you should see a verified checkmark show up on your SSH-signed commits. If you select it, you can see the SSH key used to sign it.

![A Bitbucket commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/bitbucket-verified.png)![A Bitbucket commit marked with the verified badge and showing the SSH public key used to sign.](/img/ssh/bitbucket-verified.png)

To verify commits locally, run the following command:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## Advanced configuration[â€‹](#advanced-configuration "Direct link to Advanced configuration") 

### Configure commit signing in a single repository[â€‹](#configure-commit-signing-in-a-single-repository "Direct link to Configure commit signing in a single repository") 

You can enable Git commit signing with SSH for specific repositories or directories instead of globally. To do this:

1.  Open the SSH key you want to use in your 1Password desktop app.
2.  Select \> **Configure Commit Signing**.
3.  In the next window, select **Copy Snippet**.
4.  Paste the snippet in the repository\'s `<git-repo>/.git/config` file instead of the global `~/.gitconfig` file.

### Configure multiple commit signing setups[â€‹](#configure-multiple-commit-signing-setups "Direct link to Configure multiple commit signing setups") 

If you want to configure multiple commit signing setups, you can use the `includeIf` directive in your `~/.gitconfig`.

For example, to use an SSH commit signing setup with 1Password as your default configuration and a non-1Password GPG setup for the `/work/acme` subdirectory:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)\~/.gitconfig

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)\~/work/acme/.gitconfig

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

In this example, every repository under `~/work/acme` will use the GPG configuration, while the SSH configuration will be used everywhere else.

### Configure commit signing in remote environments[â€‹](#configure-commit-signing-in-remote-environments "Direct link to Configure commit signing in remote environments") 

You can [set up SSH agent forwarding](/docs/ssh/agent/forwarding) to authenticate Git requests and sign commits in remote environments, like from a [cloud development environment](/docs/ssh/agent/forwarding#cde) or [remote workstation](/docs/ssh/agent/forwarding#remote-workstation).

## Get help[â€‹](#get-help "Direct link to Get help") 

### If Git says that SSH is an unsupported format 

If you see the following error message, then your Git version may be outdated:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Support for SSH commit signing was added to Git in version **2.34**. Run this command to check your Git version:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

It\'s common for operating systems and Git GUI clients to ship with an outdated version of Git out of the box. To install a more up-to-date version, see the [Git install docs. ](https://git-scm.com/downloads)

In the case of Git GUI clients, check the app preferences to see if they allow you to change the Git binary to a more up-to-date version.

### If your commits fail after you change your Git configuration 

If you see one of the following error messages, it\'s likely related to your `user.signingkey` value. Make sure that\'s set to a valid SSH public key.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If your `user.signingkey` is set correctly in your `~/.gitconfig` file, check the value at the repository level by running the following command from your repo\'s directory:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Example of a correct output:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If the signing key is not the SSH public key you\'ve configured in your `~/.gitconfig`, you may have a [local override](#local-git-overrides) in your repository.

### If you see errors related to the allowed signers file 

If you see the following error message, make sure you\'ve properly configured your [allowed signers file](#step-2-register-your-public-key):

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

This error should not block you from browsing your commit log - it just prevents you from locally verifying the commit authenticity.

### If your SSH-signed commit doesn\'t get verified by Git, GitHub, GitLab, and/or Bitbucket 

If you believe you\'ve signed your commits through SSH but they\'re not showing up as verified, there are a few things that could be happening:

#### Commit author email mismatch[â€‹](#commit-author-email-mismatch "Direct link to Commit author email mismatch") 

Commit signatures will only show up as verified if the registered public key matches the commit author email. Make sure it matches the email you\'ve registered on [GitHub ](https://github.com/settings/emails), [GitLab ](https://gitlab.com/-/user_settings/profile), or [Bitbucket ](https://id.atlassian.com/manage-profile/profile-and-visibility) in your allowed signers file.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]Case-sensitive email addresses

If your signed commits are verified locally but aren\'t verified on GitLab.com or Bitbucket, check for any case mismatches in your email address.

For example, if the email address in your GitLab or Bitbucket account is `wendy@appleseed.com` but your `~/.gitconfig` file uses `Wendy@appleseed.com`, your commits will show as unverified in those accounts.

If you have the correct email in your `~/.gitconfig`, check that the settings have correctly propagated down to the repository level as well. To validate this, run the following command from your repo\'s directory:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If this is not the email you\'ve configured in your `~/.gitconfig`, you may have a [local override](#local-git-overrides) in your repository.

#### Misconfigured public key[â€‹](#misconfigured-public-key "Direct link to Misconfigured public key") 

On GitHub, visit the [SSH key settings ](https://github.com/settings/keys) and check that the key you\'ve locally configured as `user.signingkey` shows up under \"Signing keys\".

On GitLab, visit the [SSH key settings ](https://gitlab.com/-/user_settings/ssh_keys) and check that the key you\'ve locally configured as `user.signingkey` shows up under \"Your SSH keys\".

On Bitbucket, visit the [SSH key settings ](https://bitbucket.org/account/settings/ssh-keys/) and check that the key you\'ve locally configured as `user.signingkey` shows up under \"SSH keys\".

For a local allowed signers file, make sure your public key is present and matches your email.

#### Unsupported Git client[â€‹](#unsupported-git-client "Direct link to Unsupported Git client") 

Most Git clients support SSH commit signing out of the box, but there are [a few exceptions](/docs/ssh/agent/compatibility/). Even though you may have configured Git correctly, a Git client that doesn\'t support SSH commit signing will leave your commit unsigned.

Make sure to also [check that you\'re on the latest version of your Git client](#get-help).

#### Local Git overrides[â€‹](#local-git-overrides "Direct link to Local Git overrides") 

Even though you may have configured your `~/.gitconfig` well, make sure to also check that the settings have correctly propagated down to the repository level.

To validate this, run the following command from your repo\'s directory:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Example of a correct output:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If this output does not match up with what you\'ve configured in your `~/.gitconfig`, unset the local values:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If you still end up with the wrong value somewhere, you can check where it originates from using the `--show-origin` flag:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]