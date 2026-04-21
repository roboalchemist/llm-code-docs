<!-- Source: https://namespace.so/docs/reference/cli/token-revoke -->

# nsc token revoke

Revoke a token.

`nsc token revoke` immediately revokes a token, preventing it from being used for further
authentication. Once revoked, a token cannot be reactivated and any attempts to use it will fail.

Revoking tokens is important for security best practices, especially when:

- A token is no longer needed
- A token may have been compromised
- Access needs to be removed immediately
- Rotating credentials as part of regular security maintenance

## Usage

```
nsc token revoke --token_id <id>
```

### Example

```
$ nsc token revoke --token_id tok-abc123def456
Successfully revoked token tok-abc123def456.
```

## Options

### --token\_id <id>

The token ID to revoke. Required.

Last updated February 13, 2026
