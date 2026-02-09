# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/object-deserialization.md

---
title: Prevent deserialization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent deserialization
---

# Prevent deserialization

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/object-deserialization`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [502](https://cwe.mitre.org/data/definitions/502.html)

## Description{% #description %}

Deserialization of untrusted data can lead to system compromise. Make sure you only deserialize data you trust.

#### Learn More{% #learn-more %}

- [CWE-502](https://cwe.mitre.org/data/definitions/502.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class SerializationHelper {

  private static final char[] hexArray = "0123456789ABCDEF".toCharArray();

  public static Object fromString(String s) throws IOException, ClassNotFoundException {
    byte[] data = Base64.getDecoder().decode(s);
    ObjectInputStream ois = new ObjectInputStream(new ByteArrayInputStream(data));
    Object o = ois.readObject();
    ois.close();
    return o;
  }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 