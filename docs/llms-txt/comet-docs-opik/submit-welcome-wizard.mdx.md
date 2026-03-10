# Source: https://www.comet.com/docs/opik/reference/rest-api/welcome-wizard/submit-welcome-wizard.mdx

# Submit welcome wizard

POST http://localhost:5173/api/v1/private/welcome-wizard
Content-Type: application/json

Submit welcome wizard with user information

Reference: https://www.comet.com/docs/opik/reference/rest-api/welcome-wizard/submit-welcome-wizard

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/welcome-wizard:
    post:
      operationId: submit-welcome-wizard
      summary: Submit welcome wizard
      description: Submit welcome wizard with user information
      tags:
        - subpackage_welcomeWizard
      responses:
        '204':
          description: Welcome wizard submitted successfully
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Welcome
                  Wizard_submitWelcomeWizard_Response_204
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WelcomeWizardSubmission'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    WelcomeWizardSubmission:
      type: object
      properties:
        role:
          type: string
          description: Optional user role
        integrations:
          type: array
          items:
            type: string
          description: List of integrations the user selected
        email:
          type: string
          format: email
          description: Optional user email
        join_beta_program:
          type: boolean
          description: Whether user wants to join beta programs
      title: WelcomeWizardSubmission
    Welcome Wizard_submitWelcomeWizard_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Welcome Wizard_submitWelcomeWizard_Response_204

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/private/welcome-wizard"

payload = {}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/welcome-wizard';
const options = {method: 'POST', headers: {'Content-Type': 'application/json'}, body: '{}'};

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

	url := "http://localhost:5173/api/v1/private/welcome-wizard"

	payload := strings.NewReader("{}")

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

url = URI("http://localhost:5173/api/v1/private/welcome-wizard")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Post.new(url)
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.post("http://localhost:5173/api/v1/private/welcome-wizard")
  .header("Content-Type", "application/json")
  .body("{}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'http://localhost:5173/api/v1/private/welcome-wizard', [
  'body' => '{}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/welcome-wizard");
var request = new RestRequest(Method.POST);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/welcome-wizard")! as URL,
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