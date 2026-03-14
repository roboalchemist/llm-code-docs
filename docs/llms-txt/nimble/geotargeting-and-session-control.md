# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-quick-start-guide/geotargeting-and-session-control.md

# Geotargeting and session control

### Adding targeting parameters

Connecting to Nimble IP with <mark style="color:red;background-color:yellow;">user:password</mark> authentication allows you to control session targeting and behavior by modifying the <mark style="color:red;background-color:yellow;">user</mark> portion of the request.

### Selecting your target geolocation

To request an IP from a specific country, add <mark style="color:red;background-color:yellow;">country-\<country\_code></mark> to the user portion:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-country-countryCode:pipelinePassword@ip.nimbleway.com:7000 https://targetpage.com
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-country-countryCode:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-country-countryCode:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-country-countryCode:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-country-countryCode:pipelinePassword@ip.nimbleway.com")
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

We use [ISO 3166 alpha-2 Country Codes](https://www.iban.com/country-codes) (use ALL to randomly select a country).

If you’d like to get even more specific, you can also add <mark style="color:red;background-color:yellow;">state-\<state\_code></mark>  or <mark style="color:red;background-color:yellow;">city-\<city\_code></mark> to target a US state or a City. For more details see [country-state-city-geotargeting](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/country-state-city-geotargeting "mention")

{% hint style="info" %}
If no peers are available in a supported country/state/city, Nimble IP will return a 525 response. For more information, see Nimble IP's [Response Codes](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/response-codes).
{% endhint %}

### Using sticky IPs

A sticky IP allows you to make multiple requests through the same IP address. This is done by initiating a session, which associates your request with the sticky IP address.

To create a session, add <mark style="color:red;background-color:yellow;">session-\<random\_string></mark> to the user portion.

{% hint style="info" %}
Session IDs are limited to 32 alphanumeric characters (no minimum). Session IDs cannot include hyphens "-" as this will act as a separator and end the "username" portion of the connection string.
{% endhint %}

For example:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-session-randomString:pipelinePassword@ip.nimbleway.com:7000 https://targetpage.com
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-session-randomString:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-session-randomString:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-session-randomString:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-session-randomString:pipelinePassword@ip.nimbleway.com:7000")
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

### Geo-sessions: Precise location-based sessions

Nimble Geo-sessions are a next-gen session solution that provides a variety of upgrades, including:

* [x] **Consistent Proxies:** Geo-sessions select for the most stable proxies in our pool, reducing rotation during the session substantially.
* [x] **Persistent Geolocation:** Any rotated IP during the session is selected from a limited geographic zone of up to only 15km.
* [x] **ASN Consistency**: IPs selected within a Geo-session will retain the same ASN throughout the session.

Geo-sessions are incredibly easy to use; simply pass the parameter `geosession` along with a random string of your choosing that will serve as the Geo-session ID.

{% hint style="info" %}
Geosession IDs are limited to between 16 to 32 alphanumeric characters (16 characters minimum).
{% endhint %}

For example:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000 https://targetpage.com
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-geosession-randomGeoSessionString:pipelinePassword@ip.nimbleway.com:7000")
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
Be sure to use the same parameters across requests that share the same Geo-session. If the location targeting is changed, but the Geo-session ID remains the same, a new session will still be initiated.
{% endhint %}

{% hint style="info" %}
Geo-sessions are currently only supported within the US. Support for additional countries is coming soon.
{% endhint %}

Learn more about [how Geo-sessions work and how to use them](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/geo-sessions-stickier-location-based-sessions).

### Combining parameters

All of the parameters we’ve covered before can be used together in a single request. This is done by chaining them together, like in this example:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -x http://account-MyCompany-pipeline-residential-country-US-state-NY-session-sess1:Password123@ip.nimbleway.com:7000 https://ipinfo.io
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-MyCompany-pipeline-residential-country-US-state-NY-session-sess1:Password123@ip.nimbleway.com:7000',
    'https': 'https://account-MyCompany-pipeline-residential-country-US-state-NY-session-sess1:Password123@ip.nimbleway.com:7000'
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
      host: "account-MyCompany-pipeline-residential-country-US-state-NY-session-sess1:Password123@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-MyCompany-pipeline-residential-country-US-state-NY-session-sess1:Password123@ip.nimbleway.com:7000")
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
