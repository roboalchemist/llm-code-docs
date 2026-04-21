<!-- Source: https://namespace.so/docs/reference/cli/vault-add -->

# nsc vault add

Add a secret to the vault.

`vault add` creates a new secret in your workspace's [vault](/docs/workspaces/security).

## Usage

```
nsc vault add [--from_file <path>]
```

### Example

```
$ nsc vault add --description "Database password" --label env=production
Enter secret value: ****
 
Object ID:    sec_8fumgjd5jk
Description:  Database password
Version:      secv_hk6jk1j6d0
```

## Options

### --description, -d <text>

Description of the secret.

### --revealable

If set, the secret value can be retrieved in future calls.

### --label <key=value>

Key-value labels to attach to the secret.

### --from\_file <path>

Load the file contents as the secret value.

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

Last updated February 13, 2026
