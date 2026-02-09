# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/arrays-aslist.md

---
title: Use asList to create a list from array
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use asList to create a list from array
---

# Use asList to create a list from array

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/arrays-aslist`

**Language:** Java

**Severity:** Warning

**Category:** Performance

## Description{% #description %}

Using `Arrays.asList` is much faster and cleaner than creating an array by iterating over the values.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public List<Integer> getListOfSomething() {
        List<Integer> myList = new ArrayList<>();
        Integer[] myArray = getArrayFromCall();
        
        foo();
        for (int i = 0; i < myArray.length; i++) {
            myList.add(myArray[i]);
        }
        return myList;
    }
}
```

```java
class Main {
    public List<Integer> getListOfSomething() {
        Integer[] myArray = getArrayFromCall();
        List<Integer> myList = new ArrayList<>();
        foo();
        for (int i = 0; i < myArray.length; i++) {
            myList.add(myArray[i]);
        }
        return myList;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public List<Integer> getListOfSomething() {
        Integer[] myArray = getArrayFromCall();
        return Arrays.asList(myArray);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 