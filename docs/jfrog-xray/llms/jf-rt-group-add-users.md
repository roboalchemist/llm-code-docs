# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-group-add-users.md

# Add users to a group with jf rt group-add-users

Add users to an existing group in Artifactory.

## Prerequisites

Before running this command, ensure the following:

* A JFrog server is configured using [`jf config add`](/docs/jfrog-cli/authentication). You can also supply `--url` and authentication flags directly on each command.
* You have **admin privileges** on the Artifactory instance.
* The target group already exists. Use [`jf rt group-create`](/docs/jf-rt-group-create) to create one first.
* All users to be added already exist in Artifactory. Use [`jf rt users-create`](/docs/jf-rt-users-create) to create users.

## Synopsis

```
jf rt group-add-users <group-name> <users-list> [options]
```

**Aliases:** `rt gau`

## Arguments

| Argument       | Required | Description                                          |
| -------------- | -------- | ---------------------------------------------------- |
| `<group-name>` | Yes      | The name of the group                                |
| `<users-list>` | Yes      | Comma-separated list of usernames: `user1,user2,...` |

## Options

| Flag               | Default | Description                                                                                                      |
| ------------------ | ------- | ---------------------------------------------------------------------------------------------------------------- |
| `--access-token`   | —       | JFrog access token                                                                                               |
| `--password`       | —       | JFrog password (for authentication)                                                                              |
| `--server-id`      | —       | Server ID configured using the `jf config` command. Required if no default server is configured.                 |
| `--ssh-key-path`   | —       | SSH key file path                                                                                                |
| `--ssh-passphrase` | —       | SSH key passphrase                                                                                               |
| `--url`            | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`). Required if `--server-id` is not provided. |
| `--user`           | —       | JFrog username                                                                                                   |

## Examples

### Add a Single User

**To add one user to a group:**

1. Run:

```bash
jf rt group-add-users <group-name> <users-list>
```

**Where:**

* `<group-name>` — target group (see [Arguments](#arguments)).
* `<users-list>` — one or more comma-separated usernames.

**Full example:**

```bash
jf rt group-add-users developers alice
```

**Expected output:**

```
[Info] Done adding user(s) to group developers.
```

### Add Multiple Users

**To add multiple users to a group:**

1. Run:

```bash
jf rt group-add-users <group-name> <users-list>
```

**Full example:**

```bash
jf rt group-add-users developers alice,bob,charlie
```

**Expected output:**

```
[Info] Done adding user(s) to group developers.
```

### Display Command Help

**To view command help:**

1. Run:

```bash
jf rt group-add-users --help
```

## Important Notes

* Requires **admin privileges** on the Artifactory instance.
* Users must already exist in Artifactory before running this command. If one or more usernames do not exist, the command returns a `404 Not Found` error with no indication of which user was not found. Create missing users first with [`jf rt users-create`](/docs/jf-rt-users-create), then retry. To confirm all users were added successfully, check group membership in the Artifactory UI (**Administration → Identity and Access → Groups**).
* Adding users to a group does not change their existing group memberships — it only adds them to the specified group.
* Users inherit all permissions assigned to the group's permission targets immediately.

## Next Steps

After adding users to a group, [assign permissions to the group](/docs/permission-targets) to control what they can access.

<br />