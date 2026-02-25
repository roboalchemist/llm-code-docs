# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/tempfile-delete.md

---
title: Temporary file not deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Temporary file not deleted
---

# Temporary file not deleted

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/tempfile-delete`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [459](https://cwe.mitre.org/data/definitions/459.html)

## Description{% #description %}

This rule identifies instances where temporary files are created but not properly deleted after use. Leaving temporary files undeleted can lead to resource leaks, unnecessary disk space consumption, and potential exposure of sensitive data if the files contain confidential information.

To comply with this rule, always delete temporary files explicitly when they are no longer needed, or use mechanisms like `deleteOnExit()` to schedule automatic deletion when the JVM terminates. For example, after creating a temporary file with `File.createTempFile()`, invoke `tempFile.deleteOnExit()` to ensure cleanup. This practice helps maintain application stability and security.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import java.io.File;
import java.io.IOException;

public class SecureTempFileExample {
    public static void main(String[] args) throws IOException {
        File tempFile = File.createTempFile("tempfile_", ".tmp");
        System.out.println("Temporary file created at: " + tempFile.getAbsolutePath());
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```java
import java.io.File;
import java.io.IOException;

public class SecureTempFileWithPermissionsExample {
    public static void main(String[] args) throws IOException {
        File tempFile = File.createTempFile("secure_tempfile_", ".tmp");
        tempFile.deleteOnExit();
        System.out.println("Temporary file created with secure permissions at: "
            + tempFile.getAbsolutePath());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
