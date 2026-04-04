# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-group-create.md

# Create an Artifactory group with jf rt group-create

Create a new users group in Artifactory.

## Prerequisites

* JFrog CLI installed and configured: run `jf config show` to verify an active server is set.
* **Admin privileges** on the Artifactory instance are required.
* Confirm your server is reachable before running commands.

## Synopsis

```
jf rt group-create <group-name> [options]
```

**Aliases:** `rt gc`

## Arguments

| Argument       | Required | Description               |
| -------------- | -------- | ------------------------- |
| `<group-name>` | Yes      | The name of the new group |

## Options

| Flag               | Default | Description                                                                |
| ------------------ | ------- | -------------------------------------------------------------------------- |
| `--access-token`   | —       | JFrog access token                                                         |
| `--password`       | —       | JFrog password (for authentication)                                        |
| `--replace`        | `false` | Set to true to replace an existing group (or its users) with the same name |
| `--server-id`      | —       | Server ID configured using the `jf config` command                         |
| `--ssh-key-path`   | —       | SSH key file path                                                          |
| `--ssh-passphrase` | —       | SSH key passphrase                                                         |
| `--url`            | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)       |
| `--user`           | —       | JFrog username                                                             |

## Examples

### Create a New Group

**To create a new group:**

1. Run:

```bash
jf rt group-create <group-name>
```

**Where:**

* `<group-name>` — name for the new group (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt group-create my-team
```

> On success, the command exits with code 0 and produces no output. See [Verifying the group was created](#verifying-the-group-was-created) below.

### Create a Group with Replace

**To create or replace a group:**

1. Run:

```bash
jf rt group-create <group-name> --replace
```

**Full example:**

```bash
jf rt group-create developers --replace
```

## When to Use

Use `jf rt group-create` to create a logical grouping of users for access control. Groups simplify permission management — instead of assigning permissions to individual users, assign them to groups and add users to those groups.

**Typical access control workflow:**

**To set up a group and grant repository permissions:**

1. Create the group:

```bash
jf rt group-create backend-team
```

<Callout icon="📘" theme="info">
  Note

  On success, the command exits with code 0 and produces no output. This is expected behavior.
</Callout>

2. Add users to the group (see [jf rt group-add-users](/docs/jf-rt-group-add-users) for full options):

```bash
jf rt group-add-users backend-team alice,bob,charlie
```

3. Generate a permission target template interactively, then create it (`jf rt ptt` requires an interactive terminal; in CI, write the JSON manually instead):

```bash
jf rt ptt ./backend-permissions.json
jf rt ptc ./backend-permissions.json
```

`jf rt ptt` walks you through prompts and writes the template file. If you prefer to write the JSON manually, the minimal schema looks like this:

```json
{
  "name": "backend-permissions",
  "repo": {
    "repositories": "libs-release-local",
    "actions": {
      "groups": {
        "backend-team": ["read", "write", "annotate", "delete", "manage"]
      }
    }
  }
}
```

<Callout icon="❗️" theme="error">
  Important

  `repositories` must be a **string** (a single repository key), not a JSON array. Using an array produces: `json: cannot unmarshal array into Go struct field`. See [Permission Target Template](/docs/jf-rt-permission-target-template) for the full schema reference.
</Callout>

## Verifying the Group Was Created

The `group-create` command produces no output on success.

**To confirm the group exists:**

1. Query the groups API:

```bash
jf rt curl /api/security/groups/<group-name>
```

**Full example:**

```bash
jf rt curl /api/security/groups/backend-team
```

## Important Notes

* Requires **admin privileges** on the Artifactory instance.
* Use `--replace` to overwrite an existing group with the same name.
* Creating a group does not automatically assign any permissions — you need to create a permission target that references the group. See [Creating Permission Targets](https://jfrog.com/help/r/jfrog-artifactory-documentation/managing-permissions).

<br />