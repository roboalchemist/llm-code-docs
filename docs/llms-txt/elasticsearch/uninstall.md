# Source: https://www.elastic.co/docs/deploy-manage/uninstall

﻿---
title: Uninstall
description: Uninstalling Elastic components, such as Elasticsearch clusters, deployments, or orchestrators, may be necessary for several reasons. You might need to...
url: https://www.elastic.co/docs/deploy-manage/uninstall
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud Serverless
  - Elastic Cloud on Kubernetes
  - Elastic Stack
  - Elasticsearch
applies_to:
  - Elastic Cloud Serverless: Generally available
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Uninstall
Uninstalling Elastic components, such as Elasticsearch clusters, deployments, or orchestrators, may be necessary for several reasons. You might need to decommission a host, scale down a self-managed cluster, recover from an installation issue that can't be resolved, or start fresh with a clean setup.
Different Elastic environments require different uninstallation steps. Choose the guide that matches your setup:
- Uninstall an orchestrator:
  - [Uninstall an Elastic Cloud Enterprise host](https://www.elastic.co/docs/deploy-manage/uninstall/uninstall-elastic-cloud-enterprise)
- [Uninstall Elastic Cloud on Kubernetes operator](https://www.elastic.co/docs/deploy-manage/uninstall/uninstall-elastic-cloud-on-kubernetes)
- Delete an orchestrated deployment:
  - [Elastic Cloud Hosted deployments](/docs/deploy-manage/uninstall/delete-a-cloud-deployment#elastic-cloud-hosted)
- [Serverless projects](/docs/deploy-manage/uninstall/delete-a-cloud-deployment#serverless)
- [Elastic Cloud Enterprise deployments](/docs/deploy-manage/uninstall/delete-a-cloud-deployment#ece)

<note>
  You can uninstall Elasticsearch nodes or Kibana instances on self-managed clusters, but step-by-step instructions are not currently available. For more details on the implications of removing Elasticsearch nodes, refer to [Add and Remove Elasticsearch nodes](https://www.elastic.co/docs/deploy-manage/maintenance/add-and-remove-elasticsearch-nodes).
</note>