# Source: https://securego.io/docs/rules/g107

G107: Url provided to HTTP request as taint input · Secure Go## Secure Go
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
# G107: Url provided to HTTP request as taint input
Getting a URL from an untrusted source like user input gives the ability of an attacker to redirect your application to bad websites and perform additional attacks.
One of the examples is as shown below the [http.Get()](https://golang.org/pkg/net/http/#Client.Get) function issues a GET to the specified URL and if the result is appropriate GET will follow the redirect after calling Client's CheckRedirect function. That means that the attacker can send your application to various places.
This problem can be used to achieve [SSRF](https://www.acunetix.com/blog/articles/server-side-request-forgery-vulnerability/) attacks via http requests with variable url.

## [](#example-problematic-code)Example problematic code:

```
package main
import (
 "net/http"
 "io/ioutil"
 "fmt"
 "os"
)
func main() {
 url := os.Getenv("tainted_url")
 resp, err := http.Get(url)
 if err != nil {
 panic(err)
 }
 defer resp.Body.Close()
 body, err := ioutil.ReadAll(resp.Body)
 if err != nil {
 panic(err)
 }
 fmt.Printf("%s", body)
}

```

```
package main

import (
 "fmt"
 "io/ioutil"
 "net/http"
)

var url string = "https://www.google.com"

func main() {

 resp, err := http.Get(url)
 if err != nil {
 panic(err)
 }
 defer resp.Body.Close()
 body, err := ioutil.ReadAll(resp.Body)
 if err != nil {
 panic(err)
 }
 fmt.Printf("%s", body)
}

```

## [](#gosec-command-line-output)Gosec command line output

```
[examples/main.go:12] - G107: Potential HTTP request made with variable url (Confidence: MEDIUM, Severity: MEDIUM)
 &gt; http.Get(url)

```

```
[/Users/mvrachev/Martins/go/src/github.com/securego/examples/main.go:17] - G107: Potential HTTP request made with variable url (Confidence: MEDIUM, Severity: MEDIUM)
 &gt; http.Get(url)

```

## [](#the-right-way)The right way

```
package main

import (
 "fmt"
 "net/http"
)

const url = "http://127.0.0.1"

func main() {
 resp, err := http.Get(url)
 if err != nil {
 fmt.Println(err)
 }
 fmt.Println(resp.Status)
}

```

## [](#see-also)See also

- [http://projects.webappsec.org/w/page/13246981/URL%20Redirector%20Abuse](http://projects.webappsec.org/w/page/13246981/URL%20Redirector%20Abuse)

- [https://www.owasp.org/index.php/Top_10_2010-A10-Unvalidated_Redirects_and_Forwards](https://www.owasp.org/index.php/Top_10_2010-A10-Unvalidated_Redirects_and_Forwards)

[← G104: Audit errors not checked](/docs/rules/g104)[G201/G202: SQL query construction using format string/string concatenation →](/docs/rules/g201-g202)- [Example problematic code:](#example-problematic-code)
- [Gosec command line output](#gosec-command-line-output)
- [The right way](#the-right-way)
- [See also](#see-also)
[](/)##### Docs
[Secure development guidelines](/docs/en/guidelines.html)[API Reference](https://godoc.org/github.com/securego/gosec)##### Community
[Stack Overflow](http://stackoverflow.com/questions/tagged/gosec)[Slack](http://securego.herokuapp.com/)##### More
[Blog](/blog)[GitHub](https://github.com/securego)[Star](/securego/gosec/stargazers)[](https://code.facebook.com/projects/)Copyright © 2020 Grant Murphy