# Source: https://securego.io/docs/rules/g102

G102: Bind to all interfaces · Secure Go## Secure Go
- [Guidelines](/docs/rules/rule-intro)
- [Tools](/docs/tools)
- [Help](/help)
- [Blog](/blog/)
## *›*Guidelines
**### Guidelines
- [About gosec&#x27;s security rules](/docs/rules/rule-intro)
- [G101: Hardcoded credentials](/docs/rules/g101)
- [G102: Bind to all interfaces](/docs/rules/g102)
- [G103: Use of unsafe block](/docs/rules/g103)
- [G104: Audit errors not checked](/docs/rules/g104)
- [G107: Url provided to HTTP request as taint input](/docs/rules/g107)
- [G201/G202: SQL query construction using format string/string concatenation](/docs/rules/g201-g202)
- [G304: File path provided as taint input](/docs/rules/g304)
# G102: Bind to all interfaces
Binding to all network interfaces can potentially open up a service to traffic on unintended interfaces, that may not be properly documented or secured. This plugin test looks for a string pattern “0.0.0.0” that may indicate a hardcoded binding to all network interfaces.

## [](#example-code)Example code:

```
package main
import (
 "log"
 "net"
)
func main() {
 l, err := net.Listen("tcp", "0.0.0.0:2000")
 if err != nil {
 log.Fatal(err)
 }
 defer l.Close()
}

```

## [](#gosec-command-line-output)Gosec command line output

```
[examples/main.go:9] - G102: Binds to all network interfaces (Confidence: HIGH, Severity: MEDIUM)
 &gt; net.Listen("tcp", "0.0.0.0:2000")

```

## [](#see-also)See also

- [https://nvd.nist.gov/vuln/detail/CVE-2018-1281](https://nvd.nist.gov/vuln/detail/CVE-2018-1281)

[← G101: Hardcoded credentials](/docs/rules/g101)[G103: Use of unsafe block →](/docs/rules/g103)- [Example code:](#example-code)
- [Gosec command line output](#gosec-command-line-output)
- [See also](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy