# Source: https://developer.1password.com/docs/ssh/agent

On this page

# 1Password SSH agent

The 1Password SSH agent uses the SSH keys you have saved in 1Password to seamlessly integrate with your Git and SSH workflows. It authenticates your Git and SSH clients without those clients ever being able to read your private key.

In fact, your private key never even leaves the 1Password app. The SSH agent works with the SSH keys stored in 1Password, but never without your consent. Only SSH clients you explicitly authorize will be able to use your SSH keys until 1Password locks.

Learn how to [turn on the 1Password SSH agent](/docs/ssh/get-started#step-3-turn-on-the-1password-ssh-agent) and [configure your SSH clients](/docs/ssh/get-started#step-4-configure-your-ssh-or-git-client).

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

## Configuration[â€‹](#configuration "Direct link to Configuration") 

By default, the 1Password SSH agent will make every [eligible key](/docs/ssh/agent#eligible-keys) in the built-in [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault of your 1Password accounts available to offer to SSH servers. This configuration is automatically set up when you [turn on the SSH agent](/docs/ssh/get-started#step-3-turn-on-the-1password-ssh-agent).

If you need to use the SSH agent with keys saved in shared or custom vaults, you can create and customize an [SSH agent config file](/docs/ssh/agent/config/) (`~/.config/1Password/ssh/agent.toml`) to override the default agent configuration.

If you have more than six SSH keys available in the agent, you can edit your SSH config file or use [SSH Bookmarks](/docs/ssh/bookmarks/) to match your keys to specific hosts. This will help you avoid authentication failures with OpenSSH servers that limit the number of connection attempts. Learn more about the [SSH server six-key limit](/docs/ssh/agent/advanced#ssh-server-six-key-limit).

## Eligible keys[â€‹](#eligible-keys "Direct link to Eligible keys") 

For the 1Password SSH agent to work with your SSH keys, your 1Password SSH key items must meet the following requirements. They must be:

- [Generated](/docs/ssh/manage-keys#generate-an-ssh-key) or [imported](/docs/ssh/manage-keys#import-an-ssh-key) using the `SSH Key` item type (which supports [`Ed25519` or `RSA`](/docs/ssh/manage-keys#supported-ssh-key-types) key types).
- Stored in the vaults [the SSH agent is configured to use](#configuration) in 1Password. By default, this is the [Personal](https://support.1password.com/1password-glossary#personal-vault), [Private](https://support.1password.com/1password-glossary#private-vault), or [Employee](https://support.1password.com/1password-glossary#employee-vault) vault of any 1Password account you\'re signed in to.
- Active items (not archived or deleted).

Any key meeting these requirements will automatically be available in the SSH agent for authentication. You will still be required to explicitly [authorize any request](/docs/ssh/agent/security#authorization-model) an SSH client makes to use your keys.

To see a list of all keys that the agent has available, [set the `SSH_AUTH_SOCK` environment variable](/docs/ssh/get-started#step-4-configure-your-ssh-or-git-client) (Mac and Linux only) and run:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]