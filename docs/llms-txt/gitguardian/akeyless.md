# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/akeyless.md

# Akeyless

> Guide to configuring ggscout to collect and monitor secrets from Akeyless using API key authentication.

# Akeyless Integration

GGScout supports integration with Akeyless to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- API key authentication
- Regular accessibility mode
- Cross-environment support

## Configuration

To configure GGScout to work with Akeyless, add the following configuration to your `ggscout.toml` file:

```toml
[sources.akeyless]
type = "akeyless"
api_url = "https://api.akeyless.io"
access_id = "${AKEYLESS_ACCESS_ID}"
access_key = "${AKEYLESS_ACCESS_KEY}"
accessibility = "regular"
auth_mode = "apikey"
fetch_all_versions = true
mode = "read"
env = "production"
owner = "devops-team@example.com"

[[sources.akeyless.include]]
resource_ids = ["/app/*", "/database/*", "/api-key"]

[[sources.akeyless.exclude]]
resource_ids = ["/test/*", "/temp/*", "/old-secret"]
```

### Configuration Parameters

| Parameter            | Description                                | Required | Default Value |
| -------------------- | ------------------------------------------ | -------- | ------------- |
| `type`               | Must be set to `"akeyless"`                | Yes      |             |
| `access_id`          | Your Akeyless access ID                    | Yes      |             |
| `access_key`         | Your Akeyless access key                   | Yes      |             |
| `accessibility`      | Accessibility mode (default: "regular")    | No       | "regular"   |
| `auth_mode`          | Authentication mode (e.g., "apikey")       | Yes      |             |
| `fetch_all_versions` | Whether to collect all versions of secrets | Yes      |             |
| `mode`               | Integration mode (one of:  "read", "write", "read/write") | No       | "read"      |
| `api_url`            | Akeyless API URL                           | No       | "https://api.akeyless.io" |
| `env`                | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No       |             |
| `owner`              | Owner of this source (an email, usually of an employee or a team) | No       |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

### Authentication

GGScout supports authentication with Akeyless through:

1. **API Key**: Using access ID and access key
2. **Environment Variables**: Using standard Akeyless environment variables

### Environment Variables

- `AKEYLESS_ACCESS_ID`: Your Akeyless access ID
- `AKEYLESS_ACCESS_KEY`: Your Akeyless access key

## Best Practices

1. Use environment variables for sensitive credentials
2. Follow the principle of least privilege for access policies
3. Enable `fetch_all_versions` to track changes in your secrets over time
4. Regularly rotate access keys
5. Use separate access IDs for different environments
6. Implement proper secret rotation policies
7. Monitor access logs for suspicious activity
