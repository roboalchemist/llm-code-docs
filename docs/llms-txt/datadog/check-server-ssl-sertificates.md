# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/csharp-security/check-server-ssl-sertificates.md

---
title: Do not bypass certificates validation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not bypass certificates validation
---

# Do not bypass certificates validation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `csharp-security/check-server-ssl-sertificates`

**Language:** C#

**Severity:** Error

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

Never bypass certificate validation. Certificates should be correctly checked to avoid attacks from untrusted sources.

#### Learn More{% #learn-more %}

- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/295)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```csharp
using System.Net;
using System.Net.Http;

class MyClass {
public static void connect()
    {
        ServicePointManager.ServerCertificateValidationCallback +=
            (sender, certificate, chain, errors) => {
                return true;
            };

    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
