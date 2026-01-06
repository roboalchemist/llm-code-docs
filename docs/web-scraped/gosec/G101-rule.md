# Source: https://securego.io/docs/rules/g101

G101: Hardcoded credentials · Secure Go## Secure Go
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
# G101: Hardcoded credentials
The use of hard-coded passwords increases the possibility of password guessing tremendously. This plugin test looks for all string literals and checks the following conditions:

Variables are considered to look like a password if they have match any one of:

- “password”

- “pass”

- “passwd”

- “pwd”

- “secret”

- “token”

Note: this can be noisy and may generate false positives.

## [](#example-code)Example code:

```
package main

import "fmt"

func main() {
 username := "admin"
 var password = "f62e5bcda4fae4f82370da0c6f20697b8f8447ef"

 fmt.Println("Doing something with: ", username, password)
}

```

## [](#gosec-command-line-output)Gosec command line output

```
[examples/main.go:7] - G101: Potential hardcoded credentials (Confidence: LOW, Severity: HIGH)
 &gt; password = "f62e5bcda4fae4f82370da0c6f20697b8f8447ef"

```

## [](#see-also)See also:

- [https://www.owasp.org/index.php/Use_of_hard-coded_password](https://www.owasp.org/index.php/Use_of_hard-coded_password)

- [http://gotowebsecurity.com/what-is-hardcoded-password-and-how-to-fix-it/](http://gotowebsecurity.com/what-is-hardcoded-password-and-how-to-fix-it/)

[← About gosec&#x27;s security rules](/docs/rules/rule-intro)[G102: Bind to all interfaces →](/docs/rules/g102)- [Example code:](#example-code)
- [Gosec command line output](#gosec-command-line-output)
- [See also:](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy