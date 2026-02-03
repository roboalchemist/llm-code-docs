# Source: https://docs.datadoghq.com/security/default_rules/def-000-1km.md

---
title: Route uses HTTP to connect to external APIs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Route uses HTTP to connect to external
  APIs
---

# Route uses HTTP to connect to external APIs
 
## Description{% #description %}

The service communicates with third-party APIs using HTTP. The request or its response may be tampered with between your server and that of the third party. Moreover, the content of the request or response may be inspected.

## Rationale{% #rationale %}

This finding works by identifying an API that makes use of an external HTTP dependency over an insecure protocol (HTTP).

## Remediation{% #remediation %}

- Perform calls to external APIs over HTTPS.
