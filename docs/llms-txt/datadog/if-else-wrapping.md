# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/kotlin-code-style/if-else-wrapping.md

---
title: Enforce single line if statement styling
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Enforce single line if statement styling
---

# Enforce single line if statement styling

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `kotlin-code-style/if-else-wrapping`

**Language:** Kotlin

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

Inconsistent formatting of our if/else statements could mislead you to their structure, especially if you have multiple nested if/else statements.

- Use braces whenever you nest an 'if' statement inside another 'if' statement, except for `if ... else if ...` sequences.
- If one of the branches of the 'if' statement uses braces, use braces in both branches.
- Short, single-line branches of an 'if' statement should not use braces. If you must use braces, split it into several lines.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```kotlin
fun foobar() {
    if (true) if (false) foo()
    if (true)
        foo()
    else
        if (false)
            bar()
    if (true) { foo() }
    if (true) {
        foo()
    } else { bar() }

    if (true) {
        foo()
    } else bar()
    if (true) foo()
    else {
        bar()
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```kotlin
fun foobar() {
    if (true) foo()
    if (true) foo() else bar()
    if (true) foo() else if (false) bar() else baz()

    if (true)
        foo()
    else if (false)
        bar()

    if (true)
        foo()
    else
        bar()

    if (true) {
        if (false) foo() else bar()
    } else {
        bar()
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 