# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/no-single-line-block-comment.md

---
title: Use an EOL comment over a single line block comment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use an EOL comment over a single line block comment
---

# Use an EOL comment over a single line block comment

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/no-single-line-block-comment`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule flags single-line block comments (`/* ... */`) that could be more appropriately replaced by end-of-line (EOL) comments (`// ...`). A violation occurs when a block comment starts and ends on the same line and is followed only by whitespace until the end of the line. While syntactically valid, using `/* ... */` for such cases can be less clear, potentially misleading developers into thinking it's part of a larger multi-line comment block.

## How to remediate{% #how-to-remediate %}

To fix this, replace the single-line block comment with an end-of-line comment. For example, change `/* Some comment */` to `// Some comment`. This improves code readability and aligns with common Kotlin style guidelines where `//` is used for concise, single-line explanations and `/* */` is reserved for multi-line documentation or temporarily disabling code blocks.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
/* Some comment */

val foo = "foo" /* Some comment */
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
/*
 * Some comment
 */
val foo = "foo" // Some comment
val foo = { /* no-op */ }

/** Documentation */
val foo = "foo"
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 