# Source: https://www.comet.com/docs/opik/reference/rest-api/alerts/update-alert.mdx

# Update alert

PUT http://localhost:5173/api/v1/private/alerts/{id}
Content-Type: application/json

Update alert

Reference: https://www.comet.com/docs/opik/reference/rest-api/alerts/update-alert

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/alerts/{id}:
    put:
      operationId: update-alert
      summary: Update alert
      description: Update alert
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
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Alerts_updateAlert_Response_204'
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
    Alerts_updateAlert_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Alerts_updateAlert_Response_204
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

url = "http://localhost:5173/api/v1/private/alerts/id"

payload = { "webhook": { "url": "https://hooks.example.com/alerts" } }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/alerts/id';
const options = {
  method: 'PUT',
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

	url := "http://localhost:5173/api/v1/private/alerts/id"

	payload := strings.NewReader("{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}")

	req, _ := http.NewRequest("PUT", url, payload)

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

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/alerts/id")
  .header("Content-Type", "application/json")
  .body("{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/alerts/id', [
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

var client = new RestClient("http://localhost:5173/api/v1/private/alerts/id");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"webhook\": {\n    \"url\": \"https://hooks.example.com/alerts\"\n  }\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["webhook": ["url": "https://hooks.example.com/alerts"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/alerts/id")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PUT"
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