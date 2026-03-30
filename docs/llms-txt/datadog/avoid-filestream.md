# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-filestream.md

---
title: Avoid creating FileStream directly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid creating FileStream directly
---

# Avoid creating FileStream directly

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-filestream`

**Language:** Java

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

The classes that creates `FileInputStream` and `FileOutputStream` triggers too much garbage collection. Instead, use methods from the `nio` package that cause less garbage collection.

#### Learn More{% #learn-more %}

- [JDK-8080225: # FileInput/OutputStream/FileChannel cleanup should be improved](https://bugs.openjdk.org/browse/JDK-8080225)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        String filename = "/path/to/file.txt";
        FileInputStream fis = new FileInputStream(filename);
        FileOutputStream fos = new FileOutputStream(filename);
        FileReader fr = new FileReader(filename);
        FileWriter fw = new FileWriter(filename);

        String s = new String("woeijf");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
class Main {
    public static void main(String[] args) {
        String filename = "/path/to/file.txt";
        try(InputStream is = Files.newInputStream(Paths.get(filename))) {
        }
        try(OutputStream os = Files.newOutputStream(Paths.get(filename))) {
        }
        try(BufferedReader br = Files.newBufferedReader(Paths.get(filename), StandardCharsets.UTF_8)) {
        }
        try(BufferedWriter wr = Files.newBufferedWriter(Paths.get(filename), StandardCharsets.UTF_8)) {
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
