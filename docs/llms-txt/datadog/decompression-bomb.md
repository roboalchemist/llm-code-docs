# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/decompression-bomb.md

---
title: Prevent decompression bomb
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > Prevent decompression bomb
---

# Prevent decompression bomb

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/decompression-bomb`

**Language:** Go

**Severity:** Warning

**Category:** Security

**CWE**: [409](https://cwe.mitre.org/data/definitions/409.html)

## Description{% #description %}

Reading continuously from a compressed file without any limit of bytes may read too much data and lead to a denial of service (DoS). Prefer reading data by chunks of bytes.

#### Learn More{% #learn-more %}

- [CWE-409: Improper Handling of Highly Compressed Data](https://cwe.mitre.org/data/definitions/409.html)
- [Stackoverflow: Potential DoS by Decompression Bomb](https://stackoverflow.com/questions/67327323/g110-potential-dos-vulnerability-via-decompression-bomb-gosec)

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
	"bytes"
	"compress/bzip2"
	"io"
	"os"
)

func main() {
	buff := []byte{42, 51}
	b := bytes.NewReader(buff)

	r, err := zlib.NewReader(b)
	if err != nil {
		panic(err)
	}
	_, err = io.CopyBuffer(os.Stdout, r)
	if err != nil {
		panic(err)
	}

	r.Close()
}
```

```go
package main

import (
	"bytes"
	"compress/zlib"
	"io"
	"os"
)

func main() {
	buff := []byte{42, 51}
	b := bytes.NewReader(buff)

	r, err := zlib.NewReader(b)
	if err != nil {
		panic(err)
	}
	_, err = io.Copy(os.Stdout, r)
	if err != nil {
		panic(err)
	}

	r.Close()
}
```

## Compliant Code Examples{% #compliant-code-examples %}

```go
package main

import (
	"bytes"
	"compress/bzip2"
	"io"
	"os"
)

func main() {
	buff := []byte{42, 51}
	b := bytes.NewReader(buff)

	r, err := zlib.NewReader(b)
	if err != nil {
		panic(err)
	}
	_, err = io.CopyN(os.Stdout, r, 64)
	if err != nil {
		panic(err)
	}

	r.Close()
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security 
{% icon name="icon-external-link" /%}
 