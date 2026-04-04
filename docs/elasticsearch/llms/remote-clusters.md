# Source: https://www.elastic.co/docs/deploy-manage/remote-clusters

﻿---
title: Remote clusters
description: By setting up remote clusters, you can connect an Elasticsearch cluster to other Elasticsearch clusters. Remote clusters can be located in different data...
url: https://www.elastic.co/docs/deploy-manage/remote-clusters
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud on Kubernetes
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Unavailable
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Remote clusters
By setting up **remote clusters**, you can connect an Elasticsearch cluster to other Elasticsearch clusters. Remote clusters can be located in different data centers, geographic regions, and run on a different type of environment: Elastic Cloud Hosted, Elastic Cloud Enterprise, Elastic Cloud on Kubernetes, or self-managed.
Remote clusters are especially useful in two cases:
- **Cross-cluster replication**
  With [cross-cluster replication](https://www.elastic.co/docs/deploy-manage/tools/cross-cluster-replication), or CCR, you ingest data to an index on a remote cluster. This leader index is replicated to one or more read-only follower indices on your local cluster. Creating a multi-cluster architecture with cross-cluster replication enables you to configure disaster recovery, bring data closer to your users, or establish a centralized reporting cluster to process reports locally.
- **Cross-cluster search**
  [Cross-cluster search](https://www.elastic.co/docs/explore-analyze/cross-cluster-search), or CCS, enables you to run a search request against one or more remote clusters. This capability provides each region with a global view of all clusters, allowing you to send a search request from a local cluster and return results from all connected remote clusters. For full cross-cluster search capabilities, the local and remote cluster must be on the same [subscription level](https://www.elastic.co/subscriptions).

<admonition title="Note about terminology">
  In the case of remote clusters, the Elasticsearch cluster or deployment initiating the connection and requests is often referred to as the **local cluster**, while the Elasticsearch cluster or deployment receiving the requests is referred to as the **remote cluster**.
</admonition>


## Security models and connection modes

When configuring remote clusters, you can choose between two security models and two connection modes. Both security models are compatible with either connection mode.
- [Security models](https://www.elastic.co/docs/deploy-manage/remote-clusters/security-models): API key–based authentication (recommended) or TLS certificate–based authentication (deprecated). Starting with Elastic Stack 9.3, API key-based authentication also supports strong identity verification for an additional layer of security.
- [Connection modes](https://www.elastic.co/docs/deploy-manage/remote-clusters/connection-modes): Sniff mode (direct connections to Elasticsearch nodes) or proxy mode (connections through a reverse proxy or load balancer endpoint).

<note>
  In managed or orchestrated environments, such as Elastic Cloud Hosted, Elastic Cloud Enterprise, and Elastic Cloud on Kubernetes, you can select the security model, but the connection mode is effectively limited to *proxy*. This is because sniff mode requires Elasticsearch nodes publish addresses to be directly reachable across clusters, which is generally not practical in containerized deployments.
</note>


## Setup

Depending on the environment the local and remote clusters are deployed on and the security model you wish to use, the exact details needed to add a remote cluster vary but generally follow the same path:
1. **Configure trust between clusters.** In the settings of the local deployment or cluster, configure the trust security model that your remote connections will use to access the remote cluster. This step involves specifying API keys or certificates retrieved from the remote clusters.
2. **Establish the connection.** In Kibana on the local cluster, or using the Elasticsearch API, finalize the connection by specifying each remote cluster's details.

Find the instructions with details on the supported security models and available connection modes for your specific scenario:
- [Remote clusters on Elastic Cloud Hosted](https://www.elastic.co/docs/deploy-manage/remote-clusters/ec-enable-ccs)
- [Remote clusters on Elastic Cloud Enterprise](https://www.elastic.co/docs/deploy-manage/remote-clusters/ece-enable-ccs)
- [Remote clusters on Elastic Cloud on Kubernetes](https://www.elastic.co/docs/deploy-manage/remote-clusters/eck-remote-clusters)
- [Remote clusters on self-managed installations](https://www.elastic.co/docs/deploy-manage/remote-clusters/remote-clusters-self-managed)


## Remote clusters and network security

<applies-to>
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud Enterprise: Generally available
</applies-to>

In Elastic Cloud Hosted (ECH) and Elastic Cloud Enterprise (ECE), the remote clusters functionality interacts with [network security](https://www.elastic.co/docs/deploy-manage/security/network-security) traffic filtering rules in different ways, depending on the [security model](/docs/deploy-manage/remote-clusters/remote-clusters-self-managed#remote-clusters-security-models) you use.
- **TLS certificate–based authentication (deprecated):**
  For remote clusters configured using the TLS certificate–based security model, network security policies or rule sets have no effect on remote clusters functionality. Connections established with this method (mTLS) are already considered secure and are always accepted, regardless of any filtering policies or rule sets applied on the local or remote deployment to restrict other traffic.
- **API key–based authentication (recommended):**
  When remote clusters use the API key–based authentication model, network security policies or rule sets on the **destination (remote) deployment** do affect remote cluster functionality if enabled. In this case, you can use traffic filters to explicitly control which deployments are allowed to connect to the remote cluster service endpoint.
  <note>
  Because of [how network security works](/docs/deploy-manage/security/network-security#how-network-security-works):
  - If network security is disabled, all traffic is allowed by default, and remote clusters work without requiring any specific filtering policy.
  - If network security is enabled on the remote cluster, apply a [remote cluster filter](/docs/deploy-manage/security/remote-cluster-filtering#create-remote-cluster-filter) to allow incoming connections from the local clusters. Without this filter, the connections are blocked.
  </note>

This section explains how remote clusters interact with network security when using API key–based authentication, and describes the supported use cases.

### Filter types and supported use cases for remote cluster traffic

With API key–based authentication, remote clusters require the local cluster (A) to trust the transport SSL certificate presented by the remote cluster server (B). When network security is enabled on the destination cluster (B), it’s also necessary to explicitly allow the incoming traffic from cluster A. This can be achieved using different types of traffic filters:
- [Remote cluster filters](https://www.elastic.co/docs/deploy-manage/security/remote-cluster-filtering), available exclusively in ECH and ECE. They allow filtering by organization ID or Elasticsearch cluster ID and are the recommended option, as they combine mTLS with API key authentication for stronger security.
- [IP filters](https://www.elastic.co/docs/deploy-manage/security/ip-filtering), which allow traffic based on IP addresses or CIDR ranges.

The applicable filter type for the remote cluster depends on the local and remote deployment types:

| Remote cluster → Local cluster ↓               | Elastic Cloud Hosted                                                                                 | Elastic Cloud Enterprise                                                                                                                                                                | Self-managed / Elastic Cloud on Kubernetes                                                                                                                                           |
|------------------------------------------------|------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Elastic Cloud Hosted**                       | [Remote cluster filter](https://www.elastic.co/docs/deploy-manage/security/remote-cluster-filtering) | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering)                                                                                                            | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering) or [Kubernetes network policy](https://www.elastic.co/docs/deploy-manage/security/k8s-network-policies) |
| **Elastic Cloud Enterprise**                   | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering)                         | [Remote cluster filter](https://www.elastic.co/docs/deploy-manage/security/remote-cluster-filtering) / [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering) (*) | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering) or [Kubernetes network policy](https://www.elastic.co/docs/deploy-manage/security/k8s-network-policies) |
| **Self-managed / Elastic Cloud on Kubernetes** | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering)                         | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering)                                                                                                            | [IP filter](https://www.elastic.co/docs/deploy-manage/security/ip-filtering) or [Kubernetes network policy](https://www.elastic.co/docs/deploy-manage/security/k8s-network-policies) |

(*) For ECE, remote cluster filters apply when both clusters are in the **same environment**. Use IP filters when the clusters belong to **different environments**.
<note>
  When using self-managed security mechanisms (such as firewalls), keep in mind that remote clusters with API key–based authentication use port `9443` by default. Specify this port if a destination port is required.
</note>