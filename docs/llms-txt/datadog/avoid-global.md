# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/apex-code-style/avoid-global.md

---
title: Avoid global definitions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid global definitions
---

# Avoid global definitions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `apex-code-style/avoid-global`

**Language:** Apex

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

This rule discourages the use of the `global` access modifier for classes, variables, methods, and inner classes in Apex code. Declaring elements as `global` exposes them beyond the namespace boundary, making them accessible to all Apex code in any installed package or org, which can lead to unintended dependencies and security concerns.

To comply with this rule, use more restrictive access modifiers such as `private`, `protected`, or `public` whenever possible. For example, instead of `global class MyClass`, declare it as `public class MyClass` unless there is a compelling reason to expose it globally. Similarly, avoid defining variables or methods as `global`; prefer `private` or `public` based on the intended visibility.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```
global without sharing class GlobalClass {
    global String globalAttribute = 'my-attr';


    global static void globalStaticMethod() { }

    global class GlobalInnerClass { }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```
private class PrivateClass {
    global void exposedMethod() {
        // foobar
    }
}
```

```
class NotGlobalClass {
    String notGlobalAttribute = 'my-attr';

    static void staticMethod() { }

    class InnerClass { }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
