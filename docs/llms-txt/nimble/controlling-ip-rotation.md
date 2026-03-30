# Source: https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/controlling-ip-rotation.md

# Controlling IP rotation

{% hint style="success" %}
If retaining sessions for long periods of time with high geographic accuracy is important for your use case, we recommend trying [**our new Geo-sessions.**](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/geo-sessions-stickier-location-based-sessions)
{% endhint %}

### Using sticky sessions with user:password authentication

By default, IPs are rotated for every request. To create a sticky session and retain an IP for continuous use, add a –session– value to the username portion with an arbitrary session ID:

{% hint style="info" %}
Session IDs are limited to 32 alphanumeric characters (no minimum). Session IDs cannot include hyphens "-" as this will act as a separator and end the "username" portion of the connection string.
{% endhint %}

{% tabs %}
{% tab title="cURL" %}

<pre class="language-bash" data-overflow="wrap"><code class="lang-bash"><strong>curl -x http://account-accountName-pipeline-pipelineName-session-randomSessionString:pipelinePassword@ip.nimbleway.com:7000 https://ipinfo.io
</strong></code></pre>

{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

proxies = {
    'http': 'http://account-accountName-pipeline-pipelineName-session-randomSessionString:pipelinePassword@ip.nimbleway.com:7000',
    'https': 'https://account-accountName-pipeline-pipelineName-session-randomSessionString:pipelinePassword@ip.nimbleway.com:7000'
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
      host: "account-accountName-pipeline-pipelineName-session-randomSessionString:pipelinePassword@ip.nimbleway.com",
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
 proxyURL, err := url.Parse("http://account-accountName-pipeline-pipelineName-session-randomSessionString:pipelinePassword@ip.nimbleway.com:7000")
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

A session retains its assigned IP as long as it remains active. If activity stops, Nimble will keep the session alive for 10 additional minutes before rotating the IP.

### Using sticky sessions with Authenticated IPs

When using an Authenticated IP, your sticky/rotating session settings are defined only in the target pipeline's configuration. When defining/modifying a pipeline, you can choose if your IP should be rotated for every request, or in fixed session intervals such as 1, 3, 5, 10, or 30 minutes.

You can create/modify your pipelines in one of two ways:

* [x] Using the **Nimble IP** page in the [Nimble User Dashboard](https://app.nimbleway.com/login)
* [x] Using the `/account/pipelines` endpoint of the [**Admin API**](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference#pipelines)**.**

### Handling IP Replacement

Inevitably, IPs will occasionally become unavailable during a session. Nimble provides you with three options that instruct our system how to handle an IP becoming unavailable during a session:

1. **Replace IP when it's no longer available:** Nimble will replace a lost IP with another IP that meets your original request settings.
2. **Select another IP within the same ASN:** Nimble will replace a lost IP with another IP from the same ASN as the previous one, improving the likelihood of smooth session resumption.
3. **Do not replace - Fail request:** Nimble will not replace the IP, and will fail the request with a message that the session's IP has been lost.

If retaining sessions for long periods of time with high geographic accuracy is important for your use case, we recommend trying [**our new Geo-sessions.**](https://docs.nimbleway.io/nimble-sdk/proxy-api/nimble-ip-functions/geo-sessions-stickier-location-based-sessions)

IP Replacement behavior is set in your pipeline settings. This can be adjusted via the [Nimble Dashboard](https://docs.nimbleway.io/management-tools/nimble-dashboard/managing-pipelines) under the settings of each pipeline, or [Nimble Admin API's](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference) `/v1/account/pipelines/{pipelineName}` "Update a Pipeline" endpoint.&#x20;
