# Source: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/get-evaluator-logs-by-id.mdx

# Get automation rule evaluator logs by id

GET http://localhost:5173/api/v1/private/automations/evaluators/{id}/logs

Get automation rule evaluator logs by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/automation-rule-evaluators/get-evaluator-logs-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/automations/evaluators/{id}/logs:
    get:
      operationId: get-evaluator-logs-by-id
      summary: Get automation rule evaluator logs by id
      description: Get automation rule evaluator logs by id
      tags:
        - subpackage_automationRuleEvaluators
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 1000
      responses:
        '200':
          description: Automation rule evaluator logs resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/LogPage'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    LogItemLevel:
      type: string
      enum:
        - INFO
        - WARN
        - ERROR
        - DEBUG
        - TRACE
      title: LogItemLevel
    LogItem:
      type: object
      properties:
        timestamp:
          type: string
          format: date-time
        rule_id:
          type: string
          format: uuid
        level:
          $ref: '#/components/schemas/LogItemLevel'
        message:
          type: string
        markers:
          type: object
          additionalProperties:
            type: string
      title: LogItem
    LogPage:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/LogItem'
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
      title: LogPage

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/automations/evaluators/id/logs"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/automations/evaluators/id/logs';
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

	url := "http://localhost:5173/api/v1/private/automations/evaluators/id/logs"

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

url = URI("http://localhost:5173/api/v1/private/automations/evaluators/id/logs")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/automations/evaluators/id/logs")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/automations/evaluators/id/logs', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/automations/evaluators/id/logs");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/automations/evaluators/id/logs")! as URL,
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