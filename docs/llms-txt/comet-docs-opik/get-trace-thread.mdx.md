# Source: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-thread.mdx

# Get trace thread

POST http://localhost:5173/api/v1/private/traces/threads/retrieve
Content-Type: application/json

Get trace thread

Reference: https://www.comet.com/docs/opik/reference/rest-api/traces/get-trace-thread

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/traces/threads/retrieve:
    post:
      operationId: get-trace-thread
      summary: Get trace thread
      description: Get trace thread
      tags:
        - subpackage_traces
      responses:
        '200':
          description: Trace thread resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TraceThread'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TraceThreadIdentifier'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    TraceThreadIdentifier:
      type: object
      properties:
        project_name:
          type: string
        project_id:
          type: string
          format: uuid
        thread_id:
          type: string
        truncate:
          type: boolean
      required:
        - thread_id
      title: TraceThreadIdentifier
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

url = "http://localhost:5173/api/v1/private/traces/threads/retrieve"

payload = { "thread_id": "thread-9f8b7c6d5e4a3b2c1d0e" }
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/traces/threads/retrieve';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"thread_id":"thread-9f8b7c6d5e4a3b2c1d0e"}'
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

	url := "http://localhost:5173/api/v1/private/traces/threads/retrieve"

	payload := strings.NewReader("{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/traces/threads/retrieve")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/traces/threads/retrieve")
  .header("Content-Type", "application/json")
  .body("{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/traces/threads/retrieve', [
  'body' => '{
  "thread_id": "thread-9f8b7c6d5e4a3b2c1d0e"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/traces/threads/retrieve");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"thread_id\": \"thread-9f8b7c6d5e4a3b2c1d0e\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["thread_id": "thread-9f8b7c6d5e4a3b2c1d0e"] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/traces/threads/retrieve")! as URL,
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