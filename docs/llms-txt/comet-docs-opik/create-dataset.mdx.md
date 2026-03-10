# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset.mdx

# Create dataset

POST http://localhost:5173/api/v1/private/datasets
Content-Type: application/json

Create dataset

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets:
    post:
      operationId: create-dataset
      summary: Create dataset
      description: Create dataset
      tags:
        - subpackage_datasets
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Datasets_createDataset_Response_201'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Dataset_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetWriteType:
      type: string
      enum:
        - dataset
        - evaluation_suite
      title: DatasetWriteType
    DatasetWriteVisibility:
      type: string
      enum:
        - private
        - public
      title: DatasetWriteVisibility
    Dataset_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/DatasetWriteType'
        visibility:
          $ref: '#/components/schemas/DatasetWriteVisibility'
        tags:
          type: array
          items:
            type: string
        description:
          type: string
      required:
        - name
      title: Dataset_Write
    Datasets_createDataset_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createDataset_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets"

payload = { "name": "ImageNet 2024 Dataset" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"ImageNet 2024 Dataset"}'
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

	url := "http://localhost:5173/api/v1/private/datasets"

	payload := strings.NewReader("{\n  \"name\": \"ImageNet 2024 Dataset\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"ImageNet 2024 Dataset\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"ImageNet 2024 Dataset\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets', [
  'body' => '{
  "name": "ImageNet 2024 Dataset"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"ImageNet 2024 Dataset\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "ImageNet 2024 Dataset"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets")! as URL,
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