# Source: https://www.comet.com/docs/opik/reference/rest-api/datasets/delete-dataset-items.mdx

# Delete dataset items

POST http://localhost:5173/api/v1/private/datasets/items/delete
Content-Type: application/json

Delete dataset items using one of two modes:
1. **Delete by IDs**: Provide 'item_ids' to delete specific items by their IDs
2. **Delete by filters**: Provide 'dataset_id' with optional 'filters' to delete items matching criteria

When using filters, an empty 'filters' array will delete all items in the specified dataset.


Reference: https://www.comet.com/docs/opik/reference/rest-api/datasets/delete-dataset-items

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/datasets/items/delete:
    post:
      operationId: delete-dataset-items
      summary: Delete dataset items
      description: >
        Delete dataset items using one of two modes:

        1. **Delete by IDs**: Provide 'item_ids' to delete specific items by
        their IDs

        2. **Delete by filters**: Provide 'dataset_id' with optional 'filters'
        to delete items matching criteria


        When using filters, an empty 'filters' array will delete all items in
        the specified dataset.
      tags:
        - subpackage_datasets
      responses:
        '204':
          description: No content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Datasets_deleteDatasetItems_Response_204'
        '400':
          description: Bad request - invalid parameters or conflicting fields
          content:
            application/json:
              schema:
                description: Any type
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DatasetItemsDelete'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    DatasetItemFilterOperator:
      type: string
      enum:
        - contains
        - not_contains
        - starts_with
        - ends_with
        - '='
        - '!='
        - '>'
        - '>='
        - <
        - <=
        - is_empty
        - is_not_empty
      title: DatasetItemFilterOperator
    DatasetItemFilter:
      type: object
      properties:
        field:
          type: string
        operator:
          $ref: '#/components/schemas/DatasetItemFilterOperator'
        key:
          type: string
        value:
          type: string
      description: >-
        Filters to select dataset items to delete within the specified dataset.
        Must be used with 'dataset_id'. Mutually exclusive with 'item_ids'.
        Empty array means 'delete all items in the dataset'.
      title: DatasetItemFilter
    DatasetItemsDelete:
      type: object
      properties:
        item_ids:
          type: array
          items:
            type: string
            format: uuid
          description: >-
            List of dataset item IDs to delete (max 1000). Use this to delete
            specific items by their IDs. Mutually exclusive with 'dataset_id'
            and 'filters'.
        dataset_id:
          type: string
          format: uuid
          description: >-
            Dataset ID to scope the deletion. Required when using 'filters'.
            Mutually exclusive with 'item_ids'.
        filters:
          type: array
          items:
            $ref: '#/components/schemas/DatasetItemFilter'
          description: >-
            Filters to select dataset items to delete within the specified
            dataset. Must be used with 'dataset_id'. Mutually exclusive with
            'item_ids'. Empty array means 'delete all items in the dataset'.
        batch_group_id:
          type: string
          format: uuid
          description: >-
            Optional batch group ID to group multiple delete operations into a
            single dataset version. If null, mutates the latest version instead
            of creating a new one.
      description: Request to delete multiple dataset items
      title: DatasetItemsDelete
    Datasets_deleteDatasetItems_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Datasets_deleteDatasetItems_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/datasets/items/delete"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/datasets/items/delete';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/datasets/items/delete"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/datasets/items/delete")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/datasets/items/delete")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/datasets/items/delete', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/datasets/items/delete");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/datasets/items/delete")! as URL,
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