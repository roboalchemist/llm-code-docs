# Source: https://docs.cohere.com/reference/oauthauthorize-connector.mdx

# Authorize with oAuth

POST https://api.cohere.com/v1/connectors/{id}/oauth/authorize

Authorize the connector with the given ID for the connector oauth app.  See ['Connector Authentication'](https://docs.cohere.com/docs/connector-authentication) for more information.

Reference: https://docs.cohere.com/reference/oauthauthorize-connector

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/connectors/{id}/oauth/authorize:
    post:
      operationId: o-auth-authorize
      summary: Authorize with oAuth
      description: >-
        Authorize the connector with the given ID for the connector oauth app. 
        See ['Connector
        Authentication'](https://docs.cohere.com/docs/connector-authentication)
        for more information.
      tags:
        - subpackage_connectors
      parameters:
        - name: id
          in: path
          description: The ID of the connector to authorize.
          required: true
          schema:
            type: string
        - name: after_token_redirect
          in: query
          description: The URL to redirect to after the connector has been authorized.
          required: false
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
                $ref: '#/components/schemas/OAuthAuthorizeResponse'
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
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestBadRequestError
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestUnauthorizedError
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestForbiddenError
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestNotFoundError
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
                  #/components/schemas/OAuthAuthorize-connectorRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestTooManyRequestsError
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestInvalidTokenError
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestInternalServerError
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestNotImplementedError
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/OAuthAuthorize-connectorRequestGatewayTimeoutError
servers:
  - url: https://api.cohere.com
components:
  schemas:
    OAuthAuthorizeResponse:
      type: object
      properties:
        redirect_url:
          type: string
          description: >-
            The OAuth 2.0 redirect url. Redirect the user to this url to
            authorize the connector.
      title: OAuthAuthorizeResponse
    OAuthAuthorize-connectorRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestBadRequestError
    OAuthAuthorize-connectorRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestUnauthorizedError
    OAuthAuthorize-connectorRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestForbiddenError
    OAuthAuthorize-connectorRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestNotFoundError
    OAuthAuthorize-connectorRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestUnprocessableEntityError
    OAuthAuthorize-connectorRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestTooManyRequestsError
    OAuthAuthorize-connectorRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestInvalidTokenError
    OAuthAuthorize-connectorRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestClientClosedRequestError
    OAuthAuthorize-connectorRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestInternalServerError
    OAuthAuthorize-connectorRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestNotImplementedError
    OAuthAuthorize-connectorRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestServiceUnavailableError
    OAuthAuthorize-connectorRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: OAuthAuthorize-connectorRequestGatewayTimeoutError
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

	resp, err := co.Connectors.OAuthAuthorize(
		context.TODO(),
		"connector_id",
		&cohere.ConnectorsOAuthAuthorizeRequest{
			AfterTokenRedirect: cohere.String("https://test.com"),
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
response = co.connectors.o_auth_authorize(
    connector_id="test-id", after_token_redirect="https://test.com"
)
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.connectors.o_auth_authorize(
        connector_id="test-id", after_token_redirect="https://test.com"
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.connectors.o_auth_authorize(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.connectors.requests.ConnectorsOAuthAuthorizeRequest;
import com.cohere.api.types.OAuthAuthorizeResponse;

public class ConnectorsIdOauthAuthorizePost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    OAuthAuthorizeResponse response =
        cohere
            .connectors()
            .oAuthAuthorize(
                "test-id",
                ConnectorsOAuthAuthorizeRequest.builder()
                    .afterTokenRedirect("https://connector-example.com/search")
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const connector = await cohere.connectors.oAuthAuthorize('connector-id', {
    redirect_uri: 'https://example.com/oauth/callback',
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
    await client.connectors.oAuthAuthorize("id", {});
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/connectors/id/oauth/authorize")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
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

$response = $client->request('POST', 'https://api.cohere.com/v1/connectors/id/oauth/authorize', [
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

var client = new RestClient("https://api.cohere.com/v1/connectors/id/oauth/authorize");
var request = new RestRequest(Method.POST);
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/connectors/id/oauth/authorize")! as URL,
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