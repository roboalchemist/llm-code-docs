# Source: https://northflank.com/docs/v1/application/secure/manage-secret-groups.md

# Manage secret groups

Secret groups contain collections of runtime variables or build arguments that will be inherited by services and jobs in a project.

To create or modify a group of secrets, open the secrets page from the project menu.

Enter the secrets as key value pairs, in JSON format, or import from a `.env` file.

You can also [link addons](https://northflank.com/docs/v1/application/databases-and-persistence/connect-database-secrets-to-workloads) to the secret group, or [upload secret files](upload-secret-files), which will be inherited like manually-added secrets.

After creating or editing a secret group you can click restart dependents   to redeploy all services and jobs that inherit the secrets with the new values.

> [!note] 
> [Click here](https://app.northflank.com/s/project/secrets) to view your project secret groups.

![Configuring a secret group in the Northflank application](https://assets.northflank.com/documentation/v1/application/secure/manage-secret-groups/secret-group-settings.png)

## Secret group type

You can set the type for a secret group as either secret values or configuration values. This is useful when working with colleagues if you need to control access to certain secrets, but allow team members to view or edit other values inherited by services and jobs.

[RBAC permissions](use-role-based-access-control) can be configured separately for the two types of secret group. This allows you to, for example, create a role that has full access to configuration groups, but access only to secret group keys and not their values.

The group type can be edited from the group settings page of a secret group.

## Secret group scope

You can create a group of either [runtime variables](./inject-secrets#runtime-variables), [build arguments](./inject-secrets#build-arguments), or both.

The scope will define when your secrets are inherited by services and jobs: at build time, runtime, or both. The group scope can be edited from the group settings page of a secret group.

## Restrict secrets

You can restrict these secrets to specific services or jobs within your project from the group settings page of a secret group.

Secrets from an unrestricted group will be inherited by all services or jobs within the project that use the type of secret set in the group. Secrets that have been restricted to specific services or jobs will only be inherited by the selected services and jobs that use the type of secret set in the group.

### Restrict by tag

You can also make secret groups available to resources with [selected tags](https://northflank.com/docs/v1/application/release/tag-workloads-and-resources), in addition to specific services and jobs. You can combine restrictions to specific resources with restrictions by tag, so that both the selected resources and resources with the chosen tags will inherit secrets from the group.

## Group priority

The priority of a secret group determines the value of which group is used if multiple secrets contain the same key. The group priority can be edited from the group settings page of a secret group.

You can set the priority of a group as any integer between `0` and `100`. The secret group with a higher priority will take precedence.

For example if the priority for Group A is `50` and the priority of Group B is `20`, the values of Group A will be used for any conflicting keys between the groups:

| Secret group A (priority `50`) | Secret group B (priority `20`) | Secret group value used |
| --- | --- | --- |
| `KEY_1` | `KEY_1` | Group A |
| `KEY_2` | `KEY_2` | Group A |
|  | `KEY_3` | Group B |

Build arguments and environment variables set directly in a service or job will always override variables with the same name inherited from secret groups.

## Dynamic templating

You can use [dynamic templating](inject-secrets#dynamic-templating) to create new variables from variables previously defined in the secret group.

## Next steps

- [Manage global secrets: Create and manage team-level secrets and configuration data that can be referenced across multiple templates and projects.](/v1/application/secure/manage-global-secrets)
- [Reference global secrets: Reference global secrets in your template definitions to inject configuration and sensitive data.](/v1/application/secure/reference-global-secrets)
