<!-- Source: https://namespace.so/docs/reference/cli/vault-delete -->

# nsc vault delete

Delete an object from the vault.

`vault delete` removes a secret from your workspace's [vault](/docs/workspaces/security).

## Usage

```
nsc vault delete --object_id <id>
```

### Example

```
$ nsc vault delete --object_id sec_8fumgjd5jk
Successfully deleted object sec_8fumgjd5jk.
```

## Options

### --object\_id <id>

The object to delete.

### --if-version-matches <version>

Only delete if the object version matches this value.

Last updated February 13, 2026
