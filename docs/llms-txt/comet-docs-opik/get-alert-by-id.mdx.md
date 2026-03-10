# Source: https://www.comet.com/docs/opik/reference/rest-api/alerts/get-alert-by-id.mdx

# Get Alert by id

GET http://localhost:5173/api/v1/private/alerts/{id}

Get Alert by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/alerts/get-alert-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/alerts/{id}:
    get:
      operationId: get-alert-by-id
      summary: Get Alert by id
      description: Get Alert by id
      tags:
        - subpackage_alerts
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Alert resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Alert_Public'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AlertPublicAlertType:
      type: string
      enum:
        - general
        - slack
        - pagerduty
      title: AlertPublicAlertType
    Webhook_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        url:
          type: string
        secret_token:
          type: string
        headers:
          type: object
          additionalProperties:
            type: string
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
      required:
        - url
      title: Webhook_Public
    AlertTriggerPublicEventType:
      type: string
      enum:
        - trace:errors
        - trace:feedback_score
        - trace_thread:feedback_score
        - prompt:created
        - prompt:committed
        - trace:guardrails_triggered
        - prompt:deleted
        - experiment:finished
        - trace:cost
        - trace:latency
      title: AlertTriggerPublicEventType
    AlertTriggerConfigPublicType:
      type: string
      enum:
        - scope:project
        - threshold:feedback_score
        - threshold:cost
        - threshold:latency
        - threshold:errors
      title: AlertTriggerConfigPublicType
    AlertTriggerConfig_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        alert_trigger_id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/AlertTriggerConfigPublicType'
        config_value:
          type: object
          additionalProperties:
            type: string
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
      required:
        - type
      title: AlertTriggerConfig_Public
    AlertTrigger_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        alert_id:
          type: string
          format: uuid
        event_type:
          $ref: '#/components/schemas/AlertTriggerPublicEventType'
        trigger_configs:
          type: array
          items:
            $ref: '#/components/schemas/AlertTriggerConfig_Public'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
      required:
        - event_type
      title: AlertTrigger_Public
    Alert_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        enabled:
          type: boolean
        alert_type:
          $ref: '#/components/schemas/AlertPublicAlertType'
        metadata:
          type: object
          additionalProperties:
            type: string
        webhook:
          $ref: '#/components/schemas/Webhook_Public'
        triggers:
          type: array
          items:
            $ref: '#/components/schemas/AlertTrigger_Public'
        created_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
      required:
        - webhook
      title: Alert_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/alerts/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/alerts/id';
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

	url := "http://localhost:5173/api/v1/private/alerts/id"

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

url = URI("http://localhost:5173/api/v1/private/alerts/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/alerts/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/alerts/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/alerts/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/alerts/id")! as URL,
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