# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions/custom-headers-and-cookies.md

# Custom Headers & Cookies

## What? <a href="#what-and-why" id="what-and-why"></a>

The Nimble Web API provides the ability to enhance your scraping requests by including custom headers or cookies. These can be defined in either string or object format and sent as part of your request to the target domain. This feature is crucial for accessing additional data that may be gated behind specific user settings or preferences stored in cookies, allowing you to interact with the website in a more personalized and context-aware manner.

## &#x20;Why? <a href="#what-and-why" id="what-and-why"></a>

* **Unlock Access to Personalized Data**: By including custom headers or cookies, you can retrieve data that is tailored to specific user session contexts, which is often otherwise inaccessible.
* **Enhance Data Retrieval Capabilities**: Support diverse use cases by leveraging cookies and headers to interact with websites in ways that mimic real user behavior, ensuring you capture the most relevant data.
* **Improve Data Retrieval Efficiency**: Reduce the need for additional scraping attempts by ensuring that your initial requests are as comprehensive and accurate as possible, saving time and resources.

## Additional Information <a href="#how" id="how"></a>

* <mark style="color:green;">Supported</mark> by real-time, asynchronous, and batch requests.
* <mark style="color:green;">Supported</mark> Endpoints: [Web](https://docs.nimbleway.io/nimble-sdk/web-api)
* <mark style="color:red;">Not supported</mark> Endpoints: [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api) and [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api).

{% hint style="warning" %}
Misconfiguration of custom headers or cookies may negatively impact the success rates of your scraping tasks, as improper use may trigger detection by the target website. \
\
This feature is intended for advanced users, so please exercise caution and ensure configurations are accurate.
{% endhint %}

## Request Option <a href="#request-option" id="request-option"></a>

<table><thead><tr><th width="198">Parameter</th><th width="206">Required</th><th>Description</th></tr></thead><tbody><tr><td><code>url</code></td><td>Required </td><td>URL | The page or resource to be fetched. Note: when using a URL with a query string, encode the URL and place it at the end of the query string</td></tr><tr><td><code>headers</code>*</td><td>Optional</td><td>String | JSON with key/value structure to pass the required headers</td></tr><tr><td><code>method</code></td><td>Required when <code>headers</code> is used to send POST request</td><td>Enum | <code>GET</code>, <code>POST</code>. <br>Use POST to send forms to the target site</td></tr><tr><td><code>body</code></td><td>Required when <code>headers</code> is used to send POST request</td><td>Object | JSON with key/value structure or string to pass needed payload</td></tr><tr><td><code>cookies</code></td><td>Optional</td><td>String | The cookie string uses a syntax of <code>key1=value1;key2=value2;...</code> format, and does not accept a domain parameter, always defaulting to the requested URL's domain.<br><br>OR<br><br>List Objects | List of attach cookie objects. The cookie object allows for one or multiple cookies to be set, with each one containing three parameters - <code>key</code>, <code>value</code>, <code>domain</code></td></tr><tr><td><code>cookies.key</code></td><td>Required when <code>cookies</code> is used</td><td>String | The name of the attached cookie</td></tr><tr><td><code>cookies.value</code></td><td>Required when <code>cookies</code> is used</td><td>String | The value of the attached cookie.</td></tr><tr><td><code>cookies.domain</code></td><td>Optional</td><td>URL | The domain with which this cookie is associated. If a domain is not defined, Nimble will use the requested URL's domain by default.</td></tr></tbody></table>

{% hint style="info" %}
\* Please do not include any cookies when sending custom headers.
{% endhint %}

### Example Request - Sending POST Request with Headers <a href="#example" id="example"></a>

If you wish to send POST data with your target domain as part of your request, such as when submitting a form, please use the following syntax:

{% tabs %}
{% tab title="cURL" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com",
    "method": "POST",
    "headers": {
    "Content-Type": "application/json",
        "Some-Extra-Header": "some-extra-header"
    },
    "body": {
        "a": 1,
        "b": 2
    }
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com",
    "method": "POST",
    "headers": {
        "Content-Type": "application/json",
        "Some-Extra-Header": "some-extra-header"
    },
    "body": {
        "a": 1,
        "b": 2
    }
}

response = requests.post(url, headers=headers, json=data)

```

{% endtab %}

{% tab title="Node.js" %}

```n4js
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json",
    "Some-Extra-Header": "some-extra-header"
  },
  "body": {
    "a": 1,
    "b": 2
  }
};

axios.post(url, data, { headers })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
 "bytes"
 "encoding/base64"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.example.com",
  "method": "POST",
  "headers": {
   "Content-Type": "application/json",
   "Some-Extra-Header": "some-extra-header"
  },
  "body": {
   "a": 1,
   "b": 2
  }
 }`)
 headers := map[string]string{
  "Authorization":  "Basic <credential string>",
  "Content-Type":   "application/json",
 }

 req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
 if err != nil {
  fmt.Println(err)
  return
 }

 for key, value := range headers {
  req.Header.Set(key, value)
 }

 client := &http.Client{}
 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)
 // Read the response body if needed
 // body, err := ioutil.ReadAll(resp.Body)
 // fmt.Println(string(body))
}
```

{% endtab %}
{% endtabs %}

Please note that specifying a content-type header is required when submitting a POST request with data in the body.

### Example Request - **Cookie Object** <a href="#example" id="example"></a>

In the following example, a **Cookie Object** is used to select a particular store on the Lowe's website.

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/web/' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
    "country": "US",
    "cookies": [
        {
            "key": "sd",
            "value": "%7B%22id%22%3A%222209%22%2C%22zip%22%3A%2204769%22%2C%22city%22%3A%22Presque%20Isle%22%2C%22state%22%3A%22ME%22%2C%22name%22%3A%22Presque%20Isle%20Lowe's%22%2C%22region%22%3A%2218%22%7D",
            "domain": "lowes.com"
        }
    ]
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
    "country": "CA",
    "cookies": [
        {
            "key": "sd",
            "value": "%7B%22id%22%3A%222209%22%2C%22zip%22%3A%2204769%22%2C%22city%22%3A%22Presque%20Isle%22%2C%22state%22%3A%22ME%22%2C%22name%22%3A%22Presque%20Isle%20Lowe's%22%2C%22region%22%3A%2218%22%7D",
            "domain": "lowes.com"
        }
    ] 
}

response = requests.post(url, headers=headers, json=data)
```

{% endtab %}

{% tab title="Node.js" %}

```n4js
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
  "country": "CA",
  "cookies": [
        {
            "key": "sd",
            "value": "%7B%22id%22%3A%222209%22%2C%22zip%22%3A%2204769%22%2C%22city%22%3A%22Presque%20Isle%22%2C%22state%22%3A%22ME%22%2C%22name%22%3A%22Presque%20Isle%20Lowe's%22%2C%22region%22%3A%2218%22%7D",
            "domain": "lowes.com"
        }
    ]
};

axios.post(url, data, { headers })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
 "bytes"
 "encoding/base64"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
  "country": "CA",
  "cookies": [
          {
              "key": "sd",
              "value": "%7B%22id%22%3A%222209%22%2C%22zip%22%3A%2204769%22%2C%22city%22%3A%22Presque%20Isle%22%2C%22state%22%3A%22ME%22%2C%22name%22%3A%22Presque%20Isle%20Lowe's%22%2C%22region%22%3A%2218%22%7D",
              "domain": "lowes.com"
          }
      ]
 }`)
 headers := map[string]string{
  "Authorization":  "Basic <credential string>",
  "Content-Type":   "application/json",
 }

 req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
 if err != nil {
  fmt.Println(err)
  return
 }

 for key, value := range headers {
  req.Header.Set(key, value)
 }

 client := &http.Client{}
 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)
 // Read the response body if needed
 // body, err := ioutil.ReadAll(resp.Body)
 // fmt.Println(string(body))
}
```

{% endtab %}
{% endtabs %}

In the above example, the `key` is set to `sd` and the `value` is set to an encoded version of the following location object:

```json
{
    "id": "2209",
    "zip": "04769",
    "city": "Presque Isle",
    "state": "ME",
    "name": "Presque Isle Lowe's",
    "region": "18"
}
```

These values are unique to Lowe's website, and are not necessarily applicable to other websites.

### Example Request - **Cookie String**

In the following example, a **Cookie String** is used to select a particular store on the Lowe's website.

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/web/' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
    "country": "US",
    "cookies": "key1=value1;sd=%7B%22id%22%3A%222209..."
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
    "country": "CA",
    "cookies": "key1=value1;sd=%7B%22id%22%3A%222209..."
}

response = requests.post(url, headers=headers, json=data)
```

{% endtab %}

{% tab title="Node.js" %}

```n4js
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
  "country": "CA",
  "cookies": "key1=value1;sd=%7B%22id%22%3A%222209..."
};

axios.post(url, data, { headers })
  .then(response => {
    console.log(response.status);
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```

{% endtab %}

{% tab title="Go" %}

```go
package main

import (
 "bytes"
 "encoding/base64"
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  "url": "https://www.lowes.com/pd/CRAFTSMAN-M110-140-cc-21-in-Gas-Push-Lawn-Mower-with-Briggs-Stratton-Engine/1000676311",
  "country": "CA",
  "cookies": "key1=value1;sd=%7B%22id%22%3A%222209..."
 }`)
 headers := map[string]string{
  "Authorization":  "Basic <credential string>",
  "Content-Type":   "application/json",
 }

 req, err := http.NewRequest("POST", url, bytes.NewBuffer(payload))
 if err != nil {
  fmt.Println(err)
  return
 }

 for key, value := range headers {
  req.Header.Set(key, value)
 }

 client := &http.Client{}
 resp, err := client.Do(req)
 if err != nil {
  fmt.Println(err)
  return
 }
 defer resp.Body.Close()

 fmt.Println(resp.StatusCode)
 // Read the response body if needed
 // body, err := ioutil.ReadAll(resp.Body)
 // fmt.Println(string(body))
}
```

{% endtab %}
{% endtabs %}
