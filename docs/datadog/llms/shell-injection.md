# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/ruby-security/shell-injection.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/shell-injection.md

---
title: Prevent shell injection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent shell injection
---

# Prevent shell injection

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/shell-injection`

**Language:** C#

**Severity:** Warning

**Category:** Security

**CWE**: [78](https://cwe.mitre.org/data/definitions/78.html)

## Description{% #description %}

Never build a command to execute manually by concatenating strings. Instead, validate each component of the command to ensure there is no user-input.

#### Learn More{% #learn-more %}

- [CWE-78: Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')](https://cwe.mitre.org/data/definitions/78)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
public class Sample
{
    public void myMethod(string myProgram)
    {
        Process p = new Process();
        p.StartInfo.FileName = "path/to/" + myProgram;
        p.Start();
    }
}

public class Runner {
    public static int Run(string cmd, string args, string input) {
        ProcessStartInfo startInfo = new ProcessStartInfo
        {
            WorkingDirectory = Settings.RootDir,
            FileName = cmd,
            Arguments = args,
            UseShellExecute = false,
            RedirectStandardInput = true,
            RedirectStandardError = true,
            RedirectStandardOutput = true,
        };
        using (Process process = new Process())
        {
            process.EnableRaisingEvents = true;
            process.StartInfo = startInfo;
            process.Start();
        }
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
