# Source: https://securego.io/docs/rules/g104

G104: Audit errors not checked · Secure Go## Secure Go
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
# G104: Audit errors not checked
A really useful feature of Golang is the ability to return a tuple of a result and an error value from a function. There is an unspoken rule in Golang that the result of a function is unsafe until you make check the error value. Many security exploits can be performed when the error value is not checked.

## [](#example-code)Example code:

```
package main
import "fmt"
func test() (int,error) {
 return 0, nil
}
func main() {
 v, _ := test()
 fmt.Println(v)
}

```

other example:

```
package main

import (
 "fmt"
 "io/ioutil"
 "os"
)

func a() error {
 return fmt.Errorf("This is an error")
}

func b() {
 fmt.Println("b")
 ioutil.WriteFile("foo.txt", []byte("bar"), os.ModeExclusive)
}

func c() string {
 return fmt.Sprintf("This isn't anything")
}

func main() {
 _ = a()
 a()
 b()
 c()
}

```

## [](#gosec-command-line-output)Gosec command line output

The Gosec output from the first example:

```
[examples/main.go:9] - G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
 &gt; v, _ := test()

```

The output from the second example:

```
[examples/main.go:14] - G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
 &gt; ioutil.WriteFile("foo.txt", []byte("bar"), os.ModeExclusive)

[examples/main.go:20] - G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
 &gt; _ = a()

[examples/main.go:21] - G104: Errors unhandled. (Confidence: HIGH, Severity: LOW)
 &gt; a()

```

## [](#see-also)See also:

- [https://blog.golang.org/error-handling-and-go](https://blog.golang.org/error-handling-and-go)

- [https://blog.golang.org/errors-are-values](https://blog.golang.org/errors-are-values)

[← G103: Use of unsafe block](/docs/rules/g103)[G107: Url provided to HTTP request as taint input →](/docs/rules/g107)- [Example code:](#example-code)
- [Gosec command line output](#gosec-command-line-output)
- [See also:](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy