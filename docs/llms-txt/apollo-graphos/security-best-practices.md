# Source: https://www.apollographql.com/docs/apollo-operator/security-best-practices.md

# Security Best Practices

This guide provides security best practices for deploying and operating the Apollo GraphOS Operator in production environments. We strongly recommend using the Helm chart as it implements many security best practices by default.

## Using the Helm Chart (Recommended)

The Apollo GraphOS Operator Helm chart implements several security best practices out of the box:

### Service Account Security

* **Dedicated Service Account**: Creates a dedicated `apollo-operator` ServiceAccount with minimal required permissions
* **Namespace-Scoped RBAC**: Supports namespace-scoped deployments to limit operator access to specific namespaces
* **Principle of Least Privilege**: Implements granular RBAC rules that grant only necessary permissions for each controller

## Manual Deployment Security Considerations

If you cannot use the Helm chart, ensure your manual deployment includes these security measures:

### Service Account and RBAC

The Apollo GraphOS Operator requires a dedicated ServiceAccount with specific permissions for each resource type:

#### Required Permissions by resource type

**Subgraph:**

* Watch, list, and get Subgraph resources
* Create, update, and patch Subgraph status resources

**Supergraph:**

* Watch, list, and get Supergraph resources
* Create, update, and patch Supergraph status resources
* Create, update, and patch Deployments, Services, ConfigMaps, and Secrets
* Watch ReplicaSets and Events

**SupergraphSchema:**

* Watch, list, and get SupergraphSchema resources
* Create, update, and patch SupergraphSchema status resources

**SupergraphSet:**

* Watch, list, and get SupergraphSet and Supergraph resources
* Create, update, and patch SupergraphSet status resources

#### RBAC Configuration

The operator supports both cluster-scoped and namespace-scoped deployments. For production environments, use namespace-scoped mode to limit the operator's access to specific namespaces.

## API Key Security

The Apollo GraphOS Operator requires an Apollo Studio API key to function.

### API Key Best Practices

1. **Use Dedicated API Keys**: Create API keys specifically for the operator, not shared with other applications
2. **Regular Rotation**: Implement a process to rotate API keys regularly
3. **Monitor Usage**: Leverage GraphOS Platform's [Audit Logs](https://www.apollographql.com/docs/graphos/platform/access-management/audit-log) to monitor API key usage patterns

### API Key Types

The Apollo GraphOS Operator handles two types of API keys:

1. **Operator API Key**: The key you provide to the operator for accessing Apollo Studio
2. **Supergraph API Keys**: Keys that the operator creates and stores in Secrets for Supergraph resources

Both types of API keys are stored in Kubernetes Secrets and should be secured according to [Kubernetes Secrets Good Practices](https://kubernetes.io/docs/concepts/security/secrets-good-practices/).

## Namespace Scoping

Configure the operator to only access specific namespaces to reduce the attack surface:

```yaml
config:
  controllers:
    subgraph:
      namespaces:
        - products-subgraph
        - orders-subgraphs
    supergraph:
      namespaces:
        - apollo
    supergraphSchema:
      namespaces:
        - apollo
```

## Security Checklist

Before deploying to production, verify:

* [ ] API key stored in Kubernetes Secret
* [ ] Using dedicated API key
* [ ] Namespace-scoped RBAC and configuration
* [ ] Service account with minimal required permissions
