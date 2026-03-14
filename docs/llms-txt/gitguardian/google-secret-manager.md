# Source: https://docs.gitguardian.com/ggscout-docs/integrations/secret-managers/google-secret-manager.md

# Google Secret Manager

> Configure ggscout to collect and monitor secrets from Google Secret Manager with service account and Workload Identity authentication.

# Google Secret Manager Integration

GGScout supports integration with Google Secret Manager to collect and monitor your secrets. This guide will help you set up and configure the integration.

## Supported Features

- Multiple secret versions collection
- Multiple authentication methods (service account, Kubernetes Workload Identity, Application Default Credentials)
- Native GCP infrastructure support (automatic metadata endpoint detection)
- Project-specific secret collection
- IAM role-based access

## Configuration

To configure GGScout to work with Google Secret Manager, add the following configuration to your `ggscout.toml` file:

### Service Account Key File Authentication

Use a JSON key file for authentication:

```toml
[sources.gcp]
type = "gcpsecretmanager"
fetch_all_versions = true
projects = ["some-project-id-441517"]
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "service_account_key_file"
auth.key_file = ".secure_files/.gcp_key.json"

[[sources.gcp.include]]
resource_ids = ["app-*", "database-*", "api-key"]

[[sources.gcp.exclude]]
resource_ids = ["test-*", "temp-*", "old-secret"]
```

### Application Default Credentials (Recommended for GCP)

When running ggscout on GCP infrastructure (GCE, GKE, Cloud Run, etc.), use Application Default Credentials for automatic authentication:

```toml
[sources.gcp]
type = "gcpsecretmanager"
fetch_all_versions = true
projects = ["some-project-id-441517"]
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "default"

[[sources.gcp.include]]
resource_ids = ["app-*", "database-*", "api-key"]

[[sources.gcp.exclude]]
resource_ids = ["test-*", "temp-*", "old-secret"]
```

:::tip Running on GCP Infrastructure
When using `auth_mode = "default"`, ggscout automatically detects its environment and uses the most appropriate authentication method:
- **On GCE/GKE**: Automatically calls GCP's metadata endpoint to retrieve credentials
- **With GOOGLE_APPLICATION_CREDENTIALS**: Uses the service account key file specified by the environment variable
- **Local development**: Falls back to `gcloud auth application-default login` credentials

This is the recommended approach for production deployments on GCP infrastructure.
:::

### Kubernetes Workload Identity Federation

For GKE clusters using Workload Identity:

```toml
[sources.gcp]
type = "gcpsecretmanager"
fetch_all_versions = true
projects = ["some-project-id-441517"]
mode = "read"
env = "production"
owner = "devops-team@example.com"

auth.auth_mode = "k8s"
auth.project_id = "my-gcp-project"
auth.project_number = "123456789012"
auth.pool_id = "my-workload-identity-pool"
auth.provider_id = "my-provider"
auth.gcp_service_account_name = "ggscout-sa"
auth.kubernetes_namespace = "ggscout"  # Optional
auth.kubernetes_service_account = "ggscout-k8s-sa"  # Optional

[[sources.gcp.include]]
resource_ids = ["app-*", "database-*", "api-key"]

[[sources.gcp.exclude]]
resource_ids = ["test-*", "temp-*", "old-secret"]
```

### Configuration Parameters

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `type` | Must be set to `"gcpsecretmanager"` | Yes |             |
| `fetch_all_versions` | Whether to collect all versions of secrets | Yes |             |
| `projects` | List of GCP project IDs to collect secrets from | No | All accessible projects |
| `auth.auth_mode` | Authentication method: "service_account_key_file", "k8s", or "default" | No | "default" |
| `mode` | Integration mode (one of:  "read", "write", "read/write") | No | "read" |
| `env` | Environment label for categorizing secrets (e.g., "production", "staging", "development") | No |             |
| `owner` | Owner of this source (an email, usually of an employee or a team) | No |             |
| `[[sources.<name>.include]]` | Table of resource_id patterns to include (see below) | No | |
| `[[sources.<name>.exclude]]` | Table of resource_id patterns to exclude (see below) | No | |

**Service Account Key File Authentication Parameters:**

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `auth.key_file` | Path to the service account JSON key file | Yes (for service_account_key_file mode) |             |

**Kubernetes Workload Identity Federation Parameters:**

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `auth.project_id` | GCP Project ID where the service account is located | Yes (for k8s mode) |             |
| `auth.project_number` | GCP Project Number | Yes (for k8s mode) |             |
| `auth.pool_id` | Workload Identity Pool ID | Yes (for k8s mode) |             |
| `auth.provider_id` | Workload Identity Provider ID | Yes (for k8s mode) |             |
| `auth.gcp_service_account_name` | Google Service Account name (without @project.iam.gserviceaccount.com) | Yes (for k8s mode) |             |
| `auth.kubernetes_namespace` | Kubernetes namespace where the service account is located | No |             |
| `auth.kubernetes_service_account` | Kubernetes service account name to use for authentication | No |             |
| `auth.audience` | Custom audience for the WIF provider | No | Standard WIF provider URL format |
| `auth.token_expiration_seconds` | Token expiration time in seconds | No | 1800 (30 minutes) |

### Authentication

GGScout supports three authentication methods for Google Cloud:

#### 1. Application Default Credentials (Recommended for GCP)

The `default` authentication mode automatically infers its configuration based on the environment:

- **Running on GCP infrastructure (GCE, GKE, Cloud Run)**: Automatically calls GCP's metadata endpoint to retrieve instance or workload credentials
- **GOOGLE_APPLICATION_CREDENTIALS environment variable set**: Uses the service account key file specified
- **Local development**: Falls back to credentials from `gcloud auth application-default login`

This is the most secure and convenient method when running ggscout on GCP infrastructure as it eliminates the need to manage service account key files.

#### 2. Service Account Key File

Explicitly specify a JSON key file path for authentication. This method works in any environment but requires managing and securing the key file.

#### 3. Kubernetes Workload Identity Federation

Use Kubernetes service account tokens with GCP Workload Identity Federation. This is the most secure method for GKE deployments as it:
- Eliminates the need for service account key files
- Provides short-lived, automatically rotated credentials
- Follows cloud-native security best practices

**Prerequisites:** Before setting up the integration, ensure that you have activated the **Cloud Resource Manager API** in your GCP account, in addition to the **Secret Manager API**.

### Environment Variables

For Service Account Key File authentication:
- `GOOGLE_APPLICATION_CREDENTIALS`: Path to the service account key file (when using default mode)

For Application Default Credentials:
- No environment variables required when running on GCP infrastructure
- `GOOGLE_APPLICATION_CREDENTIALS`: Optional, can be used to specify a key file

## Best Practices

1. **Use Application Default Credentials (`auth_mode = "default"`)** when running on GCP infrastructure (GCE, GKE, Cloud Run) for automatic, secure authentication without managing key files
2. **For GKE deployments**: Use Kubernetes Workload Identity Federation for the most secure, keyless authentication
3. **Avoid service account key files** in production when possible - use Application Default Credentials or Workload Identity instead
4. Follow the principle of least privilege for IAM permissions
5. Enable `fetch_all_versions` to track changes in your secrets over time
6. If you must use service account key files, store them securely and rotate them regularly
7. Use separate projects for different environments
8. When deploying on GCP, leverage the automatic metadata endpoint detection for seamless authentication

**Note:**
- Use `[[sources.<name>.include]]` and `[[sources.<name>.exclude]]` tables to specify multiple include/exclude rules. Each table must have a `resource_ids` array.
- Patterns support wildcards (*) only at the end for prefix matching. For exact matches, specify the complete name without wildcards.
