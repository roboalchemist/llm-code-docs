# Source: https://www.comet.com/docs/opik/reference/rest-api/prompts/update-prompt-versions.mdx

# Update prompt versions

PATCH http://localhost:5173/api/v1/private/prompts/versions
Content-Type: application/json

Update one or more prompt versions.

Note: Prompt versions are immutable by design.
Only organizational properties, such as tags etc., can be updated.
Core properties like template and metadata cannot be modified after creation.

PATCH semantics:
- non-empty values update the field
- null values preserve existing field values (no change)
- empty values explicitly clear the field


Reference: https://www.comet.com/docs/opik/reference/rest-api/prompts/update-prompt-versions

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/private/prompts/versions:
    patch:
      operationId: update-prompt-versions
      summary: Update prompt versions
      description: >
        Update one or more prompt versions.


        Note: Prompt versions are immutable by design.

        Only organizational properties, such as tags etc., can be updated.

        Core properties like template and metadata cannot be modified after
        creation.


        PATCH semantics:

        - non-empty values update the field

        - null values preserve existing field values (no change)

        - empty values explicitly clear the field
      tags:
        - subpackage_prompts
      responses:
        '204':
          description: No Content
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Prompts_updatePromptVersions_Response_204'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorMessage'
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/PromptVersionBatchUpdate'
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api
components:
  schemas:
    PromptVersionUpdate:
      type: object
      properties:
        tags:
          type: array
          items:
            type: string
          description: |
            Tags to set or merge with existing tags. Follows PATCH semantics:
            - If merge_tags is true, these tags will be added to existing tags.
            - If merge_tags is false, these tags will replace all existing tags.
            - null: preserve existing tags (no change).
            - empty set: clear all tags when merge_tags is false.
      description: >
        Update to apply to prompt versions.

        Note: Prompt versions are immutable by design.

        Only organizational properties (such as tags etc.) can be updated.

        Core properties like template, metadata etc. cannot be modified after
        creation.
      title: PromptVersionUpdate
    PromptVersionBatchUpdate:
      type: object
      properties:
        ids:
          type: array
          items:
            type: string
            format: uuid
          description: IDs of prompt versions to update
        update:
          $ref: '#/components/schemas/PromptVersionUpdate'
        merge_tags:
          type: boolean
          default: false
          description: >
            Tag merge behavior:

            - true: Add new tags to existing tags (union)

            - false: Replace all existing tags with new tags (default behaviour
            if not provided)
      required:
        - ids
        - update
      description: >
        Request to update one or more prompt versions.

        Note: Prompt versions are immutable by design - only organizational
        properties (such as tags etc.) can be updated.
      title: PromptVersionBatchUpdate
    Prompts_updatePromptVersions_Response_204:
      type: object
      properties: {}
      description: Empty response body
      title: Prompts_updatePromptVersions_Response_204
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

url = "http://localhost:5173/api/v1/private/prompts/versions"

payload = { "ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"] }
headers = {"Content-Type": "application/json"}

response = requests.patch(url, json=payload, headers=headers)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/private/prompts/versions';
const options = {
  method: 'PATCH',
  headers: {'Content-Type': 'application/json'},
  body: '{"ids":["3fa85f64-5717-4562-b3fc-2c963f66afa6","7c9e6679-7425-40de-944b-e07fc1f90ae7"]}'
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

	url := "http://localhost:5173/api/v1/private/prompts/versions"

	payload := strings.NewReader("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")

	req, _ := http.NewRequest("PATCH", url, payload)

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

url = URI("http://localhost:5173/api/v1/private/prompts/versions")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Patch.new(url)
request["Content-Type"] = 'application/json'
request.body = "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}"

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.patch("http://localhost:5173/api/v1/private/prompts/versions")
  .header("Content-Type", "application/json")
  .body("{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('PATCH', 'http://localhost:5173/api/v1/private/prompts/versions', [
  'body' => '{
  "ids": [
    "3fa85f64-5717-4562-b3fc-2c963f66afa6",
    "7c9e6679-7425-40de-944b-e07fc1f90ae7"
  ]
}',
  'headers' => [
    'Content-Type' => 'application/json',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/private/prompts/versions");
var request = new RestRequest(Method.PATCH);
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"ids\": [\n    \"3fa85f64-5717-4562-b3fc-2c963f66afa6\",\n    \"7c9e6679-7425-40de-944b-e07fc1f90ae7\"\n  ]\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = ["Content-Type": "application/json"]
let parameters = ["ids": ["3fa85f64-5717-4562-b3fc-2c963f66afa6", "7c9e6679-7425-40de-944b-e07fc1f90ae7"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/private/prompts/versions")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "PATCH"
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