# Source: https://docs.gitguardian.com/self-hosting/management/infrastructure-management/high-availability.md

# High availability

> Configure high availability for GitGuardian self-hosted by scaling replicas and ensuring database redundancy.

Achieving a high-availability (HA) setup for the GitGuardian application requires configuring several components.

### Kubernetes cluster

The foundation of a high-availability setup is a robust Kubernetes cluster.

### Existing cluster

If you are using an existing cluster deployed via either [KOTS](../../installation/installation-existing-cluster-kots) or [Helm](../../installation/installation-existing-cluster-helm), ensure it is configured for **high availability**. Kubernetes provides support for high availability out-of-the-box, as long as the pods are distributed across multiple nodes.

### Embedded cluster

:::caution
High Availability (HA) on an embedded cluster isn't recommended nor supported by GitGuardian. For HA setups, leveraging a managed existing cluster is advised.
:::

## Rolling Updates

Kubernetes natively supports rolling updates, which allows for seamless application updates without downtime. This feature is common to all installation types, ensuring that updates can be applied smoothly while maintaining high availability.

## Deployments & Pods

Pod configurations are optimized to distribute across nodes evenly, minimizing the impact of a node failure. No additional configuration is required on your part.

## Databases & Datastores

Both Redis and PostgreSQL require HA configurations. The embedded versions of these services don't support high availability, necessitating the use of external, HA-configured versions.
