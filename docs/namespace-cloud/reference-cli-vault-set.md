<!-- Source: https://namespace.so/docs/reference/cli/vault-set -->

# nsc vault set

Update an existing secret in the vault.

`vault set` updates the value of an existing secret in your workspace's [vault](/docs/workspaces/security).

## Usage

```
nsc vault set --object_id <id> [--from_file <path>]
```

### Example

```
$ nsc vault set --object_id sec_8fumgjd5jk
Enter secret value: ****
 
Object ID:    sec_8fumgjd5jk
Version:      secv_hk6jk1j6d0
```

## Options

### --object\_id <id>

The object to update.

### --if-version-matches <version>

Only update if the object version matches this value.

### --from\_file <path>

Load the file contents as the secret value.

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

Last updated February 13, 2026
