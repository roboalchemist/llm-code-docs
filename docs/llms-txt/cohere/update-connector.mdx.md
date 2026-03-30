# Source: https://docs.cohere.com/reference/update-connector.mdx

# Update a Connector

PATCH https://api.cohere.com/v1/connectors/{id}
Content-Type: application/json

Update a connector by ID. Omitted fields will not be updated. See ['Managing your Connector'](https://docs.cohere.com/docs/managing-your-connector) for more information.

Reference: https://docs.cohere.com/reference/update-connector

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/connectors/{id}:
    patch:
      operationId: update
      summary: Update a Connector
      description: >-
        Update a connector by ID. Omitted fields will not be updated. See
        ['Managing your
        Connector'](https://docs.cohere.com/docs/managing-your-connector) for
        more information.
      tags:
        - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to update.
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
                $ref: '#/components/schemas/UpdateConnectorResponse'
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
                $ref: '#/components/schemas/Update-connectorRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-connectorRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-connectorRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-connectorRequestNotFoundError'
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
                  #/components/schemas/Update-connectorRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Update-connectorRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Update-connectorRequestGatewayTimeoutError
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateConnectorRequest'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    CreateConnectorOAuth:
      type: object
      properties:
        client_id:
          type: string
          description: The OAuth 2.0 client ID. This fields is encrypted at rest.
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
      title: CreateConnectorOAuth
    AuthTokenType:
      type: string
      enum:
        - bearer
        - basic
        - noscheme
      default: noscheme
      description: >-
        The token_type specifies the way the token is passed in the
        Authorization header. Valid values are "bearer", "basic", and
        "noscheme".
      title: AuthTokenType
    CreateConnectorServiceAuth:
      type: object
      properties:
        type:
          $ref: '#/components/schemas/AuthTokenType'
        token:
          type: string
          description: >-
            The token that will be used in the HTTP Authorization header when
            making requests to the connector. This field is encrypted at rest
            and never returned in a response.
      required:
        - type
        - token
      title: CreateConnectorServiceAuth
    UpdateConnectorRequest:
      type: object
      properties:
        name:
          type: string
          description: A human-readable name for the connector.
        url:
          type: string
          description: The URL of the connector that will be used to search for documents.
        excludes:
          type: array
          items:
            type: string
          description: >-
            A list of fields to exclude from the prompt (fields remain in the
            document).
        oauth:
          $ref: '#/components/schemas/CreateConnectorOAuth'
          description: >-
            The OAuth 2.0 configuration for the connector. Cannot be specified
            if service_auth is specified.
        active:
          type: boolean
          default: true
        continue_on_failure:
          type: boolean
          default: false
        service_auth:
          $ref: '#/components/schemas/CreateConnectorServiceAuth'
          description: >-
            The service to service authentication configuration for the
            connector. Cannot be specified if oauth is specified.
      title: UpdateConnectorRequest
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
    UpdateConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector
      title: UpdateConnectorResponse
    Update-connectorRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestBadRequestError
    Update-connectorRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestUnauthorizedError
    Update-connectorRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestForbiddenError
    Update-connectorRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestNotFoundError
    Update-connectorRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestUnprocessableEntityError
    Update-connectorRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestTooManyRequestsError
    Update-connectorRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestInvalidTokenError
    Update-connectorRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestClientClosedRequestError
    Update-connectorRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestInternalServerError
    Update-connectorRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestNotImplementedError
    Update-connectorRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestServiceUnavailableError
    Update-connectorRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Update-connectorRequestGatewayTimeoutError
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

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Connectors.Update(
		context.TODO(),
		"connector_id",
		&cohere.UpdateConnectorRequest{
			Name: cohere.String("Example connector renamed"),
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()
response = co.connectors.update(
    connector_id="test-id", name="new name", url="https://example.com/search"
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.update(
        connector_id="test-id", name="new name", url="https://example.com/search"
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.connectors.update(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.UpdateConnectorRequest;

public class ConnectorPatch {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    cohere
        .connectors()
        .update(
            "test-id",
            UpdateConnectorRequest.builder()
                .name("new name")
                .url("https://connector-example.com/search")
                .build());
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.update(connector.id, {
    name: 'test-connector-renamed',
    description: 'A test connector renamed',
  });

  console.log(connector);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.connectors.update("id", {});
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Patch.new(url)
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

$response = $client->request('PATCH', 'https://api.cohere.com/v1/connectors/id', [
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
var request = new RestRequest(Method.PATCH);
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