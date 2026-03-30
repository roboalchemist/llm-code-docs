# Source: https://www.elastic.co/docs/deploy-manage/autoscaling

﻿---
title: Autoscaling
description: The autoscaling feature adjusts resources based on demand. A deployment can use autoscaling to scale resources as needed, ensuring sufficient capacity...
url: https://www.elastic.co/docs/deploy-manage/autoscaling
products:
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
---

# Autoscaling
The autoscaling feature adjusts resources based on demand. A deployment can use autoscaling to scale resources as needed, ensuring sufficient capacity to meet workload requirements. In Elastic Cloud Enterprise, Elastic Cloud on Kubernetes, and Elastic Cloud Hosted deployments, autoscaling follows predefined policies, while in Serverless, it is fully managed and automatic.
<tip>
  By default, Elastic Cloud Serverless automatically scales your Elasticsearch resources based on your usage. You don't need to enable autoscaling.
</tip>


## Cluster autoscaling

<admonition title="Indirect use only">
  This feature is designed for indirect use by Elastic Cloud Hosted, Elastic Cloud Enterprise, and Elastic Cloud on Kubernetes. Direct use is not supported.
</admonition>

Cluster autoscaling allows an operator to create tiers of nodes that monitor themselves and determine if scaling is needed based on an operator-defined policy. An Elasticsearch cluster can use the autoscaling API to report when additional resources are required. For example, an operator can define a policy that scales a warm tier based on available disk space. Elasticsearch monitors disk space in the warm tier. If it predicts low disk space for current and future shard copies, the autoscaling API reports that the cluster needs to scale. It remains the responsibility of the operator to add the additional resources that the cluster signals it requires.
A policy is composed of a list of roles and a list of deciders. The policy governs the nodes matching the roles. The deciders provide independent estimates of the capacity required. See [Autoscaling deciders](https://www.elastic.co/docs/deploy-manage/autoscaling/autoscaling-deciders) for details on available deciders.
Cluster autoscaling supports:
- Scaling machine learning nodes up and down.
- Scaling data nodes up based on storage.


## Trained model autoscaling

<admonition title="Trained model auto-scaling for self-managed deployments">
  The available resources of self-managed deployments are static, so trained model autoscaling is not applicable. However, available resources are still segmented based on the settings described in this section.
</admonition>

Trained model autoscaling automatically adjusts the resources allocated to trained model deployments based on demand. This feature is available on all cloud deployments (ECE, ECK, ECH) and Serverless. Refer to [Trained model autoscaling](https://www.elastic.co/docs/deploy-manage/autoscaling/trained-model-autoscaling) for details.
To ensure availability and avoid unnecessary scaling, trained model deployments operate with defined [cooldown periods](/docs/deploy-manage/autoscaling/trained-model-autoscaling#cooldown-periods).
Trained model autoscaling supports:
- Scaling trained model deployments

<note>
  Autoscaling is not supported on Debian 8.
</note>

Find instructions on setting up and managing autoscaling, including supported environments, configuration options, and examples:
- [Autoscaling in Elastic Cloud Enterprise and Elastic Cloud Hosted](https://www.elastic.co/docs/deploy-manage/autoscaling/autoscaling-in-ece-and-ech)
- [Autoscaling in Elastic Cloud on Kubernetes](https://www.elastic.co/docs/deploy-manage/autoscaling/autoscaling-in-eck)
- [Autoscaling deciders](https://www.elastic.co/docs/deploy-manage/autoscaling/autoscaling-deciders)
- [Trained model autoscaling](https://www.elastic.co/docs/deploy-manage/autoscaling/trained-model-autoscaling)