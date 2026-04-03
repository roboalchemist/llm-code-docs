# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-group-delete.md

# Delete an Artifactory group with jf rt group-delete

Delete a users group from Artifactory.

## Prerequisites

* JFrog CLI installed and configured (`jf config add`)
* Admin privileges on the Artifactory instance
* The group to be deleted must already exist

<Callout icon="📘" theme="info">
  Note

  The JFrog CLI does not provide a `group-list` or `group-get` command. Before deleting, verify the exact group name in the Artifactory UI (**Administration → Identity and Access → Groups**) or via the Artifactory REST API (`GET /access/api/v2/groups`). Deleting a group is irreversible — a typo in the group name cannot be undone.
</Callout>

## Synopsis

```
jf rt group-delete <group name> [options]
```

**Aliases:** `rt gdel`

<Callout icon="📘" theme="info">
  Note

  When you run `jf rt group-delete --help`, the CLI displays the alias name `jf rt gdel` in the usage line. Both `jf rt group-delete` and `jf rt gdel` are equivalent and interchangeable.
</Callout>

## Arguments

| Argument       | Required | Description                     |
| -------------- | -------- | ------------------------------- |
| `<group name>` | Yes      | The name of the group to delete |

## Options

| Flag               | Default | Description                                                          |
| ------------------ | ------- | -------------------------------------------------------------------- |
| `--access-token`   | —       | JFrog access token                                                   |
| `--password`       | —       | JFrog password (for authentication)                                  |
| `--quiet`          | `$CI`   | Set to true to skip the delete confirmation message                  |
| `--server-id`      | —       | Server ID configured using the `jf config` command                   |
| `--ssh-key-path`   | —       | SSH key file path                                                    |
| `--ssh-passphrase` | —       | SSH key passphrase                                                   |
| `--url`            | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`) |
| `--user`           | —       | JFrog username                                                       |

## Examples

### Verify Command Help

**To view command help:**

1. Run:

```bash
jf rt group-delete --help
```

### Delete a Group (Interactive)

Running without `--quiet` prompts for confirmation before proceeding.

**To delete a group with confirmation:**

1. Run:

```bash
jf rt group-delete <group name>
```

**Where:**

* `<group name>` — name of the group to delete (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt group-delete developers
```

Expected output:

```
Delete the group developers? (y/n): y
Done deleting group: developers.
```

<Callout icon="🚧" theme="warn">
  Warning

  This action permanently removes the group. You cannot undo it.
</Callout>

### Delete a Group (Non-Interactive)

Use `--quiet` to skip the confirmation prompt. Suitable for CI pipelines where the `CI` environment variable is set.

**To delete a group without a prompt:**

1. Run:

```bash
jf rt group-delete <group name> --quiet
```

**Full example:**

```bash
jf rt group-delete developers --quiet
```

On success the command exits with code 0 and produces **no output**. The absence of output is expected — it does not indicate a problem.

<Callout icon="📘" theme="info">
  Note

  The CLI prints a `[Info] Trace ID for JFrog Platform logs: <id>` line on every server request. This is informational and can be used to correlate requests in JFrog Platform logs. It does not indicate an error.
</Callout>

## Important Notes

* **Irreversible**: Deleting a group removes it permanently. Users who were members lose the group's permissions immediately.
* Deleting a group does **not** delete its member users — they remain in Artifactory but lose permissions granted through this group.
* **`--quiet` default**: In CI environments (when `CI` is set), `--quiet` defaults to `true`.
* Requires **admin privileges** on the Artifactory instance.
* Permission targets that reference this group will no longer grant access through it after deletion.

## Troubleshooting

| Error                           | Cause                                              | Resolution                                                                                  |
| ------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| `401 Token failed verification` | The stored access token is expired or invalid      | Re-authenticate with `jf config add`, or pass a fresh token using `--access-token <token>`  |
| `403 Forbidden`                 | The configured user does not have admin privileges | Use credentials for an account with admin rights, or contact your Artifactory administrator |
| `404 Not Found`                 | The specified group does not exist                 | Verify the group name in the Artifactory UI or REST API before retrying                     |

<br />