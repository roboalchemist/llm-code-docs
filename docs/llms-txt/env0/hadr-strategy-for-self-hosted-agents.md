# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/hadr-strategy-for-self-hosted-agents.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HA/DR Strategy for Self-Hosted Agents

> Configure high availability and disaster recovery for env zero self-hosted Kubernetes agents

For a high-availability configuration of the env zero self-hosted agent, you can install the agent in two different K8s clusters in two different availability zones. You can configure the self-hosted agent in the following mode:

## Active-Passive

* Setup the failover agent in a separate region or availability zone
* Once you confirmed that the agent is live and running, scale the deployment to 0.\
  `kubectl scale deploy <agentname>.agent-trigger-deployment --replicas=0`\
  if using the proxy pod, also scale the proxy deployment to 0.\
  `kubectl scale deploy <agentname>.agent-proxy-deployment --replicas=0`
* When an outage has occurred in the primary cluster, scale the failover deployments back to 1\
  `kubectl scale deploy <agentname>.agent-trigger-deployment --replicas=1`\
  if using the proxy pod, also scale the proxy deployment to 1.\
  `kubectl scale deploy <agentname>.agent-proxy-deployment --replicas=1`

## Things to consider 🤔

### Working Directory

when failing over to a new cluster, the working directory may not be in sync or backed up. This will result in the high possibility that you cannot resume or approve a deployment that was waiting for approval. A simple redeployment will allow you to resume your deployments in the new cluster.

* Alternatively you can use [env zero Hosted Encrypted State](/guides/admin-guide/self-hosted-kubernetes-agent/env0-hosted-encrypted-state) to resume deployments across multiple clusters.

### State File

When implementing a failover strategy for self-hosted env zero agents, it is critical to ensure that Terraform state files remain accessible and consistent across clusters.

<Warning>
  Losing state sync

  If the state is lost or becomes unsynchronized, deployments may fail or lead to infrastructure drift.
</Warning>

#### 🟢 Remote State Storage (Recommended)

For best reliability, state should be stored in a [remote backend](/guides/admin-guide/remote-backend)  that remains accessible regardless of cluster failures. This ensures that when a standby cluster is activated, it can resume deployments without losing state.

The common use cases are:

* [env zero's remote backend](/guides/admin-guide/remote-backend/login) as it is backed up across two AWS regions, providing built-in redundancy
* Terraform’s remote backend
* AWS S3 + DynamoDB (state locking)
* Google Cloud Storage (GCS)
* Azure Blob Storage

#### 🟡 State Stored in the Agent Namespace (Less Ideal)

If the Terraform state is stored within the env zero agent's Kubernetes namespace, read more about it [here](/guides/admin-guide/self-hosted-kubernetes-agent/#persistent-volumestorage-class-optional) .

In this case, extra steps are needed to sync state between the primary and standby clusters. This may involve:

* Persistent storage replication across clusters.
* A manual or automated process to copy state from the failed cluster to the standby.

Built with [Mintlify](https://mintlify.com).
