# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/delinea-secret-server.md

# Delinea Secret Server

> Guide to configuring ggscout to collect and monitor secrets from Delinea Secret Server using OAuth authentication.

# Delinea Secret Server Integration

GGScout supports integration with Delinea Secret Server to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- OAuth authentication
- Tenant-specific configuration
- Cross-environment support

## Configuration

To configure GGScout to work with Delinea Secret Server, add the following configuration to your `ggscout.toml` file:

```toml
[sources.delinea]
type = "delineasecretserver"
auth_mode = "oauth"
client_id = "${DELINEA_CLIENT_ID}"
client_secret = "${DELINEA_CLIENT_SECRET}"
fetch_all_versions = true
tenant = "${DELINEA_TENANT}"
tld = "com"
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.delinea.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.delinea.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### Configuration Parameters

| Parameter            | Description                                | Required | Default Value |
| -------------------- | ------------------------------------------ | -------- | ------------- |
| `type`               | Must be set to `"delineasecretserver"`     | Yes      |             |
| `auth_mode`          | Authentication mode (e.g., "oauth")        | Yes      |             |
| `client_id`          | The client ID for OAuth authentication     | Yes      |             |
| `client_secret`      | The client secret for OAuth authentication | Yes      |             |
| `tenant`             | Your Delinea tenant ID                     | Yes      |             |
| `tld`                | Top-level domain (e.g., "com")             | No       |    "com"    |
| `fetch_all_versions` | Whether to collect all versions of secrets | Yes      |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write") | No | "read" |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team) | No       |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

### Authentication

GGScout supports authentication with Delinea Secret Server through:

1. **OAuth**: Using client ID and secret
2. **Environment Variables**: Using standard Delinea environment variables

### Environment Variables

- `DELINEA_CLIENT_ID`: Your Delinea client ID
- `DELINEA_CLIENT_SECRET`: Your Delinea client secret
- `DELINEA_TENANT`: Your Delinea tenant ID

## Best Practices

1. Use environment variables for sensitive credentials
2. Follow the principle of least privilege for access policies
3. Enable `fetch_all_versions` to track changes in your secrets over time
4. Regularly rotate client secrets
5. Use separate tenants for different environments
6. Implement proper secret rotation policies
7. Monitor access logs for suspicious activity
8. Use strong password policies for secrets
