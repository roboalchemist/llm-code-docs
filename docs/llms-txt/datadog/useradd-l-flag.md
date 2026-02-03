# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/docker-best-practices/useradd-l-flag.md

---
title: Use -l with useradd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use -l with useradd
---

# Use -l with useradd

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `docker-best-practices/useradd-l-flag`

**Language:** Docker

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

When building Docker images, using `useradd -l` ensures that the new user is created without adding entries to system login tracking files like `/var/log/lastlog` or `/var/log/faillog`. These files are irrelevant in containers since they don't persist user sessions or keep login histories, and in minimal images they may not even exist, which can lead to errors or unnecessary file creation during build.

This makes your image smaller, cleaner, and more reliable. Since containers are designed to run processes rather than serve as full login environments, disabling login record tracking speeds up builds, avoids warnings, and follows best practices for lightweight, secure Docker images.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```docker
RUN useradd -u 123456 foobar
```

## Compliant Code Examples{% #compliant-code-examples %}

```docker
RUN useradd -l -u 123456 foobar
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 