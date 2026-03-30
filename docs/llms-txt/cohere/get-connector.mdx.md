# Source: https://docs.cohere.com/reference/get-connector.mdx

# Get a Connector

GET https://api.cohere.com/v1/connectors/{id}

Retrieve a connector by ID. See ['Connectors'](https://docs.cohere.com/docs/connectors) for more information.

Reference: https://docs.cohere.com/reference/get-connector

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/connectors/{id}:
    get:
      operationId: get
      summary: Get a Connector
      description: >-
        Retrieve a connector by ID. See
        ['Connectors'](https://docs.cohere.com/docs/connectors) for more
        information.
      tags:
        - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to retrieve.
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
                $ref: '#/components/schemas/GetConnectorResponse'
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
                $ref: '#/components/schemas/Get-connectorRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestNotFoundError'
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
                  #/components/schemas/Get-connectorRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-connectorRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-connectorRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-connectorRequestGatewayTimeoutError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    ConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
          description: The OAuth 2.0 client ID. This field is encrypted at rest.
        client_secret:
          type: string
          description: >-
            The OAuth 2.0 client Secret. This field is encrypted at rest and
            never returned in a response.
        authorize_url:
          type: string
          description: >-
            The OAuth 2.0 /authorize endpoint to use when users authorize the
            connector.
        token_url:
          type: string
          description: >-
            The OAuth 2.0 /token endpoint to use when users authorize the
            connector.
        scope:
          type: string
          description: The OAuth scopes to request when users authorize the connector.
      required:
        - authorize_url
        - token_url
      title: ConnectorOAuth
    ConnectorAuthStatus:
      type: string
      enum:
        - valid
        - expired
      description: >-
        The OAuth status for the user making the request. One of ["valid",
        "expired", ""]. Empty string (field is omitted) means the user has not
        authorized the connector yet.
      title: ConnectorAuthStatus
    Connector:
      type: object
      properties:
        id:
          type: string
          description: >-
            The unique identifier of the connector (used in both `/connectors` &
            `/chat` endpoints).

            This is automatically created from the name of the connector upon
            registration.
        organization_id:
          type: string
          description: >-
            The organization to which this connector belongs. This is
            automatically set to

            the organization of the user who created the connector.
        name:
          type: string
          description: A human-readable name for the connector.
        description:
          type: string
          description: A description of the connector.
        url:
          type: string
          description: The URL of the connector that will be used to search for documents.
        created_at:
          type: string
          format: date-time
          description: The UTC time at which the connector was created.
        updated_at:
          type: string
          format: date-time
          description: The UTC time at which the connector was last updated.
        excludes:
          type: array
          items:
            type: string
          description: >-
            A list of fields to exclude from the prompt (fields remain in the
            document).
        auth_type:
          type: string
          format: enum
          description: >-
            The type of authentication/authorization used by the connector.
            Possible values: [oauth, service_auth]
        oauth:
          $ref: '#/components/schemas/ConnectorOAuth'
          description: The OAuth 2.0 configuration for the connector.
        auth_status:
          $ref: '#/components/schemas/ConnectorAuthStatus'
          description: >-
            The OAuth status for the user making the request. One of ["valid",
            "expired", ""]. Empty string (field is omitted) means the user has
            not authorized the connector yet.
        active:
          type: boolean
          description: Whether the connector is active or not.
        continue_on_failure:
          type: boolean
          description: >-
            Whether a chat request should continue or not if the request to this
            connector fails.
      required:
        - id
        - name
        - created_at
        - updated_at
      description: >-
        A connector allows you to integrate data sources with the '/chat'
        endpoint to create grounded generations with citations to the data
        source.

        documents to help answer users.
      title: Connector
    GetConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector
      title: GetConnectorResponse
    Get-connectorRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestBadRequestError
    Get-connectorRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestUnauthorizedError
    Get-connectorRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestForbiddenError
    Get-connectorRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestNotFoundError
    Get-connectorRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestUnprocessableEntityError
    Get-connectorRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestTooManyRequestsError
    Get-connectorRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestInvalidTokenError
    Get-connectorRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestClientClosedRequestError
    Get-connectorRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestInternalServerError
    Get-connectorRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestNotImplementedError
    Get-connectorRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestServiceUnavailableError
    Get-connectorRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-connectorRequestGatewayTimeoutError
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

	resp, err := co.Connectors.Get(context.TODO(), "connector_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()
response = co.connectors.get("test-id")
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.get("test-id")
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.connectors.get(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.types.GetConnectorResponse;

public class ConnectorGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    GetConnectorResponse response = cohere.connectors().get("test-id");

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.get('connector-id');

  console.log(connector);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.connectors.get("id");
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
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

$response = $client->request('GET', 'https://api.cohere.com/v1/connectors/id', [
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
var request = new RestRequest(Method.GET);
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