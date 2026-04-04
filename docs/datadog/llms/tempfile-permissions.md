# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/java-security/tempfile-permissions.md

---
title: Invalid permissions for temporary file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Invalid permissions for temporary file
---

# Invalid permissions for temporary file

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `java-security/tempfile-permissions`

**Language:** Java

**Severity:** Warning

**Category:** Security

**CWE**: [732](https://cwe.mitre.org/data/definitions/732.html)

## Description{% #description %}

Always explicitly set secure permissions on temporary files immediately after creation. This includes granting read and write access only to the owner, and disabling execute permissions unless explicitly required. For example, use `tempFile.setReadable(true, true)`, `tempFile.setWritable(true, true)`, and `tempFile.setExecutable(false)` to restrict access appropriately.

Avoid relying on default file permissions or omitting permission settings altogether, as this can lead to overly permissive access. By following these best practices, you minimize security risks associated with temporary files in your Java applications.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```java
import java.io.File;
import java.io.IOException;

public class SecureTempFileWithPermissionsExample {
    public static void main(String[] args) throws IOException {
        File tempFile = File.createTempFile("secure_tempfile_", ".tmp");
        tempFile.setReadable(true, true);
        tempFile.deleteOnExit();
        System.out.println("Temporary file created with secure permissions at: "
            + tempFile.getAbsolutePath());
    }
}
```

```java
import java.io.File;
import java.io.IOException;

public class SecureTempFileExample {
    public static void main(String[] args) throws IOException {
        File tempFile = File.createTempFile("tempfile_", ".tmp");
        tempFile.deleteOnExit();
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
        tempFile.setReadable(true, true);
        tempFile.setWritable(true, true);
        tempFile.setExecutable(false);
        tempFile.deleteOnExit();
        System.out.println("Temporary file created with secure permissions at: "
            + tempFile.getAbsolutePath());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
