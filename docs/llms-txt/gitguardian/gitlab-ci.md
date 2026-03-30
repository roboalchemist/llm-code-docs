# Source: https://docs.gitguardian.com/ggscout-docs/integrations/gitlab-ci.md

# GitLab Integration

> Guide to configuring ggscout to collect and inventory CI/CD variables from GitLab instances for secret monitoring.

# GitLab Integration

GitGuardian Scout (`ggscout`) can be configured to collect secrets and CI/CD variables from GitLab instances, enabling you to inventory and monitor secrets stored in your GitLab environment.

## Overview

The GitLab integration allows ggscout to:

- **Collect CI/CD variables** from GitLab projects
- **Inventory secrets** stored in GitLab CI/CD variable settings

## Prerequisites

Before configuring the GitLab integration, ensure you have:

1. **GitLab instance access** (GitLab.com or self-hosted GitLab)
2. **Personal Access Token** or **Project/Group Access Token** with appropriate permissions
3. **GitGuardian API token** with NHI permissions
4. **ggscout deployed** in your environment (Docker, Kubernetes, or local installation)

## Configuration

### 1. GitLab Access Token

Create a GitLab access token with the `read_api scope.

**For Personal Access Tokens:**
1. Go to GitLab â User Settings â Access Tokens
2. Create a new token with required scopes
3. Note the token value securely

**For Project Access Tokens:**
1. Go to Project â Settings â Access Tokens
2. Create a token with `Developer` or higher role
3. Select required scopes

### 2. Basic Configuration

Add the GitLab source to your ggscout configuration file:

```toml
[sources.gitlab]
type = "gitlabci"
token = "${GITLAB_CI_TOKEN}"     # GitLab access token
url = "https://gitlab.com/"      # Your GitLab instance URL
env = "production"               # Optional: Environment label
owner = "devops-team@example.com" # Optional: Owner of this source

[gitguardian]
api_token = "${GITGUARDIAN_API_KEY}"
endpoint = "https://api.gitguardian.com/v1"
```

### 3. Environment Variables

Set the required environment variables:

```bash
# GitLab access token
GITLAB_CI_TOKEN="glpat-xxxxxxxxxxxxxxxxxxxx"

# GitGuardian API token
GITGUARDIAN_API_KEY="your-gitguardian-api-key"
```

## Advanced Configuration

### Self-Hosted GitLab

For self-hosted GitLab instances:

```toml
[sources.gitlab-selfhosted]
type = "gitlabci"
token = "${GITLAB_CI_TOKEN}"
url = "https://gitlab.example.com/"  # Your GitLab instance URL
```

### Multiple GitLab Instances

You can configure multiple GitLab sources:

```toml
[sources.gitlab-saas]
type = "gitlabci"
token = "${GITLAB_SAAS_TOKEN}"       # Token for GitLab.com
url = "https://gitlab.com/"

[sources.gitlab-onprem]
type = "gitlabci"
token = "${GITLAB_ONPREM_TOKEN}"     # Token for self-hosted instance
url = "https://gitlab.internal.com/"
```

### Resource Filtering

You can filter which GitLab resources ggscout collects using include and exclude patterns:

```toml
[sources.gitlab-filtered]
type = "gitlabci"
token = "${GITLAB_CI_TOKEN}"
url = "https://gitlab.com/"
env = "production"
owner = "devops-team@example.com"

# Include only specific projects or groups
[[sources.gitlab-filtered.include]]
resource_ids = ["my-group/*", "important-project"]

# Exclude test or development projects
[[sources.gitlab-filtered.exclude]]
resource_ids = ["*/test-*", "dev-*", "sandbox/*"]
```

### Configuration Parameters

| Parameter | Description | Required | Example |
|-----------|-------------|----------|---------|
| `type` | Must be `"gitlabci"` | Yes | `"gitlabci"` |
| `token` | GitLab access token | Yes | `"${GITLAB_CI_TOKEN}"` |
| `url` | GitLab instance URL | Yes | `"https://gitlab.com/"` |
| `env` | Environment label for categorizing secrets | No | `"production"` |
| `owner` | Owner of this source (an email, usually of an employee or a team) | No | `"devops-team@example.com"` |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include | No | See filtering section |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude | No | See filtering section |

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.

## Running ggscout

### Using Docker

Create a `.env` file:
```bash
GITLAB_CI_TOKEN=glpat-xxxxxxxxxxxxxxxxxxxx
GITGUARDIAN_API_KEY=your-gitguardian-api-key
```

Then run ggscout to collect GitLab data:
```bash
docker run --rm -ti \
  -v ${PWD}/config.toml:/tmp/config.toml:ro \
  --env-file .env \
  ghcr.io/gitguardian/ggscout/chainguard:latest \
  fetch-and-send /tmp/config.toml
```

### Using Helm

Deploy ggscout with GitLab integration using the official Helm chart:

```bash
# Add the ggscout Helm repository
helm repo add ggscout https://gitguardian.github.io/ggscout-helm-charts
helm repo update

# Create a values file for GitLab integration
cat > gitlab-values.yaml << EOF
config:
  sources:
    gitlab:
      type: "gitlabci"
      token: "${GITLAB_CI_TOKEN}"
      url: "https://gitlab.com/"

  gitguardian:
    api_token: "${GITGUARDIAN_API_KEY}"
    endpoint: "https://api.gitguardian.com/v1"

secrets:
  GITLAB_CI_TOKEN: "glpat-xxxxxxxxxxxxxxxxxxxx"
  GITGUARDIAN_API_KEY: "your-gitguardian-api-key"

schedule: "0 */6 * * *"  # Run every 6 hours
EOF

# Install ggscout with GitLab integration
helm install ggscout-gitlab ggscout/ggscout -f gitlab-values.yaml
```

## Data Collected

The GitLab integration collects the following data:

- **Project Variables**: CI/CD variables defined at the project level
- **Variable Metadata**: Variable names, visibility settings, and environment scopes
- **Project Information**: Project names, paths, and accessibility

## Troubleshooting

### Debug Mode

Enable debug logging to troubleshoot issues:

```bash
# Using Docker
docker run --rm -ti \
  -v ${PWD}/config.toml:/tmp/config.toml:ro \
  --env-file .env \
  -e RUST_LOG=debug \
  ghcr.io/gitguardian/ggscout/chainguard:latest \
  fetch /tmp/config.toml --verbose -o /tmp/inventory.json
```
