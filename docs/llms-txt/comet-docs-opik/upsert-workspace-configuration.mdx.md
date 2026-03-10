# Source: https://www.comet.com/docs/opik/reference/rest-api/workspaces/upsert-workspace-configuration.mdx

# Upsert workspace configuration

PUT http://localhost:5173/api/v1/private/workspaces/configurations
Content-Type: application/json

Upsert workspace configuration

Reference: https://www.comet.com/docs/opik/reference/rest-api/workspaces/upsert-workspace-configuration

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/workspaces/configurations:
    put:
      operationId: upsert-workspace-configuration
      summary: Upsert workspace configuration
      description: Upsert workspace configuration
      tags:
        - subpackage_workspaces
      responses:
        '200':
          description: Configuration Updated
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkspaceConfiguration'
        '400':
          description: Bad Request
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
              $ref: '#/components/schemas/WorkspaceConfiguration'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    WorkspaceConfiguration:
      type: object
      properties:
        timeout_to_mark_thread_as_inactive:
          type: string
          description: >-
            Duration in ISO-8601 format (e.g., PT30M for 30 minutes, PT2H for 2
            hours, P1D for 1 day). Minimum precision supported is seconds,
            please use a duration with seconds precision or higher. Also, the
            max duration allowed is 7 days.
        truncation_on_tables:
          type: boolean
          description: >-
            Enable or disable data truncation in table views. When disabled, the
            frontend will limit pagination to prevent performance issues.
            Default: true (truncation enabled).
        color_map:
          type: object
          additionalProperties:
            type: string
          description: >-
            Workspace-level color map. Maps label names to hex color values
            (e.g. #FF0000). Max 10000 entries.
      title: WorkspaceConfiguration
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

url = "http://localhost:5173/api/v1/private/workspaces/configurations"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/workspaces/configurations';
const options = {method: 'PUT', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/workspaces/configurations"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/workspaces/configurations")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/workspaces/configurations")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/workspaces/configurations', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/workspaces/configurations");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/workspaces/configurations")! as URL,
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