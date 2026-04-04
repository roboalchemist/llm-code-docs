# Source: https://docs.datadoghq.com/security/default_rules/def-000-l4f.md

---
title: Elasticsearch domains should have at least three dedicated master nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Elasticsearch domains should have at
  least three dedicated master nodes
---

# Elasticsearch domains should have at least three dedicated master nodes

## Description{% #description %}

This control verifies whether Elasticsearch domains are configured with at least three dedicated primary nodes and ensures that dedicated master is enabled.

**Note**: Using more than three primary nodes may be excessive for mitigating availability risks and can lead to higher costs. For high availability and fault tolerance, an Elasticsearch domain should have at least three dedicated primary nodes. These nodes can become heavily utilized during data node blue/green deployments due to the additional management required. Ensuring an Elasticsearch domain has at least three dedicated primary nodes provides adequate primary node resources and maintains cluster operations in the event of a node failure.

## Remediation{% #remediation %}

To modify the number of data nodes in an Elasticsearch domain:

1. Log in to the [Amazon OpenSearch Service console](https://console.aws.amazon.com/aos/).
1. Under `Domains`, choose the name of the domain you want to edit.
1. Click `Edit domain`.
1. Under `Dedicated master nodes`, set `Instance type` to the desired instance type.
1. Set `Number of master nodes` equal to three or greater.
1. Click `Submit`.
