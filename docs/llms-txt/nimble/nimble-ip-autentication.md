# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-quick-start-guide/nimble-ip-autentication.md

# Nimble IP Autentication

Requests to the BackConnect Gateway can be authenticated using **username and password** authentication or through an **authenticated IP**.

### Username and password

In its most simple form, a request with username/password authentication looks like this:

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
    'http': 'http://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName:pipelinePassword@ip.nimbleway.com:7000'
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

Replace **accountName**, **pipelineName,** and **pipelinePassword** with your account details before performing a request.

### Authenticated IPs

Instead of sending username and password credentials with every request, trusted IPs can be authenticated by adding them to your account's allow list, and any request coming from those authenticated IPs does not need to include a username or password.

{% hint style="warning" %}
It's important to be cautious with which IPs you authenticate. If a shared IP (such as an AWS shared IP) is added, it's possible your account will be used by other parties through the shared IP.
{% endhint %}

#### Authenticated IPs overview

Your account has a single, centralized list of authenticated IP addresses. When sending a request from an authenticated IP, since there is no longer a username portion through which additional parameters (such as geotargeting or session control) can be controlled, all parameters are defined in and inherited from the request's target pipeline, which is set using a custom port. For example:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://ip.nimbleway.com:9400 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://ip.nimbleway.com:9400',
    'https': 'https://ip.nimbleway.com:9400'
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
      host: "ip.nimbleway.com",
      port: 9400
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
 proxyURL, err := url.Parse("http://ip.nimbleway.com:9400")
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

In the above example, the request is written without a username or password, but targets port 9400 instead of 7000. Assuming the request is sent from an authenticated IP, port 9400 would be used to identify which pipeline the request should run through, and the request would inherit geotargeting and session control parameters from the target pipeline's configuration.

Each pipeline can allow or disallow authenticated IPs to connect to it. You can create a new pipeline, or modify an existing pipeline, in order to enable authenticated IP connection, define the port range that is used to target that particular pipeline, and manage your authenticated IPs.

#### Managing Pipelines

Pipelines can be managed in one of two ways:

* [x] Using the **pipeline creation wizard** in the [Nimble User Dashboard](https://app.nimbleway.com/login)
* [x] Using the `/account/pipelines` endpoint of the [**Admin API**](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference)**.**
