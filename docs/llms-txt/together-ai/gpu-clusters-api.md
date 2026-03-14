# Source: https://docs.together.ai/docs/gpu-clusters-api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API & Integrations

> Manage clusters programmatically with CLI, REST API, Terraform, and third-party tools

## Overview

All cluster management operations are available through multiple interfaces for programmatic control and automation:

* **tcloud CLI** – Command-line tool for cluster operations
* **REST API** – Full HTTP API for custom integrations
* **Terraform Provider** – Infrastructure-as-code for reproducible deployments
* **SkyPilot** – Orchestrate AI workloads across clusters

## tcloud CLI

The tcloud CLI provides a command-line interface for managing clusters, storage, and scaling.

### Installation

Download the CLI for your platform:

* [Mac (Universal)](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-darwin-universal.tar.gz)
* [Linux (AMD64)](https://tcloud-cli-downloads.s3.us-west-2.amazonaws.com/releases/latest/tcloud-linux-amd64.tar.gz)

### Authentication

Authenticate via Google SSO:

```bash  theme={null}
tcloud sso login
```

### Common Commands

**Create a cluster:**

```bash  theme={null}
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --reservation-duration 1 \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1
```

**Specify billing type (reserved vs on-demand):**

```bash  theme={null}
# Reserved capacity
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --billing-type prepaid \
  --reservation-duration 30 \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1

# On-demand capacity
tcloud cluster create my-cluster \
  --num-gpus 8 \
  --billing-type on_demand \
  --instance-type H100-SXM \
  --region us-central-8 \
  --shared-volume-name my-volume \
  --size-tib 1
```

**Delete a cluster:**

```bash  theme={null}
tcloud cluster delete <CLUSTER_UUID>
```

**List clusters:**

```bash  theme={null}
tcloud cluster list
```

**Scale a cluster:**

```bash  theme={null}
tcloud cluster scale <CLUSTER_UUID> --num-gpus 16
```

## REST API

All cluster management actions are available via REST API endpoints.

### API Reference

Complete API documentation is available at:
[GPU Cluster API Reference →](https://docs.together.ai/reference/clusters-create)

### Example: Create Cluster

```bash  theme={null}
curl -X POST "https://manager.cloud.together.ai/api/v1/gpu_cluster" \
  -H "Authorization: Bearer $TOGETHER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "my-cluster",
    "num_gpus": 8,
    "instance_type": "H100-SXM",
    "region": "us-central-8",
    "billing_type": "prepaid",
    "reservation_duration": 30,
    "shared_volume": {
      "name": "my-volume",
      "size_tib": 1
    }
  }'
```

### Example: List Clusters

```bash  theme={null}
curl -X GET "https://manager.cloud.together.ai/api/v1/gpu_clusters" \
  -H "Authorization: Bearer $TOGETHER_API_KEY"
```

### Example: Delete Cluster

```bash  theme={null}
curl -X DELETE "https://manager.cloud.together.ai/api/v1/gpu_cluster/{cluster_id}" \
  -H "Authorization: Bearer $TOGETHER_API_KEY"
```

## Terraform Provider

Use the Together Terraform Provider to define clusters, storage, and scaling policies as code.

### Setup

```hcl  theme={null}
terraform {
  required_providers {
    together = {
      source = "together-ai/together"
      version = "~> 1.0"
    }
  }
}

provider "together" {
  api_key = var.together_api_key
}
```

### Example: Define a Cluster

```hcl  theme={null}
resource "together_gpu_cluster" "training_cluster" {
  name              = "training-cluster"
  num_gpus          = 8
  instance_type     = "H100-SXM"
  region            = "us-central-8"
  billing_type      = "prepaid"
  reservation_days  = 30

  shared_volume {
    name     = "training-data"
    size_tib = 5
  }
}
```

### Benefits

* **Version control** – Track infrastructure changes in Git
* **Reproducibility** – Deploy identical clusters across environments
* **Automation** – Integrate with CI/CD pipelines
* **State management** – Terraform tracks cluster state automatically

## SkyPilot Integration

Orchestrate AI workloads on GPU Clusters using SkyPilot for simplified cluster management and job scheduling.

### Installation

```bash  theme={null}
uv pip install skypilot[kubernetes]
```

### Setup

1. **Launch a Kubernetes cluster** via Together Cloud

2. **Configure kubeconfig:**

Download the kubeconfig from the cluster UI and merge it:

```bash  theme={null}
# Option 1: Replace existing config
cp together-kubeconfig ~/.kube/config

# Option 2: Merge with existing config
KUBECONFIG=./together-kubeconfig:~/.kube/config \
  kubectl config view --flatten > /tmp/merged_kubeconfig && \
  mv /tmp/merged_kubeconfig ~/.kube/config
```

3. **Verify SkyPilot access:**

```bash  theme={null}
sky check k8s
```

Expected output:

```
Checking credentials to enable infra for SkyPilot.
  Kubernetes: enabled [compute]
    Allowed contexts:
    └── t-51326e6b-25ec-42dd-8077-6f3c9b9a34c6-admin: enabled.

🎉 Enabled infra 🎉
  Kubernetes [compute]
```

4. **Check available GPUs:**

```bash  theme={null}
sky show-gpus --infra k8s
```

### Example: Launch a Workload

Create a SkyPilot task file (`task.yaml`):

```yaml  theme={null}
resources:
  accelerators: H100:8
  cloud: kubernetes

setup: |
  pip install torch transformers

run: |
  python train.py
```

Launch the task:

```bash  theme={null}
sky launch -c my-job task.yaml
```

### Example: Fine-tune GPT OSS

Download the [gpt-oss-20b.yaml](https://github.com/skypilot-org/skypilot/tree/master/llm/gpt-oss-finetuning#lora-finetuning) configuration.

Launch fine-tuning:

```bash  theme={null}
sky launch -c gpt-together gpt-oss-20b.yaml
```

### Benefits

* **Simplified orchestration** – Abstract away Kubernetes complexity
* **Multi-cloud support** – Same workflow across different clouds
* **Cost optimization** – Auto-select cheapest available resources
* **Job management** – Easy monitoring and cancellation

## Automation Patterns

### CI/CD Integration

**GitHub Actions example:**

```yaml  theme={null}
name: Train Model

on: push

jobs:
  train:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Create GPU Cluster
        run: |
          tcloud cluster create training-${{ github.sha }} \
            --num-gpus 8 \
            --billing-type on_demand \
            --instance-type H100-SXM \
            --region us-central-8

      - name: Run Training
        run: |
          # Submit training job to cluster
          kubectl apply -f training-job.yaml

      - name: Cleanup
        if: always()
        run: |
          tcloud cluster delete training-${{ github.sha }}
```

### Scheduled Jobs

**Cron-based cluster creation:**

```bash  theme={null}
# Create cluster daily at 6 AM for batch processing
0 6 * * * tcloud cluster create daily-batch \
  --num-gpus 16 \
  --billing-type on_demand \
  --instance-type H100-SXM
```

### Auto-scaling Scripts

```python  theme={null}
import requests


def scale_cluster(cluster_id, target_gpus):
    response = requests.put(
        f"https://manager.cloud.together.ai/api/v1/gpu_cluster",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"cluster_id": cluster_id, "num_gpus": target_gpus},
    )
    return response.json()


# Scale based on job queue length
if job_queue_length > 100:
    scale_cluster("cluster-123", 16)
else:
    scale_cluster("cluster-123", 8)
```

## Best Practices

### API Usage

* **Use environment variables** for API keys (never hardcode)
* **Implement retry logic** for transient failures
* **Check cluster status** before submitting jobs
* **Clean up resources** after completion

### CLI Usage

* **Authenticate once** per session with `tcloud sso login`
* **Use UUIDs** for cluster references (more reliable than names)
* **Script common operations** for team consistency
* **Version control** your cluster configuration scripts

### Terraform

* **Use remote state** for team collaboration
* **Tag resources** for cost tracking
* **Use variables** for environment-specific configs
* **Test in dev** before applying to production

## Troubleshooting

### Authentication issues

* Verify API key is set: `echo $TOGETHER_API_KEY`
* Re-authenticate with SSO: `tcloud sso login`
* Check token expiration

### API rate limits

* Implement exponential backoff
* Batch operations when possible
* Contact support for higher limits

### Terraform state conflicts

* Use remote state locking
* Coordinate with team on apply operations
* Use `terraform plan` before `apply`

## What's Next?

* [Review API reference documentation](/reference/clusters-create)
* [Learn about cluster management](/docs/gpu-clusters-management)
* [Understand billing](/docs/gpu-clusters-billing)


Built with [Mintlify](https://mintlify.com).