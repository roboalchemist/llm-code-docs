# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/untrusted-env-var.md

---
title: Do not define env vars from user input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not define env vars from user input
---

# Do not define env vars from user input

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/untrusted-env-var`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [454](https://cwe.mitre.org/data/definitions/454.html)

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Diagnostics;

public class Controller { }

public class ExampleController : Controller
{
    public void Example(string name, string value)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = "path/to/executable";
        proc.StartInfo.EnvironmentVariables.Add(name, value); // Noncompliant: name is a variable
        proc.Start();
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```csharp
using System.Diagnostics;
using System.Text.RegularExpressions;

public class Controller { }

public class ExampleController : Controller
{
    public void Example(string value)
    {
        Process proc = new Process();
        proc.StartInfo.FileName = "path/to/executable";
        string pattern = "^*$";
        Match m = Regex.Match(value, pattern);
        if (m.Success) {
            // Name "ENV_VAR" is not in the sensitive list, so value being dynamic is ok here.
            proc.StartInfo.EnvironmentVariables.Add("ENV_VAR", value);
        }
        proc.Start();
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 