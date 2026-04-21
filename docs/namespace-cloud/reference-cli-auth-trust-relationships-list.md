<!-- Source: https://namespace.so/docs/reference/cli/auth-trust-relationships-list -->

# nsc auth trust-relationships list

List existing trust relationships.

`nsc auth trust-relationships list` displays all currently configured trust relationships for your workspace, showing the issuer and subject match patterns for each relationship.

## Usage

```
nsc auth trust-relationships list
```

### Example Output

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

## Understanding the Output

Each trust relationship displays:

- **ID**: Unique identifier for the trust relationship, used when removing relationships
- **Issuer**: The external identity provider that issued the tokens
- **Subject Match**: Pattern that defines which subjects are trusted
- **Created**: When the trust relationship was established

## Related Topics

- [nsc auth trust-relationships](/docs/reference/cli/auth-trust-relationships) - Main command overview
- [nsc auth trust-relationships add](/docs/reference/cli/auth-trust-relationships-add) - Add new relationships
- [nsc auth trust-relationships remove](/docs/reference/cli/auth-trust-relationships-remove) - Remove relationships
- [Workspace Access Controls](/docs/workspaces/access) - Authentication and access management

Last updated September 10, 2025
