# Source: https://www.comet.com/docs/opik/reference/rest-api/attachments/complete-multi-part-upload.mdx

# Complete multipart attachment upload

POST http://localhost:5173/api/v1/private/attachment/upload-complete
Content-Type: application/json

Complete multipart attachment upload

Reference: https://www.comet.com/docs/opik/reference/rest-api/attachments/complete-multi-part-upload

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/attachment/upload-complete:
    post:
      operationId: complete-multi-part-upload
      summary: Complete multipart attachment upload
      description: Complete multipart attachment upload
      tags:
        - subpackage_attachments
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Attachments_completeMultiPartUpload_Response_204
        '401':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '403':
          description: Access forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CompleteMultipartUploadRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    CompleteMultipartUploadRequestEntityType:
      type: string
      enum:
        - trace
        - span
      title: CompleteMultipartUploadRequestEntityType
    MultipartUploadPart:
      type: object
      properties:
        e_tag:
          type: string
        part_number:
          type: integer
      required:
        - e_tag
        - part_number
      title: MultipartUploadPart
    CompleteMultipartUploadRequest:
      type: object
      properties:
        file_name:
          type: string
        project_name:
          type: string
          description: If null, the default project is used
        entity_type:
          $ref: '#/components/schemas/CompleteMultipartUploadRequestEntityType'
        entity_id:
          type: string
          format: uuid
        container_id:
          type: string
          format: uuid
        file_size:
          type: integer
          format: int64
        mime_type:
          type: string
        upload_id:
          type: string
        uploaded_file_parts:
          type: array
          items:
            $ref: '#/components/schemas/MultipartUploadPart'
      required:
        - file_name
        - entity_type
        - entity_id
        - file_size
        - upload_id
        - uploaded_file_parts
      title: CompleteMultipartUploadRequest
    Attachments_completeMultiPartUpload_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Attachments_completeMultiPartUpload_Response_204
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

url = "http://localhost:5173/api/v1/private/attachment/upload-complete"

payload = {
    "file_name": "experiment_results.csv",
    "entity_type": "trace",
    "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "file_size": 5242880,
    "upload_id": "upload-12345abcde",
    "uploaded_file_parts": [
        {
            "e_tag": "9b2cf535f27731c974343645a3985328",
            "part_number": 1
        },
        {
            "e_tag": "a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890",
            "part_number": 2
        }
    ]
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/attachment/upload-complete';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"file_name":"experiment_results.csv","entity_type":"trace","entity_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","file_size":5242880,"upload_id":"upload-12345abcde","uploaded_file_parts":[{"e_tag":"9b2cf535f27731c974343645a3985328","part_number":1},{"e_tag":"a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890","part_number":2}]}'
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

	url := "http://localhost:5173/api/v1/private/attachment/upload-complete"

	payload := strings.NewReader("{\n  \"file_name\": \"experiment_results.csv\",\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"file_size\": 5242880,\n  \"upload_id\": \"upload-12345abcde\",\n  \"uploaded_file_parts\": [\n    {\n      \"e_tag\": \"9b2cf535f27731c974343645a3985328\",\n      \"part_number\": 1\n    },\n    {\n      \"e_tag\": \"a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890\",\n      \"part_number\": 2\n    }\n  ]\n}")

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

url = URI("http://localhost:5173/api/v1/private/attachment/upload-complete")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"file_name\": \"experiment_results.csv\",\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"file_size\": 5242880,\n  \"upload_id\": \"upload-12345abcde\",\n  \"uploaded_file_parts\": [\n    {\n      \"e_tag\": \"9b2cf535f27731c974343645a3985328\",\n      \"part_number\": 1\n    },\n    {\n      \"e_tag\": \"a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890\",\n      \"part_number\": 2\n    }\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/attachment/upload-complete")
  .header("Content-Type", "application/json")
  .body("{\n  \"file_name\": \"experiment_results.csv\",\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"file_size\": 5242880,\n  \"upload_id\": \"upload-12345abcde\",\n  \"uploaded_file_parts\": [\n    {\n      \"e_tag\": \"9b2cf535f27731c974343645a3985328\",\n      \"part_number\": 1\n    },\n    {\n      \"e_tag\": \"a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890\",\n      \"part_number\": 2\n    }\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/attachment/upload-complete', [
  'body' => '{
  "file_name": "experiment_results.csv",
  "entity_type": "trace",
  "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "file_size": 5242880,
  "upload_id": "upload-12345abcde",
  "uploaded_file_parts": [
    {
      "e_tag": "9b2cf535f27731c974343645a3985328",
      "part_number": 1
    },
    {
      "e_tag": "a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890",
      "part_number": 2
    }
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

var client = new RestClient("http://localhost:5173/api/v1/private/attachment/upload-complete");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"file_name\": \"experiment_results.csv\",\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"file_size\": 5242880,\n  \"upload_id\": \"upload-12345abcde\",\n  \"uploaded_file_parts\": [\n    {\n      \"e_tag\": \"9b2cf535f27731c974343645a3985328\",\n      \"part_number\": 1\n    },\n    {\n      \"e_tag\": \"a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890\",\n      \"part_number\": 2\n    }\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "file_name": "experiment_results.csv",
  "entity_type": "trace",
  "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "file_size": 5242880,
  "upload_id": "upload-12345abcde",
  "uploaded_file_parts": [
    [
      "e_tag": "9b2cf535f27731c974343645a3985328",
      "part_number": 1
    ],
    [
      "e_tag": "a3c1e5f7d8b9c0e1f2a3b4c5d6e7f890",
      "part_number": 2
    ]
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/attachment/upload-complete")! as URL,
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