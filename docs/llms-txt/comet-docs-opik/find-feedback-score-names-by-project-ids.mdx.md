# Source: https://www.comet.com/docs/opik/reference/rest-api/projects/find-feedback-score-names-by-project-ids.mdx

# Find Feedback Score names By Project Ids

GET http://localhost:5173/api/v1/private/projects/feedback-scores/names

Find Feedback Score names By Project Ids

Reference: https://www.comet.com/docs/opik/reference/rest-api/projects/find-feedback-score-names-by-project-ids

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/projects/feedback-scores/names:
    get:
      operationId: find-feedback-score-names-by-project-ids
      summary: Find Feedback Score names By Project Ids
      description: Find Feedback Score names By Project Ids
      tags:
        - subpackage_projects
      parameters:
        - name: project_ids
          in: query
          required: false
          schema:
            type: string
      responses:
        '200':
          description: Feedback Scores resource
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackScoreNames'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ScoreName:
      type: object
      properties:
        name:
          type: string
        type:
          type: string
      title: ScoreName
    FeedbackScoreNames:
      type: object
      properties:
        scores:
          type: array
          items:
            $ref: '#/components/schemas/ScoreName'
      title: FeedbackScoreNames

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/projects/feedback-scores/names"

querystring = {"project_ids":"proj_12345,proj_67890"}

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890';
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

	url := "http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890"

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

url = URI("http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/projects/feedback-scores/names?project_ids=proj_12345%2Cproj_67890")! as URL,
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