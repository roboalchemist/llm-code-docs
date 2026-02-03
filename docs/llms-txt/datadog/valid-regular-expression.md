# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/valid-regular-expression.md

---
title: Avoid invalid regular expression
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Avoid invalid regular expression
---

# Avoid invalid regular expression

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/valid-regular-expression`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Regular expression in Go must be valid regular expressions. You can check the validity of regular expressions on [regex101.com](https://regex101.com/).

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
func main() {
    var c1 = "["
    c2 := "["

    regexp.MustCompile(c1)

    if something {
        regexp.MustCompile(c2)
    } else {
        regexp.MustCompile(c2)
    }
    
}
```

```go
func main() {
    regexp.MustCompile("[")
    regexp.Compile("(")
    regexp.Match("(")
    regexp.MatchReader("(")
    regexp.MatchString("(")
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    regexp.MustCompile("[a-z]+")
    regexp.Compile("[a-z]+")
    regexp.Match("[a-z]+")
    regexp.MatchReader("[a-z]+")
    regexp.MatchString("[a-z]+")
    regexp.MustCompile("^error-tracking-(.+)$")
    regexp.MustCompile("(?i)windows")    
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 