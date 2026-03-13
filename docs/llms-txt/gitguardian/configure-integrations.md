# Source: https://docs.gitguardian.com/ggscout-docs/configure-integrations.md

# Configure integrations

> How to configure ggscout integration sources in the TOML configuration file, including modes, environment variables, and filtering.

# Configure integrations

ggscout integrates with various secrets managers, CI/CD systems, and infrastructure components to collect and monitor secrets. This page covers how to configure and use integrations for secret discovery and monitoring.

## Integration Modes

Sources can be configured with different operational modes:

- **`read`** - Only collect data from the source (default)
- **`write`** - Only write data to the source
- **`read/write`** - Both collect data and write to the source

```toml
[sources.my-source]
type = "source_type"
mode = "read/write"  # Supports both operations
```

## Configuration File

ggscout configuration file uses the TOML format to describe:

- How ggscout will communicate with GitGuardian platform
- How to access the different secrets managers to collect secrets

**Configuration example:**

```yaml
[gitguardian]
# SaaS US
endpoint = "https://api.gitguardian.com/v1"
# SaaS EU
# endpoint = "https://api.eu1.gitguardian.com/v1"
# Self-hosted
# endpoint = "https://my-gg-instance.com/exposed/v1"
api_token = "${GITGUARDIAN_API_KEY}"

[sources.my-hashicorp-vault]
# This lets ggscout know what source to contact
type = "hashicorpvault"
# And this lets ggscout know how to contact it
vault_address = "${HASHICORP_VAULT_ADDRESS}"
auth.auth_mode = "token"
auth.token = "${HASHICORP_VAULT_TOKEN}"

# Many vaults support secret versioning. Set this to false if you only
# want to collect the latest version of the vault secrets
fetch_all_versions = true
# Allow ggscout instance to read from and write to that vault
mode = "read/write" # "read" and "write" are other possible values
# Will help assess policy breaches and their severity
env = "staging"
# Optional: specify the owner of this source
owner = "devops-team@example.com"

# Configure another vault to collect here
# [sources.my-other-vault]
# type = "gcpsecretmanager"
```

The config file supports reading environment variables (`"${GITGUARDIAN_API_KEY}"`) instead of raw values. 
You can set these variables in a `.env` file:
```bash
GITGUARDIAN_API_KEY=<your-gitguardian-api-key>

HASHICORP_VAULT_ADDRESS=<your-vault-url>
HASHICORP_VAULT_TOKEN=<your-vault-token>
```

Please refer to **[Secrets Managers](./integrations/secret-managers)** section to properly configure the collection of secrets.

## Supported Integration Types

ggscout supports multiple integration types across different categories. The table below shows all available integrations and their capabilities:

| Integration Type | Integration Name | Type Identifier | Write Support |
|------------------|------------------|-----------------|---------------|
| **Secrets Managers** | HashiCorp Vault | `hashicorpvault` | â Yes |
| | AWS Secrets Manager | `awssecretsmanager` | â Yes |
| | CyberArk Secrets Manager SaaS | `cyberarksaas` | â Yes |
| | CyberArk Secrets Manager Self-Hosted | `cyberarkselfhosted` | â Yes |
| | Akeyless | `akeyless` | â Yes |
| | Delinea Secret Server | `delineasecretserver` | â Yes |
| | Azure Key Vault | `azurekeyvault` | â No |
| | Google Secret Manager | `gcpsecretmanager` | â No |
| **CI/CD Systems** | GitLab CI | `gitlabci` | â No |
| **Infrastructure** | Kubernetes | `k8s` | â No |

:::info
Integrations that don't support writing can still be used for secret discovery and monitoring with the `fetch-and-send` command. Only integrations with write support can be used with the `sync-secrets` command.

Refer to the **[Secret synchronization](./sync-secrets)** section for more details on `sync-secrets`.
:::

## Common Configuration Parameters

All secrets manager integrations support the following common parameters in addition to their specific configuration:

### Environment Categorization

- **`env`**: Environment label for categorizing secrets (e.g., "production", "staging", "development"). This helps organize and filter secrets by their intended environment.

### Source Ownership

- **`owner`**: Owner of this source (an email, usually of an employee or a team). This field is optional and helps identify who is responsible for managing the source.

### Resource Filtering

- **`[[sources.<name>.include]]`**: Table of resource_id patterns to include. Only secrets matching these patterns will be collected.
- **`[[sources.<name>.exclude]]`**: Table of resource_id patterns to exclude. Secrets matching these patterns will be ignored.

Each `include` or `exclude` table must have a `resource_ids` array. You can specify multiple `include` or `exclude` tables for different sets of patterns.

Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

### Example Configuration

```toml
[sources.my-vault]
type = "hashicorpvault"
vault_address = "${HASHICORP_VAULT_ADDRESS}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.my-vault.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.my-vault.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]

auth.auth_mode = "token"
auth.token = "${HASHICORP_VAULT_TOKEN}"
```

In this example:
- **Prefix patterns**: `"app/*"` and `"database/*"` match all secrets starting with those prefixes
- **Exact matches**: `"api-key"` matches only the exact secret with that name
