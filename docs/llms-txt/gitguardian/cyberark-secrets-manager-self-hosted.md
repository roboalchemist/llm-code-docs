# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/cyberark-secrets-manager-self-hosted.md

# CyberArk Secrets Manager Self-Hosted

> Configure ggscout to collect and monitor secrets from CyberArk Secrets Manager Self-Hosted (Conjur) with user and API authentication.

# CyberArk Secrets Manager Self-Hosted Integration

ggscout supports integration with CyberArk Secrets Manager Self-Hosted (Conjur Enterprise and OSS) to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- User and API authentication
- Self-hosted server configuration
- Account-based access

## Configuration

The following table lists the available configuration options for ggscout when integrating with CyberArk Secrets Manager Self-Hosted:

| Parameter              | Description                                                                               | Required | Default Value |
|------------------------|-------------------------------------------------------------------------------------------|----------|---------------|
| `type`                 | Must be set to `"cyberarkselfhosted"`                                                     | Yes      |               |
| `server_url`           | The URL of your self-hosted CyberArk Secrets Manager server                               | Yes      |               |
| `account`              | The Conjur account name                                                                   | Yes      |               |
| `auth_mode`            | Authentication mode (one of: "user", "api")                                               | Yes      |               |
| `fetch_all_versions`   | Whether to collect all versions of secrets                                                | Yes      |               |
| `accept_invalid_certs` | Accept invalid/self-signed certificates (for development only)                            | No       | `false`       |
| `mode`                 | Integration mode (one of: "read", "write", "read/write")                                  | No       | "read"        |
| `env`                  | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |               |
| `owner`                | Owner of this source (an email, usually of an employee or a team)                         | No       |               |
| `include`              | List of path patterns to include in secret collection                                     | No       |               |
| `exclude`              | List of path patterns to exclude from secret collection                                   | No       |               |

With additional parameters depending on the chosen authentication mode:

For User Authentication:

| Parameter  | Description                      | Required | Default Value |
|------------|----------------------------------|----------|---------------|
| `username` | Username for authentication      | Yes      |               |
| `password` | Password for authentication      | Yes      |               |

For API Authentication:

| Parameter | Description                                             | Required | Default Value |
|-----------|---------------------------------------------------------|----------|---------------|
| `login`   | Login identity (including `host/` prefix for workloads) | Yes      |               |
| `api_key` | API key for authentication                              | Yes      |               |

## Authentication

ggscout supports two authentication methods for CyberArk Secrets Manager Self-Hosted:

### User Authentication

Use this method when authenticating with a username and password:

```toml
[sources.cyberarkselfhosted]
type = "cyberarkselfhosted"
server_url = "https://conjur.example.com"
account = "myorg"
auth_mode = "user"
username = "${CONJUR_USERNAME}"
password = "${CONJUR_PASSWORD}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.cyberarkselfhosted.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.cyberarkselfhosted.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

### API Authentication

Use this method when authenticating with an API key and login identity. This is the recommended approach for workloads:

```toml
[sources.cyberarkselfhosted]
type = "cyberarkselfhosted"
server_url = "https://conjur.example.com"
account = "myorg"
auth_mode = "api"
login = "${CONJUR_LOGIN}"
api_key = "${CONJUR_API_KEY}"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.cyberarkselfhosted.include]]
resource_ids = ["app/*", "database/*", "api-key"]

[[sources.cyberarkselfhosted.exclude]]
resource_ids = ["test/*", "temp/*", "old-secret"]
```

:::tip
For host/workload authentication, the `login` parameter should include the `host/` prefix followed by the host identity path. For example: `host/myapp/production/ggscout`.
:::

## Self-Signed Certificates

If your self-hosted CyberArk Secrets Manager uses self-signed certificates, you can disable certificate verification for development environments:

```toml
[sources.cyberarkselfhosted]
type = "cyberarkselfhosted"
server_url = "https://conjur.example.com"
account = "myorg"
auth_mode = "api"
login = "${CONJUR_LOGIN}"
api_key = "${CONJUR_API_KEY}"
fetch_all_versions = true
accept_invalid_certs = true  # Only for development!
```

:::warning
Setting `accept_invalid_certs = true` disables TLS certificate verification. This should **only** be used in development environments, never in production.
:::

## Include and Exclude Patterns

You can control which secrets are collected using include and exclude patterns:

```toml
[sources.cyberarkselfhosted]
type = "cyberarkselfhosted"
server_url = "https://conjur.example.com"
account = "myorg"
auth_mode = "api"
login = "${CONJUR_LOGIN}"
api_key = "${CONJUR_API_KEY}"
fetch_all_versions = true

# Only collect secrets matching these patterns
[[sources.cyberarkselfhosted.include]]
resource_ids = ["production/*", "shared/*"]

# Exclude secrets matching these patterns
[[sources.cyberarkselfhosted.exclude]]
resource_ids = ["test-*", "temp-*"]
```

## Write Mode

To enable secret synchronization (writing secrets back to CyberArk Secrets Manager Self-Hosted), set the mode to `read/write` or `write`:

```toml
[sources.cyberarkselfhosted]
type = "cyberarkselfhosted"
server_url = "https://conjur.example.com"
account = "myorg"
auth_mode = "api"
login = "${CONJUR_LOGIN}"
api_key = "${CONJUR_API_KEY}"
fetch_all_versions = true
mode = "read/write"
```

:::note
The identity must have `update` privileges on the target variables to write secrets.
:::
