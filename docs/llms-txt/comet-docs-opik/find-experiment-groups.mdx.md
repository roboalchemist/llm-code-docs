# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiment-groups.mdx

# Find experiment groups

GET http://localhost:5173/api/v1/private/experiments/groups

Find experiments grouped by specified fields

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiment-groups

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments/groups:
    get:
      operationId: find-experiment-groups
      summary: Find experiment groups
      description: Find experiments grouped by specified fields
      tags:
        - subpackage_experiments
      parameters:
        - name: groups
          in: query
          required: false
          schema:
            type: string
        - name: types
          in: query
          required: false
          schema:
            type: string
        - name: name
          in: query
          required: false
          schema:
            type: string
        - name: project_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
        - name: project_deleted
          in: query
          required: false
          schema:
            type: boolean
        - name: filters
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Experiment groups
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExperimentGroupResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    GroupContent:
      type: object
      properties:
        label:
          type: string
      title: GroupContent
    GroupDetail:
      type: object
      properties:
        group_sorting:
          type: array
          items:
            type: string
      title: GroupDetail
    GroupDetails:
      type: object
      properties:
        groups_details:
          type: array
          items:
            $ref: '#/components/schemas/GroupDetail'
      title: GroupDetails
    ExperimentGroupResponse:
      type: object
      properties:
        content:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/GroupContent'
        details:
          $ref: '#/components/schemas/GroupDetails'
      title: ExperimentGroupResponse
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

url = "http://localhost:5173/api/v1/private/experiments/groups"

querystring = {"groups":"status,model","types":"training,validation","name":"resnet","project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","project_deleted":"false","filters":"accuracy>0.8"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8';
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

	url := "http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8"

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

url = URI("http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments/groups?groups=status%2Cmodel&types=training%2Cvalidation&name=resnet&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=accuracy%3E0.8")! as URL,
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