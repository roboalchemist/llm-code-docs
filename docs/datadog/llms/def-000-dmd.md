# Source: https://docs.datadoghq.com/security/default_rules/def-000-dmd.md

---
title: >-
  OpenSearch domain connections should be encrypted using the latest TLS
  security policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > OpenSearch domain connections should be
  encrypted using the latest TLS security policy
---

# OpenSearch domain connections should be encrypted using the latest TLS security policy

## Description{% #description %}

This control checks whether an Amazon OpenSearch Service domain endpoint is configured to use the latest TLS security policy, `Policy-Min-TLS-1-2-PFS-2023-10`. The control fails if the endpoint is not using this policy or if HTTPS is not enabled. Enforcing the latest version of TLS 1.2 helps secure data in transit by preventing eavesdropping and manipulation through man-in-the-middle attacks.

## Remediation{% #remediation %}

To configure your Amazon OpenSearch Service domain endpoint to use the latest TLS security policy, refer to the [Requiring HTTPS for Amazon OpenSearch Service Domains](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-domain.html#enforce-https) section of the Amazon OpenSearch Service Developer Guide.
