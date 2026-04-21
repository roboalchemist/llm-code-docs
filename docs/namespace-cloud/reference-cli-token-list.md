<!-- Source: https://namespace.so/docs/reference/cli/token-list -->

# nsc token list

List revokable tokens.

`nsc token list` displays all revokable tokens that have been created in your workspace. By default, only active (non-revoked) tokens are shown, but you can include revoked tokens using the `--include_revoked` flag.

## Usage

```
nsc token list
```

### Example

```
$ nsc token list
Token ID           Name              Created                 Status
tok-abc123def456   production-api    2024-01-10T10:30:00Z    Active
tok-ghi789jkl012   ci-cd-token       2024-01-01T14:20:00Z    Expired
```

## Options

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

### --include\_revoked

Include revoked tokens in the list.

Last updated February 13, 2026
