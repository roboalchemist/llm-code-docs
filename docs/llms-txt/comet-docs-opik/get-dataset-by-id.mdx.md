# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-by-id.mdx

# Get dataset by id

GET http://localhost:5173/api/v1/private/datasets/{id}

Get dataset by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-by-id

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}:
    get:
      operationId: get-dataset-by-id
      summary: Get dataset by id
      description: Get dataset by id
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: Dataset resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dataset_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetPublicType:
      type: string
      enum:
        - dataset
        - evaluation_suite
      title: DatasetPublicType
    DatasetPublicVisibility:
      type: string
      enum:
        - private
        - public
      title: DatasetPublicVisibility
    DatasetPublicStatus:
      type: string
      enum:
        - unknown
        - processing
        - completed
        - failed
      title: DatasetPublicStatus
    DatasetVersionSummary_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier of the version
        version_hash:
          type: string
          description: Hash of the version content
        version_name:
          type: string
          description: Sequential version name formatted as 'v1', 'v2', etc.
        change_description:
          type: string
          description: Description of changes in this version
        tags:
          type: array
          items:
            type: string
          description: Tags associated with this version
      description: Summary of the latest dataset version
      title: DatasetVersionSummary_Public
    Dataset_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/DatasetPublicType'
        visibility:
          $ref: '#/components/schemas/DatasetPublicVisibility'
        tags:
          type: array
          items:
            type: string
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
        experiment_count:
          type: integer
          format: int64
        dataset_items_count:
          type: integer
          format: int64
        optimization_count:
          type: integer
          format: int64
        most_recent_experiment_at:
          type: string
          format: date-time
        last_created_experiment_at:
          type: string
          format: date-time
        most_recent_optimization_at:
          type: string
          format: date-time
        last_created_optimization_at:
          type: string
          format: date-time
        status:
          $ref: '#/components/schemas/DatasetPublicStatus'
        latest_version:
          $ref: '#/components/schemas/DatasetVersionSummary_Public'
      required:
        - name
      title: Dataset_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/id"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id';
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

	url := "http://localhost:5173/api/v1/private/datasets/id"

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

url = URI("http://localhost:5173/api/v1/private/datasets/id")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/datasets/id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/datasets/id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id")! as URL,
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