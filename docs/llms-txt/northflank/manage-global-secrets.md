# Source: https://northflank.com/docs/v1/application/secure/manage-global-secrets.md

# Manage global secrets

Global secrets are team-level resources that store configuration data, values, and files that can be referenced across multiple templates and services. Unlike secret groups which are project-scoped, global secrets are accessible at the team level.

To create or modify a global secret, navigate to the [secrets page](http://app.northflank.com/s/account/global-secrets) from your team menu.

Enter values as JSON-structured objects, or upload secret files, which will be accessible in your templates.

> [!note] 
> [Click here](http://app.northflank.com/s/account/global-secrets) to view your global secrets.

## Global secret type

You can set the type for a global secret as either `secret` or `configuration` values. This is useful when working with teams if you need to control access to certain secrets, but allow team members to view or edit other configuration.

[RBAC permissions](use-role-based-access-control) can be configured separately for the two types of global secrets. This allows you to, for example, create a role that has full access to config values, but access only to secret keys and not their values.

| Feature | Secret type | Config type |
| --- | --- | --- |
| Access control | Restricted | Broader team access |
| [GitOps support]((/docs/v1/application/infrastructure-as-code/gitops-on-northflank)) | Not supported | Supported |
| Typical use cases | API keys, passwords, credentials | Feature flags, endpoints, non-sensitive settings |

The secret type cannot be edited from the settings page of a global secret.

## Global secret values

Global secrets store JSON structured objects that support nesting and arrays. This allows you to organize related configuration hierarchically.

```json
{
  "database": {
    "host": "db.example.com",
    "port": 5432,
    "credentials": {
      "username": "admin",
      "password": "secure-password"
    }
  },
  "allowedIPs": [
    "127.0.0.1",
    "192.168.1.0/24"
  ]
}
```

You can access nested values in templates using dot notation: `database.credentials.username`

## Global secret files

You can upload files to a global secret. Each file requires an identifier, path, content, and encoding.

The identifier is used to reference the file in templates.

## GitOps support

Global secrets of type `Configuration` support GitOps workflows. This allows you to version control your configuration and automatically sync from Git repositories.

To enable GitOps for a Configuration, create a global secret with type "Configuration", enable GitOps in the settings, and connect your Git repository.

Secret type global secrets do not support GitOps for security reasons.

## Dynamic templating

You can use [dynamic templating](inject-secrets#dynamic-templating) within global secret values to reference other values in the same secret.

For example:

```json
{
  "baseUrl": "https://api.example.com",
  "users": "${baseUrl}/users",
  "posts": "${baseUrl}/posts"
}
```

## Functions

You can use the `randomSecret` [function](inject-secrets#functions) when creating global secret values. The function will be evaluated when you save the secret, and the generated value will be stored securely.

```json
{
  "apiKey": "${fn.randomSecret(32)}",
  "secretToken": "${fn.randomSecret(64, 'hex')}"
}
```

## Next steps

- [Reference global secrets: Reference global secrets in your template definitions to inject configuration and sensitive data.](/v1/application/secure/reference-global-secrets)
