# Source: https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/go-security/import-cgi.md

---
title: CGI is outdated
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Code Security > Static Code Analysis (SAST) > SAST
  Rules > CGI is outdated
---

# CGI is outdated

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

## Metadata{% #metadata %}

**ID:** `go-security/import-cgi`

**Language:** Go

**Severity:** Warning

**Category:** Security

## Description{% #description %}

In Go, it is generally recommended to avoid using the `net/http/cgi` package for executing Common Gateway Interface (CGI) scripts. The `cgi` package provides functionality to execute CGI scripts within an HTTP server, but there are several reasons why it is advised to avoid its usage:

1. Performance: The `cgi` package uses an external CGI process for each request, which can introduce significant performance overhead. Starting and managing external processes for each request can be resource-intensive and impact the server's overall throughput and response time. In contrast, using native Go handler functions or a framework like Gorilla Mux can offer better performance and efficiency.
1. Security: Running CGI scripts inherently introduces security risks due to the need to execute external programs with potentially untrusted input. The `cgi` package lacks features and safeguards provided by other server setups or frameworks that are designed to mitigate common CGI-related security vulnerabilities. It is generally safer to handle HTTP requests using native Go handlers that allow for more granular control and security checks.
1. Lack of standardization: CGI is an older and less commonly used protocol for executing web scripts. The `cgi` package does not support some newer HTTP features and has limited support for handling specific aspects of the CGI specification. Using more modern and widely-adopted frameworks or libraries can provide better support and tooling for handling HTTP requests and responses.
1. Code complexity: The `cgi` package's API can be more complex and less intuitive compared to other HTTP server and routing frameworks available in the Go ecosystem. Depending on the specific use case and requirements, using a simpler and more idiomatic approach with native Go handlers or a well-established framework can lead to easier-to-understand and maintainable code.

While the `cgi` package can still be suitable for specific scenarios where compatibility with existing CGI scripts or server configurations is a strict requirement, it is generally recommended to explore alternative approaches for building HTTP servers in Go. Leveraging the native `net/http` package, along with frameworks like Gorilla Mux or Gin, can provide better performance, security, and flexibility for handling HTTP requests and building web applications in a more idiomatic and efficient manner.

## Non-Compliant Code Examples{% #non-compliant-code-examples %}

```go
package main

import (
    "net/http/cgi"
    "net/http"
 )

func main() {
    cgi.Serve(http.NotFoundHandler())
}
```
  Seamless integrations. Try Datadog Code SecurityDatadog Code Security
{% icon name="icon-external-link" /%}
