# Source: https://www.comet.com/docs/opik/reference/rest-api/dashboards/update-dashboard.mdx

# Update dashboard

PATCH http://localhost:5173/api/v1/private/dashboards/{dashboardId}
Content-Type: application/json

Update dashboard by id. Partial updates are supported - only provided fields will be updated.

Reference: https://www.comet.com/docs/opik/reference/rest-api/dashboards/update-dashboard

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/dashboards/{dashboardId}:
    patch:
      operationId: update-dashboard
      summary: Update dashboard
      description: >-
        Update dashboard by id. Partial updates are supported - only provided
        fields will be updated.
      tags:
        - subpackage_dashboards
      parameters:
        - name: dashboardId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Updated dashboard
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dashboard_Public'
        '404':
          description: Dashboard not found
          content:
            application/json:
              schema:
                description: Any type
        '409':
          description: Conflict - dashboard with this name already exists
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DashboardUpdate_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    DashboardUpdate_Public:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        config:
          $ref: '#/components/schemas/JsonNode_Public'
      title: DashboardUpdate_Public
    Dashboard_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        workspace_id:
          type: string
        name:
          type: string
        slug:
          type: string
        description:
          type: string
        config:
          $ref: '#/components/schemas/JsonNode_Public'
        created_by:
          type: string
        last_updated_by:
          type: string
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
      required:
        - name
        - config
      title: Dashboard_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/dashboards/dashboardId"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/dashboards/dashboardId';
const options = {method: 'PATCH', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/dashboards/dashboardId"

	payload := strings.NewReader("{}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/dashboards/dashboardId")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/dashboards/dashboardId")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/dashboards/dashboardId', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/dashboards/dashboardId");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/dashboards/dashboardId")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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