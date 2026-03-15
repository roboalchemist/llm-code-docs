# Source: https://docs.jit.io/docs/k8s-agent.md

# Jit Kubernetes Agent

The **Jit Kubernetes Agent** is a comprehensive security and resource monitoring solution that automatically collects Kubernetes cluster information and performs security scanning using Kubescape. The agent runs as a scheduled job in your cluster to keep your security posture up-to-date in Jit.

## Overview

The Jit Kubernetes Agent provides:

* **Automated Resource Collection**: Gathers comprehensive Kubernetes resource information
* **Security Scanning**: Performs automated security assessments using Kubescape NSA framework
* **Unified Reporting**: Integrates security findings and resource data in your Jit dashboard

## Prerequisites

Before installing the Jit Kubernetes Agent, ensure you have:

* A Kubernetes cluster with appropriate permissions
* Jit service credentials (Client ID and Client Secret)
* Helm 3.x installed on your local machine
* Minimum 2GB memory available on cluster nodes

## Quick Start

### 1. Add the Jit Helm Repository

```bash
helm repo add jitsecurity https://jitsecurity.github.io/helm-charts
helm repo update
```

### 2. Get Your Jit Credentials

1. Log in to your [Jit dashboard](https://platform.jit.io/)
2. Navigate to **Settings** → **API Tokens**
3. Generate a new API token or use an existing one
4. Generate a new API token (with the "**CLI Agent**" role) or use an existing one with that role.
5. Note your **Client ID** and **Client Secret**

<br />

### 3. Install the Agent

```shell
helm install jit-k8s-agent \
  --set jit.clientId=<YOUR_CLIENT_ID> \
  --set jit.clientSecret=<YOUR_CLIENT_SECRET> \
  --set cluster.name=<YOUR_CLUSTER_NAME> \
  -n jit-k8s-agent --create-namespace \
  jitsecurity/jit-k8s-agent
```

> 🔁 Alternatively, you can use an existing Kubernetes Secret that already contains the credentials:
>
> (The secret must include keys named `clientId` and `clientSecret`)

```shell Bash
helm install jit-k8s-agent \
  --set existingSecret=<SECRET_NAME> \
  --set cluster.name=<YOUR_CLUSTER_NAME> \
  -n jit-k8s-agent --create-namespace \
  jitsecurity/jit-k8s-agent
```

The agent will automatically start collecting cluster information and performing security scans.

## Configuration

The Jit Kubernetes Agent works out-of-the-box with minimal configuration. You only need to provide:

| Parameter          | Description                                                                                           | Example                   |
| ------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------- |
| `jit.clientId`     | Your Jit Client ID                                                                                    | `jit_1234567890abcdef`    |
| `jit.clientSecret` | Your Jit Client Secret                                                                                | `secret_abcdef1234567890` |
| `cluster.name`     | Unique cluster identifier                                                                             | `production-us-east-1`    |
| `existingSecret`   | Name of an existing Kubernetes Secret that stores the Jit credentials (`clientId` and `clientSecret`) | `jitExistingSecret`       |

### Optional: Disable Security Scanning

If you need to disable security scanning (e.g., for resource-constrained environments):

```bash
helm upgrade jit-k8s-agent \
  --set kubescape.enabled=false \
  -n jit-k8s-agent \
  jitsecurity/jit-k8s-agent
```

## Security Scanning

The Jit Kubernetes Agent includes **Kubescape security scanning** by default, which:

* Scans your cluster
* Identifies security misconfigurations and vulnerabilities
* Uploads findings to your Jit dashboard for analysis
* Runs automatically with each resource collection cycle

## Monitoring and Verification

### Check Agent Status

```bash
# View recent job logs
kubectl logs -n jit-k8s-agent job/jit-k8s-agent-initial-job

# Check CronJob status
kubectl get cronjobs -n jit-k8s-agent

# View job history
kubectl get jobs -n jit-k8s-agent
```

### Success Indicators

Look for these log messages to confirm successful operation:

```
✅ "Starting Kubescape security scan..."
✅ "Kubescape security scan completed"
✅ "Successfully uploaded Kubescape scan results"
✅ "Reported 2 upload paths"
```

## Troubleshooting

### Common Issues

| Issue                     | Solution                                                                                   |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Memory pressure**       | Ensure nodes have adequate resources or disable Kubescape: `--set kubescape.enabled=false` |
| **Authentication errors** | Verify your Jit credentials are correct and have proper permissions                        |
| **Network connectivity**  | Ensure the cluster can reach `api.jit.io` and `public.ecr.aws`                             |
| **RBAC permissions**      | The agent requires cluster-wide read permissions for resource collection                   |

### Rollback

If you need to rollback to a previous version:

```bash
helm rollback jit-k8s-agent -n jit-k8s-agent
```

### Uninstall

To completely remove the agent:

```bash
helm uninstall jit-k8s-agent -n jit-k8s-agent
kubectl delete namespace jit-k8s-agent
```

## Resource Requirements

The Jit Kubernetes Agent requires minimal resources and will work on most Kubernetes clusters. No persistent storage is required.

## What's Next

After successful installation and scan:

1. **View Results**: Check your [Jit dashboard](https://platform.jit.io/risks/backlog) → **Findings** page and filter by **asset name** = \<YOUR\_CLUSTER\_NAME>