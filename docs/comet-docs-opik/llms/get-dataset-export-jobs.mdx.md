# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-export-jobs.mdx

# Get all dataset export jobs

GET http://localhost:5173/api/v1/private/datasets/export-jobs

Retrieves all export jobs for the workspace. This is used to restore the export panel state after page refresh.

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/get-dataset-export-jobs

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/export-jobs:
    get:
      operationId: get-dataset-export-jobs
      summary: Get all dataset export jobs
      description: >-
        Retrieves all export jobs for the workspace. This is used to restore the
        export panel state after page refresh.
      tags:
        - subpackage_datasets
      responses:
        '200':
          description: List of export jobs
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/DatasetExportJob_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetExportJobPublicStatus:
      type: string
      enum:
        - PENDING
        - PROCESSING
        - COMPLETED
        - FAILED
      title: DatasetExportJobPublicStatus
    DatasetExportJob_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        dataset_id:
          type: string
          format: uuid
        dataset_name:
          type: string
        status:
          $ref: '#/components/schemas/DatasetExportJobPublicStatus'
        file_path:
          type: string
        error_message:
          type: string
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
        expires_at:
          type: string
          format: date-time
        viewed_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
      title: DatasetExportJob_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/export-jobs"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/export-jobs';
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

	url := "http://localhost:5173/api/v1/private/datasets/export-jobs"

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

url = URI("http://localhost:5173/api/v1/private/datasets/export-jobs")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/datasets/export-jobs")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/datasets/export-jobs', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/export-jobs");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/export-jobs")! as URL,
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