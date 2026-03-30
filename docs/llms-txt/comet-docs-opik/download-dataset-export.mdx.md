# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/download-dataset-export.mdx

# Download dataset export file

GET http://localhost:5173/api/v1/private/datasets/export-jobs/{jobId}/download

Downloads the exported CSV file for a completed export job. This endpoint proxies the file download to avoid exposing internal storage URLs.

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/download-dataset-export

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/export-jobs/{jobId}/download:
    get:
      operationId: download-dataset-export
      summary: Download dataset export file
      description: >-
        Downloads the exported CSV file for a completed export job. This
        endpoint proxies the file download to avoid exposing internal storage
        URLs.
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
        '200':
          description: CSV file content
          content:
            application/octet-stream:
              schema:
                type: string
                format: binary
        '400':
          description: Export job is not ready for download
          content:
            application/json:
              schema:
                description: Any type
        '404':
          description: Export job not found
          content:
            application/json:
              schema:
                description: Any type
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download"

response = requests.get(url)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download';
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

	url := "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download"

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

url = URI("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/export-jobs/jobId/download")! as URL,
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