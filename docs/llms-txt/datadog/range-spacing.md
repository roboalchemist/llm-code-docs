# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/range-spacing.md

---
title: Enforce range operator spacing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce range operator spacing
---

# Enforce range operator spacing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/range-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Kotlin suggests having consistent spacing around range operators by having no spacing.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val foo1 = (1.. 12 step 2).last
val foo2 = (1 .. 12 step 2).last
val foo3 = (1 ..12 step 2).last
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val foo1 = (1..12 step 2).last
val foo2 = (1..12 step 2).last
val foo3 = (1..12 step 2).last
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
