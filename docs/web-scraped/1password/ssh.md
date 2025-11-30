# Source: https://developer.1password.com/docs/ssh

On this page

# 1Password for SSH & Git

Introducing 1Password for SSH & Git, the single source of truth for all your SSH keys. With 1Password, you can:

- [Generate and import](/docs/ssh/manage-keys/) your SSH keys.
- [Autofill public keys](/docs/ssh/public-key-autofill/) in your browser for Git and other cloud platforms.
- Automatically configure [Git commit signing with SSH](/docs/ssh/git-commit-signing/) from the 1Password app.
- Use the [1Password SSH Agent](/docs/ssh/agent/) to authenticate all your Git and SSH workflows.

![A terminal with a git push command, overlaid with a 1Password authorization prompt to approve the request to use an SSH key.](/img/ssh/1password-ssh-git.png)![A terminal with a git push command, overlaid with a 1Password authorization prompt to approve the request to use an SSH key.](/img/ssh/1password-ssh-git.png)

The SSH agent works with your existing SSH clients and acts as their key provider. Use your keys in your SSH workflows, like when you work with Git to check code into source control, or when you log in to virtual machines.

1Password stores all your SSH keys behind secure end-to-end encryption, allowing you to access your keys when you need them without your SSH keys ever leaving 1Password.

## Quick start[â€‹](#quick-start "Direct link to Quick start") 

### [Get started](/docs/ssh/get-started/)[â€‹](#get-started "Direct link to get-started") 

If you\'re setting up SSH in 1Password for the first time, start here.

## Guides[â€‹](#guides "Direct link to Guides") 

### [Manage SSH keys](/docs/ssh/manage-keys/)[â€‹](#manage-ssh-keys "Direct link to manage-ssh-keys") 

Learn how to generate and import SSH keys, and how to copy or download your public key if you need to share it.

### [Autofill public keys](/docs/ssh/public-key-autofill/)[â€‹](#autofill-public-keys "Direct link to autofill-public-keys") 

Learn how to use 1Password in your browser to fill your public keys on your favourite Git or cloud platforms.

### [Sign Git commits with SSH](/docs/ssh/git-commit-signing/)[â€‹](#sign-git-commits-with-ssh "Direct link to sign-git-commits-with-ssh") 

Learn how to automatically configure Git commit signing with SSH through the 1Password app.

### [Advanced use cases](/docs/ssh/agent/advanced/)[â€‹](#advanced-use-cases "Direct link to advanced-use-cases") 

Learn how to configure the 1Password SSH agent for specific hosts and how to avoid rate limits with OpenSSH servers.

### [1Password agent config file](/docs/ssh/agent/config/)[â€‹](#1password-agent-config-file "Direct link to 1password-agent-config-file") 

Learn how to create and customize an SSH agent config file if you need to use SSH keys from shared or custom vaults or have more fine-grained control over the behavior of the SSH agent.

## Reference documentation[â€‹](#reference-documentation "Direct link to Reference documentation") 

### [SSH client compatibility](/docs/ssh/agent/compatibility/)[â€‹](#ssh-client-compatibility "Direct link to ssh-client-compatibility") 

Learn which SSH and Git clients have been tested with the 1Password SSH agent.

### [About 1Password SSH Agent security](/docs/ssh/agent/security/)[â€‹](#about-1password-ssh-agent-security "Direct link to about-1password-ssh-agent-security") 

Learn about the authorization model for the 1Password SSH agent, how it\'s different from the OpenSSH agent, and what\'s kept in local storage.