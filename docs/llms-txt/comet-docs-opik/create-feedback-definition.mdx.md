# Source: https://www.comet.com/docs/opik/reference/rest-api/feedback-definitions/create-feedback-definition.mdx

# Create feedback definition

POST http://localhost:5173/api/v1/private/feedback-definitions
Content-Type: application/json

Get feedback definition

Reference: https://www.comet.com/docs/opik/reference/rest-api/feedback-definitions/create-feedback-definition

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/feedback-definitions:
    post:
      operationId: create-feedback-definition
      summary: Create feedback definition
      description: Get feedback definition
      tags:
        - subpackage_feedbackDefinitions
      responses:
        '201':
          description: Created
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Feedback-definitions_createFeedbackDefinition_Response_201
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Feedback_Create'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    NumericalFeedbackDefinitionCreateType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: NumericalFeedbackDefinitionCreateType
    NumericalFeedbackDetail_Create:
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
      title: NumericalFeedbackDetail_Create
    FeedbackCreateType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: FeedbackCreateType
    CategoricalFeedbackDefinitionCreateType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: CategoricalFeedbackDefinitionCreateType
    CategoricalFeedbackDetail_Create:
      type: object
      properties:
        categories:
          type: object
          additionalProperties:
            type: number
            format: double
      required:
        - categories
      title: CategoricalFeedbackDetail_Create
    BooleanFeedbackDefinitionCreateType:
      type: string
      enum:
        - numerical
        - categorical
        - boolean
      title: BooleanFeedbackDefinitionCreateType
    BooleanFeedbackDetail_Create:
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
      title: BooleanFeedbackDetail_Create
    Feedback_Create:
      oneOf:
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackCreateType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            details:
              $ref: '#/components/schemas/NumericalFeedbackDetail_Create'
          required:
            - type
            - name
            - details
          description: numerical variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackCreateType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            details:
              $ref: '#/components/schemas/CategoricalFeedbackDetail_Create'
          required:
            - type
            - name
            - details
          description: categorical variant
        - type: object
          properties:
            type:
              $ref: '#/components/schemas/FeedbackCreateType'
            id:
              type: string
              format: uuid
            name:
              type: string
            description:
              type: string
              description: Optional description for the feedback definition
            details:
              $ref: '#/components/schemas/BooleanFeedbackDetail_Create'
          required:
            - type
            - name
            - details
          description: boolean variant
      discriminator:
        propertyName: type
      title: Feedback_Create
    Feedback-definitions_createFeedbackDefinition_Response_201:
      type: object
      properties: {}
      description: Empty response body
      title: Feedback-definitions_createFeedbackDefinition_Response_201

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/feedback-definitions"

payload = {
    "type": "numerical",
    "name": "Response Time Feedback"
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/feedback-definitions';
const options = {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: '{"type":"numerical","name":"Response Time Feedback"}'
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

	url := "http://localhost:5173/api/v1/private/feedback-definitions"

	payload := strings.NewReader("{\n  \"type\": \"numerical\",\n  \"name\": \"Response Time Feedback\"\n}")

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

url = URI("http://localhost:5173/api/v1/private/feedback-definitions")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"type\": \"numerical\",\n  \"name\": \"Response Time Feedback\"\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/feedback-definitions")
  .header("Content-Type", "application/json")
  .body("{\n  \"type\": \"numerical\",\n  \"name\": \"Response Time Feedback\"\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/feedback-definitions', [
  'body' => '{
  "type": "numerical",
  "name": "Response Time Feedback"
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/feedback-definitions");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"type\": \"numerical\",\n  \"name\": \"Response Time Feedback\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [
  "type": "numerical",
  "name": "Response Time Feedback"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/feedback-definitions")! as URL,
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