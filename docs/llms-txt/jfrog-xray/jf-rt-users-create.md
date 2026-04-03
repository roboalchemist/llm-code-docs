# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-users-create.md

# Create users from a CSV with jf rt users-create

Create new users in Artifactory from a CSV file with usernames, passwords, and emails.

## Synopsis

```
jf rt users-create --csv <path> [options]
```

**Aliases:** `rt uc`

## Arguments

| Argument | Required | Description                                            |
| -------- | -------- | ------------------------------------------------------ |
| —        | —        | No positional arguments. Use `--csv` for the file path |

## Options

| Flag               | Required | Default | Description                                                                                                                        |
| ------------------ | -------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `--access-token`   | No       | —       | JFrog access token                                                                                                                 |
| `--csv`            | **Yes**  | —       | Path to a CSV file. First row must be headers: `username`, `password`, `email`                                                     |
| `--password`       | No       | —       | JFrog password (for authentication)                                                                                                |
| `--replace`        | No       | `false` | Without this flag, users that already exist are skipped. Set to `true` to overwrite existing users' password and email instead     |
| `--server-id`      | No       | —       | Server ID configured using the `jf config` command                                                                                 |
| `--ssh-key-path`   | No       | —       | SSH key file path                                                                                                                  |
| `--ssh-passphrase` | No       | —       | SSH key passphrase                                                                                                                 |
| `--url`            | No       | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)                                                               |
| `--user`           | No       | —       | JFrog username                                                                                                                     |
| `--users-groups`   | No       | —       | Comma-separated list of groups for the new users to join. **Groups must already exist in Artifactory** before running this command |

## Examples

### Create Users from a CSV File

**To create users from a CSV file:**

1. Create a CSV file with the user details (see [CSV Format](#csv-format) below):

```csv
username,password,email
alice,Secret1!,alice@example.com
bob,Secret2!,bob@example.com
```

2. Save it as `users.csv`, then run:

```bash
jf rt users-create --csv <path>
```

**Where:**

* `<path>` — path to your CSV file (for example `./users.csv`).

**Full example:**

```bash
jf rt users-create --csv ./users.csv
```

**Expected output:**

```
[Info] Creating user alice...
[Info] Creating user bob...
[Info] Done creating 2 users.
```

### Create Users with Group Assignment

The groups `developers` and `readers` must already exist in Artifactory before running this command.

**To create users from a CSV and assign groups:**

1. Use a CSV file in the format described in [CSV Format](#csv-format).
2. Run:

```bash
jf rt users-create --csv <path> --users-groups <group-list>
```

**Where:**

* `<path>` — path to the CSV file.
* `<group-list>` — comma-separated Artifactory group names (no spaces), for example `developers,readers`.

**Full example:**

```bash
jf rt users-create --csv ./users.csv --users-groups developers,readers
```

**Expected output:**

```
[Info] Creating user alice...
[Info] Creating user bob...
[Info] Done creating 2 users.
```

### Replace Existing Users

Use `--replace` when users in the CSV already exist and you want to overwrite their password and email. Without this flag, existing users are skipped.

**To replace existing users from a CSV:**

1. Run:

```bash
jf rt users-create --csv <path> --replace
```

**Where:**

* `<path>` — path to the CSV file.

**Full example:**

```bash
jf rt users-create --csv ./users.csv --replace
```

**Expected output:**

```
[Info] Creating user alice...
[Info] Creating user bob...
[Info] Done creating 2 users.
```

## CSV Format

The CSV file must contain these headers in the first row: `username`, `password`, `email`.

```csv
username,password,email
alice,secret1,alice@example.com
bob,secret2,bob@example.com
```

## When to Use

Use `jf rt users-create` for **bulk user provisioning** — for example, when onboarding an entire team or migrating users from another system. Prepare a CSV file and run a single command.

**Typical onboarding workflow:**

**To onboard a new team with groups and permissions:**

1. **Create the groups** (skip if they already exist). See [jf rt group-create](/docs/jf-rt-group-create) for details.

```bash
jf rt group-create developers
jf rt group-create readers
```

2. **Create users and assign them to the groups:**

```bash
jf rt users-create --csv ./new-team.csv --users-groups developers,readers
```

3. **Set up a permission target for the team.** Generate a template with [jf rt permission-target-template](/docs/jf-rt-permission-target-template), fill in the repositories and actions, then apply it:

```bash
jf rt permission-target-update ./team-permissions.json
```

## Troubleshooting

| Error                                | Likely Cause                       | Resolution                                                                 |
| ------------------------------------ | ---------------------------------- | -------------------------------------------------------------------------- |
| `401 Token failed verification`      | Expired or missing access token    | Re-authenticate: run `jf config add` to reconfigure your server            |
| `CSV must include headers`           | First row is missing or misspelled | Ensure the first row is exactly `username,password,email`                  |
| `403 Forbidden`                      | Insufficient privileges            | Confirm your account has **Admin** rights on the Artifactory instance      |
| Users created but not added to group | Group name does not exist          | Create the group first with `jf rt group-create <group-name>`, then re-run |

<Callout icon="👍" theme="okay">
  Tip

  If the CLI reports a server-side error, it also prints a `Trace ID` (for example, `[Info] Trace ID for JFrog Platform logs: abc123`). Include this ID when contacting JFrog Support to speed up diagnosis.
</Callout>

## Important Notes

* The CSV file **must** have headers: `username`, `password`, `email` in the first row.
* Requires **admin privileges** on the Artifactory instance.
* Use `--replace` to update existing users if they already exist.
* Passwords in the CSV are sent over HTTPS. Do not commit CSV files with real passwords to version control.
* Restrict the file's permissions before use to prevent other users on the system from reading plaintext passwords:
  ```bash
  chmod 600 users.csv
  ```

<br />