# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/apply-dataset-item-changes.mdx

# Apply changes to dataset items

POST http://localhost:5173/api/v1/private/datasets/{id}/items/changes
Content-Type: application/json

Apply delta changes (add, edit, delete) to a dataset version with conflict detection.

This endpoint:
- Creates a new version with the applied changes
- Validates that baseVersion matches the latest version (unless override=true)
- Returns 409 Conflict if baseVersion is stale and override is not set

Use `override=true` query parameter to force version creation even with stale baseVersion.


Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/apply-dataset-item-changes

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}/items/changes:
    post:
      operationId: apply-dataset-item-changes
      summary: Apply changes to dataset items
      description: >
        Apply delta changes (add, edit, delete) to a dataset version with
        conflict detection.


        This endpoint:

        - Creates a new version with the applied changes

        - Validates that baseVersion matches the latest version (unless
        override=true)

        - Returns 409 Conflict if baseVersion is stale and override is not set


        Use `override=true` query parameter to force version creation even with
        stale baseVersion.
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
        - name: override
          in: query
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '201':
          description: Version created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DatasetVersion_Public'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
        '404':
          description: Dataset or version not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
        '409':
          description: Version conflict - baseVersion is not the latest
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItemChanges_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemChanges_Public:
      type: object
      properties: {}
      title: DatasetItemChanges_Public
    EvaluatorItemPublicType:
      type: string
      enum:
        - llm_judge
        - code_metric
      title: EvaluatorItemPublicType
    JsonNode_Public:
      type: object
      properties: {}
      title: JsonNode_Public
    EvaluatorItem_Public:
      type: object
      properties:
        name:
          type: string
        type:
          $ref: '#/components/schemas/EvaluatorItemPublicType'
        config:
          $ref: '#/components/schemas/JsonNode_Public'
      required:
        - name
        - type
        - config
      description: Default evaluators for items in this version
      title: EvaluatorItem_Public
    ExecutionPolicy_Public:
      type: object
      properties:
        runs_per_item:
          type: integer
        pass_threshold:
          type: integer
      description: Default execution policy for items in this version
      title: ExecutionPolicy_Public
    DatasetVersion_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        dataset_id:
          type: string
          format: uuid
        version_hash:
          type: string
        tags:
          type: array
          items:
            type: string
        is_latest:
          type: boolean
          description: Indicates whether this is the latest version of the dataset
        version_name:
          type: string
          description: Sequential version name formatted as 'v1', 'v2', etc.
        items_total:
          type: integer
          description: Total number of items in this version
        items_added:
          type: integer
          description: Number of items added since last version
        items_modified:
          type: integer
          description: Number of items modified since last version
        items_deleted:
          type: integer
          description: Number of items deleted since last version
        change_description:
          type: string
        metadata:
          type: object
          additionalProperties:
            type: string
        evaluators:
          type: array
          items:
            $ref: '#/components/schemas/EvaluatorItem_Public'
          description: Default evaluators for items in this version
        execution_policy:
          $ref: '#/components/schemas/ExecutionPolicy_Public'
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
      title: DatasetVersion_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/id/items/changes"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id/items/changes';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/datasets/id/items/changes"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/id/items/changes")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/id/items/changes")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/id/items/changes', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id/items/changes");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id/items/changes")! as URL,
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