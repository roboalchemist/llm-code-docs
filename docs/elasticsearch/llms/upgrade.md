# Source: https://www.elastic.co/docs/deploy-manage/upgrade

﻿---
title: Upgrade your deployment, cluster, or orchestrator
description: Upgrading to the latest version provides access to the newest Elastic features, security patches, performance improvements, and bug fixes. These updates...
url: https://www.elastic.co/docs/deploy-manage/upgrade
products:
  - Elastic Cloud Enterprise
  - Elastic Cloud Hosted
  - Elastic Cloud on Kubernetes
  - Elasticsearch
  - Kibana
applies_to:
  - Elastic Cloud Hosted: Generally available
  - Elastic Cloud on Kubernetes: Generally available
  - Elastic Cloud Enterprise: Generally available
  - Self-managed Elastic deployments: Generally available
---

# Upgrade your deployment, cluster, or orchestrator
Upgrading to the latest version provides access to the newest Elastic features, security patches, performance improvements, and bug fixes. These updates reduce costs, speed up threat response, and improve investigative and analytical data tools.
As Elastic releases new versions, older versions of Elastic products reach their end of life on a set schedule. To keep your deployment supported, stay up to date. For more information, refer to [Product End of Life Dates](https://www.elastic.co/support/eol).
<note>
  With [Elastic Cloud Serverless](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/serverless), upgrades of the Elastic-managed infrastructure and project components are fully handled by Elastic. Users automatically receive the latest features and improvements, with no need to plan or perform project-level upgrades.Keep in mind that the [ingest components](https://www.elastic.co/docs/deploy-manage/upgrade/ingest-components) or clients you manage externally, such as Elastic Agent, Beats, Logstash, or custom applications, still need to be updated manually.
</note>

The upgrade procedure depends on how your deployment is managed. If you're using Elastic Cloud Hosted or Elastic Cloud Enterprise, upgrades can often be performed with a single click in the Elastic Cloud UI. For self-managed deployments, upgrades must be carried out manually using a rolling upgrade process, upgrading the nodes one by one to minimize downtime and ensure cluster stability.
This section provides guidance to help you plan and safely perform upgrades of your Elastic Stack components, with a primary focus on Elasticsearch and Kibana as the core of the stack. It also covers upgrades for orchestration platforms like Elastic Cloud Enterprise and Elastic Cloud on Kubernetes, as well as related components such as APM, Beats, Elastic Agent, and Logstash.
<important>
  In Elastic Stack 9.0.0 and beyond, Enterprise Search is unavailable. For more information, refer to [Migrating to 9.x from Enterprise Search 8.x versions](https://www.elastic.co/guide/en/enterprise-search/8.19/upgrading-to-9-x.html).
</important>


## Upgrade overview

Upgrading your Elastic cluster or deployment involves several stages, including planning, preparation, and execution. This section guides you through the full upgrade process:
- [Plan your upgrade](https://www.elastic.co/docs/deploy-manage/upgrade/plan-upgrade): Review compatibility, define your upgrade path and order, and understand important pre-upgrade considerations.
- [Prepare to upgrade](https://www.elastic.co/docs/deploy-manage/upgrade/prepare-to-upgrade): Follow detailed preparation steps for major, minor, and patch upgrades. Identify breaking changes, run the Upgrade Assistant (for major upgrades), and verify readiness.
- [Upgrade your deployment or cluster](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster): Step-by-step instructions for performing the upgrade, organized by deployment type:
  - [Upgrade deployments on Elastic Cloud Hosted](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/upgrade-on-ech)
- [Upgrade deployments on Elastic Cloud Enterprise](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/upgrade-on-ece)
- [Upgrade deployments on Elastic Cloud on Kubernetes](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/upgrade-on-eck)
- [Upgrade self-managed clusters](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/self-managed)
- [Upgrade ingest components](https://www.elastic.co/docs/deploy-manage/upgrade/ingest-components): Covers supporting components such as Beats, Elastic Agent, Logstash, and APM Server.

<note>
  If you’re still running Elastic Stack version 7.17 or earlier, refer to the [Upgrade from 7.17 guide](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/upgrade-717) for detailed guidance on planning and executing the upgrade to the latest 9.3.1 release.
</note>

Additionally, if you're using a self-managed orchestration platform such as Elastic Cloud Enterprise or Elastic Cloud on Kubernetes, refer to [Upgrade your ECE or ECK orchestrator](https://www.elastic.co/docs/deploy-manage/upgrade/orchestrator) to keep the orchestrator up to date.

## Availability during upgrades

Elasticsearch supports rolling upgrades, where nodes are upgraded one at a time to minimize downtime and ensure cluster stability. If your deployment or cluster follows high availability best practices, such as using replicated indices and distributing nodes across multiple availability zones, it should remain available throughout the entire upgrade process.
Kibana upgrades, however, require downtime. All running instances must be shut down before starting the upgrade.
<important>
  Ensure your deployment is properly sized and configured for high availability to reduce the risk of service interruption during upgrades.If you want to learn more about scaling, high availability, and performance, refer to:
  - [Run Elasticsearch in production](https://www.elastic.co/docs/deploy-manage/production-guidance/elasticsearch-in-production-environments)
  - [Run Kibana in production](https://www.elastic.co/docs/deploy-manage/production-guidance/kibana-in-production-environments)
  - [Elastic Cloud Hosted > Plan for production](https://www.elastic.co/docs/deploy-manage/deploy/elastic-cloud/elastic-cloud-hosted-planning)
</important>

You’ll find more information about availability considerations for specific deployment types in the related upgrade guides within this section.

## Upgrade paths

You can upgrade to a higher version if the target version was released *after* your current version. Upgrades to versions released *before* your current version are not supported, even if the version number is higher. Refer to [out-of-order releases](/docs/deploy-manage/upgrade/deployment-or-cluster#out-of-order-releases) for more information.
For example:
- ✅ Upgrade allowed: From 9.0.4 to 9.1.0 (9.1.0 released *after* 9.0.4)
- ❌ Not allowed: From 9.0.5 to 9.1.0 (9.1.0 released *before* 9.0.5) → wait for 9.1.1 to be released


### Upgrade paths from 8.x

To perform a major upgrade from 8.x, the required starting version depends on the target release:
- To upgrade to the **9.0.x series**, you must be on **8.18.x**.
- To upgrade to **9.1.0 or later**, you must be on **8.19.x**, which is the latest minor release of the 8.x series.

<note>
  While 8.19 is the final minor release in the 8.x series, 8.18 was released at the same time as 9.0, enabling a supported upgrade path between the 8.18.x and 9.0.x series. This compatibility also applies to other features and clients.
</note>

If you're upgrading to the current 9.3.1 release from an earlier 8.x version, first upgrade to the latest available 8.19 release.

#### Ingest tools and clients considerations

For flexible upgrade scheduling, 8.19 Elastic Agent, Beats, and Logstash are compatible with all 9.x versions of Elasticsearch.
By default, 8.x Elasticsearch clients are compatible with 9.x and use [REST API compatibility](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/compatibility) to maintain compatibility with the 9.x cluster.

### Upgrade paths from 7.17

Upgrading from Elastic Stack version 7.17 to the latest 9.3.1 release involves two major upgrades:
- From 7.17 to 8.19
- From 8.19 to 9.3.1

For detailed guidance on planning and executing these upgrades, refer to the [Upgrade from 7.17 guide](https://www.elastic.co/docs/deploy-manage/upgrade/deployment-or-cluster/upgrade-717).