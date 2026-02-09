# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/no-wildcard-import.md

---
title: No wildcard imports
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > No wildcard imports
---

# No wildcard imports

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/no-wildcard-import`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Wild card imports should be avoided in favor of directly importing a class or function. This rule helps to ensure dependencies are explicitly defined.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
import foobar.foo.*
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
import foo
import foobar.Bar
import foobar.Foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 