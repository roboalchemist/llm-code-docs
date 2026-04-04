# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-best-practices/no-empty-file.md

---
title: A Kotlin (script) file should not be empty.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > A Kotlin (script) file should not be empty.
---

# A Kotlin (script) file should not be empty.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-best-practices/no-empty-file`

**Language:** Kotlin

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

A Kotlin (script) file should not be empty. It needs to contain at least one declaration. Files only containing a package and/or import statements are disallowed.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
package foo

import foo
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
package test.foo.bar

import foo

fun foo() {
    println("File has declaration")
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
