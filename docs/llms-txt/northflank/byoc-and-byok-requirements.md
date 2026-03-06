# Source: https://northflank.com/docs/v1/application/bring-your-own-cloud/byoc-and-byok-requirements.md

# BYOC and BYOK requirements

Before connecting your own cloud infrastructure or importing an existing Kubernetes cluster to Northflank, ensure your setup meets the following requirements.

## BYOC vs BYOK

**BYOC (Bring Your Own Cloud)**: Northflank provisions and manages a new Kubernetes cluster in your cloud account (AWS, GCP, Azure, etc.).

**BYOK (Bring Your Own Kubernetes)**: You import an existing Kubernetes cluster to be managed by Northflank.

## Resource requirements

### BYOC minimum requirements

| Resource | Per node | Per cluster |
| --- | --- | --- |
| Nodes | - | 1 node minimum |
| vCPUs | 4 vCPUs | 12 vCPUs |
| Memory | 8 GB | 24 GB |
| Ephemeral storage | 100 GB (recommended) | - |

### BYOK minimum requirements

| Resource | Per node | Per cluster |
| --- | --- | --- |
| Nodes | - | **3 nodes minimum** |
| vCPUs | 4 vCPUs | 12 vCPUs |
| Memory | 8 GB | 24 GB |
| Ephemeral storage | 100 GB (recommended) | - |

### Optimization recommendations

**Node sizing**: Prefer fewer larger nodes over many smaller nodes. Some system components must run on every node, so larger nodes minimize the relative per-node overhead, leaving more capacity for your workloads.

**Storage ratio**: Maintain at least 5 GB of ephemeral storage per vCPU for optimal performance.

## BYOK requirements

If you're importing an existing Kubernetes cluster (BYOK), your cluster must have these components pre-installed and meet additional requirements.

### Required system components

Your cluster must have these components already installed:

| Component | Requirement | Notes |
| --- | --- | --- |
| CNI plugin | Cilium | Required for networking |
| CSI driver | Any compatible driver | Required for persistent volumes and stateful workloads |
| CoreDNS | Installed at `kube-system/coredns` | Existing installation may be replaced/reconfigured during import |

**Note on Kube-DNS**: If you're currently using Kube-DNS instead of CoreDNS, contact Northflank support before importing your cluster.

### L4 load balancer support

Your Kubernetes installation must be able to provision external, public IPs for Kubernetes `Service` resources of type `LoadBalancer`.

**Requirements:**

- Must provision L4 load balancers by default

- If your provider requires specific annotations on `Service` resources to provision L4 load balancers, contact Northflank support for assistance

### Component conflicts

Ensure the following components are **NOT** pre-installed on your cluster (except CoreDNS), as they will be installed during the import process:

- Istio

- Envoy Gateway

- Prometheus

- Promtail

- Grafana

- RuntimeClass resources (except those required by your provider)

If these components exist before import, the installation process may fail due to conflicting resources.

## Import process and installation

During the BYOK import process, Northflank installs several system components:

**Networking:**

- CoreDNS + configuration

- Istio service mesh

- Envoy Gateway

**Logging and metrics:**

- Prometheus

- Promtail

- Grafana

**Runtime:**

- RuntimeClass resources

These components are essential for Northflank to manage your cluster and provide observability, networking, and runtime capabilities.

## Important warnings

### Use a new cluster for BYOK import

We strongly recommend using a new, dedicated cluster for BYOK import. Do NOT import clusters that:

- Are running production workloads

- Host important or business-critical applications

- Are shared with other systems or teams

**Potential risks:**

- The installation might fail and leave the cluster in an unhealthy state

- There is currently no full deinstallation process

- Existing configurations may be overwritten or modified

**If something goes wrong:**
If the import fails or your cluster becomes unhealthy, you may need to redeploy a fresh cluster.

## Getting help

Contact Northflank support if:

- You have questions about the installation process

- Your Kubernetes provider doesn't meet some requirements

- Your provider requires customization (e.g., specific annotations, non-standard configurations)

- You need assistance during or after the import process

- Your cluster uses Kube-DNS instead of CoreDNS

## Next steps

- [Configure your Kubernetes cluster: Manage your clusters on other cloud providers using Northflank.](/v1/application/bring-your-own-cloud/configure-your-cluster)
- [Deploy node pools: Configure and deploy node pools on a Kubernetes cluster with Northflank.](/v1/application/bring-your-own-cloud/deploy-and-scale-node-pools)
- [Deploy workloads to your cluster: Deploy services, jobs, and addons to your own cluster, and configure workloads to schedule on specific node pools.](/v1/application/bring-your-own-cloud/deploy-workloads-to-your-cluster)
- [Run GPU workloads: Deploy GPU workloads on Northflank for AI, machine learning, HPC workloads, and other tasks.](/v1/application/gpu-workloads/gpus-on-northflank)
