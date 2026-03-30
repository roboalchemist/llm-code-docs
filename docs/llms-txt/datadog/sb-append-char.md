# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/sb-append-char.md

---
title: Do not append char as strings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not append char as strings
---

# Do not append char as strings

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/sb-append-char`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Do not append a string with single character to a `StringBuffer`. Instead, append a character type. This is better practice and results in better performance. While this is negligible if the operation occurs once, it has performance impact if done at scale.

### Learn More{% #learn-more %}

- [JavaDoc - StringBuffer](https://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html)
- [Benchmark for StringBuffer and append](https://stackoverflow.com/a/34793025)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Main{
    public static void main(String[] args){
        StringBuffer sb = new StringBuffer();
        sb.append("a");
        sb.append("abc");

        while (true) {
            sb.append("a");
        }

        for (Element e: elements) {
            sb.append("a");
        }

        if (true) {
            sb.append("a");
        } else {
            sb.append("a");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Main{
    public static void main(String[] args){
        StringBuffer sb = new StringBuffer();
        sb.append('a');
        sb.append("<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.0//EN\" ");
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
