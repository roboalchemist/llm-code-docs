# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-best-practices/variable-names.md

---
title: Avoid keywords as variables names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid keywords as variables names
---

# Avoid keywords as variables names

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-best-practices/variable-names`

**Language:** C#

**Severity:** Warning

**Category:** Code Style

## Description{% #description %}

Avoid using language keywords to declare variables. While being authorized by the compiler, it makes the code harder to understand.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net;

class MyClass {
    public static void routine()
    {
        bool await = false;
        bool async = true;
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
