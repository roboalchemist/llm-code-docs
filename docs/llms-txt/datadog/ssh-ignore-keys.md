# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/ssh-ignore-keys.md

---
title: Do not ignore SSH host validation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Do not ignore SSH host validation
---

# Do not ignore SSH host validation

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/ssh-ignore-keys`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [295](https://cwe.mitre.org/data/definitions/295.html)

## Description{% #description %}

SSH host validation should never be ignored and always be enforced to avoid man-in-the-middle attacks.

#### Learn More{% #learn-more %}

- [CWE-295: Improper Certificate Validation](https://cwe.mitre.org/data/definitions/295.html)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"golang.org/x/crypto/ssh"
)

func main() {
	_ =  ssh.InsecureIgnoreHostKey()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
	"golang.org/x/crypto/ssh"
)

func main() {
	// Use a more secure approach instead of InsecureIgnoreHostKey
	hostKeyCallback, _ := ssh.NewKnownHostsCallback("/path/to/known_hosts")
}
```

```go
package main

import (
	"golang.org/x/crypto/ssh"
)

func main() {
	// not valid in tests
	_ =  ssh.InsecureIgnoreHostKey()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 