# Source: https://www.comet.com/docs/opik/reference/rest-api/service-toggles/get-service-toggles.mdx

# Get Service Toggles

GET http://localhost:5173/api/v1/private/toggles

Get Service Toggles

Reference: https://www.comet.com/docs/opik/reference/rest-api/service-toggles/get-service-toggles

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/toggles:
    get:
      operationId: get-service-toggles
      summary: Get Service Toggles
      description: Get Service Toggles
      tags:
        - subpackage_serviceToggles
      responses:
        '200':
          description: Service Toggles
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServiceTogglesConfig'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    ServiceTogglesConfig:
      type: object
      properties:
        pythonEvaluatorEnabled:
          type: boolean
        traceThreadPythonEvaluatorEnabled:
          type: boolean
        spanLlmAsJudgeEnabled:
          type: boolean
        spanUserDefinedMetricPythonEnabled:
          type: boolean
        guardrailsEnabled:
          type: boolean
        opikAIEnabled:
          type: boolean
        alertsEnabled:
          type: boolean
        welcomeWizardEnabled:
          type: boolean
        csvUploadEnabled:
          type: boolean
        exportEnabled:
          type: boolean
        optimizationStudioEnabled:
          type: boolean
        datasetVersioningEnabled:
          type: boolean
        datasetExportEnabled:
          type: boolean
        openaiProviderEnabled:
          type: boolean
        anthropicProviderEnabled:
          type: boolean
        geminiProviderEnabled:
          type: boolean
        openrouterProviderEnabled:
          type: boolean
        vertexaiProviderEnabled:
          type: boolean
        bedrockProviderEnabled:
          type: boolean
        customllmProviderEnabled:
          type: boolean
        ollamaProviderEnabled:
          type: boolean
        collaboratorsTabEnabled:
          type: boolean
      required:
        - pythonEvaluatorEnabled
        - traceThreadPythonEvaluatorEnabled
        - spanLlmAsJudgeEnabled
        - spanUserDefinedMetricPythonEnabled
        - guardrailsEnabled
        - opikAIEnabled
        - alertsEnabled
        - welcomeWizardEnabled
        - csvUploadEnabled
        - exportEnabled
        - optimizationStudioEnabled
        - datasetVersioningEnabled
        - datasetExportEnabled
        - openaiProviderEnabled
        - anthropicProviderEnabled
        - geminiProviderEnabled
        - openrouterProviderEnabled
        - vertexaiProviderEnabled
        - bedrockProviderEnabled
        - customllmProviderEnabled
        - ollamaProviderEnabled
        - collaboratorsTabEnabled
      title: ServiceTogglesConfig

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/toggles"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.get(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/toggles';
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

	url := "http://localhost:5173/api/v1/private/toggles"

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

url = URI("http://localhost:5173/api/v1/private/toggles")

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

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/private/toggles")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/private/toggles', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/toggles");
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

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/toggles")! as URL,
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