# Source: https://www.comet.com/docs/opik/reference/rest-api/workspaces/get-cost.mdx

# Get cost daily data

POST http://localhost:5173/api/v1/private/workspaces/costs
Content-Type: application/json

Get cost daily data

Reference: https://www.comet.com/docs/opik/reference/rest-api/workspaces/get-cost

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/workspaces/costs:
    post:
      operationId: get-cost
      summary: Get cost daily data
      description: Get cost daily data
      tags:
        - subpackage_workspaces
      responses:
        '200':
          description: Workspace cost data by days
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkspaceMetricResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WorkspaceMetricsSummaryRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    WorkspaceMetricsSummaryRequest:
      type: object
      properties:
        project_ids:
          type: array
          items:
            type: string
            format: uuid
        interval_start:
          type: string
          format: date-time
        interval_end:
          type: string
          format: date-time
        start_before_end:
          type: boolean
      required:
        - interval_start
        - interval_end
      title: WorkspaceMetricsSummaryRequest
    Result:
      type: object
      properties:
        name:
          type: string
        current:
          type: number
          format: double
        previous:
          type: number
          format: double
      title: Result
    WorkspaceMetricResponse:
      type: object
      properties:
        results:
          type: array
          items:
            $ref: '#/components/schemas/Result'
      title: WorkspaceMetricResponse
    ErrorMessage:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/workspaces/costs"

payload = {
    "interval_start": "2024-04-01T00:00:00Z",
    "interval_end": "2024-04-07T23:59:59Z"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/workspaces/costs';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"interval_start":"2024-04-01T00:00:00Z","interval_end":"2024-04-07T23:59:59Z"}'
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

	url := "http://localhost:5173/api/v1/private/workspaces/costs"

	payload := strings.NewReader("{\n  \"interval_start\": \"2024-04-01T00:00:00Z\",\n  \"interval_end\": \"2024-04-07T23:59:59Z\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/workspaces/costs")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"interval_start\": \"2024-04-01T00:00:00Z\",\n  \"interval_end\": \"2024-04-07T23:59:59Z\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/workspaces/costs")
  .header("Content-Type", "application/json")
  .body("{\n  \"interval_start\": \"2024-04-01T00:00:00Z\",\n  \"interval_end\": \"2024-04-07T23:59:59Z\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/workspaces/costs', [
  'body' => '{
  "interval_start": "2024-04-01T00:00:00Z",
  "interval_end": "2024-04-07T23:59:59Z"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/workspaces/costs");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"interval_start\": \"2024-04-01T00:00:00Z\",\n  \"interval_end\": \"2024-04-07T23:59:59Z\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "interval_start": "2024-04-01T00:00:00Z",
  "interval_end": "2024-04-07T23:59:59Z"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/workspaces/costs")! as URL,
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