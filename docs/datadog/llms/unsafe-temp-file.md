# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/unsafe-temp-file.md

---
title: Avoid unsafe temporary file creation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid unsafe temporary file creation
---

# Avoid unsafe temporary file creation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/unsafe-temp-file`

**Language:** C#

**Severity:** Notice

**Category:** Security

**CWE**: [377](https://cwe.mitre.org/data/definitions/377.html)

## Description{% #description %}

The function `GetTempFileName` is known to have security issues and may lead to attacks. Temporary files should not be predictable and safe to use. Avoid the function `GetTempFileName`.

#### Learn More{% #learn-more %}

- [Stackoverflow thread on creating temporary directory atomically](https://stackoverflow.com/questions/33446371/anybody-got-a-good-way-to-atomically-create-a-temporary-directory-in-net-manage)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
class MyClass {
    public static void payloadDecode()
    {
        var temporaryPath = Path.GetTempFileName();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Xml;

class MyClass {
    public static void payloadDecode()
    {
        var temporaryPath = Path.Combine(Path.GetTempPath(), Path.GetRandomFileName());
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
