# Source: https://www.comet.com/docs/opik/reference/rest-api/dashboards/delete-dashboards-batch.mdx

# Delete dashboards

POST http://localhost:5173/api/v1/private/dashboards/delete-batch
Content-Type: application/json

Delete dashboards batch

Reference: https://www.comet.com/docs/opik/reference/rest-api/dashboards/delete-dashboards-batch

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/dashboards/delete-batch:
    post:
      operationId: delete-dashboards-batch
      summary: Delete dashboards
      description: Delete dashboards batch
      tags:
        - subpackage_dashboards
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Dashboards_deleteDashboardsBatch_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BatchDelete'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    BatchDelete:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
            format: uuid
      required:
        - ids
      title: BatchDelete
    Dashboards_deleteDashboardsBatch_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Dashboards_deleteDashboardsBatch_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/dashboards/delete-batch"

payload = { "ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7", "f47ac10b-58cc-4372-a567-0e02b2c3d479"] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/dashboards/delete-batch';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"ids":["3fa85f64-5717-4562-b3fc-2c963f66afa6","7c9e6679-7425-40de-944b-e07fc1f90ae7","f47ac10b-58cc-4372-a567-0e02b2c3d479"]}'
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
	"strings"
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/private/dashboards/delete-batch"

	payload := strings.NewReader("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n    \"f47ac10b-58cc-4372-a567-0e02b2c3d479\"\n  ]\n}")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/dashboards/delete-batch")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n    \"f47ac10b-58cc-4372-a567-0e02b2c3d479\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/dashboards/delete-batch")
  .header("Content-Type", "application/json")
  .body("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n    \"f47ac10b-58cc-4372-a567-0e02b2c3d479\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/dashboards/delete-batch', [
  'body' => '{
  "ids": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "7c9e6679-7425-40de-944b-e07fc1f90ae7",
    "f47ac10b-58cc-4372-a567-0e02b2c3d479"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/dashboards/delete-batch");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\",\n    \"f47ac10b-58cc-4372-a567-0e02b2c3d479\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7", "f47ac10b-58cc-4372-a567-0e02b2c3d479"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/dashboards/delete-batch")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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