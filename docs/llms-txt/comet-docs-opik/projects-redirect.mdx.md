# Source: https://www.comet.com/docs/opik/reference/rest-api/redirect/projects-redirect.mdx

# Create project redirect url

GET http://localhost:5173/api/v1/session/redirect/projects

Create project redirect url

Reference: https://www.comet.com/docs/opik/reference/rest-api/redirect/projects-redirect

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: Opik REST API
  version: 1.0.0
paths:
  /v1/session/redirect/projects:
    get:
      operationId: projects-redirect
      summary: Create project redirect url
      description: Create project redirect url
      tags:
        - subpackage_redirect
      parameters:
        - name: trace_id
          in: query
          required: true
          schema:
            type: string
            format: uuid
        - name: workspace_name
          in: query
          required: false
          schema:
            type: string
        - name: path
          in: query
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
servers:
  - url: http://localhost:5173/api
  - url: https://www.comet.com/opik/api

```

## SDK Code Examples

```python
import requests

url = "http://localhost:5173/api/v1/session/redirect/projects"

querystring = {"trace_id":"trace_id","path":"path"}

response = requests.get(url, params=querystring)

print(response.json())
```

```javascript
const url = 'http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path';
const options = {method: 'GET'};

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
	"net/http"
	"io"
)

func main() {

	url := "http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path"

	req, _ := http.NewRequest("GET", url, nil)

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

url = URI("http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path")

http = Net::HTTP.new(url.host, url.port)

request = Net::HTTP::Get.new(url)

response = http.request(request)
puts response.read_body
```

```java
import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

HttpResponse<String> response = Unirest.get("http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path")
  .asString();
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path');

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path");
var request = new RestRequest(Method.GET);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let request = NSMutableURLRequest(url: NSURL(string: "http://localhost:5173/api/v1/session/redirect/projects?trace_id=trace_id&path=path")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"

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