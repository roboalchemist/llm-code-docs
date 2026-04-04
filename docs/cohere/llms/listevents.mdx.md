# Source: https://docs.cohere.com/reference/listevents.mdx

# Fetch history of statuses for a fine-tuned model.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{finetuned_model_id}/events

Returns a list of events that occurred during the life-cycle of the fine-tuned model.
The events are ordered by creation time, with the most recent event first.
The list can be paginated using `page_size` and `page_token` parameters.

Reference: https://docs.cohere.com/reference/listevents

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/events:
    get:
      operationId: list-events
      summary: Fetch history of statuses for a fine-tuned model.
      description: >-
        Returns a list of events that occurred during the life-cycle of the
        fine-tuned model.

        The events are ordered by creation time, with the most recent event
        first.

        The list can be paginated using `page_size` and `page_token` parameters.
      tags:
        - subpackage_finetuning
      parameters:
        - name: finetuned_model_id
          in: path
          description: The parent fine-tuned model ID.
          required: true
          schema:
            type: string
        - name: page_size
          in: query
          description: >-
            Maximum number of results to be returned by the server. If 0,
            defaults to

            50.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: Request a specific page of the list results.
          required: false
          schema:
            type: string
        - name: order_by
          in: query
          description: >-
            Comma separated list of fields. For example: "created_at,name". The
            default

            sorting order is ascending. To specify descending order for a field,
            append

            " desc" to the field name. For example: "created_at desc,name".


            Supported sorting fields:
              - created_at (default)
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
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListEventsResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '503':
          description: Status Service Unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    Status:
      type: string
      enum:
        - STATUS_UNSPECIFIED
        - STATUS_FINETUNING
        - STATUS_DEPLOYING_API
        - STATUS_READY
        - STATUS_FAILED
        - STATUS_DELETED
        - STATUS_TEMPORARILY_OFFLINE
        - STATUS_PAUSED
        - STATUS_QUEUED
      default: STATUS_UNSPECIFIED
      description: |-
        The possible stages of a fine-tuned model life-cycle.

         - STATUS_UNSPECIFIED: Unspecified status.
         - STATUS_FINETUNING: The fine-tuned model is being fine-tuned.
         - STATUS_DEPLOYING_API: Deprecated: The fine-tuned model is being deployed.
         - STATUS_READY: The fine-tuned model is ready to receive requests.
         - STATUS_FAILED: The fine-tuned model failed.
         - STATUS_DELETED: The fine-tuned model was deleted.
         - STATUS_TEMPORARILY_OFFLINE: Deprecated: The fine-tuned model is temporarily unavailable.
         - STATUS_PAUSED: Deprecated: The fine-tuned model is paused (Vanilla only).
         - STATUS_QUEUED: The fine-tuned model is queued for training.
      title: Status
    Event:
      type: object
      properties:
        user_id:
          type: string
          description: >-
            ID of the user who initiated the event. Empty if initiated by the
            system.
        status:
          $ref: '#/components/schemas/Status'
          description: Status of the fine-tuned model.
        created_at:
          type: string
          format: date-time
          description: Timestamp when the event happened.
      description: A change in status of a fine-tuned model.
      title: Event
    ListEventsResponse:
      type: object
      properties:
        events:
          type: array
          items:
            $ref: '#/components/schemas/Event'
          description: List of events for the fine-tuned model.
        next_page_token:
          type: string
          description: >-
            Pagination token to retrieve the next page of results. If the value
            is "",

            it means no further results for the request.
        total_size:
          type: integer
          description: Total count of results.
      description: Response to a request to list events of a fine-tuned model.
      title: ListEventsResponse
    Error:
      type: object
      properties:
        message:
          type: string
          description: A developer-facing error message.
      description: Error is the response for any unsuccessful event.
      title: Error
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```java Cohere java SDK
/* (C)2024 */
package finetuning;

import com.cohere.api.Cohere;
import com.cohere.api.resources.finetuning.finetuning.types.ListEventsResponse;

public class ListEvents {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListEventsResponse response = cohere.finetuning().listEvents("test-id");

    System.out.println(response);
  }
}

```

```go Cohere Go SDK
package main

import (
	"context"
	"log"
	"os"

	"github.com/cohere-ai/cohere-go/v2/client"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.ListEvents(
		context.TODO(),
		"test-finetuned-model-id",
		nil,
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.Events)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const events = await cohere.finetuning.listEvents('test-finetuned-model-id');

  console.log(events);
})();

```

```typescript /finetuning_ListEvents_example
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.finetuning.listEvents("finetuned_model_id", {});
}
main();

```

```python Sync
import cohere

co = cohere.Client()
response = co.finetuning.list_events(finetuned_model_id="test-id")
print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.list_events(finetuned_model_id="test-id")
    print(response)


asyncio.run(main())

```

```python /finetuning_ListEvents_example
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.finetuning.list_events(
    finetuned_model_id="finetuned_model_id"
)

```

```ruby /finetuning_ListEvents_example
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php /finetuning_ListEvents_example
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp /finetuning_ListEvents_example
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift /finetuning_ListEvents_example
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/events")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "GET"
request.allHTTPHeaderFields = headers

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