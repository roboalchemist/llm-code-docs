# Source: https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api/real-time-ecommerce-request.md

# Real-time ecommerce request

### Request Example: product search

To make a simple request for a single market search page, use the `/realtime/ecommerce` endpoint and include the Amazon/Walmart URL.

{% hint style="success" %}
We support any Amazon/Walmart/HomeDepot **`URL`** including product page, search page, category page, etc.
{% endhint %}

### **Request Options**

| Parameter | Required                   | Description                                                                                                                                                                                                                                                                   |
| --------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vendor    | Required                   | ENUM \| `walmart`, `amazon`, `homedepot`                                                                                                                                                                                                                                      |
| url       | Required                   | String \| any walmart/amazon/homedepot URL (product, search, category, etc)                                                                                                                                                                                                   |
| country   | Optional (default = all)   | String \| Country used to access the target URL, use [ISO Alpha-2 Country Codes](https://www.nationsonline.org/oneworld/country_code_list.htm) i.e. US, DE, GB                                                                                                                |
| state     | Optional                   | String \| For targeting US states (does not include regions or territories in other countries). Two-letter state code, e.g. NY, IL, etc.                                                                                                                                      |
| city      | Optional                   | String \| For targeting large cities and metro areas around the globe. When targeting major US cities, you must include state as well. [Click here for a list of available cities.](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference#location) |
| zip       | optional                   | String \| A 5-digit US zip code. If provided, the closest store to the provided zip code is selected.                                                                                                                                                                         |
| locale    | Optional (default = en)    | String \| LCID standard locale used for the URL request. Alternatively, user can use `auto` for automatic locale based on country targeting.                                                                                                                                  |
| parse     | Optional (default = false) | Boolean \| true \| false Instructs Nimble whether to structure the results into a JSON format or return the raw HTML.                                                                                                                                                         |

**Walmart Options**

| Parameter | Required                                                                                         | Description                                                                        |
| --------- | ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- |
| store     | <p>optional<br>(<code>zip</code> is <strong>required</strong> when using <code>store</code>)</p> | String \| If not provided, the closest store to the provided zip code is selected. |

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see \
[E-commerce API Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api/e-commerce-api-authentication).
{% endhint %}

{% hint style="success" %}
Every request sent through Nimble API is automatically routed through Nimble IP - our premium proxy network!
{% endhint %}

### Request Example: product page

To make a simple request for a single market page, use the `/realtime/ecommerce` endpoint with the following syntax:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/ecommerce' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "vendor": "walmart",
    "url": "https://www.walmart.com/ip/Simple-Mobile-Apple....",
    "country": "US",
    "zip": "90210",
    "locale": "en"
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/ecommerce'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "vendor": "walmart",
    "url": "https://www.walmart.com/ip/Simple-Mobile-Apple....",
    "country": "US",
    "zip": "90210",
    "locale": "en"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/ecommerce';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "vendor": "walmart",
  "url": "https://www.walmart.com/ip/Simple-Mobile-Apple....",
  "country": "US",
  "zip": "90210",
  "locale": "en"
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
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/ecommerce"
 payload := []byte(`{
  "vendor": "walmart",
  "url": "https://www.walmart.com/ip/Simple-Mobile-Apple....",
  "country": "US",
  "zip": "90210",
  "locale": "en"
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

### Request Example: product search

This is example for Product Search requests - use the same endpoint and parameters as a simple product page request, and simply require a different `URL` to be sent in the URL field.&#x20;

To make a simple request for a single market search page, use the `/realtime/ecommerce` endpoint with the following syntax:

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/ecommerce' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "vendor": "walmart",
    "url": "https://www.walmart.com/search?q=A-Product-Search..."
    "country": "US",
    "zip": "90210",
    "locale": "en"
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/ecommerce'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "vendor": "walmart",
    "url": "https://www.walmart.com/search?q=A-Product-Search...",
    "country": "US",
    "zip": "90210",
    "locale": "en"
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())

```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/ecommerce';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "vendor": "walmart",
  "url": "https://www.walmart.com/search?q=A-Product-Search...",
  "country": "US",
  "zip": "90210",
  "locale": "en"
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
 "fmt"
 "net/http"
 "encoding/json"
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/ecommerce"
 payload := []byte(`{
  "vendor": "walmart",
  "url": "https://www.walmart.com/search?q=A-Product-Search...",
  "country": "US",
  "zip": "90210",
  "locale": "en"
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

### **Response**

**Headers**

X-Task-ID: string

**Payload examples:**

If parsing was disabled or omitted in the request, the result data will be the raw HTML of the requested page. If parsing was enabled, a JSON object with a parsed version of the page will be delivered, with the raw HTML included under the `html_content` property.

**200 OK**

{% code overflow="wrap" %}

```json
{
    "status": "success",
    "html_content": "<html>[market page HTML]... </html>",
    "parsing": {
        "status": "success",
        "entities": {
            [EntityType1]: [{
                ...
            }, {
                ...
            }],
            [EntityType2]: [{
                ...
            }, {
                ...
            }]

        },
        "total_entities_count": 20,
    "entities_count": {
        [EntityType1]: 10,
        [EntityType2]: 10
    },
    "metrics": {}
    }
}
```

{% endcode %}

**500 Error**

{% code overflow="wrap" %}

```json
{
          "status": "error",
        "task_id": "<task_id>",
        "msg": "can't download the query response - please try again"
}
```

{% endcode %}

**400 Input Error**

{% code overflow="wrap" %}

```json
{
        "status": "failed",
        "msg": error
}
```

{% endcode %}

### **Response Codes**

| Status | Description                                   |
| ------ | --------------------------------------------- |
| 200    | OK                                            |
| 400    | The requested resource could not be reached   |
| 401    | Unauthorized/invalid credental string         |
| 500    | Internal service error                        |
| 501    | An error was encountered by the proxy service |
