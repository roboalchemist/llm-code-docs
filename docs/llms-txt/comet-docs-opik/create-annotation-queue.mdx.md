# Source: https://www.comet.com/docs/opik/reference/rest-api/annotation-queues/create-annotation-queue.mdx

# Create annotation queue

POST http://localhost:5173/api/v1/private/annotation-queues
Content-Type: application/json

Create annotation queue for human annotation workflows

Reference: https://www.comet.com/docs/opik/reference/rest-api/annotation-queues/create-annotation-queue

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/annotation-queues:
    post:
      operationId: create-annotation-queue
      summary: Create annotation queue
      description: Create annotation queue for human annotation workflows
      tags:
        - subpackage_annotationQueues
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Annotation
                  Queues_createAnnotationQueue_Response_201
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '422':
          description: Unprocessable Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AnnotationQueue_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    AnnotationQueueWriteScope:
      type: string
      enum:
        - trace
        - thread
      title: AnnotationQueueWriteScope
    AnnotationQueue_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        name:
          type: string
        description:
          type: string
        instructions:
          type: string
        scope:
          $ref: '#/components/schemas/AnnotationQueueWriteScope'
        comments_enabled:
          type: boolean
        feedback_definition_names:
          type: array
          items:
            type: string
      required:
        - project_id
        - name
        - scope
      description: List of annotation queues to create
      title: AnnotationQueue_Write
    Annotation Queues_createAnnotationQueue_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Annotation Queues_createAnnotationQueue_Response_201
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

url = "http://localhost:5173/api/v1/private/annotation-queues"

payload = {
    "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "name": "Image Labeling Queue",
    "scope": "trace"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/annotation-queues';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","name":"Image Labeling Queue","scope":"trace"}'
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

	url := "http://localhost:5173/api/v1/private/annotation-queues"

	payload := strings.NewReader("{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"name\": \"Image Labeling Queue\",\n  \"scope\": \"trace\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/annotation-queues")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"name\": \"Image Labeling Queue\",\n  \"scope\": \"trace\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/annotation-queues")
  .header("Content-Type", "application/json")
  .body("{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"name\": \"Image Labeling Queue\",\n  \"scope\": \"trace\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/annotation-queues', [
  'body' => '{
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "Image Labeling Queue",
  "scope": "trace"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/annotation-queues");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"project_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"name\": \"Image Labeling Queue\",\n  \"scope\": \"trace\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "project_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "name": "Image Labeling Queue",
  "scope": "trace"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/annotation-queues")! as URL,
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