# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/multiple-entrypoint.md

---
title: Do not use multiple ENTRYPOINT
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not use multiple ENTRYPOINT
---

# Do not use multiple ENTRYPOINT

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/multiple-entrypoint`

**Language:** Docker

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not use multiple `ENTRYPOINT` instructions, only the last one is used.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
FROM awesomeimage
ENTRYPOINT /foo/bar
ENTRYPOINT /foo/baz
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
FROM awesomeimage
ENTRYPOINT /foo/bar
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 