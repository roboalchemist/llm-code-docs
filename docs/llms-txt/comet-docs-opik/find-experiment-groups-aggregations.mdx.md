# Source: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiment-groups-aggregations.mdx

# Find experiment groups with aggregations

GET http://localhost:5173/api/v1/private/experiments/groups/aggregations

Find experiments grouped by specified fields with aggregation metrics

Reference: https://www.comet.com/docs/opik/reference/rest-api/experiments/find-experiment-groups-aggregations

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/experiments/groups/aggregations:
    get:
      operationId: find-experiment-groups-aggregations
      summary: Find experiment groups with aggregations
      description: Find experiments grouped by specified fields with aggregation metrics
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
          description: Experiment groups with aggregations
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ExperimentGroupAggregationsResponse'
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
    PercentageValues:
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
      title: PercentageValues
    FeedbackScoreAverage:
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
      title: FeedbackScoreAverage
    AggregationData:
      type: object
      properties:
        experiment_count:
          type: integer
          format: int64
        trace_count:
          type: integer
          format: int64
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_avg:
          type: number
          format: double
        duration:
          $ref: '#/components/schemas/PercentageValues'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage'
        experiment_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScoreAverage'
      title: AggregationData
    GroupContentWithAggregations:
      type: object
      properties:
        label:
          type: string
        aggregations:
          $ref: '#/components/schemas/AggregationData'
      title: GroupContentWithAggregations
    ExperimentGroupAggregationsResponse:
      type: object
      properties:
        content:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/GroupContentWithAggregations'
      title: ExperimentGroupAggregationsResponse
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

url = "http://localhost:5173/api/v1/private/experiments/groups/aggregations"

querystring = {"groups":"project_id,experiment_type","types":"count,sum,avg","name":"image-classification","project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","project_deleted":"false","filters":"status:completed,created_at>2023-01-01"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01';
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

	url := "http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01"

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

url = URI("http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/experiments/groups/aggregations?groups=project_id%2Cexperiment_type&types=count%2Csum%2Cavg&name=image-classification&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&project_deleted=false&filters=status%3Acompleted%2Ccreated_at%3E2023-01-01")! as URL,
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