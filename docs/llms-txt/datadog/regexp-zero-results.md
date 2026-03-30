# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/regexp-zero-results.md

---
title: Regexp FindAll with n=0 returns nothing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Regexp FindAll with n=0 returns nothing
---

# Regexp FindAll with n=0 returns nothing

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/regexp-zero-results`

**Language:** Go

**Severity:** Info

**Category:** Best Practices

## Description{% #description %}

Go, invoking the function `re.FindAll()` with the second argument set to 0 will not return any results.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import "regexp"

func check(re *regexp.Regexp) [][]byte {
    return re.FindAll([]byte(`seafood fool`), 0)
}

func other() {
    check := func(re regexp.Regexp) [][]byte {
        return re.FindAll([]byte(`foo`), 0)
    }
}
```

```go
import "regexp"

func main () {
    re := regexp.MustCompile("foo(")
    re.FindAll([]byte(`seafood fool`), 0)
}
```

```go
import "regexp"

func main () {

    var re *regexp.Regexp

    res := re.FindAll(something, 0)
}
```

```go
import "regexp"

func main () {

    re := regexp.MustCompile(`foo.?`)

    res := re.FindAll(something, 0)
}
```

```go
import "regexp"

func main () {
    var r *regexp.Regexp
    res := r.FindAll(something, 0)

    var r2 regexp.Regexp
    res := r2.FindAll(something, 0)

    regexp.MustCompile("foo(").FindAll(nil, 0)
    regexp.MustCompile(`foo.?`).FindAll([]byte(`seafood fool`), -1)

    res = r.FindAll(something, 0)

    if something {
        re.FindAll([]byte(`seafood fool`), -1)
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
func main() {
    res1 := regexp.MustCompile("foo(").FindAll(nil, 1)

    var r2 regexp.Regexp
    res := r2.FindAll(something, 1)

    // FindAll called on a non-Regexp object
    var myObj MyClass
    res2 := myObj.FindAll(something, 0)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
