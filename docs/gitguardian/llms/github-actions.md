# Source: https://docs.gitguardian.com/ggshield-docs/integrations/cicd-integrations/github-actions.md

# Source: https://docs.gitguardian.com/ggscout-docs/integrations/github-actions.md

# GitHub Actions Integration

> Guide to configuring ggscout to inventory GitHub Actions secrets for NHI governance.

# GitHub Actions Integration

GitGuardian Scout (`ggscout`) can inventory secrets stored in GitHub Actions â at the organization, repository, and environment level â enabling you to discover and monitor Non-Human Identities across your GitHub CI/CD infrastructure.

## Overview

Unlike other ggscout integrations, the GitHub Actions fetcher runs **inside a GitHub Actions workflow**. It reads secrets directly from the runner environment, requiring zero credentials for basic operation. For full visibility, we recommend configuring an API token to enrich each secret with metadata such as scope, ownership, and timestamps.

The integration supports both **github.com** and **GitHub Enterprise Server** (GHES) instances.

Key capabilities:

- **Inventory all GitHub Actions secrets** available to a workflow (org, repo, and environment-level)
- **Enrich with metadata** (scope, visibility, environment, owner, timestamps) when an API token is provided

## Prerequisites

Before configuring the GitHub Actions integration, ensure you have:

1. **A GitHub repository** with GitHub Actions enabled (github.com or GHES)
2. **GitGuardian API token** with NHI permissions
3. **(Recommended)** A GitHub API token for metadata enrichment â see [Metadata Enrichment](#metadata-enrichment)

## Workflow Setup

ggscout is embedded as a step in a GitHub Actions workflow. Secrets are relatively static and do not change on every commit, so we recommend running it on a **nightly schedule** to avoid unnecessary workflow minutes.

### Deployment Scope

GitHub Actions secrets exist at three levels: **organization**, **repository**, and **environment**. A single ggscout workflow can see all secrets available to its job, but repo-level and environment-level secrets are only visible from within that specific repository's workflow.

To get full coverage:

1. **Deploy on at least one repository** â this captures all organization-level secrets shared across the org.
2. **Deploy on each repository with secrets of interest** â repo-level and environment-level secrets are only accessible from within the repository where they are defined.

### Workflow Examples

Create a dedicated workflow file (e.g., `.github/workflows/ggscout-nhi.yml`).

#### Option A: Docker Image (Recommended)

```yaml
name: NHI Inventory with ggscout
on:
  schedule:
    - cron: '0 2 * * *'  # Run nightly at 2:00 AM UTC
  workflow_dispatch:        # Allow manual runs

jobs:
  inventory:
    runs-on: ubuntu-latest
    container:
      image: ghcr.io/gitguardian/ggscout/chainguard:latest
    steps:
      - name: Create ggscout config
        run: |
          cat > /tmp/config.toml << 'EOF'
          [sources.github-actions]
          type = "githubactions"
          env = "production"

          [gitguardian]
          api_token = "${GITGUARDIAN_API_KEY}"
          endpoint = "https://api.gitguardian.com/v1"
          EOF

      - name: Collect secrets with ggscout
        env:
          GGSCOUT_GITHUB_ACTION_SECRETS: ${{ toJSON(secrets) }}
          GGSCOUT_GITHUB_ACTION_CONTEXT: ${{ toJSON(github) }}
          GGSCOUT_GITHUB_API_TOKEN: ${{ secrets.GGSCOUT_API_TOKEN }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}
        run: ggscout fetch-and-send /tmp/config.toml
```

#### Option B: Binary Download

If you prefer not to use Docker:

```yaml
name: NHI Inventory with ggscout
on:
  schedule:
    - cron: '0 2 * * *'  # Run nightly at 2:00 AM UTC
  workflow_dispatch:        # Allow manual runs

jobs:
  inventory:
    runs-on: ubuntu-latest
    steps:
      - name: Download ggscout
        run: |
          wget https://ggscout-repository.gitguardian.com/ggscout/latest/x86_64-unknown-linux-gnu/ggscout
          chmod +x ggscout

      - name: Create ggscout config
        run: |
          cat > /tmp/config.toml << 'EOF'
          [sources.github-actions]
          type = "githubactions"
          env = "production"

          [gitguardian]
          api_token = "${GITGUARDIAN_API_KEY}"
          endpoint = "https://api.gitguardian.com/v1"
          EOF

      - name: Collect secrets with ggscout
        env:
          GGSCOUT_GITHUB_ACTION_SECRETS: ${{ toJSON(secrets) }}
          GGSCOUT_GITHUB_ACTION_CONTEXT: ${{ toJSON(github) }}
          GGSCOUT_GITHUB_API_TOKEN: ${{ secrets.GGSCOUT_API_TOKEN }}
          GITGUARDIAN_API_KEY: ${{ secrets.GITGUARDIAN_API_KEY }}
        run: ./ggscout fetch-and-send /tmp/config.toml
```

### Environment Variables

The workflow must inject the following environment variables on the ggscout step. These variables are how ggscout discovers which secrets exist and where they come from â without them, ggscout has no visibility into your GitHub Actions environment.

| Variable | Description | Required |
|----------|-------------|----------|
| `GGSCOUT_GITHUB_ACTION_SECRETS` | `${{ toJSON(secrets) }}` â JSON object of all secrets available to the job. This is ggscout's primary input for discovering secrets. | Yes |
| `GGSCOUT_GITHUB_ACTION_CONTEXT` | `${{ toJSON(github) }}` â GitHub context providing source identity (server URL, repository owner, repository name). | Yes |
| `GGSCOUT_GITHUB_API_TOKEN` | GitHub API token for metadata enrichment (see [Metadata Enrichment](#metadata-enrichment)). | No (recommended) |
| `GITGUARDIAN_API_KEY` | GitGuardian API token with NHI permissions. | Yes |

## Configuration

The ggscout TOML configuration for GitHub Actions is minimal â the source identity (hostname, org, repo) is derived automatically from the GitHub runner context.

In the workflow examples above, the configuration is created inline during the workflow run. Alternatively, you can commit a `config.toml` file to your repository and reference it directly (using `actions/checkout` to make it available):

```toml
[sources.github-actions]
type = "githubactions"
env = "production"               # Optional: Environment label
owner = "devops-team@example.com" # Optional: Owner of this source
token = "${GGSCOUT_GITHUB_API_TOKEN}" # Optional: GitHub API token for metadata enrichment

[gitguardian]
api_token = "${GITGUARDIAN_API_KEY}"
endpoint = "https://api.gitguardian.com/v1"
```

### Configuration Parameters

| Parameter | Description | Required | Example |
|-----------|-------------|----------|---------|
| `type` | Must be `"githubactions"` | Yes | `"githubactions"` |
| `env` | Environment label for categorizing secrets | No | `"production"` |
| `owner` | Owner of this source (an email, usually of an employee or a team) | No | `"devops-team@example.com"` |
| `token` | GitHub API token (fallback if `GGSCOUT_GITHUB_API_TOKEN` env var is not set) | No | `"ghp_xxxx"` |

## Metadata Enrichment

By default, ggscout inventories secret names and values from the runner environment. When a GitHub API token is provided (via `GGSCOUT_GITHUB_API_TOKEN` or the `token` config field), ggscout also calls the GitHub REST API to enrich each secret with additional metadata:

- **`created_at`** and **`updated_at`** timestamps
- **`scope`** tag â `"org"`, `"repo"`, or `"env"`, indicating where the secret is defined
- **`visibility`** tag â for org-level secrets: `"all"`, `"private"`, or `"selected"`
- **`environment`** tag â for environment-level secrets: the environment name (e.g., `"production"`)
- **`owner_email`** tag â from the GitHub user profile of the repository/org owner

### Required Token Permissions

| Token Type | Permissions | Scope |
|------------|-------------|-------|
| **Fine-grained PAT** | Repository: **Secrets: Read** + **Environments: Read**. Organization: **Secrets: Read** | Repo + environment + org secrets |
| **Classic PAT** | `repo` + `admin:org` | Repo + environment + org secrets |
| **GitHub App** | `secrets:read` + `environments:read` + `organization_secrets:read` | Repo + environment + org secrets |

Missing scopes result in `403 Forbidden` warnings in logs. The fetcher continues without the corresponding metadata (graceful degradation).

### Rate Limit Considerations

When metadata enrichment is enabled, ggscout makes approximately 5â10 API calls per run (listing org, repo, and environment-level secrets, plus owner info). The rate limits depend on the token type:

| Token Type | Rate Limit |
|------------|------------|
| **GITHUB_TOKEN** | 1,000 req/hr per repository (15,000 for Enterprise Cloud) |
| **Personal Access Token** | 5,000 req/hr shared across all uses (15,000 for Enterprise Cloud) |
| **GitHub App** | 5,000â15,000 req/hr depending on installation size |

**Important:** PAT rate limits are **shared across all uses by that user**. If multiple repositories run ggscout with the same PAT concurrently, the combined API calls can exhaust the quota.

**Recommendation:** Use a **GitHub App token** or a **dedicated service account PAT** rather than a personal PAT. Personal PATs share their rate limit quota with all other API activity by that user, which can lead to unexpected throttling. A GitHub App token provides a dedicated rate limit pool per installation and avoids long-lived credentials.

## GitHub Enterprise Server

The integration automatically supports GHES instances. The hostname and API URL are derived from the `github` context provided by the runner â no additional configuration is needed.

The `server_url` field from the GitHub context is parsed to determine the hostname (e.g., `github.example.com` instead of `github.com`), and `api_url` is used for REST API calls when metadata enrichment is enabled.

## Data Collected

The GitHub Actions integration collects the following data:

- **All user-defined secrets** available to the workflow job at runtime, including org-level, repo-level, and environment-level secrets
- **Secret metadata** (when API token is provided): timestamps, scope, visibility, environment, and owner

**Excluded:** `GITHUB_TOKEN` â this is an ephemeral token automatically generated by GitHub for every workflow run. It expires when the job ends or after 24 hours and is not a user-managed NHI.

**Note on environment secret shadowing:** GitHub Actions environments (e.g., `production`, `staging`) can define secrets that override repo or org secrets with the same name. The `secrets` context presents all scopes as a flat object, so the origin is not visible from within the workflow. When metadata enrichment is enabled, ggscout queries all environments and applies environment > repo > org precedence to correctly attribute the `scope` and `environment` tags.

## Troubleshooting

### No Metadata Appearing

- Verify that `GGSCOUT_GITHUB_API_TOKEN` is set (or `token` is configured in the TOML file)
- Check that the token has the required permissions (see [Required Token Permissions](#required-token-permissions))
- Look for `403 Forbidden` warnings in the workflow logs â this indicates missing scopes

### Empty Inventory

- Ensure `GGSCOUT_GITHUB_ACTION_SECRETS` is set to `${{ toJSON(secrets) }}` in the workflow step
- Ensure `GGSCOUT_GITHUB_ACTION_CONTEXT` is set to `${{ toJSON(github) }}`
- Verify that the repository has GitHub Actions secrets configured

### Debug Mode

Enable verbose logging to troubleshoot issues:

```yaml
- name: Collect secrets with ggscout (debug)
  env:
    GGSCOUT_GITHUB_ACTION_SECRETS: ${{ toJSON(secrets) }}
    GGSCOUT_GITHUB_ACTION_CONTEXT: ${{ toJSON(github) }}
    RUST_LOG: debug
  run: ggscout fetch /tmp/config.toml --verbose -o inventory.json

- name: View inventory.json
  run: cat inventory.json | python3 -m json.tool
```
