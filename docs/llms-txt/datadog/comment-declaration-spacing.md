# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/comment-declaration-spacing.md

---
title: Enforce proper spacing for declarations with comments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce proper spacing for declarations with comments
---

# Enforce proper spacing for declarations with comments

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/comment-declaration-spacing`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Declarations with comments should be separated by a blank line to improve readability of code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
// some comment 1
bar()
/*
 * some comment 2
 */
foo()
// some comment 1
bar()
/*
 * some comment 2
 */
foo()
// testing 1
/*
 * some comment 2
 */
foo()
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
// some comment 1
bar()

/*
 * some comment 2
 */
foo()
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 