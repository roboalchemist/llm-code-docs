# Source: https://docs.cohere.com/reference/create-connector.mdx

# Create a Connector

POST https://api.cohere.com/v1/connectors
Content-Type: application/json

Creates a new connector. The connector is tested during registration and will cancel registration when the test is unsuccessful. See ['Creating and Deploying a Connector'](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector) for more information.

Reference: https://docs.cohere.com/reference/create-connector

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/connectors:
    post:
      operationId: create
      summary: Create a Connector
      description: >-
        Creates a new connector. The connector is tested during registration and
        will cancel registration when the test is unsuccessful. See ['Creating
        and Deploying a
        Connector'](https://docs.cohere.com/v1/docs/creating-and-deploying-a-connector)
        for more information.
      tags:
        - subpackage_connectors
      parameters:
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
                $ref: '#/components/schemas/CreateConnectorResponse'
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
                $ref: '#/components/schemas/Create-connectorRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-connectorRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-connectorRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-connectorRequestNotFoundError'
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
                  #/components/schemas/Create-connectorRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-connectorRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-connectorRequestGatewayTimeoutError
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateConnectorRequest'
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
    CreateConnectorRequest:
      type: object
      properties:
        name:
          type: string
          description: A human-readable name for the connector.
        description:
          type: string
          description: A description of the connector.
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
          description: Whether the connector is active or not.
        continue_on_failure:
          type: boolean
          default: false
          description: >-
            Whether a chat request should continue or not if the request to this
            connector fails.
        service_auth:
          $ref: '#/components/schemas/CreateConnectorServiceAuth'
          description: >-
            The service to service authentication configuration for the
            connector. Cannot be specified if oauth is specified.
      required:
        - name
        - url
      title: CreateConnectorRequest
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
    CreateConnectorResponse:
      type: object
      properties:
        connector:
          $ref: '#/components/schemas/Connector'
      required:
        - connector
      title: CreateConnectorResponse
    Create-connectorRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestBadRequestError
    Create-connectorRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestUnauthorizedError
    Create-connectorRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestForbiddenError
    Create-connectorRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestNotFoundError
    Create-connectorRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestUnprocessableEntityError
    Create-connectorRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestTooManyRequestsError
    Create-connectorRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestInvalidTokenError
    Create-connectorRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestClientClosedRequestError
    Create-connectorRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestInternalServerError
    Create-connectorRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestNotImplementedError
    Create-connectorRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestServiceUnavailableError
    Create-connectorRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-connectorRequestGatewayTimeoutError
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

	resp, err := co.Connectors.Create(
		context.TODO(),
		&cohere.CreateConnectorRequest{
			Name: "Example connector",
			Url:  "https://you-connector-url",
			ServiceAuth: &cohere.CreateConnectorServiceAuth{
				Token: "dummy-connector-token",
				Type:  "bearer",
			},
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
response = co.connectors.create(
    name="Example connector",
    url="https://connector-example.com/search",
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.create(
        name="Example connector",
        url="https://connector-example.com/search",
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.connectors.create(
    name="Salesforce CRM Connector",
    url="https://api.salesforce.com/v1/search"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.CreateConnectorRequest;
import com.cohere.api.types.CreateConnectorResponse;

public class ConnectorCreate {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateConnectorResponse response =
        cohere
            .connectors()
            .create(
                CreateConnectorRequest.builder()
                    .name("Example connector")
                    .url("https://connector-example.com/search")
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.create({
    name: 'test-connector',
    url: 'https://example.com/search',
    description: 'A test connector',
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
    await client.connectors.create({
        name: "Salesforce CRM Connector",
        url: "https://api.salesforce.com/v1/search",
    });
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Salesforce CRM Connector\",\n  \"url\": \"https://api.salesforce.com/v1/search\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/connectors', [
  'body' => '{
  "name": "Salesforce CRM Connector",
  "url": "https://api.salesforce.com/v1/search"
}',
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

var client = new RestClient("https://api.cohere.com/v1/connectors");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Salesforce CRM Connector\",\n  \"url\": \"https://api.salesforce.com/v1/search\"\n}", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "application/json"
]
let parameters = [
  "name": "Salesforce CRM Connector",
  "url": "https://api.salesforce.com/v1/search"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors")! as URL,
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