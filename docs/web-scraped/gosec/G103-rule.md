# Source: https://securego.io/docs/rules/g103

G103: Use of unsafe block · Secure Go## Secure Go
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
# G103: Use of unsafe block
Using the unsafe package in Go gives you low-level memory management and many of the strength of the C language but also gives flexibility to the attacker of your application. The pointer arithmetic is one of the examples from the unsafe package which can be used for data leak, memory corruption or even execution of attackers own script.

Also, you should keep in mind that the &quot;unsafe&quot; package is not protected by [Go 1 compatibility guidelines](https://golang.org/doc/go1compat).

If you want to ignore this rule you can do it, as usual, using the &quot;exclude&quot; option in the command line interface.

## [](#example-code)Example code:

```
package main
import (
 "fmt"
 "unsafe"
)
type Fake struct{}
func (Fake) Good() {}
func main() {
 unsafeM := Fake{}
 unsafeM.Good()
 intArray := [...]int{1, 2}
 fmt.Printf("\nintArray: %v\n", intArray)
 intPtr := &amp;intArray[0]
 fmt.Printf("\nintPtr=%p, *intPtr=%d.\n", intPtr, *intPtr)
 addressHolder := uintptr(unsafe.Pointer(intPtr)) + unsafe.Sizeof(intArray[0])
 intPtr = (*int)(unsafe.Pointer(addressHolder))
 fmt.Printf("\nintPtr=%p, *intPtr=%d.\n\n", intPtr, *intPtr)
}

```

## [](#gosec-command-line-output)Gosec command line output

```
[examples/main.go:18] - G103: Use of unsafe calls should be audited (Confidence: HIGH, Severity: LOW)
 &gt; unsafe.Pointer(intPtr)

[/Users/mvrachev/Martins/go/src/github.com/securego/examples/main.go:18] - G103: Use of unsafe calls should be audited (Confidence: HIGH, Severity: LOW)
 &gt; unsafe.Sizeof(intArray[0])

[examples/main.go:19] - G103: Use of unsafe calls should be audited (Confidence: HIGH, Severity: LOW)
 &gt; unsafe.Pointer(addressHolder)

```

## [](#see-also)See also:

- [https://golang.org/pkg/unsafe/](https://golang.org/pkg/unsafe/)

[← G102: Bind to all interfaces](/docs/rules/g102)[G104: Audit errors not checked →](/docs/rules/g104)- [Example code:](#example-code)
- [Gosec command line output](#gosec-command-line-output)
- [See also:](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy