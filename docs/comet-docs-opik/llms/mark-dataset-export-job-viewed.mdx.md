# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/mark-dataset-export-job-viewed.mdx

# Mark dataset export job as viewed

PUT http://localhost:5173/api/v1/private/datasets/export-jobs/{jobId}/mark-viewed

Marks a dataset export job as viewed by setting the viewed_at timestamp. This is used to track that a user has seen a failed job's error message. This operation is idempotent.

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/mark-dataset-export-job-viewed

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/export-jobs/{jobId}/mark-viewed:
    put:
      operationId: mark-dataset-export-job-viewed
      summary: Mark dataset export job as viewed
      description: >-
        Marks a dataset export job as viewed by setting the viewed_at timestamp.
        This is used to track that a user has seen a failed job's error message.
        This operation is idempotent.
      tags:
        - subpackage_datasets
      parameters:
        - name: jobId
          in: path
          required: true
          schema:
            type: string
            format: uuid
      responses:
        '204':
          description: Job marked as viewed
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Datasets_markDatasetExportJobViewed_Response_204
        '404':
          description: Export job not found
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    Datasets_markDatasetExportJobViewed_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_markDatasetExportJobViewed_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed';
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

	url := "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed"

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

url = URI("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed")

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

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/mark-viewed")! as URL,
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