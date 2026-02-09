# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/block-comment-formatting.md

---
title: Enforce block comment alignment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce block comment alignment
---

# Enforce block comment alignment

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/block-comment-formatting`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Block comments should contain asterisks that visually form a vertical line. This promotes visual simplicity and makes the comment easier to read.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
/*
 * This comment is not formatted well.
   */

/*
  * This comment is not either.
 */

/*
*   Nor is this comment.
 */
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
/*
 * This comment is formatted well.
 */

        /*
         * As is this comment.
         */
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 