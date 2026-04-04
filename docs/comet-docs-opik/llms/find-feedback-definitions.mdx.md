# Source: https://www.comet.com/docs/opik/reference/rest-api/feedback-definitions/find-feedback-definitions.mdx

# Find Feedback definitions

GET http://localhost:5173/api/v1/private/feedback-definitions

Find Feedback definitions

Reference: https://www.comet.com/docs/opik/reference/rest-api/feedback-definitions/find-feedback-definitions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/feedback-definitions:
    get:
      operationId: find-feedback-definitions
      summary: Find Feedback definitions
      description: Find Feedback definitions
      tags:
        - subpackage_feedbackDefinitions
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
        - name: name
          in: query
          required: false
          schema:
            type: string
        - name: type
          in: query
          required: false
          schema:
            $ref: '#/components/schemas/V1PrivateFeedbackDefinitionsGetParametersType'
      responses:
        '200':
          description: Feedback definitions resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackDefinitionPage_Public'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    V1PrivateFeedbackDefinitionsGetParametersType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: V1PrivateFeedbackDefinitionsGetParametersType
    NumericalFeedbackDefinitionPublicType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: NumericalFeedbackDefinitionPublicType
    NumericalFeedbackDetail_Public:
      type: object
      properties:
        max:
          type: number
          format: double
        min:
          type: number
          format: double
      required:
        - max
        - min
      title: NumericalFeedbackDetail_Public
    FeedbackObjectPublicType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: FeedbackObjectPublicType
    CategoricalFeedbackDefinitionPublicType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: CategoricalFeedbackDefinitionPublicType
    CategoricalFeedbackDetail_Public:
      type: object
      properties:
        categories:
          type: object
          additionalProperties:
            type: number
            format: double
      required:
        - categories
      title: CategoricalFeedbackDetail_Public
    BooleanFeedbackDefinitionPublicType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: BooleanFeedbackDefinitionPublicType
    BooleanFeedbackDetail_Public:
      type: object
      properties:
        trueLabel:
          type: string
          description: Label for true/1 value
        falseLabel:
          type: string
          description: Label for false/0 value
      required:
        - trueLabel
        - falseLabel
      title: BooleanFeedbackDetail_Public
    FeedbackObject_Public:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackObjectPublicType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            createdAt:
              type: string
              format: date-time
            createdBy:
              type: string
            lastUpdatedAt:
              type: string
              format: date-time
            lastUpdatedBy:
              type: string
            details:
              $ref: '#/components/schemas/NumericalFeedbackDetail_Public'
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
          required:
            - type
            - name
            - details
          description: numerical variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackObjectPublicType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            createdAt:
              type: string
              format: date-time
            createdBy:
              type: string
            lastUpdatedAt:
              type: string
              format: date-time
            lastUpdatedBy:
              type: string
            details:
              $ref: '#/components/schemas/CategoricalFeedbackDetail_Public'
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
          required:
            - type
            - name
            - details
          description: categorical variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackObjectPublicType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            createdAt:
              type: string
              format: date-time
            createdBy:
              type: string
            lastUpdatedAt:
              type: string
              format: date-time
            lastUpdatedBy:
              type: string
            details:
              $ref: '#/components/schemas/BooleanFeedbackDetail_Public'
            created_at:
              type: string
              format: date-time
            created_by:
              type: string
            last_updated_at:
              type: string
              format: date-time
            last_updated_by:
              type: string
          required:
            - type
            - name
            - details
          description: boolean variant
      discriminator:
        propertyName: type
      title: FeedbackObject_Public
    FeedbackDefinitionPage_Public:
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
            $ref: '#/components/schemas/FeedbackObject_Public'
      title: FeedbackDefinitionPage_Public

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/feedback-definitions"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/feedback-definitions';
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

	url := "http://localhost:5173/api/v1/private/feedback-definitions"

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

url = URI("http://localhost:5173/api/v1/private/feedback-definitions")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/feedback-definitions")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/feedback-definitions', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/feedback-definitions");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/feedback-definitions")! as URL,
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