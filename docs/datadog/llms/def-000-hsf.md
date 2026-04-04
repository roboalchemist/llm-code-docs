# Source: https://docs.datadoghq.com/security/default_rules/def-000-hsf.md

---
title: OpenSearch domains should have fine-grained access control enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domains should have
  fine-grained access control enabled
---

# OpenSearch domains should have fine-grained access control enabled

## Description{% #description %}

This control checks whether Amazon OpenSearch Service domains have fine-grained access control (FGAC) enabled. Fine-grained access control provides granular permissions management, including index-level, document-level, and field-level security. The control fails if FGAC is not enabled, as it is required through the advanced-security-options in the OpenSearch parameter update-domain-config. Enabling FGAC enhances data security by offering additional methods to control access to your data on Amazon OpenSearch Service.

## Remediation{% #remediation %}

To enable fine-grained access control for an Amazon OpenSearch Service domain, refer to the [Fine-Grained Access Control in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/fgac.html) section of the Amazon OpenSearch Service Developer Guide.
