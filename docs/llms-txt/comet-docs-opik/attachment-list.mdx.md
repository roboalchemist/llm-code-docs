# Source: https://www.comet.com/docs/opik/reference/rest-api/attachments/attachment-list.mdx

# Attachments list for entity

GET http://localhost:5173/api/v1/private/attachment/list

Attachments list for entity

Reference: https://www.comet.com/docs/opik/reference/rest-api/attachments/attachment-list

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/attachment/list:
    get:
      operationId: attachment-list
      summary: Attachments list for entity
      description: Attachments list for entity
      tags:
        - subpackage_attachments
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
            default: 100
        - name: project_id
          in: query
          required: true
          schema:
            type: string
            format: uuid
        - name: entity_type
          in: query
          required: true
          schema:
            $ref: >-
              #/components/schemas/V1PrivateAttachmentListGetParametersEntityType
        - name: entity_id
          in: query
          required: true
          schema:
            type: string
            format: uuid
        - name: path
          in: query
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Attachment Resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AttachmentPage'
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
    V1PrivateAttachmentListGetParametersEntityType:
      type: string
      enum:
        - trace
        - span
      title: V1PrivateAttachmentListGetParametersEntityType
    Attachment:
      type: object
      properties:
        link:
          type: string
        file_name:
          type: string
        file_size:
          type: integer
          format: int64
        mime_type:
          type: string
      required:
        - file_name
        - file_size
        - mime_type
      title: Attachment
    AttachmentPage:
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
            $ref: '#/components/schemas/Attachment'
        sortableBy:
          type: array
          items:
            type: string
      title: AttachmentPage
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

url = "http://localhost:5173/api/v1/private/attachment/list"

querystring = {"project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","entity_type":"trace","entity_id":"7c9e6679-7425-40de-944b-e07fc1f90ae7","path":"/logs/error","page":"1","size":"50"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50';
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

	url := "http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50"

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

url = URI("http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/attachment/list?project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&entity_type=trace&entity_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&path=%2Flogs%2Ferror&page=1&size=50")! as URL,
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