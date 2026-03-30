# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-code-style/avoid-using-native-code.md

---
title: Avoid `System.loadLibrary` for improved Java portability.
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid `System.loadLibrary` for improved Java portability.
---

# Avoid `System.loadLibrary` for improved Java portability.

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-code-style/avoid-using-native-code`

**Language:** Java

**Severity:** Notice

**Category:** Code Style

## Description{% #description %}

When Java applications use native code, typically through the Java Native Interface (JNI) and methods like `System.loadLibrary()` or `System.load()`, it introduces a strong dependency on platform-specific binaries. This practice significantly reduces the portability of the application, as the native libraries must be compiled and distributed for each target operating system and architecture. It also increases deployment complexity, makes debugging more challenging, and can lead to instability or crashes if native code interactions are not meticulously managed.

## How to Remediate{% #how-to-remediate %}

To enhance portability and maintainability, favor pure Java solutions over native code whenever possible. If interacting with system-specific features or achieving critical performance gains necessitates native calls, consider abstracting them behind an interface to minimize their direct impact on the codebase. Prioritize using well-established, cross-platform libraries or external services that handle native interactions internally, rather than directly managing `System.loadLibrary()` calls within your application logic.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
public class Foo {
    public Foo() {
        System.loadLibrary("nativelib");
    }

    static {
        System.loadLibrary("nativelib");
    }

    public void foo() throws SecurityException, NoSuchMethodException {
        System.loadLibrary("nativelib");
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
public class Bar {
    public void baz() {
        System.out.println("Executing pure Java code without native dependencies.");
        // No System.loadLibrary or System.load calls here
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
