# Source: https://redocly.com/docs/realm/reunite/organization/sso/sso.md

# Source: https://redocly.com/docs/realm/config/access/sso.md

# `sso`


This configuration determines which IdPs are available for logging in to a project.
Configuring SSO by itself does not require users to log in to access a project.
To require login to a project, [`rbac`](/docs/realm/config/access/rbac) or [`requiresLogin`](/docs/realm/config/access/requires-login) must also be configured.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| sso
 | [string]
 | List of identity provider types from Reunite.
Possible values: `REDOCLY`, `CORPORATE`, `GUEST`, or `[]`.
Default value: `AUTO` - when no `sso` is defined, this special value is used.
It redirects users to `GUEST` IdP if it's defined in Reunite.
Otherwise, it redirects to `CORPORATE` IdP, if defined in Reunite.
If no IdPs are defined it falls back to the `REDOCLY` IdP, giving users the option to log in using their Redocly credentials or Social Login providers (like `Google`).
 |


## Examples

### Use the access object (recommended)

The recommended way to configure `sso` is within the `access` object:


```yaml redocly.yaml
access:
  sso:
    - GUEST
    - REDOCLY
```

### Disable SSO

The following example disables SSO using the `access` object:


```yaml redocly.yaml
access:
  sso: []
```

After applying this configuration, if you have `rbac` configured for the same project, and there are pages assigned to the `authenticated` default team, those pages are not accessible to anyone.
Otherwise, if you do not have `rbac` configured, or you have all pages assigned to the `anonymous` default team, all pages are accessible.

### Root-level configuration (deprecated)

**Deprecated:** Root-level `sso` is still supported for backward compatibility but will show deprecation warnings when used alongside the `access` object. Please migrate to the `access` object format.


```yaml redocly.yaml
sso:
  - GUEST
  - REDOCLY
```

## Resources

- **[Access configuration](/docs/realm/config/access)** - Group authentication and access settings together using the `access` object
- **[RBAC configuration](/docs/realm/config/access/rbac)** - Complete options for configuring role-based access control for granular project permissions and user management
- **[RequiresLogin configuration](/docs/realm/config/access/requires-login)** - Require login for all users to your project without implementing complex role-based access control
- **[Google Workspace SAML 2 SSO](/docs/realm/reunite/organization/sso/configure-google-sso)** - Integrate Google Workspace SAML 2 SSO with Reunite for enterprise authentication workflows
- **[Single Sign-on concepts](/docs/realm/reunite/organization/sso/sso)** - Understand different identity provider types in Reunite and how they apply to project authentication
- **[Add an identity provider](/docs/realm/reunite/organization/sso/add-idp)** - Follow steps to add identity providers in Reunite for centralized authentication management
- **[Configure SSO](/docs/realm/reunite/organization/sso/configure-sso)** - Enable multiple identity provider types to give users flexible authentication options for your projects
- **[Role-based access control (RBAC)](/docs/realm/config/access/rbac)** - Implement advanced access control scenarios to grant specific users access to specific content and features