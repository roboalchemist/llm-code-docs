# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/update-dataset.mdx

# Update dataset by id

PUT http://localhost:5173/api/v1/private/datasets/{id}
Content-Type: application/json

Update dataset by id

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/update-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/{id}:
    put:
      operationId: update-dataset
      summary: Update dataset by id
      description: Update dataset by id
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
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
                $ref: '#/components/schemas/Datasets_updateDataset_Response_204'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetUpdateVisibility:
      type: string
      enum:
        - private
        - public
      title: DatasetUpdateVisibility
    DatasetUpdate:
      type: object
      properties:
        name:
          type: string
        description:
          type: string
        visibility:
          $ref: '#/components/schemas/DatasetUpdateVisibility'
        tags:
          type: array
          items:
            type: string
      required:
        - name
      title: DatasetUpdate
    Datasets_updateDataset_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_updateDataset_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/id"

payload = { "name": "Customer Purchase Data Q2 2024" }
headers = {"Content-Type": "application/json"}

response = requests.put(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/id';
const options = {
  method: 'PUT',
  headers: {'Content-Type': 'application/json'},
  body: '{"name":"Customer Purchase Data Q2 2024"}'
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

	url := "http://localhost:5173/api/v1/private/datasets/id"

	payload := strings.NewReader("{\n  \"name\": \"Customer Purchase Data Q2 2024\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/id")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Put.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Customer Purchase Data Q2 2024\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.put("http://localhost:5173/api/v1/private/datasets/id")
  .header("Content-Type", "application/json")
  .body("{\n  \"name\": \"Customer Purchase Data Q2 2024\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PUT', 'http://localhost:5173/api/v1/private/datasets/id', [
  'body' => '{
  "name": "Customer Purchase Data Q2 2024"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/id");
var request = new RestRequest(Method.PUT);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Customer Purchase Data Q2 2024\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["name": "Customer Purchase Data Q2 2024"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/id")! as URL,
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