<!-- Source: https://namespace.so/docs/reference/cli/auth-trust-relationships-remove -->

# nsc auth trust-relationships remove

Remove a trust relationship.

`nsc auth trust-relationships remove` deletes an existing trust relationship from your workspace. Once removed, tokens from the specified issuer and subject pattern will no longer be accepted for authentication.

## Usage

```
nsc auth trust-relationships remove [trust-relationship-id]
```

### Example

First, list existing trust relationships to get the ID:

```
$ nsc auth trust-relationships list
Trust Relationships:
 
ID: tr_abc123
Issuer: https://accounts.google.com
Subject Match: projects/123456789/serviceAccounts/my-service@my-project.iam.gserviceaccount.com
Created: 2024-01-15 10:30:00 UTC
 
ID: tr_def456
Issuer: https://fly.io/example-org
Subject Match: example-org:app:*
Created: 2024-01-10 14:22:00 UTC
 
ID: tr_ghi789
Issuer: https://cloud.rwx.com/mint
Subject Match: org:my-org:vault:deploy-vault
Created: 2024-01-08 09:15:00 UTC
```

Then remove the specific trust relationship:

```
$ nsc auth trust-relationships remove tr_abc123
Successfully removed trust relationship tr_abc123
```

## Arguments

### trust-relationship-id

The unique identifier of the trust relationship to remove. You can find this ID by running [`nsc auth trust-relationships list`](/docs/reference/cli/auth-trust-relationships-list).

## Important Notes

- **Immediate Effect**: Removing a trust relationship takes effect immediately
- **Active Sessions**: Existing authenticated sessions using the removed trust relationship will remain valid until they expire
- **Irreversible**: Once removed, you'll need to recreate the trust relationship with [`nsc auth trust-relationships add`](/docs/reference/cli/auth-trust-relationships-add) if you need it again

## Related Topics

- [nsc auth trust-relationships](/docs/reference/cli/auth-trust-relationships) - Main command overview
- [nsc auth trust-relationships add](/docs/reference/cli/auth-trust-relationships-add) - Add new relationships
- [nsc auth trust-relationships list](/docs/reference/cli/auth-trust-relationships-list) - List existing relationships
- [Security](/docs/workspaces/security) - Security best practices and audit logging

Last updated September 10, 2025
