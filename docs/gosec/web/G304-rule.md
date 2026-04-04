# Source: https://securego.io/docs/rules/g304

G304: File path provided as taint input · Secure Go## Secure Go
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
# G304: File path provided as taint input
Trying to open a file provided as an input in a variable. The content of this variable might be controlled by an attacker who could change it to hold unauthorised file paths from the system. In this way, it is possible to exfiltrate confidential information or such.

## [](#example-problematic-code)Example problematic code:

This code lets an attacker read a `/private/path`

```
package main

import (
 "fmt"
 "io/ioutil"
 "strings"
)

func main() {
 repoFile := "/safe/path/../../private/path"
 if !strings.HasPrefix(repoFile, "/safe/path/") {
 panic(fmt.Errorf("Unsafe input"))
 }
 byContext, err := ioutil.ReadFile(repoFile)
 if err != nil {
 panic(err)
 }
 fmt.Printf("%s", string(byContext))
}

```

## [](#gosec-command-line-output)Gosec command line output

```
[examples/main.go:11] - G304 (CWE-22): Potential file inclusion via variable (Confidence: HIGH, Severity: MEDIUM)
 &gt; ioutil.ReadFile(repoFile)

```

## [](#the-right-way)The right way

This code panics if `/safe/path` was removed by an attacker

```
package main

import (
 "fmt"
 "io/ioutil"
 "path/filepath"
 "strings"
)

func main() {
 repoFile := "/safe/path/../../private/path"
 repoFile = filepath.Clean(repoFile)
 if !strings.HasPrefix(repoFile, "/safe/path/") {
 panic(fmt.Errorf("Unsafe input"))
 }
 byContext, err := ioutil.ReadFile(repoFile)
 if err != nil {
 panic(err)
 }
 fmt.Printf("%s", string(byContext))}

```

## [](#see-also)See also

- [https://pkg.go.dev/path/filepath?tab=doc#Clean](https://pkg.go.dev/path/filepath?tab=doc#Clean)

[← G201/G202: SQL query construction using format string/string concatenation](/docs/rules/g201-g202)- [Example problematic code:](#example-problematic-code)
- [Gosec command line output](#gosec-command-line-output)
- [The right way](#the-right-way)
- [See also](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy