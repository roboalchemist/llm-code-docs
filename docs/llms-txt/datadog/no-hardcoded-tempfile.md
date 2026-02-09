# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/no-hardcoded-tempfile.md

---
title: Avoid temporary hardcoded files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid temporary hardcoded files
---

# Avoid temporary hardcoded files

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/no-hardcoded-tempfile`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [377](https://cwe.mitre.org/data/definitions/377.html)

## Description{% #description %}

Never create a temporary file with a hardcoded path. Hardcoded paths may have write permissions for all users, enabling multiple types of attacks (for example, another application can also modify the temporary file and its content and potentially write executable code).

Always make sure temporary files are non deterministic and created programmatically.

#### Learn More{% #learn-more %}

- [CWE-379: Creation of Temporary File in Directory with Insecure Permissions](https://cwe.mitre.org/data/definitions/379)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        using (var streamWriter = new StreamWriter("%USERPROFILE%\AppData\Local\Temp\f"))
        {
            streamWriter.WriteLine("foobar");
        }
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        using (var streamWriter = new StreamWriter("/var/tmp/f"))
        {
            streamWriter.WriteLine("foobar");
        }
    }
}
```

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        using (var streamWriter = new StreamWriter("/tmp/f"))
        {
            streamWriter.WriteLine("foobar");
        }
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
class MyClass {
    public static void payloadDecode()
    {
        // Create the temporary file stream by getting programmatically a temporary path and filename
        var temporaryPath = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());

        // make sure you can create the file with write access
        using var temporaryFileStream = new FileStream(randomPath, FileMode.CreateNew, FileAccess.Write, FileShare.None, 4096, FileOptions.DeleteOnClose);

        using (var streamWriter = new StreamWriter(temporaryFileStream))
        {
            streamWriter.WriteLine("foobar");
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 