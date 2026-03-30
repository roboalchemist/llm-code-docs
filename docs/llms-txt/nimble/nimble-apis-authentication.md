# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/nimble-apis-authentication.md

# Nimble APIs Authentication

Nimble API uses Basic access authentication on every request. Use your [Nimble Admin API](https://docs.nimbleway.io/management-tools/nimble-admin-api/admin-api-reference) credentials to generate a base64 encoded credential string before making requests. Your account manager will provide you with your credentials when your account is opened.

To generate a credential string, use the following syntax:

```javascript
base64(username:password)
```

For example, for the username `user@nimbleway.com` and the password `pass123`, the following credential string would be generated:\
\
`dXNlckBuaW1ibGV3YXkuY29tOnBhc3MxMjM=`

This credential string is then applied to the header of every request in the following form:

{% hint style="info" %}
Applicable for all API Endpoints - [Web](https://docs.nimbleway.io/nimble-sdk/web-api), [SERP](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api), [Maps](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api), [eCommerce](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api) and [Social](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/social-api) &#x20;
{% endhint %}

{% tabs %}
{% tab title="cURL" %}

```bash
curl --location --request POST 'https://api.webit.live/api/v1/realtime/web' \
--header 'Authorization: Basic dXNlckBuaW1ibGV3YXkuY29tOnBhc3MxMjM=' \
--header 'Content-Type: application/json' \
--data-raw '{
    // add your parameters here
}'
```

{% endtab %}

{% tab title="Python" %}

```python
import requests

url = 'https://api.webit.live/api/v1/realtime/web'
headers = {
    'Authorization': 'Basic dXNlckBuaW1ibGV3YXkuY29tOnBhc3MxMjM=',
    'Content-Type': 'application/json'
}
data = {
    # Add your parameters here
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
```

{% endtab %}

{% tab title="Node.js" %}

```javascript
const axios = require('axios');

const url = 'https://api.webit.live/api/v1/realtime/web';
const headers = {
  'Authorization': 'Basic dXNlckBuaW1ibGV3YXkuY29tOnBhc3MxMjM=',
  'Content-Type': 'application/json'
};
const data = {
  // Add your parameters here
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
)

func main() {
 url := "https://api.webit.live/api/v1/realtime/web"
 payload := []byte(`{
  // Add your parameters here
 }`)
 headers := map[string]string{
  "Authorization":  "Basic dXNlckBuaW1ibGV3YXkuY29tOnBhc3MxMjM=",
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
