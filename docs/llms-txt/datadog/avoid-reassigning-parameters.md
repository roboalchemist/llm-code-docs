# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-best-practices/avoid-reassigning-parameters.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-reassigning-parameters.md

---
title: Avoid reassigning parameters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid reassigning parameters
---

# Avoid reassigning parameters

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-reassigning-parameters`

**Language:** Java

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

Avoid reassigning values to method parameters as it can make the code harder to understand. Typically, parameter values are expected to remain unchanged throughout the method's execution, and any reassignment might be not be noticed by other developers.

We consider it acceptable to reassign parameters in small functions, smaller than 20 lines. Otherwise, consider using temporary local variables with clear naming to enhance code readability.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Person {
  private void greet(String name) {
    System.println("this is a long method");
    System.println("this is a very long method");
    name = name.trim(); // reassigning parameter value
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
    System.println("this is a long method");
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Main {
    public static void subscribeResult(
        @Advice.Enter final int callDepth,
        @Advice.Origin final Method method,
        @Advice.FieldValue("bucket") final String bucket,
        @Advice.Return(readOnly = false) Observable result) {
      if (callDepth > 0) {
        return;
      }
      CallDepthThreadLocalMap.reset(CouchbaseCluster.class);

      result = Observable.create(new CouchbaseOnSubscribe(result, method, bucket));
    }
}
```

```java
public class Main {
    private static void addStrSegment(List<LogProbe.Segment> segments, String str) {
        str = Strings.replace(str, "{{", "{");
        str = Strings.replace(str, "}}", "}");
        segments.add(new LogProbe.Segment(str));
    }
}
```

```java
public class Person {
  private void greet(String name) {
    String trimmedName = name.trim();
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 