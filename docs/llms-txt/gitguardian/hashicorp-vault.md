# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/hashicorp-vault.md

# HashiCorp Vault

> Guide to configuring ggscout to collect and monitor secrets from HashiCorp Vault, including KV1/KV2 engines, namespace filtering, and HCD support.

# HashiCorp Vault Integration

GGScout supports integration with HashiCorp Vault to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- KV1 and KV2 secret engines
- Multiple secret versions collection
- Path-based filtering
- Token-based authentication
- **HashiCorp Vault Enterprise namespaces**
- **HashiCorp Cloud Dedicated (HCD) support**

## HashiCorp Cloud Dedicated Support

GGScout fully supports HashiCorp Cloud Dedicated (HCD) environments. When using HCD, namespaces are automatically included as part of the exported `resource_id`, following the Vault API pattern described in the [HashiCorp documentation](https://developer.hashicorp.com/vault/docs/enterprise/namespaces#vault-api-and-namespaces).

## Namespace Filtering

### Restricting Namespace Access

With HCD and Vault Enterprise, you can limit which namespaces ggscout accesses using the `namespaces` configuration parameter:

```toml
[sources.vault]
type = "hashicorpvault"
vault_address = "${VAULT_ADDR}"
fetch_all_versions = true
namespaces = ["admin", "prod", "shared"]  # Only fetch from these namespaces
```

:::info
If the `namespaces` parameter is not specified, ggscout will fetch secrets from **all accessible namespaces**. Use this parameter to limit the scope of secret collection and improve performance.
:::

### Resource-Level Filtering

You can also filter secrets by namespace directly in your include/exclude patterns. The namespace becomes part of the resource path, allowing for precise filtering:

```toml
# Include all secrets from the 'admin' namespace, 'kv' mount, under 'my_app' path
[[sources.vault.include]]
resource_ids = ["admin/kv/my_app/*"]

# Include secrets from multiple namespaces
[[sources.vault.include]]
resource_ids = ["admin/kv/*", "dev/secrets/*", "prod/database/*"]

# Exclude test secrets from all namespaces
[[sources.vault.exclude]]
resource_ids = ["*/test/*", "*/temp/*"]
```

The filtering works seamlessly with the namespace structure, where the resource_id format follows: `namespace/mount/path`

## Configuration

To configure GGScout to work with HashiCorp Vault, add the following configuration to your `ggscout.toml` file:

### Token-based Authentication

```toml
[sources.vault]
type = "hashicorpvault"
vault_address = "${VAULT_ADDR}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "token"
auth.token = "${VAULT_TOKEN}"

# Optional: Limit to specific namespaces (Enterprise/HCD only)
namespaces = ["admin", "prod", "shared"]

# Standard filtering (self-hosted Vault)
[[sources.vault.include]]
resource_ids = ["app/*", "database/*", "api-key"]

# Namespace-aware filtering (HCD/Enterprise)
[[sources.vault.include]]
resource_ids = ["admin/kv/my_app/*", "prod/secrets/database/*"]

[[sources.vault.exclude]]
resource_ids = ["*/test/*", "*/temp/*", "dev/old-secret"]
```

### HashiCorp Cloud Dedicated Configuration

For HashiCorp Cloud Dedicated environments, the configuration is identical, but the filtering automatically works with namespaces:

```toml
[sources.vault_hcd]
type = "hashicorpvault"
vault_address = "${HCD_VAULT_ADDR}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "token"
auth.token = "${HCD_VAULT_TOKEN}"

# Optional: Limit to specific namespaces
namespaces = ["admin", "prod", "shared"]

# Namespace-specific filtering
[[sources.vault_hcd.include]]
resource_ids = [
    "admin/kv/my_app/*",           # All secrets in admin namespace, kv mount, my_app path
    "prod/database/credentials/*", # Database credentials in prod namespace
    "shared/api-keys/*"            # Shared API keys across teams
]

[[sources.vault_hcd.exclude]]
resource_ids = [
    "*/test/*",                    # Exclude test secrets from all namespaces
    "dev/temp/*",                  # Exclude temporary secrets in dev namespace
    "*/legacy/*"                   # Exclude legacy secrets from all namespaces
]
```

### Kubernetes Authentication

```toml
[sources.vault]
type = "hashicorpvault"
vault_address = "${VAULT_ADDR}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "k8s"
auth.k8s.service_account = "${KUBERNETES_SERVICE_ACCOUNT}"
auth.k8s.namespace = "${KUBERNETES_NAMESPACE}"
auth.k8s.role = "${KUBERNETES_ROLE}"

[[sources.vault.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.vault.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### Configuration Parameters

| Parameter            | Description                                 | Required | Default Value |
| -------------------- | ------------------------------------------- | -------- | ------------- |
| `type`               | Must be set to `"hashicorpvault"`           | Yes      |             |
| `vault_address`      | The address of your Vault server            | Yes      |             |
| `fetch_all_versions` | Whether to collect all versions of secrets  | Yes      |             |
| `namespaces`         | List of Vault namespaces to fetch from (Enterprise/HCD only). If not specified, fetches from all accessible namespaces | No       | All accessible namespaces |
| `auth.auth_mode`     | Authentication mode (e.g., "token", "k8s") | Yes      |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write") | No | "read" |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team) | No       |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

With additional parameters depending on the chosen authentication mode:

For Token-based Authentication:

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `auth.token` | The Vault authentication token | Yes |             |

For Kubernetes Authentication:

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `auth.k8s.service_account` | The Kubernetes service account | Yes |             |
| `auth.k8s.namespace` | The Kubernetes namespace | Yes |             |
| `auth.k8s.role` | The Kubernetes role | Yes |             |

### Environment Variables

- `VAULT_ADDR`: The address of your Vault server (e.g., `http://localhost:8200`)

For Token-based Authentication:
- `VAULT_TOKEN`: Your Vault authentication token

For Kubernetes Authentication:
- `KUBERNETES_SERVICE_ACCOUNT`: The Kubernetes service account
- `KUBERNETES_NAMESPACE`: The Kubernetes namespace
- `KUBERNETES_ROLE`: The Kubernetes role

## Required Vault Policies

GGScout requires specific permissions in HashiCorp Vault to collect secrets. The token used for authentication must have the following permissions:

### For KV2 Secret Engine

```hcl
path "secret/data/*" {
  capabilities = ["read", "list"]
}

path "secret/metadata/*" {
  capabilities = ["read", "list"]
}
```

These policies allow GGScout to:

1. List all secrets in the specified path(s)
2. Read the content of each secret
3. Access metadata about the secrets

### For KV1 Secret Engine

```hcl
path "secret/*" {
  capabilities = ["read", "list"]
}
```

This policy allows GGScout to:

1. List all secrets in the specified path(s)
2. Read the content of each secret

### For HashiCorp Cloud Dedicated & Enterprise (with Namespaces)

When using HCD or Vault Enterprise with namespaces, policies are scoped to the namespace where they are created. Each namespace has its own policy space, and you create policies within specific namespaces rather than using wildcards to match across namespaces.

For namespace-specific policies, you would create policies within each namespace:

```hcl
# Policy created within the 'admin' namespace for KV2 secrets
path "kv/data/*" {
  capabilities = ["read", "list"]
}

path "kv/metadata/*" {
  capabilities = ["read", "list"]
}

# Policy for specific paths within a namespace using the + wildcard
path "kv/data/my_app/+/config" {
  capabilities = ["read", "list"]
}

path "kv/metadata/my_app/+/config" {
  capabilities = ["read", "list"]
}
```

:::info
When working with namespaces, policies are created and managed within each namespace's scope. The `+` wildcard character can be used within path segments as documented in the [HashiCorp Vault Policies documentation](https://developer.hashicorp.com/vault/docs/concepts/policies), but cross-namespace policy wildcards are not supported. For more information about namespaces, see the [HashiCorp Vault Namespace documentation](https://developer.hashicorp.com/vault/docs/enterprise/namespaces).
:::

## Best Practices

1. **Use environment variables** for sensitive values like `auth.token`
2. **Leverage namespace filtering** in HCD/Enterprise environments to precisely control which secrets are collected
3. **Consider using path restrictions** to limit the scope of secret collection
4. **Enable `fetch_all_versions`** to track changes in your secrets over time
5. **Use a dedicated service account** with minimal required permissions
6. **For HCD environments**, take advantage of the automatic namespace inclusion in resource_ids for fine-grained filtering
7. **Use wildcard patterns** like `*/test/*` to exclude test secrets across all namespaces
