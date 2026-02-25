# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/ssl-v3-insecure.md

---
title: SSLv3 is not secure and should be avoided
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > SSLv3 is not secure and should be avoided
---

# SSLv3 is not secure and should be avoided

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/ssl-v3-insecure`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [327](https://cwe.mitre.org/data/definitions/327.html)

## Description{% #description %}

Do not use SSLv3 as it is now broken. See [this issue](https://golang.org/issue/32716) for more information.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func test() {
        client := &http.Client{
        Transport: &http.Transport{
            TLSClientConfig: &tls.Config{
                MinVersion:         tls.VersionSSL30,
            },
        },
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
