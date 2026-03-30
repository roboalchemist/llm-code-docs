# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/mkdir-permissions.md

---
title: Do not create a directory with write permissions for all
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not create a directory with write permissions for all
---

# Do not create a directory with write permissions for all

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/mkdir-permissions`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [284](https://cwe.mitre.org/data/definitions/284.html)

## Description{% #description %}

In Unix-based systems like Linux or macOS, and therefore within the Go programming language's OS package, permissions are set using a three-digit code, with each digit ranging from 0-7. Each digit represents the permissions for the owner, group, and others respectively.

The call `err := os.Mkdir("/tmp/mydir", 0777)` would hence set the directory permissions to "777", giving read, write, and execute permissions to everyone: the file owner, the group, and all others.

Using "777" permissions is generally considered bad practice for maintaining secure systems. The problem is that it gives full permissionâincluding read, write, and execute powersâto every user on the system. This can create potential security risks. For instance, any user, even those without proper authority, could make unauthorized changes to the files or directories. Moreover, allowing executable permissions can be dangerous as malicious scripts may be executed.

As an alternative, it's recommended to grant the minimum needed permissions. For instance, use "755" to give the owner full permissions and read and execute permissions for the group and other users. If group write access is necessary, then "775" could be considered. In some cases, it might also be beneficial to use Access Control Lists (ACLs) for more granular control over permissions.

Therefore, it is advised to set permissions carefully, considering the principle of least privilege. Always think carefully about who needs what kind of access to ensure both the functionality and security of your applications.

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
    err := os.Mkdir("/path/to/new/directory", 0777)
    if err != nil {
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
    err := os.Mkdir("/path/to/new/directory", 0770)
    if err != nil {
        return
    }
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
