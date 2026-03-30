# Source: https://www.comet.com/docs/opik/reference/rest-api/attachments/download-attachment.mdx

# Download attachment from MinIO

GET http://localhost:5173/api/v1/private/attachment/download

Download attachment from MinIO

Reference: https://www.comet.com/docs/opik/reference/rest-api/attachments/download-attachment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/attachment/download:
    get:
      operationId: download-attachment
      summary: Download attachment from MinIO
      description: Download attachment from MinIO
      tags:
        - subpackage_attachments
      parameters:
        - name: workspace_name
          in: query
          required: false
          schema:
            type: string
        - name: container_id
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
              #/components/schemas/V1PrivateAttachmentDownloadGetParametersEntityType
        - name: entity_id
          in: query
          required: true
          schema:
            type: string
            format: uuid
        - name: file_name
          in: query
          required: true
          schema:
            type: string
        - name: mime_type
          in: query
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Attachment Resource
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    V1PrivateAttachmentDownloadGetParametersEntityType:
      type: string
      enum:
        - trace
        - span
      title: V1PrivateAttachmentDownloadGetParametersEntityType

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/attachment/download"

querystring = {"container_id":"container_id","entity_type":"trace","entity_id":"entity_id","file_name":"file_name","mime_type":"mime_type"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/attachment/download?container_id=container_id&entity_type=trace&entity_id=entity_id&file_name=file_name&mime_type=mime_type")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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