# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-spans.mdx

# Create dataset items from spans

POST http://localhost:5173/api/v1/private/datasets/{dataset_id}/items/from-spans
Content-Type: application/json

Create dataset items from spans with enriched metadata

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-spans

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{dataset_id}/items/from-spans:
    post:
      operationId: create-dataset-items-from-spans
      summary: Create dataset items from spans
      description: Create dataset items from spans with enriched metadata
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
                  #/components/schemas/Datasets_createDatasetItemsFromSpans_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateDatasetItemsFromSpansRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    SpanEnrichmentOptions:
      type: object
      properties:
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
      description: Options for enriching span data
      title: SpanEnrichmentOptions
    CreateDatasetItemsFromSpansRequest:
      type: object
      properties:
        span_ids:
          type: array
          items:
            type: string
            format: uuid
          description: Set of span IDs to add to the dataset
        enrichment_options:
          $ref: '#/components/schemas/SpanEnrichmentOptions'
      required:
        - span_ids
        - enrichment_options
      title: CreateDatasetItemsFromSpansRequest
    Datasets_createDatasetItemsFromSpans_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createDatasetItemsFromSpans_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans"

payload = { "span_ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"] }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"span_ids":["3fa85f64-5717-4562-b3fc-2c963f66afa6","7c9e6679-7425-40de-944b-e07fc1f90ae7"]}'
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

	url := "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans"

	payload := strings.NewReader("{\n  \"span_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"span_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans")
  .header("Content-Type", "application/json")
  .body("{\n  \"span_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans', [
  'body' => '{
  "span_ids": [
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

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"span_ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["span_ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/dataset_id/items/from-spans")! as URL,
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