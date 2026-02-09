# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-inclusive/function-declaration.md

---
title: Use inclusive language in function declarations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Use inclusive language in function declarations
---

# Use inclusive language in function declarations

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-inclusive/function-declaration`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

Use inclusive language in function declaration.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func whitelistFunc(master, slaveParamSlave string){
    return nil
}

func blacklistFunc()(whitelist, blAckliSt []string){
    return []string{}
}

func slaveFunc(blAckliSt int){
    return nil
}

func masterFunc(){
    return nil
}

func myFunc(){
    return nil
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 