# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/no-empty-class-bodies.md

---
title: Class bodies should not be empty
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Class bodies should not be empty
---

# Class bodies should not be empty

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/no-empty-class-bodies`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Kotlin, Class bodies should not be empty. It can make it unclear whether the class is intended to be used as a placeholder or if it is just incomplete.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
class Foo {}

data class Bar(val v: Any) { }

interface Baz {

}

object FooBar {}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
class Foo

data class Bar(val v: Any)

interface Baz

object FooBar
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 