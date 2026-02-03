# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/parens-before-trailing-lambda.md

---
title: An empty parentheses block before a lambda is redundant.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > An empty parentheses block before a lambda is redundant.
---

# An empty parentheses block before a lambda is redundant.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/parens-before-trailing-lambda`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

If a function has a lambda parameter and you're passing a lambda expression, parentheses are unnecessary. Including unnecessary syntax makes the code less readable.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
val foo = "some-string".count() { it == '-' }
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
val foo = "some-string".count { it == '-' }
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 