# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/value-argument-comment.md

---
title: Enforce comment placement in value argument
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce comment placement in value argument
---

# Enforce comment placement in value argument

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/value-argument-comment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Having comments between the name of a named argument and its value makes code harder to read and can lead to confusion.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
doTask(name = "parse", filename = /* A list of IP addresses */ "ips.txt")

doTask(
    name = "parse",
    filename =
    // A list of IP addresses
        "ips.txt"
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
doTask(name = "parse", filename = "ips.txt")
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 