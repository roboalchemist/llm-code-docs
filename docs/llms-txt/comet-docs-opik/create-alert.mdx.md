# Source: https://www.comet.com/docs/opik/reference/rest-api/alerts/create-alert.mdx

# Create alert

POST http://localhost:5173/api/v1/private/alerts
Content-Type: application/json

Create alert

Reference: https://www.comet.com/docs/opik/reference/rest-api/alerts/create-alert

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/alerts:
    post:
      operationId: create-alert
      summary: Create alert
      description: Create alert
      tags:
        - subpackage_alerts
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Alerts_createAlert_Response_201'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '409':
          description: Conflict
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '422':
          description: Unprocessable Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Alert_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AlertWriteAlertType:
      type: string
      enum:
        - general
        - slack
        - pagerduty
      title: AlertWriteAlertType
    Webhook_Write:
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
      required:
        - url
      title: Webhook_Write
    AlertTriggerWriteEventType:
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
      title: AlertTriggerWriteEventType
    AlertTriggerConfigWriteType:
      type: string
      enum:
        - scope:project
        - threshold:feedback_score
        - threshold:cost
        - threshold:latency
        - threshold:errors
      title: AlertTriggerConfigWriteType
    AlertTriggerConfig_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        type:
          $ref: '#/components/schemas/AlertTriggerConfigWriteType'
        config_value:
          type: object
          additionalProperties:
            type: string
      required:
        - type
      title: AlertTriggerConfig_Write
    AlertTrigger_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        event_type:
          $ref: '#/components/schemas/AlertTriggerWriteEventType'
        trigger_configs:
          type: array
          items:
            $ref: '#/components/schemas/AlertTriggerConfig_Write'
      required:
        - event_type
      title: AlertTrigger_Write
    Alert_Write:
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
          $ref: '#/components/schemas/AlertWriteAlertType'
        metadata:
          type: object
          additionalProperties:
            type: string
        webhook:
          $ref: '#/components/schemas/Webhook_Write'
        triggers:
          type: array
          items:
            $ref: '#/components/schemas/AlertTrigger_Write'
      required:
        - webhook
      title: Alert_Write
    Alerts_createAlert_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Alerts_createAlert_Response_201
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

url = "http://localhost:5173/api/v1/private/alerts"

payload = { "webhook": { "url": "https://hooks.example.com/alerts" } }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/alerts';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"webhook":{"url":"https://hooks.example.com/alerts"}}'
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

	url := "http://localhost:5173/api/v1/private/alerts"

	payload := strings.NewReader("{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}")

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

url = URI("http://localhost:5173/api/v1/private/alerts")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/alerts")
  .header("Content-Type", "application/json")
  .body("{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/alerts', [
  'body' => '{
  "webhook": {
    "url": "https://hooks.example.com/alerts"
  }
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/alerts");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["webhook": ["url": "https://hooks.example.com/alerts"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/alerts")! as URL,
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