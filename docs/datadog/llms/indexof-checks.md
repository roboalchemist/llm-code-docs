# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/indexof-checks.md

---
title: IndexOf function should check the first character
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > IndexOf function should check the first character
---

# IndexOf function should check the first character

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/indexof-checks`

**Language:** C#

**Severity:** Warning

**Category:** Error Prone

## Description{% #description %}

When using `Indexof` or `LastIndexOf`, using `> 0` may miss the first item of the collection (string, list, etc). Instead, the code should use `>=0` to take the first element into account.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine(string str, string str2)
    {
        str.IndexOf(str2)>0;
        str.IndexOf(str2)>0;
        str.LastIndexOf(str2)>0;
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine(string str, string str2)
    {
        str.IndexOf(str2)>=0;
        str.IndexOf(str2)>=0;
        str.LastIndexOf(str2)>=0;
        if (serverPackages.Any(x => x.Version.CompareTo(currentVersion) > 0)) {

        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
