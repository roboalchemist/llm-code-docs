# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/platform-compatibility.md

---
title: Validate platform capatibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Validate platform capatibility
---

# Validate platform capatibility

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/platform-compatibility`

**Language:** C#

**Severity:** Warning

**Category:** Best Practices

## Description{% #description %}

The 'Validate platform compatibility' rule is an important static analysis rule in C# that ensures your code is compatible with the platforms it is intended to run on. This rule checks for platform compatibility attributes like `SupportedOSPlatform` and `UnsupportedOSPlatform` in your code, which indicate the specific platforms or versions of platforms on which the annotated code elements are supported or unsupported, respectively.

Ignoring this rule can lead to runtime errors if your code attempts to call APIs that are not supported on the host operating system. For example, a method marked with `[UnsupportedOSPlatform("windows")]` will throw an exception if called on a Windows machine.

To comply with this rule, always mark your platform-specific APIs with the appropriate attributes and ensure that your code does not call any APIs that are not supported on the current platform. Use the `RuntimeInformation.IsOSPlatform` method to check the platform at runtime before calling any platform-specific APIs. Additionally, consider providing alternative implementations for different platforms to improve the portability of your code.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
[UnsupportedOSPlatform("foobar")]
[SupportedOSPlatform("baz")]
[UnsupportedOSPlatform("bla")]
public void ApiSupportedFromWindows8UnsupportedFromWindows10();
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
// An API supported only on Linux.
[SupportedOSPlatform("linux")]
public void LinuxOnlyApi() { }

// API is supported on Windows, iOS from version 14.0, and MacCatalyst from version 14.0.
[SupportedOSPlatform("windows")]
[SupportedOSPlatform("ios14.0")] // MacCatalyst is a superset of iOS, therefore it's also supported.
public void SupportedOnWindowsIos14AndMacCatalyst14() { }

public void Caller()
{
    LinuxOnlyApi(); // This call site is reachable on all platforms. 'LinuxOnlyApi()' is only supported on: 'linux'

    SupportedOnWindowsIos14AndMacCatalyst14(); // This call site is reachable on all platforms. 'SupportedOnWindowsIos14AndMacCatalyst14()'
                                               // is only supported on: 'windows', 'ios' 14.0 and later, 'MacCatalyst' 14.0 and later.
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 