# Source: https://www.comet.com/docs/opik/reference/rest-api/annotation-queues/find-annotation-queues.mdx

# Find annotation queues

GET http://localhost:5173/api/v1/private/annotation-queues

Find annotation queues with filtering and sorting

Reference: https://www.comet.com/docs/opik/reference/rest-api/annotation-queues/find-annotation-queues

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/annotation-queues:
    get:
      operationId: find-annotation-queues
      summary: Find annotation queues
      description: Find annotation queues with filtering and sorting
      tags:
        - subpackage_annotationQueues
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
        - name: filters
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
          description: Annotation queues page
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationQueuePage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AnnotationQueuePublicScope:
      type: string
      enum:
        - trace
        - thread
      title: AnnotationQueuePublicScope
    AnnotationQueueReviewer_Public:
      type: object
      properties:
        username:
          type: string
        status:
          type: integer
          format: int64
      title: AnnotationQueueReviewer_Public
    FeedbackScoreAverage_Public:
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
      title: FeedbackScoreAverage_Public
    AnnotationQueue_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        project_name:
          type: string
        name:
          type: string
        description:
          type: string
        instructions:
          type: string
        scope:
          $ref: '#/components/schemas/AnnotationQueuePublicScope'
        comments_enabled:
          type: boolean
        feedback_definition_names:
          type: array
          items:
            type: string
        reviewers:
          type: array
          items:
            $ref: '#/components/schemas/AnnotationQueueReviewer_Public'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage_Public'
        items_count:
          type: integer
          format: int64
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
      required:
        - project_id
        - name
        - scope
      title: AnnotationQueue_Public
    AnnotationQueuePage_Public:
      type: object
      properties:
        page:
          type: integer
        size:
          type: integer
        total:
          type: integer
          format: int64
        content:
          type: array
          items:
            $ref: '#/components/schemas/AnnotationQueue_Public'
        sortableBy:
          type: array
          items:
            type: string
      title: AnnotationQueuePage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/annotation-queues"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/annotation-queues';
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

	url := "http://localhost:5173/api/v1/private/annotation-queues"

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

url = URI("http://localhost:5173/api/v1/private/annotation-queues")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/annotation-queues")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/annotation-queues', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/annotation-queues");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/annotation-queues")! as URL,
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