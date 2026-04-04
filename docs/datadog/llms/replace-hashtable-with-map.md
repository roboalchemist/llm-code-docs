# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/replace-hashtable-with-map.md

---
title: Should use Map instead of Hashtable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Should use Map instead of Hashtable
---

# Should use Map instead of Hashtable

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/replace-hashtable-with-map`

**Language:** Java

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

If your application does not require thread safety, it is recommended to use the modern `java.util.Map` interface instead of `java.util.Hashtable`.

`Map` offers efficient implementations like `HashMap`, which offer greater flexibility and faster execution. If thread safety is needed, you can opt for `ConcurrentHashMap`, which maintains thread safety while still adhering to modern coding practices associated with `Map`.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    void bar() {
        Hashtable hashtable1 = new Hashtable(); // consider using java.util.Map instead
        Hashtable<String, Integer> hashtable2 = new Hashtable<>();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    void bar() {
        Map<String, Integer> h = new HashMap<>();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
