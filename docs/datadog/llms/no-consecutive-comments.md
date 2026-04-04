# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-consecutive-comments.md

---
title: Enforce correct block comment usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce correct block comment usage
---

# Enforce correct block comment usage

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-consecutive-comments`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Consecutive block comments are not allowed. However, block comments followed by line comments and vice versa are allowed, as long as there is at least one blank line between them.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
/*
 * Block comments can not be consecutive ...
 */

/*
 * ... even when separated by a new line.
 */

// Two comments
/* With no line in between */
// Foo
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// An EOL comment
// may be followed by another EOL comment
val foo = "foo"

// Different comment types (including KDoc) may be consecutive ..

/*
 * ... but do need to be separated by a blank line ...
 */

// ... as demonstrated here
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
