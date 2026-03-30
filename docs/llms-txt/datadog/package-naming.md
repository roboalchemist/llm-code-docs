# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/package-naming.md

---
title: Enforce packing naming convention
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce packing naming convention
---

# Enforce packing naming convention

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/package-naming`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Package names in Kotlin should be lowercase, and should not contain underscores.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
package foo.`foo bar`
```

```kotlin
package `foo bar`
```

```kotlin
package Foo
```

```kotlin
package foo.Foo
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
package foo.bar
```

```kotlin
package foo
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
