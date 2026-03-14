# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/azure-key-vault.md

# Azure Key Vault

> Guide to configuring ggscout to collect and monitor secrets from Azure Key Vault, including authentication methods and filtering options.

# Azure Key Vault Integration

GGScout supports integration with Azure Key Vault to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- DefaultAzureCredential authentication
- Managed Identity authentication
- Service Principal authentication
- Cross-tenant access

## Configuration

To configure GGScout to work with Azure Key Vault, add the following configuration to your `ggscout.toml` file:

```toml
[sources.azure-source-playground]
type = "azurekeyvault"
fetch_all_versions = true
subscription_id = "${AZURE_SUBSCRIPTION_ID}"
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.azure-source-playground.include]]
resource_ids = ["app-*", "database-*", "api-key"]

[[sources.azure-source-playground.exclude]]
resource_ids = ["test-*", "temp-*", "old-secret"]
```

### Configuration Parameters

| Parameter            | Description                                | Required | Default Value |
| -------------------- | ------------------------------------------ | -------- | ------------- |
| `type`               | Must be set to `"azurekeyvault"`           | Yes      |             |
| `fetch_all_versions` | Whether to collect all versions of secrets | Yes      |             |
| `subscription_id`    | Your Azure subscription ID                 | Yes      |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write") | No       | "read"      |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team) | No       |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

### Authentication

GGScout uses the DefaultAzureCredential for authentication, which attempts to authenticate using the following methods in order:

1. Environment variables
2. Workload Identity
3. Managed Identity
4. Shared Token Cache
5. Visual Studio
6. Azure CLI
7. Azure PowerShell
8. Azure Developer CLI
9. Interactive Browser

:::note
Authentication methods cannot be directly configured in the TOML file. Instead, you must provide the necessary environment variables for your chosen authentication method.
:::

### Environment Variables

For Service Principal authentication, you must set the following environment variables:

- `AZURE_SUBSCRIPTION_ID`: Your Azure subscription ID
- `AZURE_TENANT_ID`: Your Azure tenant ID
- `AZURE_CLIENT_ID`: Your service principal client ID
- `AZURE_CLIENT_SECRET`: Your service principal client secret

For other authentication methods, refer to the [Azure Identity documentation](https://learn.microsoft.com/en-us/dotnet/api/azure.identity.defaultazurecredential?view=azure-dotnet) for the required environment variables.

## Required Azure Permissions

To fetch secrets from Azure Key Vault, the identity used by GGScout (whether it's a Managed Identity, Service Principal, or user account) must have the appropriate permissions assigned.

### RBAC Permissions

The identity must have at least one of the following built-in roles assigned to the Key Vault:

1. **Key Vault Secrets User** (`Key Vault Secrets User`): Allows reading secret values
2. **Key Vault Secrets Officer** (`Key Vault Secrets Officer`): Allows reading and managing secrets
3. **Key Vault Administrator** (`Key Vault Administrator`): Full access to Key Vault

For more granular control, you can create a custom role with the following permissions:

```json
{
  "Name": "GGScout Key Vault Reader",
  "Description": "Allows GGScout to read secrets from Key Vault",
  "Actions": [
    "Microsoft.KeyVault/vaults/secrets/read",
    "Microsoft.KeyVault/vaults/secrets/versions/read",
    "Microsoft.KeyVault/vaults/secrets/list"
  ],
  "NotActions": [],
  "DataActions": [],
  "NotDataActions": [],
  "AssignableScopes": [
    "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.KeyVault/vaults/{vault-name}"
  ]
}
```

### Access Policy (Legacy)

If your Key Vault is using the older Access Policy model instead of RBAC, the identity must have the following permissions:

- **Get** and **List** permissions for secrets

:::tip
For production environments, it's recommended to use RBAC for Key Vault access management as it provides more granular control and better integration with Azure's identity management.
:::

## Best Practices

1. Use Managed Identity when running on Azure infrastructure
2. Follow the principle of least privilege for role assignments
3. Enable `fetch_all_versions` to track changes in your secrets over time
4. Regularly rotate service principal credentials
5. Use separate Key Vaults for different environments
