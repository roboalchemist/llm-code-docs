# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/delete-span-by-id.mdx

# Delete span by id

DELETE http://localhost:5173/api/v1/private/spans/{id}

Delete span by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/delete-span-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans/{id}:
    delete:
      operationId: delete-span-by-id
      summary: Delete span by id
      description: Delete span by id
      tags:
        - subpackage_spans
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Spans_deleteSpanById_Response_204'
        '501':
          description: Not implemented
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    Spans_deleteSpanById_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Spans_deleteSpanById_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.delete(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b';
const options = {method: 'DELETE', headers: {'Content-Type': 'application/json'}, body: '{}'};

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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("DELETE", url, payload)

	req.Header.Add("Content-Type", "application/json")

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

url = URI("http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Delete.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.delete("http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b");
var request = new RestRequest(Method.DELETE);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans/a3f47b9e-8c2d-4f1a-9b7e-2d5f3c6a1e4b")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

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