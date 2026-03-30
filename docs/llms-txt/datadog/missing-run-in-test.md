# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/missing-run-in-test.md

---
title: Detects if `m.Run()` was actually called in `TestMain`
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Detects if `m.Run()` was actually called in `TestMain`
---

# Detects if `m.Run()` was actually called in `TestMain`

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/missing-run-in-test`

**Language:** Go

**Severity:** Error

**Category:** Error Prone

## Description{% #description %}

No description found

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package example

import (
    "os"
    "testing"
)

func TestMain(m *testing.M) {
    // Setup code
    doSetup()

    // Missing call to Run() here!
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
// GOOD: Correct implementation with m.Run()
package example

import (
    "os"
    "testing"
)

func TestMain(m *testing.M) {
    // Setup code
    doSetup()

    // Run the tests
    code := m.Run()

    os.Exit(code)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
