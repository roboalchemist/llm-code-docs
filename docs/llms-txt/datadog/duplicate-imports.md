# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-best-practices/duplicate-imports.md

---
title: Verify that duplicate imports are necessary
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Verify that duplicate imports are necessary
---

# Verify that duplicate imports are necessary

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-best-practices/duplicate-imports`

**Language:** Go

**Severity:** Notice

**Category:** Best Practices

## Description{% #description %}

In Go, duplicate imports refer to importing the same package multiple times in a single file. It is considered a best practice to avoid duplicate imports in Go for the following reasons:

1. Code readability and maintainability: Duplicate imports can make code harder to read and understand. When the same package is imported multiple times, it can lead to confusion and make it more difficult to determine the source of a particular symbol or function. Keeping imports concise and free of duplicates helps improve code readability and maintainability.
1. Name conflicts: Duplicate imports introduce the risk of name conflicts. If the same package is imported multiple times, Go does not distinguish between them, which can result in name clashes between symbols from different imports. This can cause compilation errors or unexpected behavior, making the code prone to bugs and difficult to troubleshoot.
1. Package initialization: Each package in Go can have an initialization function, `init()`, which is executed during package initialization. When the same package is imported multiple times, the `init()` function is run multiple times as well. This can lead to unexpected side effects and violate assumptions made by the package initialization code.
1. Compilation efficiency: Duplicate imports can impact compilation time and increase the size of the resulting binary. The Go compiler needs to process each imported package, and duplicating imports can cause unnecessary overhead during the build process.

To avoid these issues, it is recommended to keep imports concise and remove any duplicates. Go provides a handy feature where you can group multiple imports from the same package on a single line, reducing duplication. Additionally, using aliases when necessary can help resolve naming conflicts between symbols from different packages.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
import (
    "fmt"
    fmt2 "fmt"
    fmt3 "fmt"
    _ "fmt"
    "io"
    io2 "io"
    "log"
)
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
import (
    "fmt"
    log1 "log"
)
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
