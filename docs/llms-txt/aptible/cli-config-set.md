# Source: https://www.aptible.com/docs/reference/aptible-cli/cli-commands/cli-config-set.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# aptible config:set

This command sets [Configuration](/core-concepts/apps/deploying-apps/configuration) variables for an [App](/core-concepts/apps/overview).

# Synopsis

```
Usage:
  aptible config:set [--app APP] [VAR1=VAL1] [VAR2=VAL2] [...]

Options:
      [--app=APP]
  --env, [--environment=ENVIRONMENT]
  -r, [--remote=REMOTE]
```

# Examples

## Setting variables

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        VARIABLE_1=VALUE_1 \
        VARIABLE_2=VALUE_2
```

## Setting a variable from a file

> 📘 Setting variables from a file is a convenient way to set complex variables that contain spaces, newlines, or other special characters.

```shell  theme={null}
# This will read file.txt and set it as VARIABLE

aptible config:set --app "$APP_HANDLE" \
        "VARIABLE=$(cat file.txt)"
```

> ❗️ Warning: When setting variables from a file using PowerShell, you need to use `Get-Content` with the `-Raw` option to preserve newlines.

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        VARIABLE=$(Get-Content file.txt -Raw)
```

## Deleting variables

To delete a variable, set it to an empty value:

```shell  theme={null}
aptible config:set --app "$APP_HANDLE" \
        VARIABLE=
```
