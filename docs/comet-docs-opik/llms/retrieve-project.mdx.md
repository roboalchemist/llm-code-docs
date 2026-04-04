# Source: https://www.comet.com/docs/opik/reference/rest-api/projects/retrieve-project.mdx

# Retrieve project

POST http://localhost:5173/api/v1/private/projects/retrieve
Content-Type: application/json

Retrieve project

Reference: https://www.comet.com/docs/opik/reference/rest-api/projects/retrieve-project

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/projects/retrieve:
    post:
      operationId: retrieve-project
      summary: Retrieve project
      description: Retrieve project
      tags:
        - subpackage_projects
      responses:
        '200':
          description: Project resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Project_Detailed'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Detailed'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Detailed'
        '422':
          description: Unprocessable Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Detailed'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ProjectRetrieve_Detailed'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ProjectRetrieve_Detailed:
      type: object
      properties:
        name:
          type: string
      required:
        - name
      title: ProjectRetrieve_Detailed
    ProjectDetailedVisibility:
      type: string
      enum:
        - private
        - public
      title: ProjectDetailedVisibility
    FeedbackScoreAverage_Detailed:
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
      title: FeedbackScoreAverage_Detailed
    PercentageValues_Detailed:
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
      title: PercentageValues_Detailed
    ErrorCountWithDeviation_Detailed:
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
      title: ErrorCountWithDeviation_Detailed
    Project_Detailed:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        visibility:
          $ref: '#/components/schemas/ProjectDetailedVisibility'
        description:
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
        last_updated_trace_at:
          type: string
          format: date-time
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage_Detailed'
        duration:
          $ref: '#/components/schemas/PercentageValues_Detailed'
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
          $ref: '#/components/schemas/ErrorCountWithDeviation_Detailed'
      required:
        - name
      title: Project_Detailed
    ErrorMessage_Detailed:
      type: object
      properties:
        errors:
          type: array
          items:
            type: string
      title: ErrorMessage_Detailed

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/projects/retrieve"

payload = { "name": "AlphaProject" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/projects/retrieve';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"AlphaProject"}'
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

	url := "http://localhost:5173/api/v1/private/projects/retrieve"

	payload := strings.NewReader("{\n  \"name\": \"AlphaProject\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/projects/retrieve")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"AlphaProject\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/projects/retrieve")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"AlphaProject\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/projects/retrieve', [
  'body' => '{
  "name": "AlphaProject"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/projects/retrieve");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"AlphaProject\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "AlphaProject"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/projects/retrieve")! as URL,
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