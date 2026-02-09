# Source: https://docs.sandboxes.cloud/docs/git-access.md

# Git Access

Access the git repos is a necessary step for developers to use Crafting as their dev environments. This page talks about how to set up the git repo access from Crafting sandbox.

## General Git Access via SSH Public Keys

Crafting setup a secure key pair for each user on its platform. It would use the private key in this key pair to authenticate and checkout code securely. You can add the public key in this key pair to your git repo to allow Crafting to access it on your behalf.

Each user can go to menu item `Connect -> Git` on web console (or [here](https://sandboxes.cloud/git) for Crafting SaaS) to see the public key.

![](https://files.readme.io/ac871d7-image.png)

Clicking one of the buttons on highlighted above to copy the public key and go to the git repo host site (e.g. GitHub) to paste it there.

This method is the most generic one, also supports private git repos, but **it requires each user to set up the access as they onboard to Crafting**

## GitHub App Integration

Crafting also supports a more convenient GitHub app integration that **doesn't require each user to have separate setup**. The admin with `Organization Owner` role on GitHub account can install Crafting GitHub app and select repos to grant access to Crafting. With GitHub app, all users from the Crafting sandboxes access the repos as the Crafting GitHub app, therefore no separate per-user setup is required.

To connect GitHub app, go to the menu item `Connect -> GitHub` on web console (or [here](https://sandboxes.cloud/github) for Crafting SaaS), read the instructions, and click `Install`.

![](https://files.readme.io/21d688b-image.png)

**Note that only the user with`Organization Owner` on the GitHub side can finish the flow.**

Keep in mind that Crafting SaaS supports GitHub app directly and can be self-served. For Crafting Self-hosted, it requires extra setup, please [contact us](https://crafting.dev/contact) for more information.

## Git Protocol Remap

When git submodules are used, the submodules can be referenced using SSH protocol (`git@...`) or HTTPS (`https://...`) and this may cause checkout failure in sandboxes if the protocol is different from the git access configured on the system. The resolution will be putting a file `/etc/gitconfig` in the base snapshot to map the protocol one to another.

If git access is configured using SSH protocol, the content of `/etc/gitconfig` should be (use `github.com` as an example, for other hosts, please modify accordingly, please also replace `ORG`):

```
[url "git@github.com:ORG/"]
  insteadOf = "https://github.com/ORG/"
```

If git access is configured with GitHub App Integration (using HTTPS protocol), the content of `/etc/gitconfig` should be

```
[url "https://github.com/ORG/"]
  insteadOf = "git@github.com:ORG/"
```