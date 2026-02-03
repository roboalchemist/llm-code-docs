# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/avoid-random.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/python-security/avoid-random.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/avoid-random.md

---
title: Prefer SecureRandom over Random
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prefer SecureRandom over Random
---

# Prefer SecureRandom over Random

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/avoid-random`

**Language:** Java

**Severity:** Notice

**Category:** Security

**CWE**: [330](https://cwe.mitre.org/data/definitions/330.html)

## Description{% #description %}

Functions as `Math.random()` and objects like `java.util.Random()` do not provide strong enough randomness. Consider using `java.security.SecureRandom()` instead.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
@RestController
public class ImageServlet {

  public static final int PINCODE = new java.util.Random().nextInt(10000);

  @RequestMapping(
      method = {GET, POST},
      value = "/challenge/logo",
      produces = MediaType.IMAGE_PNG_VALUE)
  @ResponseBody
  public byte[] logo() throws IOException {
    byte[] in = getBytes();

    String pincode = String.format("%04d", PINCODE);

    in[81216] = (byte) pincode.charAt(0);
    in[81217] = (byte) pincode.charAt(1);
    in[81218] = (byte) pincode.charAt(2);
    in[81219] = (byte) pincode.charAt(3);

    return in;
  }
}
```

```java
@RestController
public class ImageServlet {

  public static final int PINCODE = new Random().nextInt(10000);

  @RequestMapping(
      method = {GET, POST},
      value = "/challenge/logo",
      produces = MediaType.IMAGE_PNG_VALUE)
  @ResponseBody
  public byte[] logo() throws IOException {
    byte[] in = getBytes();

    String pincode = String.format("%04d", PINCODE);

    in[81216] = (byte) pincode.charAt(0);
    in[81217] = (byte) pincode.charAt(1);
    in[81218] = (byte) pincode.charAt(2);
    in[81219] = (byte) pincode.charAt(3);

    return in;
  }
}
```

```java
@RestController
public class ImageServlet {

  public static final int PINCODE = new Random().nextInt(10000);

  @RequestMapping(
      method = {GET, POST},
      value = "/challenge/logo",
      produces = MediaType.IMAGE_PNG_VALUE)
  @ResponseBody
  public byte[] logo() throws IOException {
    var v = Math.random();
  }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import org.apache.commons.codec.binary.Hex;

class Class {
    String generateSecretToken() {
        SecureRandom secRandom = new SecureRandom();

        byte[] result = new byte[32];
        secRandom.nextBytes(result);
        return Hex.encodeHexString(result);
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 