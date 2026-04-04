# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-quick-start-guide/send-a-request.md

# Send a request

### The BackConnect proxy gateway

Nimble has a single proxy gateway that manages sessions for you, freeing you from proxy lists and dynamic IPs. Requests can be authenticated with user:password combinations or by listing your IPs in the allowlist.

See our [Backconnect Gateway documentation](https://docs.nimbleway.io/nimble-sdk/proxy-api) for all gateway request options.

### Sending a request with user:password authentication

![](https://www.nimbleway.com/wp-content/uploads/2022/09/Nimble-IP-Sending-a-Requent.png)

| Server           | Proxy IP Port |
| ---------------- | ------------- |
| ip.nimbleway.com | 7000          |

### **Request Example**

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000'
}

url = 'https://ipinfo.io'

response = requests.get(url, proxies=proxies)

print(response.status_code)
print(response.text)
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const targetAddress = "http://ipinfo.io/json";
const getProxy = async () => {
  return {
    proxy: {
      host: "account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com",
      port: 7000
    }
  }
}

const run = async () => {
  const res = await axios(targetAddress, getProxy());
  return res.data;
}


(async () => {
  var response = await run()
  console.log(response);
  console.log("DONE!")
})();
```

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

```go
package main

import (
 "fmt"
 "io/ioutil"
 "net/http"
 "net/url"
)

func main() {
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000")
 if err != nil {
  fmt.Println(err)
  return
 }

 client := &http.Client{
  Transport: &http.Transport{
   Proxy: http.ProxyURL(proxyURL),
  },
 }

 url := "https://ipinfo.io"

 req, err := http.NewRequest("GET", url, nil)
 if err != nil {
  fmt.Println(err)
  return
 }

 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)

 body, err := ioutil.ReadAll(resp.Body)
 if err != nil {
  fmt.Println(err)
  return
 }

 fmt.Println(string(body))
}
```

{% endcode %}
{% endtab %}
{% endtabs %}

The following parameters are required:

* ***accountName*** – Your company gateway name.
* ***pipelineName*** – The pipeline you wish to use (every new account comes with a default pipeline named <mark style="color:red;background-color:yellow;">residential</mark> for a quick start).
* ***pipelinePassword** –* The pipeline’s password to authenticate your request.
* **Target page** – The URL you’d like to gather data from.

{% hint style="info" %}
Your account name and pipeline credentials will be provided by your account manager when your account is opened.
{% endhint %}
