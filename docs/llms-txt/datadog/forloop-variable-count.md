# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/forloop-variable-count.md

---
title: Too many control variables in for loop
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Too many control variables in for loop
---

# Too many control variables in for loop

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/forloop-variable-count`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The presence of multiple control variables in a `for` loop can obscure the range of values over which the loop iterates and make your code brittle and difficult to debug.

To follow this rule, regular `for` loops should have only one control variable.

## Arguments{% #arguments %}

- `max-variables`: Maximum number of control variables. Default: 1.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Main {
   public void foo() {
      for (int i = 0, j = 0; i < 10; i++, j += 2) { // more than one control variable
         foo();
      }
   }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Main {
   public void foo() {
      for (int i = 0; i < 10; i++) {
         foo();
      }
   }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 