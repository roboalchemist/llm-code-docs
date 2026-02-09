# Source: https://docs.sandboxes.cloud/docs/access-control.md

# Access control in sandbox

This page talks about how to manage access to the Crafting sandbox.

The Crafting platform provides a collaborative development experience by allowing members in the same organization to access each other's sandboxes. In certain instances, some sandboxes are not expected to be broadly accessible by all the members, as they may contain some sensitive information requiring restricted access. This is facilitated by **Sandbox Access Control**.

### Private mode sandbox

The access level of a sandbox can be changed at any time to be one of the following:

* `Default`: all members can access it for collaboration;
* `Private`: only the owner can access it.

The *accessibility* related to the access level includes any of the following operations, effectively locking down the access to the file system in the workspaces.

* SSH into any workspaces in the sandbox, including all SSH-based operations, like scp, rsync, mutagen, VS Code, etc;
* Launch Web IDE to access a workspace;
* Update the sandbox;
* Delete the sandbox.

When the access level is raised to `Private`, non-owners can't do any of the above operations, but are still able to:

* List the sandbox;
* Read the information about the sandbox including the full definition (endpoints, workspaces, dependencies, etc.).

The `ADMIN` users can't access the sandbox via SSH or Web IDE if they are not the owner, however, they are able to update or delete the sandbox regardless of the access level.

### Personal secrets are only mounted in private mode.

The [secrets](https://docs.sandboxes.cloud/docs/secrets) mounted in the sandbox will be changed automatically depending on the access level. The shared secrets are always mounted, and the private secrets are only mounted when the access level is `Private`. The change is applied automatically at the time when the access level is updated.

### How to set sandbox into private mode

To change the access level of a sandbox, the owner (or administrator) can do it on web console.

<Image align="center" className="border" border={true} src="https://files.readme.io/7a3c193-image.png" />

It can also be done via CLI command

```shell
$ cs sandbox access [private|shared]
```

### Use cases for private mode

The key use cases for private mode include:

* **Mount per-developer credentials for secure access to dev resources**: To make sure each developer only uses the credentials, e.g. access keys, assigned to them in their dev environment, these secrets will be stored as `Personal Secrets`. As described above, `Personal Secrets` are only mounted when the sandbox is in private mode to prevent other sandbox users from accessing them.
* **Keep source code private**: In some cases, not all developers are supposed to have equal access levels to all the source code. To prevent the developers from access the source code that they are not supposed to access, the sandbox with those source code checked out should be set in private mode.

If an organization has these use cases, they can choose to set `Private` as default for all new sandboxes launched. Please see [Organizational settings](https://docs.sandboxes.cloud/docs/org-settings) for details.

### Role-based access control (RBAC)

The enterprise version of Crafting platform supports full-featured Role-based Access Control (RBAC), which allows administrator to define fine-grained control on templates, sandboxes, resources, etc., as well as folders for each team to group their resources. Please contact us at [contact@crafting.dev](mailto:contact@crafting.dev) for detailed description and user guide for RBAC.