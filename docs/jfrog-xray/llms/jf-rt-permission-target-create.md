# Source: https://docs.jfrog.com/artifactory/docs/jf-rt-permission-target-create.md

# Create a permission target with jf rt permission-target-create

Create a new permission target in the JFrog Platform from a template file.

## Synopsis

```
jf rt permission-target-create <template-path> [options]
```

**Aliases:** `rt ptc`

## Arguments

| Argument          | Required | Description                                                             |
| ----------------- | -------- | ----------------------------------------------------------------------- |
| `<template-path>` | Yes      | Local file system path to the template file. Create it with `jf rt ptt` |

## Options

| Flag                     | Default | Description                                                                                                                                                                                                                                                                                      |
| ------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `--access-token`         | —       | JFrog access token                                                                                                                                                                                                                                                                               |
| `--client-cert-key-path` | —       | Private key file for the client certificate in PEM format                                                                                                                                                                                                                                        |
| `--client-cert-path`     | —       | Client certificate file in PEM format                                                                                                                                                                                                                                                            |
| `--password`             | —       | JFrog password                                                                                                                                                                                                                                                                                   |
| `--server-id`            | —       | Server ID configured using the `jf config` command                                                                                                                                                                                                                                               |
| `--ssh-key-path`         | —       | SSH key file path                                                                                                                                                                                                                                                                                |
| `--ssh-passphrase`       | —       | SSH key passphrase                                                                                                                                                                                                                                                                               |
| `--url`                  | —       | JFrog Artifactory URL (example: `https://acme.jfrog.io/artifactory`)                                                                                                                                                                                                                             |
| `--user`                 | —       | JFrog username                                                                                                                                                                                                                                                                                   |
| `--vars`                 | —       | Semicolon-separated variables in the form `"key1=value1;key2=value2"`. In the template, use `${key1}` placeholder syntax. Variable substitution is single-value only — to include multiple repositories or groups, list them directly in the template rather than passing them through `--vars`. |

## Template Format

The template is a JSON file that describes the full permission target definition. Generate one interactively with `jf rt ptt`, or write one manually using the format below.

<Callout icon="📘" theme="info">
  Note

  `jf rt ptt` is an interactive command that requires a TTY. It cannot be run in CI/CD pipelines or non-interactive shells. In those environments, create the template JSON file manually.
</Callout>

```json
{
  "name": "my-permission-target",
  "repo": {
    "repositories": "libs-release",
    "actions": {
      "users": {
        "alice": ["read", "write"]
      },
      "groups": {
        "developers": ["read", "write", "annotate", "delete", "manage"]
      }
    }
  },
  "build": {
    "repositories": "artifactory-build-info",
    "actions": {
      "groups": {
        "developers": ["read", "manage"]
      }
    }
  }
}
```

**Key schema notes:**

* `repositories` must be a **string** (a single repository key), not a JSON array.
* Supported permission values: `read`, `write`, `annotate`, `delete`, `manage`, `managedXrayMeta`, `distribute`.
* The `build` section is optional. Omit any top-level section (`repo`, `build`, `releaseBundle`) if it is not needed.
* To use variable substitution, replace any value with `${variableName}` and pass the variable via `--vars`.

## Examples

### Create a permission target from a template file

**To create a permission target from a template file:**

1. Run:

```bash
jf rt permission-target-create <template-path>
```

**Where:**

* `<template-path>` — path to the JSON template (see [Arguments](#arguments)).

**Full example:**

```bash
jf rt permission-target-create ./my-permission-target.json
```

Expected output:

```
[Info] Creating permission target...
```

A clean exit with this message confirms the permission target was created successfully.

### Create with variable substitution

Use `--vars` to inject values into `${placeholder}` fields in your template at runtime. This is useful for reusing a single template to create multiple permission targets or deploying across environments.

**To create a permission target with variable substitution:**

1. Run:

```bash
jf rt permission-target-create <template-path> --vars "<key1>=<value1>;<key2>=<value2>"
```

**Where:**

* `<template-path>` — path to the template JSON.
* `<key1>=<value1>;...` — semicolon-separated substitutions matching `${key1}` placeholders in the file.

**Full example:**

```bash
jf rt permission-target-create ./template.json --vars "groupName=developers;repoName=libs-release"
```

Given a template containing `"repositories": "${repoName}"` and `"${groupName}": [...]`, this command substitutes the values before submitting. Expected output:

```
[Info] Creating permission target...
```

### View command usage

**To view command usage:**

1. Run:

```bash
jf rt permission-target-create --help
```

## Important Notes

* Requires **admin privileges** on the Artifactory instance.
* The `name` field in the template becomes the permission target's identifier. If a permission target with that name already exists, the command fails with a `409 Conflict` error — use [`jf rt permission-target-update`](/docs/jf-rt-permission-target-update) to update an existing target instead.
* Use `jf rt ptt` to generate your initial template interactively, ensuring the correct schema. See the Template Format section above for the manual format.

## Troubleshooting

| Error                                                                                                   | Cause                                                                        | Fix                                                                                            |
| ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `open <path>: no such file or directory`                                                                | The template file path is wrong or the file does not exist                   | Verify the path and confirm the file exists                                                    |
| `json: cannot unmarshal array into Go struct field PermissionSectionAnswer.repositories of type string` | The `repositories` field in the template is a JSON array instead of a string | Change `["repo-name"]` to `"repo-name"` in the template                                        |
| `server response: 409`                                                                                  | A permission target with this name already exists                            | Use `jf rt permission-target-update` to update it, or choose a different name                  |
| `server response: 401`                                                                                  | Authentication failed                                                        | Re-run `jf config add` to refresh credentials, or check that your access token has not expired |
| `Wrong number of arguments (0)`                                                                         | The required `<template-path>` argument was not provided                     | Provide the path to your template file as the first argument                                   |

## Related Commands

| Command                                                                               | Description                                                        |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| [jf rt permission-target-template](/docs/jf-rt-permission-target-template) (`rt ptt`) | Create a JSON template interactively for use with create or update |
| [jf rt permission-target-update](/docs/jf-rt-permission-target-update) (`rt ptu`)     | Replace an existing permission target from a template file         |
| [jf rt permission-target-delete](/docs/jf-rt-permission-target-delete) (`rt ptdel`)   | Permanently delete a permission target                             |

<br />