# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiments.mdx

# Find experiments

GET http://localhost:5173/api/v1/private/experiments

Find experiments

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiments

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments:
    get:
      operationId: find-experiments
      summary: Find experiments
      description: Find experiments
      tags:
        - subpackage_experiments
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
            default: 10
        - name: datasetId
          in: query
          required: false
          schema:
            type: string
            format: uuid
        - name: optimization_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
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
        - name: dataset_deleted
          in: query
          required: false
          schema:
            type: boolean
        - name: prompt_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
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
        - name: sorting
          in: query
          required: false
          schema:
            type: string
        - name: filters
          in: query
          required: false
          schema:
            type: string
        - name: experiment_ids
          in: query
          required: false
          schema:
            type: string
        - name: force_sorting
          in: query
          required: false
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: Experiments resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExperimentPage_Public'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonListStringPublicOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringPublicOneOf1Items
    JsonListStringPublic1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringPublicOneOf1Items'
      title: JsonListStringPublic1
    JsonListString_Public:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListStringPublic1'
        - type: string
      title: JsonListString_Public
    ExperimentPublicType:
      type: string
      enum:
        - regular
        - trial
        - mini-batch
      title: ExperimentPublicType
    ExperimentPublicEvaluationMethod:
      type: string
      enum:
        - dataset
        - evaluation_suite
      title: ExperimentPublicEvaluationMethod
    FeedbackScoreAverage_Public:
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
      title: FeedbackScoreAverage_Public
    Comment_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        text:
          type: string
        created_at:
          type: string
          format: date-time
        last_updated_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
      required:
        - text
      title: Comment_Public
    PercentageValues_Public:
      type: object
      properties:
        p50:
          type: number
          format: double
        p90:
          type: number
          format: double
        p99:
          type: number
          format: double
      title: PercentageValues_Public
    ExperimentPublicStatus:
      type: string
      enum:
        - running
        - completed
        - cancelled
      title: ExperimentPublicStatus
    ExperimentScore_Public:
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
      title: ExperimentScore_Public
    PromptVersionLink_Public:
      type: object
      properties:
        prompt_version_id:
          type: string
          format: uuid
        commit:
          type: string
        prompt_id:
          type: string
          format: uuid
        prompt_name:
          type: string
      title: PromptVersionLink_Public
    DatasetVersionSummary_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier of the version
        version_hash:
          type: string
          description: Hash of the version content
        version_name:
          type: string
          description: Sequential version name formatted as 'v1', 'v2', etc.
        change_description:
          type: string
          description: Description of changes in this version
        tags:
          type: array
          items:
            type: string
          description: Tags associated with this version
      description: Summary of the latest dataset version
      title: DatasetVersionSummary_Public
    Experiment_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        dataset_name:
          type: string
        dataset_id:
          type: string
          format: uuid
        project_id:
          type: string
          format: uuid
        project_name:
          type: string
        name:
          type: string
        metadata:
          $ref: '#/components/schemas/JsonListString_Public'
        tags:
          type: array
          items:
            type: string
        type:
          $ref: '#/components/schemas/ExperimentPublicType'
        evaluation_method:
          $ref: '#/components/schemas/ExperimentPublicEvaluationMethod'
        optimization_id:
          type: string
          format: uuid
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage_Public'
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment_Public'
        trace_count:
          type: integer
          format: int64
        created_at:
          type: string
          format: date-time
        duration:
          $ref: '#/components/schemas/PercentageValues_Public'
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_avg:
          type: number
          format: double
        usage:
          type: object
          additionalProperties:
            type: number
            format: double
        last_updated_at:
          type: string
          format: date-time
        created_by:
          type: string
        last_updated_by:
          type: string
        status:
          $ref: '#/components/schemas/ExperimentPublicStatus'
        experiment_scores:
          type: array
          items:
            $ref: '#/components/schemas/ExperimentScore_Public'
        prompt_version:
          $ref: '#/components/schemas/PromptVersionLink_Public'
        prompt_versions:
          type: array
          items:
            $ref: '#/components/schemas/PromptVersionLink_Public'
        dataset_version_id:
          type: string
          format: uuid
          description: >-
            ID of the dataset version this experiment is linked to. If not
            provided at creation, experiment will be automatically linked to the
            latest version.
        dataset_version_summary:
          $ref: '#/components/schemas/DatasetVersionSummary_Public'
      required:
        - dataset_name
      title: Experiment_Public
    ExperimentPage_Public:
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
            $ref: '#/components/schemas/Experiment_Public'
        sortableBy:
          type: array
          items:
            type: string
      title: ExperimentPage_Public
    ErrorMessage_Public:
      type: object
      properties:
        code:
          type: integer
        message:
          type: string
        details:
          type: string
      title: ErrorMessage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/experiments"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments';
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

	url := "http://localhost:5173/api/v1/private/experiments"

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

url = URI("http://localhost:5173/api/v1/private/experiments")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/experiments")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/experiments', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/experiments");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments")! as URL,
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