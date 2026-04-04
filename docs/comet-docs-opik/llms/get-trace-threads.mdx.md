# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-threads.mdx

# Get trace threads

GET http://localhost:5173/api/v1/private/traces/threads

Get trace threads

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-threads

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads:
    get:
      operationId: get-trace-threads
      summary: Get trace threads
      description: Get trace threads
      tags:
        - subpackage_traces
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
        - name: filters
          in: query
          required: false
          schema:
            type: string
        - name: sorting
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
          description: Trace threads resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TraceThreadPage'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    JsonListStringOneOf1Items:
      type: object
      properties: {}
      title: JsonListStringOneOf1Items
    JsonListString1:
      type: array
      items:
        $ref: '#/components/schemas/JsonListStringOneOf1Items'
      title: JsonListString1
    JsonListString:
      oneOf:
        - type: object
          additionalProperties:
            description: Any type
        - $ref: '#/components/schemas/JsonListString1'
        - type: string
      title: JsonListString
    FeedbackScoreSource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: FeedbackScoreSource
    ValueEntrySource:
      type: string
      enum:
        - ui
        - sdk
        - online_scoring
      title: ValueEntrySource
    ValueEntry:
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
          $ref: '#/components/schemas/ValueEntrySource'
        last_updated_at:
          type: string
          format: date-time
        span_type:
          type: string
        span_id:
          type: string
      title: ValueEntry
    FeedbackScore:
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
          $ref: '#/components/schemas/FeedbackScoreSource'
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
            $ref: '#/components/schemas/ValueEntry'
      required:
        - name
        - value
        - source
      title: FeedbackScore
    TraceThreadStatus:
      type: string
      enum:
        - active
        - inactive
      title: TraceThreadStatus
    Comment:
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
      title: Comment
    TraceThread:
      type: object
      properties:
        id:
          type: string
        project_id:
          type: string
          format: uuid
        thread_model_id:
          type: string
          format: uuid
        start_time:
          type: string
          format: date-time
        end_time:
          type: string
          format: date-time
        duration:
          type: number
          format: double
        first_message:
          $ref: '#/components/schemas/JsonListString'
        last_message:
          $ref: '#/components/schemas/JsonListString'
        feedback_scores:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackScore'
        status:
          $ref: '#/components/schemas/TraceThreadStatus'
        number_of_messages:
          type: integer
          format: int64
        total_estimated_cost:
          type: number
          format: double
        usage:
          type: object
          additionalProperties:
            type: integer
            format: int64
        comments:
          type: array
          items:
            $ref: '#/components/schemas/Comment'
        tags:
          type: array
          items:
            type: string
        last_updated_at:
          type: string
          format: date-time
        last_updated_by:
          type: string
        created_by:
          type: string
        created_at:
          type: string
          format: date-time
      title: TraceThread
    TraceThreadPage:
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
            $ref: '#/components/schemas/TraceThread'
        sortableBy:
          type: array
          items:
            type: string
      title: TraceThreadPage

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/traces/threads"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads';
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

	url := "http://localhost:5173/api/v1/private/traces/threads"

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

url = URI("http://localhost:5173/api/v1/private/traces/threads")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/traces/threads")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/traces/threads', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads")! as URL,
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