# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-permission-target-delete.md

# Delete a permission target with jf rt permission-target-delete

Permanently delete a permission target from the JFrog Platform.

## Prerequisites

* JFrog CLI installed and configured (`jf config add`)
* **Admin privileges** on the Artifactory instance
* An existing permission target to delete. To create one, see [jf rt permission-target-create](/docs/jf-rt-permission-target-create)

## Synopsis

```
jf rt permission-target-delete <permission-target-name> [options]
```

**Aliases:** `rt ptdel`

<Callout icon="📘" theme="info">
  Note

  The CLI `--help` output displays the alias form (`jf rt ptdel`) as the command name. Both `permission-target-delete` and `ptdel` are fully equivalent.
</Callout>

## Arguments

| Argument                   | Required | Description                             |
| -------------------------- | -------- | --------------------------------------- |
| `<permission-target-name>` | Yes      | Name of the permission target to remove |

## Options

| Flag                     | Default | Description                                                                                                                                                                                                                                                    |
| ------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--access-token`         | —       | JFrog access token                                                                                                                                                                                                                                             |
| `--client-cert-key-path` | —       | Private key file for the client certificate in PEM format                                                                                                                                                                                                      |
| `--client-cert-path`     | —       | Client certificate file in PEM format                                                                                                                                                                                                                          |
| `--password`             | —       | JFrog password                                                                                                                                                                                                                                                 |
| `--quiet`                | `$CI`   | Set to `true` to skip the delete confirmation message. Defaults to `true` when the `CI` environment variable is set to any non-empty value; otherwise `false`. Also automatically skipped when stdin is non-interactive (for example, piped input in scripts). |
| `--server-id`            | —       | Server ID configured using the `jf config` command                                                                                                                                                                                                             |
| `--ssh-key-path`         | —       | SSH key file path                                                                                                                                                                                                                                              |
| `--ssh-passphrase`       | —       | SSH key passphrase                                                                                                                                                                                                                                             |
| `--url`                  | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)                                                                                                                                                                                           |
| `--user`                 | —       | JFrog username                                                                                                                                                                                                                                                 |

## Examples

### Delete a Permission Target (Interactive)

Run without `--quiet` in a terminal to see a confirmation prompt before deletion.

**To delete a permission target interactively:**

1. Run:

```bash
jf rt permission-target-delete <permission-target-name>
```

**Where:**

* `<permission-target-name>` — name of the permission target to remove (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt permission-target-delete my-permission-target
```

**Expected output:**

```
[Info] Deleting permission target...
Delete the permission target 'my-permission-target'? (y/N): y
[Info] Done deleting permission target.
```

Enter `y` to confirm or `N` (or press Enter) to cancel without making any changes.

<Callout icon="🚧" theme="warn">
  Warning

  This action permanently removes the permission target. You cannot undo it.
</Callout>

***

### Delete a Permission Target (Non-Interactive)

Use `--quiet` to suppress the confirmation prompt — required for CI pipelines and scripts.

**To delete a permission target without a confirmation prompt:**

1. Run:

```bash
jf rt permission-target-delete <permission-target-name> --quiet
```

**Full example:**

```bash
jf rt permission-target-delete my-permission-target --quiet
```

**Expected output:**

```
[Info] Deleting permission target...
[Info] Done deleting permission target.
```

<Callout icon="🚧" theme="warn">
  Warning

  This action permanently removes the permission target. You cannot undo it.
</Callout>

***

### Delete a Permission Target That Does Not Exist

If the named permission target is not found, the command exits with code `1` and prints an error.

**To handle a missing permission target (example):**

1. Run:

```bash
jf rt permission-target-delete <permission-target-name> --quiet
```

**Full example:**

```bash
jf rt permission-target-delete nonexistent-target --quiet
```

**Expected output:**

```
[Info] Deleting permission target...
[Error] server response: 404
{"errors":[{"status":404,"message":"Permission target 'nonexistent-target' does not exist"}]}
```

Use the exit code in scripts to detect this condition:

**Full example:**

```bash
jf rt permission-target-delete my-target --quiet
if [ $? -ne 0 ]; then
  echo "Delete failed — target may not exist"
fi
```

***

### View command usage

**To view command usage:**

1. Run:

```bash
jf rt permission-target-delete --help
```

**Expected output:**

```
Name:
  jf rt ptdel - Permanently delete a permission target.

Usage:
  jf rt ptdel <permission target name>

Arguments:
  permission target name
    Specifies the permission target that should be removed.

Options:
  --quiet    [Default: $CI] Set to true to skip the delete confirmation message.
  ...
```

## Important Notes

* **Irreversible**: Deleting a permission target immediately removes access control rules. Users and groups governed by this target lose their permissions instantly.
* **`--quiet` default**: Defaults to `true` when the `CI` environment variable is set to any non-empty value. In non-interactive environments (piped stdin in scripts), the confirmation prompt is also skipped automatically even without setting `--quiet` or `$CI`. To unconditionally suppress the prompt, pass `--quiet=true` explicitly.
* **Confirmation prompt**: In an interactive terminal (without `--quiet`), the CLI asks:
  ```
  Delete the permission target '<name>'? (y/N):
  ```
  Enter `y` to proceed or `N` to abort. The deletion is not performed until you confirm.
* Requires **admin privileges** on the Artifactory instance.
* If the permission target does not exist, the command exits with code `1` and returns a `404` server error. See the example above for the exact error format.
* The CLI emits `[Info] Deleting permission target...` immediately before contacting the server. If an error follows this line, the deletion did **not** occur.
* The error response includes a `Trace ID` in an `[Info]` line preceding the error. Provide this ID when raising a support ticket.

## Related Commands

| Command                                                                               | Description                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [jf rt permission-target-template](/docs/jf-rt-permission-target-template) (`rt ptt`) | Create a JSON template interactively for use with create or update |
| [jf rt permission-target-create](/docs/jf-rt-permission-target-create) (`rt ptc`)     | Create a new permission target from a template file                |
| [jf rt permission-target-update](/docs/jf-rt-permission-target-update) (`rt ptu`)     | Replace an existing permission target from a template file         |

<br />