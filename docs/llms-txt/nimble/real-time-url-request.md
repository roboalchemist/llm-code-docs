# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/real-time-url-request.md

# Real-time URL request

### Basic Request Syntax

Basic real-time requests to the Web API are made using the ***<https://api.webit.live/api/v1/realtime/web>*** endpoint. A simple request uses the following syntax:

{% hint style="info" %}
Nimble APIs requires that a base64 encoded credential string be sent with every request to authenticate your account. For detailed examples, see [Nimble APIs Authentication](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication).
{% endhint %}

{% tabs %}
{% tab title="cURL" %}
{% code overflow="wrap" %}

```bash
curl -X POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic <credential string>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://www.example.com"
}'
```

{% endcode %}
{% endtab %}

{% tab title="Python" %}
{% code overflow="wrap" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic <credential string>',
    'Content-Type': 'application/json'
}
data = {
    "url": "https://www.example.com"
}

response = requests.post(url, headers=headers, json=data)
```

{% endcode %}
{% endtab %}

{% tab title="Node.js" %}
{% code overflow="wrap" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic <credential string>',
  'Content-Type': 'application/json'
};
const data = {
  "url": "https://www.example.com"
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

{% endcode %}
{% endtab %}

{% tab title="Go" %}
{% code overflow="wrap" %}

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
  "url": "https://www.example.com"
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

{% endcode %}
{% endtab %}
{% endtabs %}

“URL” is the only required parameter that must be sent with each request besides the credential string, and defines the address from which to collect data. Additional parameters, such as geolocation targeting, parsing control, and custom headers can also be added.&#x20;

### **Response**

If successful, the WebAPI will return a **200 OK** status with the following data structure:

{% code overflow="wrap" %}

```json
{ 
        "status": "success",
        "html_content": string,
        "parsing": {
             "status": "success",
             "entities": { },
             "total_entities_count": 0,
             "entities_count": { }
        }
}
```

{% endcode %}

The <mark style="color:red;background-color:yellow;">html\_content</mark> node contains the full HTML of the requested page, and if parsing was enabled, the <mark style="color:red;background-color:yellow;">parsingnode</mark> will contain a structured JSON object of the data.
