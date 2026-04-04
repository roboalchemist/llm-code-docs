# Source: https://redocly.com/docs/realm/config/access/requires-login.md

# `requiresLogin`


Only authenticated users, who are verified through either Redocly or an identity provider (IdP) you [added in Reunite](/docs/realm/reunite/organization/sso/add-idp) can access your project.

The **requiresLogin** option cannot be used in conjunction with the **rbac**.
These configurations are mutually exclusive.

## Examples

### Use the access object (recommended)

The recommended way to configure `requiresLogin` is within the `access` object:


```yaml redocly.yaml
access:
  requiresLogin: true
```

### Root-level configuration (deprecated)

**Deprecated:** Root-level `requiresLogin` is still supported for backward compatibility but will show deprecation warnings when used alongside the `access` object. Please migrate to the `access` object format.


```yaml redocly.yaml
requiresLogin: true
```

## Resources

- **[Access configuration](/docs/realm/config/access)** - Group authentication and access settings together using the `access` object
- **[RBAC configuration](/docs/realm/config/access/rbac)** - Complete options for configuring role-based access control as an alternative to requiresLogin for granular permissions
- **[SSO configuration](/docs/realm/config/access/sso)** - Discover options for configuring single sign-on to work with requiresLogin for streamlined user authentication