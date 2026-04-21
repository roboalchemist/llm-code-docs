<!-- Source: https://namespace.so/docs/reference/cli/github-profile-list -->

# nsc github profile list

List all GitHub runner profiles.

`nsc github profile list` displays all runner profiles configured in the current workspace, including their tags, instance shapes, operating systems, and status information.

## Usage

```
nsc github profile list [flags]
```

### Examples

**List all profiles:**

```
$ nsc github profile list
```

**List profiles as JSON:**

```
$ nsc github profile list -o json
```

## Flags

### -o, --output string (optional)

Output format. Default: `plain`.

Supported values: `plain`, `json`.

## Related Topics

- [nsc github profile](/docs/reference/cli/github-profile) - Manage GitHub runner profiles
- [nsc github profile create](/docs/reference/cli/github-profile-create) - Create a profile
- [nsc github profile describe](/docs/reference/cli/github-profile-describe) - Describe a profile in detail

Last updated April 14, 2026
