# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/stream-dataset-items.mdx

# Stream dataset items

POST http://localhost:5173/api/v1/private/datasets/items/stream
Content-Type: application/json

Stream dataset items

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/stream-dataset-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/stream:
    post:
      operationId: stream-dataset-items
      summary: Stream dataset items
      description: Stream dataset items
      tags:
        - subpackage_datasets
      responses:
        '200':
          description: Dataset items stream or error during process
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Datasets_streamDatasetItems_Response_200'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItemStreamRequest'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemStreamRequest:
      type: object
      properties:
        dataset_name:
          type: string
        last_retrieved_id:
          type: string
          format: uuid
        steam_limit:
          type: integer
        dataset_version:
          type: string
        filters:
          type: string
      required:
        - dataset_name
      title: DatasetItemStreamRequest
    Datasets_streamDatasetItems_Response_200:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_streamDatasetItems_Response_200

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/items/stream"

payload = { "dataset_name": "customer_feedback_2024" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/stream';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"dataset_name":"customer_feedback_2024"}'
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

	url := "http://localhost:5173/api/v1/private/datasets/items/stream"

	payload := strings.NewReader("{\n  \"dataset_name\": \"customer_feedback_2024\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/stream")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"dataset_name\": \"customer_feedback_2024\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/items/stream")
  .header("Content-Type", "application/json")
  .body("{\n  \"dataset_name\": \"customer_feedback_2024\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/items/stream', [
  'body' => '{
  "dataset_name": "customer_feedback_2024"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/stream");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"dataset_name\": \"customer_feedback_2024\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["dataset_name": "customer_feedback_2024"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/stream")! as URL,
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