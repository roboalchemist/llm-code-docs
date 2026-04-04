# Source: https://www.comet.com/docs/opik/reference/rest-api/attachments/upload-attachment.mdx

# Upload attachment to MinIO

PUT http://localhost:5173/api/v1/private/attachment/upload

Upload attachment to MinIO

Reference: https://www.comet.com/docs/opik/reference/rest-api/attachments/upload-attachment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/attachment/upload:
    put:
      operationId: upload-attachment
      summary: Upload attachment to MinIO
      description: Upload attachment to MinIO
      tags:
        - subpackage_attachments
      parameters:
        - name: file_name
          in: query
          required: true
          schema:
            type: string
        - name: project_name
          in: query
          required: false
          schema:
            type: string
        - name: mime_type
          in: query
          required: false
          schema:
            type: string
        - name: entity_type
          in: query
          required: true
          schema:
            $ref: >-
              #/components/schemas/V1PrivateAttachmentUploadPutParametersEntityType
        - name: entity_id
          in: query
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
                $ref: '#/components/schemas/Attachments_uploadAttachment_Response_204'
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
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    V1PrivateAttachmentUploadPutParametersEntityType:
      type: string
      enum:
        - trace
        - span
      title: V1PrivateAttachmentUploadPutParametersEntityType
    Attachments_uploadAttachment_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Attachments_uploadAttachment_Response_204
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

url = "http://localhost:5173/api/v1/private/attachment/upload"

querystring = {"file_name":"file_name","entity_type":"trace","entity_id":"entity_id"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id';
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

	url := "http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id"

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

url = URI("http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id")

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

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/attachment/upload?file_name=file_name&entity_type=trace&entity_id=entity_id")! as URL,
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