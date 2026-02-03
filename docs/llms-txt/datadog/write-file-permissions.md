# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/php-security/write-file-permissions.md

# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/write-file-permissions.md

---
title: Do not create a file with too much permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not create a file with too much permissions
---

# Do not create a file with too much permissions

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/write-file-permissions`

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
	d1 := []byte("something somethingn")
	err := ioutil.WriteFile("myfile", d1, 0777)
	check(err)
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
	d1 := []byte("something somethingn")
	err := ioutil.WriteFile("myfile", d1, 0770)
	check(err)
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 