# Source: https://docs.socket.dev/docs/socket-repo.md

# socket repository

Repositories related commands

This command holds a few sub-commands for repository management in your Socket.dev account.

```
$ socket repos --help

  Repository related commands

  Usage
    $ socket repository <command>

  Commands
    create            Create a repository in an organization
    del               Delete a repository in an organization
    list              List repositories in an organization
    update            Update a repository in an organization
    view              View repositories in an organization

  Options
    (none)

  Examples
    $ socket repository --help
```

To create a new repository (only on Socket.dev) use `socket repository create`. For example `socket repository create beardev --repo-name=honey` would create a repository named "honey" for the "beardev" organization.

To delete a repository (only on Socket.dev) use `socket repository del`. For example `socket repository del beardev honey` would remove the "honey" repository from the "beardev" organization.

To see all repositories for your organization, use `socket repository list`.

You can view details on a repository with `socket repository view` and you can update these details with `socket repository update`.