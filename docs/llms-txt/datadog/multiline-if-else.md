# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/multiline-if-else.md

---
title: Braces required for multiline if or if/else statements.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Braces required for multiline if or if/else statements.
---

# Braces required for multiline if or if/else statements.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/multiline-if-else`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule enforces the use of curly braces (`{}`) for `if` and `if`/`else` statements in Kotlin when their bodies span multiple lines. Omitting braces in such cases can introduce ambiguity, making the code's control flow unclear and potentially leading to logical errors if additional statements are introduced without careful re-evaluation. This practice is crucial for maintaining code readability and preventing the "dangling else" problem, where an `else` branch might inadvertently associate with the wrong `if` statement.

## How to remediate{% #how-to-remediate %}

To remediate this, always enclose the multiline body of `if` and `else` statements within curly braces. This explicit encapsulation clearly defines the scope of the conditional blocks, enhancing code clarity and maintainability. For instance, transform `if (condition)\n statement1\n statement2` into `if (condition) {\n statement1\n statement2\n}`. Applying braces consistently ensures that your code behaves as intended and is easier to understand and debug for other developers.

## Arguments{% #arguments %}

- `foo`: Blah

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
if (true)
    doSomething()
else
    doSomethingElse()

private fun doSomethingFunc() {
    if (1 != 2) // A Comment
        doSomething()
    else // Another comment 
        doSomething()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
if (true) {
    doSomething()
} else {
    doSomethingElse()
}

if (true) doSomething()

if (true)
    return 1

if ((now - prev) < CONSTANT_VAL
    && !otherCondition // only in special cases
) {
    log.debug("A Log Line")
    return
}

if (true) {
    doSomething()
    doSomethingElse()
} else {
    doSomethingElse()
    doSomethingElse()
    doSomethingElse()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 