# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/loose-coupling.md

---
title: Avoid using specific implementation types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid using specific implementation types
---

# Avoid using specific implementation types

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/loose-coupling`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Relying on particular implementation types, such as, `HashSet` or `LinkedList` can limit your adaptability to embrace alternative implementations in the future, particularly as your requirements change and your code needs to undergo changes.

It is recommended to opt for general types such as `Set` or `List` when declaring variables and parameters.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;

public class Foo {
    private ArrayList<SomeType> list = new ArrayList<>();

    public HashSet<SomeType> set = new HashSet<SomeType>();

    public HashMap<SomeType> getMap() {
        return new HashMap<SomeType>();
    }    
    public String foo(HashMap<String, String> map) {
        return map.get("foo");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.HashMap;

public class Foo {
    private List<SomeType> list = new ArrayList<>();

    public Set<SomeType> set = new HashSet<SomeType>();

    public Map<SomeType> getMap() {
        return new HashMap<SomeType>();
    }
    public String foo(Map<String, String> map) {
        return map.get("foo");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 