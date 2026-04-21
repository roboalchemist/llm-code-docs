<!-- Source: https://namespace.so/docs/reference/cli/auth-trust-relationships -->

# nsc auth trust-relationships

Manage trust relationships for authentication.

`nsc auth trust-relationships` provides commands to manage trust relationships that enable secure authentication using OpenID Connect (OIDC) tokens from external systems like Google Cloud Platform, fly.io, and rwx.

Trust relationships allow you to establish secure access patterns by specifying issuer and subject match patterns that define which external identity providers and subjects are trusted to access your workspace.

## Usage

```
nsc auth trust-relationships [command]
```

## Available Commands

- **[add](/docs/reference/cli/auth-trust-relationships-add)** - Add a new trust relationship
- **[list](/docs/reference/cli/auth-trust-relationships-list)** - List existing trust relationships
- **[remove](/docs/reference/cli/auth-trust-relationships-remove)** - Remove a trust relationship

## Related Topics

- [Workspace Access Controls](/docs/workspaces/access) - Overview of authentication and access control
- [Workload Federation](/docs/federation) - Trust relationships with cloud providers
- [Permissions](/docs/security/permissions) - Available resources and actions
- [Security](/docs/workspaces/security) - Security best practices and audit logging

Last updated February 22, 2026
