# Source: https://www.comet.com/docs/opik/reference/rest-api/attachments/start-multi-part-upload.mdx

# Start multipart attachment upload

POST http://localhost:5173/api/v1/private/attachment/upload-start
Content-Type: application/json

Start multipart attachment upload

Reference: https://www.comet.com/docs/opik/reference/rest-api/attachments/start-multi-part-upload

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/attachment/upload-start:
    post:
      operationId: start-multi-part-upload
      summary: Start multipart attachment upload
      description: Start multipart attachment upload
      tags:
        - subpackage_attachments
      responses:
        '200':
          description: MultipartUploadResponse
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StartMultipartUploadResponse'
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
              $ref: '#/components/schemas/StartMultipartUploadRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    StartMultipartUploadRequestEntityType:
      type: string
      enum:
        - trace
        - span
      title: StartMultipartUploadRequestEntityType
    StartMultipartUploadRequest:
      type: object
      properties:
        file_name:
          type: string
        num_of_file_parts:
          type: integer
        mime_type:
          type: string
        project_name:
          type: string
          description: If null, the default project is used
        entity_type:
          $ref: '#/components/schemas/StartMultipartUploadRequestEntityType'
        entity_id:
          type: string
          format: uuid
        container_id:
          type: string
          format: uuid
        path:
          type: string
      required:
        - file_name
        - num_of_file_parts
        - entity_type
        - entity_id
        - path
      title: StartMultipartUploadRequest
    StartMultipartUploadResponse:
      type: object
      properties:
        upload_id:
          type: string
        pre_sign_urls:
          type: array
          items:
            type: string
      required:
        - upload_id
        - pre_sign_urls
      title: StartMultipartUploadResponse
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

url = "http://localhost:5173/api/v1/private/attachment/upload-start"

payload = {
    "file_name": "experiment_results.csv",
    "num_of_file_parts": 5,
    "entity_type": "trace",
    "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "path": "/uploads/2024/06/experiment_results.csv"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/attachment/upload-start';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"file_name":"experiment_results.csv","num_of_file_parts":5,"entity_type":"trace","entity_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","path":"/uploads/2024/06/experiment_results.csv"}'
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

	url := "http://localhost:5173/api/v1/private/attachment/upload-start"

	payload := strings.NewReader("{\n  \"file_name\": \"experiment_results.csv\",\n  \"num_of_file_parts\": 5,\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"path\": \"/uploads/2024/06/experiment_results.csv\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/attachment/upload-start")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"file_name\": \"experiment_results.csv\",\n  \"num_of_file_parts\": 5,\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"path\": \"/uploads/2024/06/experiment_results.csv\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/attachment/upload-start")
  .header("Content-Type", "application/json")
  .body("{\n  \"file_name\": \"experiment_results.csv\",\n  \"num_of_file_parts\": 5,\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"path\": \"/uploads/2024/06/experiment_results.csv\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/attachment/upload-start', [
  'body' => '{
  "file_name": "experiment_results.csv",
  "num_of_file_parts": 5,
  "entity_type": "trace",
  "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "path": "/uploads/2024/06/experiment_results.csv"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/attachment/upload-start");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"file_name\": \"experiment_results.csv\",\n  \"num_of_file_parts\": 5,\n  \"entity_type\": \"trace\",\n  \"entity_id\": \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n  \"path\": \"/uploads/2024/06/experiment_results.csv\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "file_name": "experiment_results.csv",
  "num_of_file_parts": 5,
  "entity_type": "trace",
  "entity_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "path": "/uploads/2024/06/experiment_results.csv"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/attachment/upload-start")! as URL,
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