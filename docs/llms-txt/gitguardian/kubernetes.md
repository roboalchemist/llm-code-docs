# Source: https://docs.gitguardian.com/ggscout-docs/integrations/infrastructure/kubernetes.md

# Kubernetes

> Configure ggscout to collect secrets from Kubernetes clusters, supporting Secrets, ConfigMaps, Deployments, and Service Accounts.

# Kubernetes Integration

ggscout supports integration with Kubernetes clusters to collect secrets and gather information about various Kubernetes resources. This integration provides comprehensive visibility into both sensitive data and resource configurations within your clusters.

## Supported Features

- **Multiple resource types**: Secrets, ConfigMaps, Deployments, Service Accounts, and External Secrets
- **Comprehensive data collection**: Collects both secrets and general resource information
- **Namespace filtering**: Target specific namespaces using glob patterns
- **Multiple authentication methods**: KubeConfig file or in-cluster authentication
- **Multi-cluster support**: Monitor multiple Kubernetes clusters simultaneously
- **Resource filtering**: Fine-grained control over which resources to scan

:::info
The Kubernetes integration is read-only and does not support writing secrets back to the cluster.
:::

## Supported Resource Types

ggscout can scan the following Kubernetes API resources:

| Resource Type | Description |
|---------------|-------------|
| **Secrets** | Native Kubernetes Secret resources |
| **ConfigMaps** | Configuration data stored in the cluster |
| **Deployments** | Application deployment configurations |
| **Service Accounts** | Kubernetes service account configurations |
| **External Secrets** | External Secrets Operator resources |

## Configuration

To configure ggscout to work with Kubernetes, add the following configuration to your `ggscout.toml` file:

### KubeConfig File Authentication

For external access to Kubernetes clusters using a kubeconfig file:

```toml
[sources.k8s-production]
type = "kubernetes"
config_source = "kubeconfigfile"
kubeconfig_path = "/path/to/kubeconfig"  # Optional, defaults to ~/.kube/config
contexts = ["production-cluster", "staging-cluster"]  # Optional, all contexts if not specified
namespaces = ["default", "production-*", "app-*"]  # Optional, all namespaces if not specified
env = "production"
owner = "devops-team@example.com"
```

### In-Cluster Authentication

For ggscout running inside a Kubernetes cluster:

```toml
[sources.k8s-cluster]
type = "kubernetes"
config_source = "incluster"
name = "production-cluster"  # Cluster name (required for in-cluster mode)
namespaces = ["default", "production-*"]  # Optional namespace filtering
env = "production"
owner = "devops-team@example.com"
```

### Configuration Parameters

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `type` | Must be set to `"kubernetes"` | Yes |             |
| `config_source` | Authentication method: `"kubeconfigfile"` or `"incluster"` | Yes |             |
| `namespaces` | List of namespace patterns to scan | No |  |
| `env` | Environment identifier | No |             |
| `owner` | Owner of this source (an email, usually of an employee or a team) | No |             |
| `mode` | Integration mode (only `"read"` is supported for Kubernetes) | No | `"read"` |

#### KubeConfig File Parameters

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `kubeconfig_path` | Path to kubeconfig file | No | `~/.kube/config` |
| `contexts` | List of contexts to use from kubeconfig | No |  |

#### In-Cluster Parameters

| Parameter | Description | Required | Default Value |
|-----------|-------------|----------|-------------|
| `name` | Name of the Kubernetes cluster | Yes |             |

### Setting Up Authentication

#### Authentication Setup Steps

1. Configure a ClusterRole

The easiest way to set up your kubernetes integration is to use our ggscout [Helm charts](https://github.com/GitGuardian/ggscout-helm-charts). Then you only need to configure this in your `values.yaml`:

```yaml
clusterRole:
    create: true
```

If you don't use our Helm charts, check the [role](https://github.com/GitGuardian/ggscout-helm-charts/blob/main/charts/ggscout/templates/clusterrole.yam]) we are using to see the list of required rules

Also see this full [values.yaml](https://github.com/GitGuardian/ggscout-helm-charts/blob/main/charts/ggscout/examples/k8s_incluster/values.yaml) example.

## Namespace Filtering

Use glob patterns to control which namespaces ggscout scans:

```toml
# Scan specific namespaces
namespaces = ["production", "staging", "development"]

# Use wildcards (only at the end) to match patterns
namespaces = ["app-*", "service-*"]

# Combine exact matches and patterns
namespaces = ["default", "kube-system", "production-*"]
```

## Resource Filtering

Control which specific resources are scanned using include/exclude filters:

```toml
[sources.k8s-filtered]
type = "kubernetes"
config_source = "incluster"
name = "production-cluster"

# Include filters - only scan these resources
[[sources.k8s-filtered.include]]
resource_ids = ["secret:*", "configmap:*"]

# Exclude filters - skip these resources
[[sources.k8s-filtered.exclude]]
resource_ids = ["secret:kube-system/*"]
```

## Multi-Cluster Configuration

Monitor multiple Kubernetes clusters by defining multiple sources:

```toml
[sources.k8s-production]
type = "kubernetes"
config_source = "kubeconfigfile"
contexts = ["production"]
env = "production"
owner = "devops-team@example.com"

[sources.k8s-staging]
type = "kubernetes"
config_source = "kubeconfigfile"
contexts = ["staging"]
env = "staging"
owner = "devops-team@example.com"

[sources.k8s-development]
type = "kubernetes"
config_source = "incluster"
name = "dev-cluster"
env = "development"
owner = "devops-team@example.com"
```

## Troubleshooting

### Common Issues

**Authentication Failures**
- Verify kubeconfig file path and permissions
- Check RBAC permissions for the configured user/service account
- Ensure cluster connectivity

**Missing Resources**
- Confirm RBAC permissions include all required resource types
- Check namespace filtering configuration
- Verify resource filtering rules

**Performance Issues**
- Reduce scope with namespace filtering
- Use resource filtering to limit scanned resource types
- Consider cluster size and API rate limits
