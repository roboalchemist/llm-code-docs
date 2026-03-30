# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-csv.mdx

# Create dataset items from CSV file

POST http://localhost:5173/api/v1/private/datasets/items/from-csv
Content-Type: multipart/form-data

Create dataset items from uploaded CSV file. CSV should have headers in the first row. Processing happens asynchronously in batches.

Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/create-dataset-items-from-csv

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/from-csv:
    post:
      operationId: create-dataset-items-from-csv
      summary: Create dataset items from CSV file
      description: >-
        Create dataset items from uploaded CSV file. CSV should have headers in
        the first row. Processing happens asynchronously in batches.
      tags:
        - subpackage_datasets
      responses:
        '202':
          description: Accepted - CSV processing started
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Datasets_createDatasetItemsFromCsv_Response_202
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
        '404':
          description: Not Found - CSV upload feature is disabled
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                file:
                  $ref: >-
                    #/components/schemas/V1PrivateDatasetsItemsFromCsvPostRequestBodyContentMultipartFormDataSchemaFile
                dataset_id:
                  type: string
                  format: uuid
              required:
                - file
                - dataset_id
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    V1PrivateDatasetsItemsFromCsvPostRequestBodyContentMultipartFormDataSchemaFile:
      type: object
      properties: {}
      title: >-
        V1PrivateDatasetsItemsFromCsvPostRequestBodyContentMultipartFormDataSchemaFile
    Datasets_createDatasetItemsFromCsv_Response_202:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_createDatasetItemsFromCsv_Response_202
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

url = "http://localhost:5173/api/v1/private/datasets/items/from-csv"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dataset_id\"\r\n\r\n3fa85f64-5717-4562-b3fc-2c963f66afa6\r\n-----011000010111000001101001--\r\n"
headers = {"Content-Type": "multipart/form-data; boundary=---011000010111000001101001"}

response = requests.post(url, data=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/from-csv';
const form = new FormData();
form.append('file', '{}');
form.append('dataset_id', '3fa85f64-5717-4562-b3fc-2c963f66afa6');

const options = {method: 'POST'};

options.body = form;

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

	url := "http://localhost:5173/api/v1/private/datasets/items/from-csv"

	payload := strings.NewReader("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dataset_id\"\r\n\r\n3fa85f64-5717-4562-b3fc-2c963f66afa6\r\n-----011000010111000001101001--\r\n")

	req, _ := http.NewRequest("POST", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/from-csv")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dataset_id\"\r\n\r\n3fa85f64-5717-4562-b3fc-2c963f66afa6\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/items/from-csv")
  .body("-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dataset_id\"\r\n\r\n3fa85f64-5717-4562-b3fc-2c963f66afa6\r\n-----011000010111000001101001--\r\n")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/items/from-csv', [
  'multipart' => [
    [
        'name' => 'file',
        'contents' => '{}'
    ],
    [
        'name' => 'dataset_id',
        'contents' => '3fa85f64-5717-4562-b3fc-2c963f66afa6'
    ]
  ]
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/from-csv");
var request = new RestRequest(Method.POST);
request.AddParameter("undefined", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"file\"\r\n\r\n{}\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"dataset_id\"\r\n\r\n3fa85f64-5717-4562-b3fc-2c963f66afa6\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation
let parameters = [
  [
    "name": "file",
    "value": "{}"
  ],
  [
    "name": "dataset_id",
    "value": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/from-csv")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
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