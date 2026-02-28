# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/no-root-user.md

---
title: Last user should not be root
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Last user should not be root
---

# Last user should not be root

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/no-root-user`

**Language:** Docker

**Severity:** Warning

**Category:** Security

## Description{% #description %}

Do not use `root` as the last user because your container runs with the `root` user. Always use a user with lower privileges.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
CMD foo
USER plop
CMD plip
USER root
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
CMD foo
USER root
CMD plip
USER normaluser
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
