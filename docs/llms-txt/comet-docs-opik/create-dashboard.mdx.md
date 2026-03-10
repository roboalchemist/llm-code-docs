# Source: https://www.comet.com/docs/opik/reference/rest-api/dashboards/create-dashboard.mdx

# Create dashboard

POST http://localhost:5173/api/v1/private/dashboards
Content-Type: application/json

Create a new dashboard in a workspace

Reference: https://www.comet.com/docs/opik/reference/rest-api/dashboards/create-dashboard

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/dashboards:
    post:
      operationId: create-dashboard
      summary: Create dashboard
      description: Create a new dashboard in a workspace
      tags:
        - subpackage_dashboards
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dashboard_Public'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Dashboard_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode_Write:
      type: object
      properties: {}
      title: JsonNode_Write
    Dashboard_Write:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        config:
          $ref: '#/components/schemas/JsonNode_Write'
      required:
        - name
        - config
      title: Dashboard_Write
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
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

url = "http://localhost:5173/api/v1/private/dashboards"

payload = { "name": "Marketing Analytics Dashboard" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/dashboards';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"Marketing Analytics Dashboard"}'
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

	url := "http://localhost:5173/api/v1/private/dashboards"

	payload := strings.NewReader("{\n  \"name\": \"Marketing Analytics Dashboard\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/dashboards")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Marketing Analytics Dashboard\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/dashboards")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Marketing Analytics Dashboard\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/dashboards', [
  'body' => '{
  "name": "Marketing Analytics Dashboard"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/dashboards");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Marketing Analytics Dashboard\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Marketing Analytics Dashboard"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/dashboards")! as URL,
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