# Source: https://docs.datadoghq.com/security/default_rules/def-000-b6i.md

---
title: OpenSearch domains should have at least three data nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domains should have at least
  three data nodes
---

# OpenSearch domains should have at least three data nodes

## Description{% #description %}

This check determines if Amazon OpenSearch Service domains are configured with at least three data nodes. Having a minimum of three data nodes is crucial for ensuring data availability and fault tolerance, especially in case of node failures or maintenance activities. It enhances the resiliency of your OpenSearch cluster by allowing it to continue operating even if one or two nodes become unavailable.

## Remediation{% #remediation %}

To configure an Amazon OpenSearch Service domain with at least three data nodes, refer to the [Managing Amazon OpenSearch Service Domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains.html) section of the Amazon OpenSearch Service Developer Guide.
