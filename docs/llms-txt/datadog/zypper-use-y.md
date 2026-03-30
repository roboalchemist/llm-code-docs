# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/zypper-use-y.md

---
title: Always use -y with zypper install
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Always use -y with zypper install
---

# Always use -y with zypper install

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/zypper-use-y`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When using `zypper` to install a package, make sure you use the `-y` flag to avoid your CI being blocked on a prompt.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN zypper install httpd-2.4.46
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN zypper install -y httpd-2.4.46
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
