# Source: https://docs.jfrog.com/artifactory/docs/user-management.md

# Create a user in Artifactory

# Create a user in Artifactory

Create a new user in Artifactory with username, password, and email using `jf rt user-create`.

<Callout icon="📘" theme="info">
  Prerequisites

  * JFrog CLI installed — see the [install guide](/docs/download-and-install-the-jfrog-cli)
  * A configured server (`jf config add`) **or** an Artifactory URL and admin access token to pass inline
  * **Admin privileges** on the target Artifactory instance
</Callout>

## Synopsis

```
jf rt user-create <username> <user-password> <email> [options]
```

**Aliases:** none

## Arguments

| Argument          | Required | Description                                                                 |
| ----------------- | -------- | --------------------------------------------------------------------------- |
| `<username>`      | Yes      | Username for the new user                                                   |
| `<user-password>` | Yes      | Login password for the new user (not the CLI's own authentication password) |
| `<email>`         | Yes      | Email address for the new user                                              |

## Options

| Flag               | Default | Description                                                                                        |
| ------------------ | ------- | -------------------------------------------------------------------------------------------------- |
| `--access-token`   | —       | JFrog access token                                                                                 |
| `--admin`          | `false` | Set to true to create an admin user                                                                |
| `--password`       | —       | JFrog password (for authentication)                                                                |
| `--replace`        | `false` | Set to true to replace existing users or groups                                                    |
| `--server-id`      | —       | Server ID configured using `jf config`                                                             |
| `--ssh-key-path`   | —       | SSH key file path                                                                                  |
| `--ssh-passphrase` | —       | SSH key passphrase                                                                                 |
| `--url`            | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)                               |
| `--user`           | —       | JFrog username                                                                                     |
| `--users-groups`   | —       | Comma-separated list of groups for the new user to join. Groups must already exist in Artifactory. |

## Examples

### Help

**To view command help:**

1. Run:

```bash
jf rt user-create --help
```

**Expected output:** CLI prints the command synopsis, arguments, and all available flags.

***

### Basic Usage

**To create a user:**

1. If you use a pre-configured server (recommended — avoids exposing the token in shell history), run:

```bash
jf rt user-create <username> <user-password> <email> --server-id=<server-id>
```

2. If you use inline credentials instead, run:

```bash
jf rt user-create <username> <user-password> <email> --url=<artifactory-url> --access-token=<Token>
```

**Where:**

* `<username>`, `<user-password>`, and `<email>` — values for the new user (see [Arguments](#arguments)).
* `<server-id>` — server ID from `jf config`.
* `<artifactory-url>` — base Artifactory URL.
* `<Token>` — admin access token (do not paste real tokens into shared history).

**Full examples:**

```bash
jf rt user-create jdoe 'P@ssw0rd!' jdoe@example.com --server-id=acme
jf rt user-create jdoe 'P@ssw0rd!' jdoe@example.com --url=https://acme.jfrog.io/artifactory --access-token=<Token>
```

**Expected output:**

```
[Info] Creating user <username>...
```

A silent exit 0 with no error message means the user was created successfully.

***

### Create User with Groups

<Callout icon="📘" theme="info">
  Note

  The groups specified in `--users-groups` must already exist in Artifactory. Use [`jf rt group-create`](/docs/jf-rt-group-create) to create them first.
</Callout>

**To create a user and assign groups:**

1. Run:

```bash
jf rt user-create <username> <user-password> <email> --users-groups <users-groups> --server-id=<server-id>
```

**Where:**

* `<users-groups>` — comma-separated list of existing group names (no spaces).

**Full example:**

```bash
jf rt user-create jdoe 'P@ssw0rd!' jdoe@example.com --users-groups developers,readers --server-id=acme
```

**Expected output:**

```
[Info] Creating user <username>...
```

***

### Create Admin User

**To create an admin user:**

1. Run:

```bash
jf rt user-create <username> <user-password> <email> --admin --server-id=<server-id>
```

**Full example:**

```bash
jf rt user-create admin-user 'P@ssw0rd!' admin@example.com --admin --server-id=acme
```

**Expected output:**

```
[Info] Creating user <username>...
```

***

### Overwrite an Existing User

Use `--replace` to reset a user's password, email, or group membership:

**To replace an existing user:**

1. Run:

```bash
jf rt user-create <username> <new-user-password> <new-email> --replace --server-id=<server-id>
```

**Full example:**

```bash
jf rt user-create jdoe 'NewSecret!' jdoe-new@example.com --replace --server-id=acme
```

**Expected output:**

```
[Info] Creating user <username>...
```

## When to Use

Use `jf rt user-create` to create a **single user** in Artifactory. For bulk user provisioning, use [`jf rt users-create`](/docs/jf-rt-users-create) with a CSV file instead.

Common scenarios:

* **Service accounts**: Create dedicated service accounts for CI/CD pipelines
* **Testing**: Create temporary users for integration testing (delete them after with [`jf rt users-delete`](/docs/jf-rt-users-delete))
* **Automation**: Part of an onboarding script that creates a user, adds them to groups, and sets permissions

## Important Notes

* Requires **admin privileges** on the Artifactory instance.
* `<user-password>` is the new user's login password. The `--password` flag in Options is a separate credential used to authenticate the CLI itself to Artifactory — do not confuse the two.
* Use `--replace` to overwrite an existing user with the same username (see the [Overwrite an Existing User](#overwrite-an-existing-user) example above).
* Passwords are sent over HTTPS. Ensure your Artifactory instance uses TLS.

<br />