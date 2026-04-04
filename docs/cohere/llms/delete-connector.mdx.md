# Source: https://docs.cohere.com/reference/delete-connector.mdx

# Delete a Connector

DELETE https://api.cohere.com/v1/connectors/{id}

Delete a connector by ID. See ['Connectors'](https://docs.cohere.com/docs/connectors) for more information.

Reference: https://docs.cohere.com/reference/delete-connector

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/connectors/{id}:
    delete:
      operationId: delete
      summary: Delete a Connector
      description: >-
        Delete a connector by ID. See
        ['Connectors'](https://docs.cohere.com/docs/connectors) for more
        information.
      tags:
        - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to delete.
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
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteConnectorResponse'
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
                $ref: '#/components/schemas/Delete-connectorRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-connectorRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-connectorRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-connectorRequestNotFoundError'
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
                  #/components/schemas/Delete-connectorRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Delete-connectorRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Delete-connectorRequestGatewayTimeoutError
servers:
  - url: https://api.cohere.com
components:
  schemas:
    DeleteConnectorResponse:
      type: object
      properties: {}
      title: DeleteConnectorResponse
    Delete-connectorRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestBadRequestError
    Delete-connectorRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestUnauthorizedError
    Delete-connectorRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestForbiddenError
    Delete-connectorRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestNotFoundError
    Delete-connectorRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestUnprocessableEntityError
    Delete-connectorRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestTooManyRequestsError
    Delete-connectorRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestInvalidTokenError
    Delete-connectorRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestClientClosedRequestError
    Delete-connectorRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestInternalServerError
    Delete-connectorRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestNotImplementedError
    Delete-connectorRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestServiceUnavailableError
    Delete-connectorRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Delete-connectorRequestGatewayTimeoutError
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

	resp, err := co.Connectors.Delete(context.TODO(), "connector_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  await cohere.connectors.delete('connector-id');
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.connectors.delete("id");
}
main();

```

```python Sync
import cohere

co = cohere.Client()
co.connectors.delete("test-id")

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    await co.connectors.delete("test-id")


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.connectors.delete(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;

public class ConnectorDelete {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere.connectors().delete("test-id");
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

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

$response = $client->request('DELETE', 'https://api.cohere.com/v1/connectors/id', [
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

var client = new RestClient("https://api.cohere.com/v1/connectors/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id")! as URL,
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