# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-best-practices/avoid-message-digest-field.md

---
title: Avoid declaring a field type as MessageDigest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid declaring a field type as MessageDigest
---

# Avoid declaring a field type as MessageDigest

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-best-practices/avoid-message-digest-field`

**Language:** Java

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

When you designate a `MessageDigest` instance as a class member, you enable direct access for multiple threads in your program. It is important to exercise caution when sharing instances among threads without proper synchronization.

Instead of sharing a single `MessageDigest` instance, consider generating new instances when necessary and using them locally within the specific context where they are needed. This practice offers two benefits. First, it guarantees that each thread operates on its own instance, thereby minimizing the possibility of interference between threads. Second, it sidesteps the intricacies of managing synchronized access to a shared instance.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    private final MessageDigest sharedMd; // should avoid this
    
    public Foo() throws Exception {
        sharedMd = MessageDigest.getInstance("SHA-256");
    }
    
    public byte[] bar(byte[] data) {
        // Incorrect outcomes could arise from sharing a 
        // MessageDigest without synchronized access.
        sharedMd.reset();
        sharedMd.update(data);
        return sharedMd.digest();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Foo {
    public byte[] bar(byte[] data) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-256");
        md.update(data);
        return md.digest();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 