# Source: https://docs.cohere.com/reference/delete-dataset.mdx

# Delete a Dataset

DELETE https://api.cohere.com/v1/datasets/{id}

Delete a dataset by ID. Datasets are automatically deleted after 30 days, but they can also be deleted manually.

Reference: https://docs.cohere.com/reference/delete-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/datasets/{id}:
    delete:
      operationId: delete
      summary: Delete a Dataset
      description: >-
        Delete a dataset by ID. Datasets are automatically deleted after 30
        days, but they can also be deleted manually.
      tags:
        - subpackage_datasets
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
        - name: Authorization
          in: header
          description: Bearer authentication
          required: true
          schema:
            type: string
        - name: X-Client-Name
          in: header
          description: |
            The name of the project that is making the request.
          required: false
          schema:
            type: string
      responses:
        '200':
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/datasets_delete_Response_200'
        '400':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestNotFoundError'
        '422':
          description: >
            This error is returned when the request is not well formed. This
            could be because:
              - JSON is invalid
              - The request is missing required fields
              - The request contains an invalid combination of fields
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-datasetRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-datasetRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-datasetRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-datasetRequestGatewayTimeoutError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    datasets_delete_Response_200:
      type: object
      properties: {}
      title: datasets_delete_Response_200
    Delete-datasetRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestBadRequestError
    Delete-datasetRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestUnauthorizedError
    Delete-datasetRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestForbiddenError
    Delete-datasetRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestNotFoundError
    Delete-datasetRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestUnprocessableEntityError
    Delete-datasetRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestTooManyRequestsError
    Delete-datasetRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestInvalidTokenError
    Delete-datasetRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestClientClosedRequestError
    Delete-datasetRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestInternalServerError
    Delete-datasetRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestNotImplementedError
    Delete-datasetRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestServiceUnavailableError
    Delete-datasetRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-datasetRequestGatewayTimeoutError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	_, err := co.Datasets.Delete(context.TODO(), "dataset_id")

	if err != nil {
		log.Fatal(err)
	}

}

```

```python Sync
import cohere

co = cohere.Client()

# delete dataset
co.datasets.delete("id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.delete_dataset("id")


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.datasets.delete(
    id="dataset_9f8b7c6d5a4e3f2b1c0d"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class DatasetDelete {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.datasets().delete("id");
  }
}

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.datasets.delete("dataset_9f8b7c6d5a4e3f2b1c0d");
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets/dataset_9f8b7c6d5a4e3f2b1c0d")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Delete.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('DELETE', 'https://api.cohere.com/v1/datasets/dataset_9f8b7c6d5a4e3f2b1c0d', [
  'body' => '{}',
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'Content-Type' => 'application/json',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/datasets/dataset_9f8b7c6d5a4e3f2b1c0d");
var request = new RestRequest(Method.DELETE);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets/dataset_9f8b7c6d5a4e3f2b1c0d")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "DELETE"
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