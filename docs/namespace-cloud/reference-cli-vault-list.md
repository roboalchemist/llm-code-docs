<!-- Source: https://namespace.so/docs/reference/cli/vault-list -->

# nsc vault list

List objects in the vault.

`vault list` lists all secrets stored in your workspace's [vault](/docs/workspaces/security).

## Usage

```
nsc vault list
```

### Example

```
$ nsc vault list
OBJECT ID        VERSION            DESCRIPTION             CREATED
---------------------------------------------------------------------------------
sec_8fumgjd5jk   secv_hk6jk1j6d0    Test ECDSA SSH Key      2023-08-30T23:03:14Z
sec_rdb1lirdp4   secv_kuifdoaheg    TestSecret              2023-10-10T22:49:41Z
```

## Options

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

Last updated February 13, 2026
