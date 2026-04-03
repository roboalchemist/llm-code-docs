# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-users-delete.md

# Delete Artifactory users with jf rt users-delete

Delete users from Artifactory by username or from a CSV file.

## Synopsis

```
jf rt users-delete <users-list> [options]
jf rt users-delete --csv <path> [options]
```

**Aliases:** `rt udel`

## Arguments

| Argument       | Required             | Description                                          |
| -------------- | -------------------- | ---------------------------------------------------- |
| `<users-list>` | If not using `--csv` | Comma-separated list of usernames: `user1,user2,...` |

## Options

| Flag               | Default | Description                                                                             |
| ------------------ | ------- | --------------------------------------------------------------------------------------- |
| `--access-token`   | —       | JFrog access token                                                                      |
| `--csv`            | —       | Path to a CSV file. First row must be the header `username`. Extra columns are ignored. |
| `--password`       | —       | JFrog password (for authentication)                                                     |
| `--quiet`          | `$CI`   | Set to true to skip the delete confirmation message                                     |
| `--server-id`      | —       | Server ID configured using the `jf config` command                                      |
| `--ssh-key-path`   | —       | SSH key file path                                                                       |
| `--ssh-passphrase` | —       | SSH key passphrase                                                                      |
| `--url`            | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)                    |
| `--user`           | —       | JFrog username                                                                          |

## Examples

### Verify Command Help

**To view command help:**

1. Run:

```bash
jf rt users-delete --help
```

### Delete Users by Name

**To delete users by username:**

1. Run:

```bash
jf rt users-delete <users-list> --quiet
```

**Where:**

* `<users-list>` — comma-separated usernames (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt users-delete alice,bob --quiet
```

**Expected output** (one line per user, exits 0 on success):

```
[Info] Deleting user alice...
[Info] Deleting user bob...
```

### Delete Users from a CSV File

**To delete users listed in a CSV file:**

1. Create a CSV file with a `username` header and one username per row:

```csv
username
alice
bob
```

2. Run:

```bash
jf rt users-delete --csv <path> --quiet
```

**Where:**

* `<path>` — path to the CSV file (for example `./users-to-remove.csv`).

**Full example:**

```bash
jf rt users-delete --csv ./users-to-remove.csv --quiet
```

**Expected output** (one line per user, exits 0 on success):

```
[Info] Deleting user alice...
[Info] Deleting user bob...
```

<Callout icon="🚧" theme="warn">
  Warning

  This action permanently removes users. You cannot undo it.
</Callout>

## Important Notes

* **Irreversible**: Deleted users cannot be recovered. Their artifacts and builds remain, but their account and authentication credentials are permanently removed.
* **`--quiet` default**: In CI environments (when `CI` is set), `--quiet` defaults to `true`.
* Requires **admin privileges** on the Artifactory instance. Before running, verify your credentials are valid:
  ```bash
  jf rt ping --server-id <your-server-id>
  ```
  If this fails with a 401, refresh your token with `jf config add <server-id>` or `jf config edit <server-id>`.
* **Sequential processing**: Users are deleted one at a time. If a user does not exist, the CLI logs an error for that user and continues with the remaining users in the list or CSV.
* Deleting a user does not remove them from groups. Clean up group memberships separately if needed.
* **Trace ID on error**: If an API error occurs, the CLI prints a `Trace ID for JFrog Platform logs` value. You can share this ID with JFrog Support to help correlate server-side logs.

<br />