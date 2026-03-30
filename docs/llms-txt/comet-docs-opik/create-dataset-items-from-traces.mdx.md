# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-traces.mdx

# Create dataset items from traces

POST http://localhost:5173/api/v1/private/datasets/{dataset_id}/items/from-traces
Content-Type: application/json

Create dataset items from traces with enriched metadata

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-traces

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{dataset_id}/items/from-traces:
    post:
      operationId: create-dataset-items-from-traces
      summary: Create dataset items from traces
      description: Create dataset items from traces with enriched metadata
      tags:
        - subpackage_datasets
      parameters:
        - name: dataset_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Datasets_createDatasetItemsFromTraces_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDatasetItemsFromTracesRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    TraceEnrichmentOptions:
      type: object
      properties:
        includeSpans:
          type: boolean
        includeTags:
          type: boolean
        includeFeedbackScores:
          type: boolean
        includeComments:
          type: boolean
        includeUsage:
          type: boolean
        includeMetadata:
          type: boolean
      description: Options for enriching trace data
      title: TraceEnrichmentOptions
    CreateDatasetItemsFromTracesRequest:
      type: object
      properties:
        trace_ids:
          type: array
          items:
            type: string
            format: uuid
          description: Set of trace IDs to add to the dataset
        enrichment_options:
          $ref: '#/components/schemas/TraceEnrichmentOptions'
      required:
        - trace_ids
        - enrichment_options
      title: CreateDatasetItemsFromTracesRequest
    Datasets_createDatasetItemsFromTraces_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createDatasetItemsFromTraces_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces"

payload = { "trace_ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"trace_ids":["3fa85f64-5717-4562-b3fc-2c963f66afa6","7c9e6679-7425-40de-944b-e07fc1f90ae7"]}'
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

	url := "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces"

	payload := strings.NewReader("{\n  \"trace_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"trace_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces")
  .header("Content-Type", "application/json")
  .body("{\n  \"trace_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces', [
  'body' => '{
  "trace_ids": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "7c9e6679-7425-40de-944b-e07fc1f90ae7"
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

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"trace_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["trace_ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-traces")! as URL,
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