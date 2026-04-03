# Source: https://docs.jfrog.com/artifactory/docs/group-management.md

# Group Management

Groups are named collections of Artifactory users. Assigning permissions to a group — rather than to individual users — simplifies access control: add a user to a group and they immediately inherit all permissions that group holds.

The JFrog CLI provides three commands for managing groups:

| Command                                                | Alias     | What it does                              |
| ------------------------------------------------------ | --------- | ----------------------------------------- |
| [`jf rt group-create`](/docs/jf-rt-group-create)       | `rt gc`   | Create a new group                        |
| [`jf rt group-add-users`](/docs/jf-rt-group-add-users) | `rt gau`  | Add one or more existing users to a group |
| [`jf rt group-delete`](/docs/jf-rt-group-delete)       | `rt gdel` | Permanently delete a group                |

<Callout icon="📘" theme="info">
  Note

  The JFrog CLI does not provide a `group-list` or `group-get` command. To view existing groups, use the Artifactory UI (**Administration → Identity and Access → Groups**) or the Artifactory REST API (`GET /access/api/v2/groups`).
</Callout>

## Prerequisites

All group management commands require:

* JFrog CLI installed and a server configured — run `jf config show` to verify.
* **Admin privileges** on the Artifactory instance.

## Typical workflow

**To create a group, add members, and apply a permission target:**

1. Create the group:

```bash
jf rt group-create backend-team
```

2. Add existing users to the group:

```bash
jf rt group-add-users backend-team alice,bob
```

3. Generate a permission target template interactively, then create it on the server:

```bash
jf rt ptt ./backend-permissions.json
jf rt ptc ./backend-permissions.json
```

After completing these steps, every member of `backend-team` inherits the permissions defined in the target. See [Permission Targets](/docs/permission-targets) for details on the JSON schema.