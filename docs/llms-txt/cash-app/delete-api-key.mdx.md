# Source: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/delete-api-key.mdx

# Delete API key

DELETE https://api.cash.app/management/v1/api-keys/{api_key_id}

Deletes an API key. After an API key is deleted, it can no longer be used for authentication. All API clients using the secret associated with this API key  will immediately be forbidden from talking to the Cash App Pay API.

<Note title="Note">
 There is no way to un-delete an API key, so treat this endpoint with caution in production environments.
</Note>

**This endpoint is rate limited to 5 QPS.**

Scopes: `API_KEYS_WRITE`

Reference: https://developers.cash.app/cash-app-pay-partner-api/api-reference/management-api/delete-api-key

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: API
  version: 1.0.0
paths:
  /api-keys/{api_key_id}:
    delete:
      operationId: delete-api-key
      summary: Delete API key
      description: >-
        Deletes an API key. After an API key is deleted, it can no longer be
        used for authentication. All API clients using the secret associated
        with this API key  will immediately be forbidden from talking to the
        Cash App Pay API.


        <Note title="Note">
         There is no way to un-delete an API key, so treat this endpoint with caution in production environments.
        </Note>


        **This endpoint is rate limited to 5 QPS.**


        Scopes: `API_KEYS_WRITE`
      tags:
        - subpackage_apiKeys
      parameters:
        - name: api_key_id
          in: path
          required: true
          schema:
            type: string
        - name: Accept
          in: header
          required: true
          schema:
            type: string
        - name: X-Region
          in: header
          required: true
          schema:
            type: string
        - name: X-Signature
          in: header
          required: true
          schema:
            type: string
        - name: User-Agent
          in: header
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/apiKeys_delete-api-key_Response_200'
servers:
  - url: https://api.cash.app/management/v1
  - url: https://sandbox.api.cash.app/management/v1
components:
  schemas:
    apiKeys_delete-api-key_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: apiKeys_delete-api-key_Response_200

```

## SDK Code Examples

```python
import requests

url = "https://api.cash.app/management/v1/api-keys/api_key_id"

headers = {
    "Accept": "Accept",
    "X-Region": "X-Region",
    "X-Signature": "X-Signature",
    "User-Agent": "User-Agent"
}

response = requests.delete(url, headers=headers)

print(response.json())
```

```javascript
const url = 'https://api.cash.app/management/v1/api-keys/api_key_id';
const options = {
  method: 'DELETE',
  headers: {
    Accept: 'Accept',
    'X-Region': 'X-Region',
    'X-Signature': 'X-Signature',
    'User-Agent': 'User-Agent'
  }
};

try {
  const response = await fetch(url, options);
  const data = await response.json();
  console.log(data);
} catch (error) {
  console.error(error);
}
```

```go
package main

import (
	"fmt"
	"net/http"
	"io"
)

func main() {

	url := "https://api.cash.app/management/v1/api-keys/api_key_id"

	req, _ := http.NewRequest("DELETE", url, nil)

	req.Header.Add("Accept", "Accept")
	req.Header.Add("X-Region", "X-Region")
	req.Header.Add("X-Signature", "X-Signature")
	req.Header.Add("User-Agent", "User-Agent")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := io.ReadAll(res.Body)

	fmt.Println(res)
	fmt.Println(string(body))

}
```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cash.app/management/v1/api-keys/api_key_id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["Accept"] = 'Accept'
request["X-Region"] = 'X-Region'
request["X-Signature"] = 'X-Signature'
request["User-Agent"] = 'User-Agent'

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("https://api.cash.app/management/v1/api-keys/api_key_id")
  .header("Accept", "Accept")
  .header("X-Region", "X-Region")
  .header("X-Signature", "X-Signature")
  .header("User-Agent", "User-Agent")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.cash.app/management/v1/api-keys/api_key_id', [
  'headers' => [
    'Accept' => 'Accept',
    'User-Agent' => 'User-Agent',
    'X-Region' => 'X-Region',
    'X-Signature' => 'X-Signature',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cash.app/management/v1/api-keys/api_key_id");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Accept", "Accept");
request.AddHeader("X-Region", "X-Region");
request.AddHeader("X-Signature", "X-Signature");
request.AddHeader("User-Agent", "User-Agent");
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "Accept": "Accept",
  "X-Region": "X-Region",
  "X-Signature": "X-Signature",
  "User-Agent": "User-Agent"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cash.app/management/v1/api-keys/api_key_id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error as Any)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
```