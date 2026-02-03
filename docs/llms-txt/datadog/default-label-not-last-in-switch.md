# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/default-label-not-last-in-switch.md

---
title: Default label should be last in a switch
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Default label should be last in a switch
---

# Default label should be last in a switch

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/default-label-not-last-in-switch`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

The widely adopted convention is putting the `default` statement at the end of a `switch` statement. By adhering to this practice, your code becomes more comprehensible and predictable for developers who engage with it in the future.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
   void bar(int a) {
      switch (a) {
         case 1:
            break;
         default:  // this should be the last statement
            break;
         case 2:
            break;
         case 3:
            break;
      }
   }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
   void bar(int a) {
      switch (a) {
         case 1:
            break;
         case 2:
            break;
      }
   }
}
```

```java
public class Foo {
   void bar(int a) {
      switch (a) {
         case 1:  // do something
            break;
         case 2:
            break;
         default:  // the default case should be last, by convention
            break;
      }
   }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 