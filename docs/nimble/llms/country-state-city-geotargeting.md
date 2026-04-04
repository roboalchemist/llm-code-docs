# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/country-state-city-geotargeting.md

# Country/state/city geotargeting

### Targeting by Country

Add a ***–country–*** value to the username portion of the request string to target a specific country:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-country-US:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-country-US:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-country-US:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-country-US:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-country-US:pipelinePassword@ip.nimbleway.com:7000")
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

Use ISO country codes to identify your target country, e.g. US, DE, BR (see the full list of [ISO 3166 alpha-2 country codes](https://www.iban.com/country-codes)). If no country parameter is specified, the target country will be randomized per each request.

{% hint style="info" %}
If no peers are available in a supported country/state/city, Nimble IP will return a 525 response. For more information, see Nimble IP's [Response Codes](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/response-codes).
{% endhint %}

### Targeting by US state

To target a US state, add a ***-state-*** value to the username:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-country-US-state-KS:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-country-US-state-KS:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-country-US-state-KS:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-country-US-state-KS:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-country-US-state-KS:pipelinePassword@ip.nimbleway.com:7000")
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

{% hint style="warning" %}
Targeting a state is only available when the country parameter is set to US.
{% endhint %}

### Targeting by city

To target a city, add a ***-city-*** value to the username:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-country-US-state-KS-city-wichita:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-country-US-state-KS-city-wichita:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-country-US-state-KS-city-wichita:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-country-US-state-KS-city-wichita:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-country-US-state-KS-city-wichita:pipelinePassword@ip.nimbleway.com:7000")
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

You can retrieve a comprehensive list of supported countries, states, and cities by using the [/location/cities endpoint](https://api.nimbleway.com/api/v1/location/cities) of the Admin API.

### Targeting geolocations with Authenticated IPs&#x20;

When using an Authenticated IP, your geolocation targeting settings are defined only in the target pipeline's configuration. When defining/modifying a pipeline, you can choose a target location country, and states/cities will be displayed if they are available for the selected location.

You can create/modify your pipelines in one of two ways:

* [x] Using the **Nimble IP** page in the [Nimble User Dashboard](https://app.nimbleway.com/login)
* [x] Using the `/account/pipelines` endpoint of the [**Admin API**](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference)**.**
