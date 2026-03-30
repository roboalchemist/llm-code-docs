# Source: https://www.comet.com/docs/opik/reference/rest-api/spans/get-spans-by-project.mdx

# Get spans by project_name or project_id and optionally by trace_id and/or type

GET http://localhost:5173/api/v1/private/spans

Get spans by project_name or project_id and optionally by trace_id and/or type

Reference: https://www.comet.com/docs/opik/reference/rest-api/spans/get-spans-by-project

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/spans:
    get:
      operationId: get-spans-by-project
      summary: >-
        Get spans by project_name or project_id and optionally by trace_id
        and/or type
      description: >-
        Get spans by project_name or project_id and optionally by trace_id
        and/or type
      tags:
        - subpackage_spans
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
        - name: project_name
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
        - name: trace_id
          in: query
          required: false
          schema:
            type: string
            format: uuid
        - name: type
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/V1PrivateSpansGetParametersType'
        - name: filters
          in: query
          required: false
          schema:
            type: string
        - name: truncate
          in: query
          required: false
          schema:
            type: boolean
            default: false
        - name: strip_attachments
          in: query
          required: false
          schema:
            type: boolean
            default: false
        - name: sorting
          in: query
          required: false
          schema:
            type: string
        - name: exclude
          in: query
          required: false
          schema:
            type: string
        - name: search
          in: query
          required: false
          schema:
            type: string
        - name: from_time
          in: query
          required: false
          schema:
            type: string
            format: date-time
        - name: to_time
          in: query
          required: false
          schema:
            type: string
            format: date-time
      responses:
        '200':
          description: Spans resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpanPage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    V1PrivateSpansGetParametersType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: V1PrivateSpansGetParametersType
    SpanPublicType:
      type: string
      enum:
        - general
        - tool
        - llm
        - guardrail
      title: SpanPublicType
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
    ErrorInfo_Public:
      type: object
      properties:
        exception_type:
          type: string
        message:
          type: string
        traceback:
          type: string
      required:
        - exception_type
        - traceback
      title: ErrorInfo_Public
    FeedbackScorePublicSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScorePublicSource
    ValueEntryPublicSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntryPublicSource
    ValueEntry_Public:
      type: object
      properties:
        value:
          type: number
          format: double
        reason:
          type: string
        category_name:
          type: string
        source:
          $ref: '#/components/schemas/ValueEntryPublicSource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry_Public
    FeedbackScore_Public:
      type: object
      properties:
        name:
          type: string
        category_name:
          type: string
        value:
          type: number
          format: double
        reason:
          type: string
        source:
          $ref: '#/components/schemas/FeedbackScorePublicSource'
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
        value_by_author:
          type: object
          additionalProperties:
            $ref: '#/components/schemas/ValueEntry_Public'
      required:
        - name
        - value
        - source
      description: >-
        Aggregated feedback scores from all spans in this trace, averaged by
        score name
      title: FeedbackScore_Public
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
    Span_Public:
      type: object
      properties:
        id:
          type: string
          format: uuid
        project_name:
          type: string
          description: If null, the default project is used
        project_id:
          type: string
          format: uuid
        trace_id:
          type: string
          format: uuid
        parent_span_id:
          type: string
          format: uuid
        name:
          type: string
        type:
          $ref: '#/components/schemas/SpanPublicType'
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        input:
          $ref: '#/components/schemas/JsonListString_Public'
        output:
          $ref: '#/components/schemas/JsonListString_Public'
        metadata:
          $ref: '#/components/schemas/JsonListString_Public'
        model:
          type: string
        provider:
          type: string
        tags:
          type: array
          items:
            type: string
        usage:
          type: object
          additionalProperties:
            type: integer
        error_info:
          $ref: '#/components/schemas/ErrorInfo_Public'
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
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore_Public'
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment_Public'
        total_estimated_cost:
          type: number
          format: double
        total_estimated_cost_version:
          type: string
        duration:
          type: number
          format: double
          description: >-
            Duration in milliseconds as a decimal number to support
            sub-millisecond precision
        ttft:
          type: number
          format: double
          description: Time to first token in milliseconds
      required:
        - start_time
      title: Span_Public
    SpanPage_Public:
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
            $ref: '#/components/schemas/Span_Public'
        sortableBy:
          type: array
          items:
            type: string
      title: SpanPage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/spans"

querystring = {"page":"1","size":"10","project_name":"weather-forecast-app","project_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","trace_id":"7c9e6679-7425-40de-944b-e07fc1f90ae7","type":"general","filters":"status:success","truncate":"true","strip_attachments":"false","sorting":"start_time:desc","exclude":"debug","search":"temperature","from_time":"2024-04-01T00:00:00Z","to_time":"2024-04-10T23:59:59Z"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z';
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

	url := "http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z"

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

url = URI("http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/spans?page=1&size=10&project_name=weather-forecast-app&project_id=3fa85f64-5717-4562-b3fc-2c963f66afa6&trace_id=7c9e6679-7425-40de-944b-e07fc1f90ae7&type=general&filters=status%3Asuccess&truncate=true&strip_attachments=false&sorting=start_time%3Adesc&exclude=debug&search=temperature&from_time=2024-04-01T00%3A00%3A00Z&to_time=2024-04-10T23%3A59%3A59Z")! as URL,
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