# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/batch-update-experiments.mdx

# Batch update experiments

PATCH http://localhost:5173/api/v1/private/experiments/batch
Content-Type: application/json

Update multiple experiments

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/batch-update-experiments

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments/batch:
    patch:
      operationId: batch-update-experiments
      summary: Batch update experiments
      description: Update multiple experiments
      tags:
        - subpackage_experiments
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Experiments_batchUpdateExperiments_Response_204
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ExperimentBatchUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonNode:
      type: object
      properties: {}
      title: JsonNode
    ExperimentUpdateType:
      type: string
      enum:
        - regular
        - trial
        - mini-batch
      title: ExperimentUpdateType
    ExperimentUpdateStatus:
      type: string
      enum:
        - running
        - completed
        - cancelled
      description: The status of the experiment
      title: ExperimentUpdateStatus
    ExperimentScore:
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
      title: ExperimentScore
    ExperimentUpdate:
      type: object
      properties:
        name:
          type: string
        metadata:
          $ref: '#/components/schemas/JsonNode'
        tags:
          type: array
          items:
            type: string
          description: Tags
        tags_to_add:
          type: array
          items:
            type: string
          description: Tags to add
        tags_to_remove:
          type: array
          items:
            type: string
          description: Tags to remove
        type:
          $ref: '#/components/schemas/ExperimentUpdateType'
        status:
          $ref: '#/components/schemas/ExperimentUpdateStatus'
          description: The status of the experiment
        experiment_scores:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentScore'
      title: ExperimentUpdate
    ExperimentBatchUpdate:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
            format: uuid
          description: List of experiment IDs to update (max 1000)
        update:
          $ref: '#/components/schemas/ExperimentUpdate'
        merge_tags:
          type: boolean
          description: >-
            If true, merge tags with existing tags instead of replacing them.
            Default: false
      required:
        - ids
        - update
      description: Request to batch update multiple experiments
      title: ExperimentBatchUpdate
    Experiments_batchUpdateExperiments_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Experiments_batchUpdateExperiments_Response_204
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

url = "http://localhost:5173/api/v1/private/experiments/batch"

payload = { "ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"] }
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments/batch';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"ids":["3fa85f64-5717-4562-b3fc-2c963f66afa6"]}'
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

	url := "http://localhost:5173/api/v1/private/experiments/batch"

	payload := strings.NewReader("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/experiments/batch")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/experiments/batch")
  .header("Content-Type", "application/json")
  .body("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/experiments/batch', [
  'body' => '{
  "ids": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/experiments/batch");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments/batch")! as URL,
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