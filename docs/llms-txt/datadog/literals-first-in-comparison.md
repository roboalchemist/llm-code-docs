# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/literals-first-in-comparison.md

---
title: The literals should be first in String comparisons
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > The literals should be first in String comparisons
---

# The literals should be first in String comparisons

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/literals-first-in-comparison`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

One should always prioritize using a string literal as the first arguments in any string comparison. This approach serves as a preventive measure against `NullPointerExceptions` because when the second argument is null, instead of encountering an exception, the comparisons will simply yield false results.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Foo {
    boolean bar(String x) {
        return x.equals("42"); // should be "42".equals(x)
    }
    boolean bar(String x) {
        return x.equalsIgnoreCase("42"); // should be "42".equalsIgnoreCase(x)
    }
    boolean bar(String x) {
        return (x.compareTo("bar") > 0); // should be: "bar".compareTo(x) < 0
    }
    boolean bar(String x) {
        return (x.compareToIgnoreCase("bar") > 0); // should be: "bar".compareToIgnoreCase(x) < 0
    }
    boolean baz(String x) {
        return x.contentEquals("baz"); // should be "baz".contentEquals(x)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Foo {
    boolean bar(String x) {
        return "42".equals(x);
    }
    boolean bar(String x) {
        return "42".equalsIgnoreCase(x);
    }
    boolean bar(String x) {
        return "bar".compareTo(x) < 0;
    }
    boolean bar(String x) {
        return "bar".compareToIgnoreCase(x) < 0;
    }
    boolean baz(String x) {
        return "baz".contentEquals(x);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 