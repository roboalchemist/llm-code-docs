# Source: https://www.comet.com/docs/opik/reference/rest-api/runners/get-runner.mdx

# Get local runner

GET http://localhost:5173/api/v1/private/local-runners/{runnerId}

Get a single local runner with its registered agents

Reference: https://www.comet.com/docs/opik/reference/rest-api/runners/get-runner

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/local-runners/{runnerId}:
    get:
      operationId: get-runner
      summary: Get local runner
      description: Get a single local runner with its registered agents
      tags:
        - subpackage_runners
      parameters:
        - name: runnerId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Runner details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LocalRunner'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    LocalRunnerStatus:
      type: string
      enum:
        - pairing
        - connected
        - disconnected
      title: LocalRunnerStatus
    Param:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
      required:
        - name
        - type
      title: Param
    Agent:
      type: object
      properties:
        name:
          type: string
        project:
          type: string
        description:
          type: string
        language:
          type: string
        executable:
          type: string
        source_file:
          type: string
        params:
          type: array
          items:
            $ref: '#/components/schemas/Param'
        timeout:
          type: integer
      title: Agent
    LocalRunner:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        status:
          $ref: '#/components/schemas/LocalRunnerStatus'
        connected_at:
          type: string
          format: date-time
        agents:
          type: array
          items:
            $ref: '#/components/schemas/Agent'
      title: LocalRunner
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

url = "http://localhost:5173/api/v1/private/local-runners/runnerId"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/local-runners/runnerId';
const options = {method: 'GET', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/local-runners/runnerId"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("GET", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/local-runners/runnerId")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/local-runners/runnerId")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/local-runners/runnerId', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/local-runners/runnerId");
var request = new RestRequest(Method.GET);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/local-runners/runnerId")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
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