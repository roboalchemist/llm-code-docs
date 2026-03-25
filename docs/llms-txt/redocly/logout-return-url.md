# Source: https://redocly.com/docs/realm/config/access/logout-return-url.md

# `logoutReturnUrl`


After a user logs out of your project and their session cookies are cleared, they will be redirected to the URL specified in `logoutReturnUrl`.
If not specified, users are redirected to the root path of your project by default.

This is useful when you want users to return to your main website or a specific page after logging out, rather than staying on the documentation site.

## Options

| Option | Type | Description |
|  --- | --- | --- |
| logoutReturnUrl | string | URL that users are redirected to after logging out. Must start with `http://` or `https://`. |


## Examples

### Use the access object (recommended)

The recommended way to configure `logoutReturnUrl` is within the `access` object:


```yaml redocly.yaml
access:
  logoutReturnUrl: https://yourcompany.com
```

### Redirect to a specific page

The following example redirects users to a custom logout page:


```yaml redocly.yaml
access:
  logoutReturnUrl: https://yourcompany.com/logout-success
```

**Note:** `logoutReturnUrl` is a new feature and is only available within the `access` object. It cannot be configured at the root level.

## Use cases

Common use cases for `logoutReturnUrl`:

- **Corporate portals:** Redirect users back to your main corporate website after logout
- **Public sites:** Redirect to your public-facing website after logout
- **Landing pages:** Send users to a specific landing page or homepage after logout


## Resources

- **[Access configuration](/docs/realm/config/access)** - Group authentication and access settings together using the `access` object
- **[RequiresLogin configuration](/docs/realm/config/access/requires-login)** - Require login for your project
- **[SSO configuration](/docs/realm/config/access/sso)** - Configure single sign-on for your project