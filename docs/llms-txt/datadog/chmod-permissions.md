# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/typescript-node-security/chmod-permissions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/javascript-node-security/chmod-permissions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/chmod-permissions.md

---
title: File permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > File permissions
---

# File permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/chmod-permissions`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [284](https://cwe.mitre.org/data/definitions/284.html)

## Description{% #description %}

Granting write access to a file is a security since other users can modify the content of the file. The issue is amplified for executable files that can be easily compromised (like scripts). Avoid giving write permissions to others to files.

#### Learn More{% #learn-more %}

- [CWE-284: Improper Access Control](https://cwe.mitre.org/data/definitions/284.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    err := os.Chmod("/tmp/somefile", 0777)
    if err != nil {
        fmt.Println("Error when changing file permissions!")
        return
    }
}
```

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    _, err := os.OpenFile("/tmp/thing", os.O_CREATE|os.O_WRONLY, 0666)
    if err != nil {
        fmt.Println("Cannot create file")
        return
    }
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    err := os.Chmod("/tmp/somefile", 0770)
    if err != nil {
        fmt.Println("Error when changing file permissions!")
        return
    }
}
```

```go
package main

import (
    "fmt"
    "os"
)

func main() {
    _, err := os.OpenFile("/tmp/thing", os.O_CREATE|os.O_WRONLY, 0660)
    if err != nil {
        fmt.Println("Cannot create file")
        return
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
