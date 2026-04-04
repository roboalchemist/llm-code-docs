# Source: https://docs.datadoghq.com/security/default_rules/def-000-jpd.md

---
title: Missing Referrer-Policy Security HTTP header
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Missing Referrer-Policy Security HTTP
  header
---

# Missing Referrer-Policy Security HTTP header

## Description{% #description %}

This publicly exposed API endpoint was found responding with HTML or browser-rendered content and lacks the Referrer-Policy header. Setting this header prevents leaking sensitive URL data (tokens, IDs, parameters) if requests go to external domains.

## Remediation{% #remediation %}

Add the Referrer-Policy header to prevent leaking URL information if the content is rendered:

Example header values:

```
# If your site makes no use of referrer
Referrer-Policy: no-referrer

# Alternatively use this if referrer can be utilized by your app
Referrer-Policy: strict-origin-when-cross-origin
```
