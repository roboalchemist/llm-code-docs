# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/for-loop-should-be-while-loop.md

---
title: Simplify for loops for while loops
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Simplify for loops for while loops
---

# Simplify for loops for while loops

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/for-loop-should-be-while-loop`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

This rule identifies instances where simplifying for loops is possible which can make these loops more concise.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
// No init or update nodes; can be rewritten `while (condition)`
public class Foo {
    void bar() {
        for(;true;) true;

        for(; true ;){
        	System.out.println("bar");
        }
        
        for(; i < 42 ;) true;
        
        for(;;);
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    void bar() {
        for(int i = 0; i < 42; i++);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 