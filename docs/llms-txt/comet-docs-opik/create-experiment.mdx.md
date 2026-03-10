# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/create-experiment.mdx

# Create experiment

POST http://localhost:5173/api/v1/private/experiments
Content-Type: application/json

Create experiment

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/create-experiment

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments:
    post:
      operationId: create-experiment
      summary: Create experiment
      description: Create experiment
      tags:
        - subpackage_experiments
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Experiments_createExperiment_Response_201'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Experiment_Write'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonListStringWriteOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringWriteOneOf1Items
    JsonListStringWrite1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringWriteOneOf1Items'
      title: JsonListStringWrite1
    JsonListString_Write:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringWrite1'
        - type: string
      title: JsonListString_Write
    ExperimentWriteType:
      type: string
      enum:
        - regular
        - trial
        - mini-batch
      title: ExperimentWriteType
    ExperimentWriteEvaluationMethod:
      type: string
      enum:
        - dataset
        - evaluation_suite
      title: ExperimentWriteEvaluationMethod
    ExperimentWriteStatus:
      type: string
      enum:
        - running
        - completed
        - cancelled
      title: ExperimentWriteStatus
    ExperimentScore_Write:
      type: object
      properties:
        name:
          type: string
        value:
          type: number
          format: double
      required:
        - name
        - value
      title: ExperimentScore_Write
    PromptVersionLink_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
      required:
        - id
      title: PromptVersionLink_Write
    Experiment_Write:
      type: object
      properties:
        id:
          type: string
          format: uuid
        dataset_name:
          type: string
        name:
          type: string
        metadata:
          $ref: '#/components/schemas/JsonListString_Write'
        tags:
          type: array
          items:
            type: string
        type:
          $ref: '#/components/schemas/ExperimentWriteType'
        evaluation_method:
          $ref: '#/components/schemas/ExperimentWriteEvaluationMethod'
        optimization_id:
          type: string
          format: uuid
        status:
          $ref: '#/components/schemas/ExperimentWriteStatus'
        experiment_scores:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentScore_Write'
        prompt_version:
          $ref: '#/components/schemas/PromptVersionLink_Write'
        prompt_versions:
          type: array
          items:
            $ref: '#/components/schemas/PromptVersionLink_Write'
        dataset_version_id:
          type: string
          format: uuid
          description: >-
            ID of the dataset version this experiment is linked to. If not
            provided at creation, experiment will be automatically linked to the
            latest version.
      required:
        - dataset_name
      title: Experiment_Write
    Experiments_createExperiment_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Experiments_createExperiment_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/experiments"

payload = { "dataset_name": "customer_churn_2024" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"dataset_name":"customer_churn_2024"}'
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

	url := "http://localhost:5173/api/v1/private/experiments"

	payload := strings.NewReader("{\n  \"dataset_name\": \"customer_churn_2024\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/experiments")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"dataset_name\": \"customer_churn_2024\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/experiments")
  .header("Content-Type", "application/json")
  .body("{\n  \"dataset_name\": \"customer_churn_2024\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/experiments', [
  'body' => '{
  "dataset_name": "customer_churn_2024"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/experiments");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"dataset_name\": \"customer_churn_2024\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["dataset_name": "customer_churn_2024"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments")! as URL,
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