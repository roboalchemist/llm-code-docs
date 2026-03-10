# Source: https://www.comet.com/docs/opik/reference/rest-api/projects/get-project-stats.mdx

# Get Project Stats

GET http://localhost:5173/api/v1/private/projects/stats

Get Project Stats

Reference: https://www.comet.com/docs/opik/reference/rest-api/projects/get-project-stats

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/projects/stats:
    get:
      operationId: get-project-stats
      summary: Get Project Stats
      description: Get Project Stats
      tags:
        - subpackage_projects
      parameters:
        - name: page
          in: query
          required: false
          schema:
            type: integer
            default: 1
        - name: size
          in: query
          required: false
          schema:
            type: integer
            default: 10
        - name: name
          in: query
          required: false
          schema:
            type: string
        - name: sorting
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Project Stats
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectStatsSummary'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    FeedbackScoreAverage:
      type: object
      properties:
        name:
          type: string
        value:
          type: number
          format: double
      required:
        - name
        - value
      title: FeedbackScoreAverage
    PercentageValues:
      type: object
      properties:
        p50:
          type: number
          format: double
        p90:
          type: number
          format: double
        p99:
          type: number
          format: double
      title: PercentageValues
    ErrorCountWithDeviation:
      type: object
      properties:
        count:
          type: integer
          format: int64
        deviation:
          type: integer
          format: int64
        deviation_percentage:
          type: integer
          format: int64
      title: ErrorCountWithDeviation
    ProjectStatsSummaryItem:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage'
        duration:
          $ref: '#/components/schemas/PercentageValues'
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_sum:
          type: number
          format: double
        usage:
          type: object
          additionalProperties:
            type: number
            format: double
        trace_count:
          type: integer
          format: int64
        thread_count:
          type: integer
          format: int64
        guardrails_failed_count:
          type: integer
          format: int64
        error_count:
          $ref: '#/components/schemas/ErrorCountWithDeviation'
      title: ProjectStatsSummaryItem
    ProjectStatsSummary:
      type: object
      properties:
        content:
          type: array
          items:
            $ref: '#/components/schemas/ProjectStatsSummaryItem'
      title: ProjectStatsSummary

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/projects/stats"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/projects/stats';
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

	url := "http://localhost:5173/api/v1/private/projects/stats"

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

url = URI("http://localhost:5173/api/v1/private/projects/stats")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/projects/stats")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/projects/stats', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/projects/stats");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/projects/stats")! as URL,
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