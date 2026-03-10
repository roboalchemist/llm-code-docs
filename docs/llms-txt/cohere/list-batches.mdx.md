# Source: https://docs.cohere.com/reference/list-batches.mdx

# List batches

GET https://api.cohere.com/v2/batches

List the batches for the current user

Reference: https://docs.cohere.com/reference/list-batches

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v2/batches:
    get:
      operationId: list
      summary: List batches
      description: List the batches for the current user
      tags:
        - subpackage_batches
      parameters:
        - name: page_size
          in: query
          description: >-
            The maximum number of batches to return. The service may return
            fewer than

            this value.

            If unspecified, at most 50 batches will be returned.

            The maximum value is 1000; values above 1000 will be coerced to
            1000.
          required: false
          schema:
            type: integer
        - name: page_token
          in: query
          description: |-
            A page token, received from a previous `ListBatches` call.
            Provide this to retrieve the subsequent page.
          required: false
          schema:
            type: string
        - name: order_by
          in: query
          description: >-
            Batches can be ordered by creation time or last updated time.

            Use `created_at` for creation time or `updated_at` for last updated
            time.
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
                $ref: '#/components/schemas/ListBatchesResponse'
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
        '500':
          description: Internal Server Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
        '503':
          description: Status Service Unavailable
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BatchError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    BatchStatus:
      type: string
      enum:
        - BATCH_STATUS_UNSPECIFIED
        - BATCH_STATUS_QUEUED
        - BATCH_STATUS_IN_PROGRESS
        - BATCH_STATUS_CANCELING
        - BATCH_STATUS_COMPLETED
        - BATCH_STATUS_FAILED
        - BATCH_STATUS_CANCELED
      default: BATCH_STATUS_UNSPECIFIED
      description: |-
        The possible stages of a batch life-cycle.

         - BATCH_STATUS_UNSPECIFIED: Unspecified status.
         - BATCH_STATUS_QUEUED: The batch has been queued.
         - BATCH_STATUS_IN_PROGRESS: The batch is in-progress.
         - BATCH_STATUS_CANCELING: The batch is being canceled.
         - BATCH_STATUS_COMPLETED: The batch has been completed.
         - BATCH_STATUS_FAILED: The batch has failed.
         - BATCH_STATUS_CANCELED: The batch has been canceled.
      title: BatchStatus
    Batch:
      type: object
      properties:
        id:
          type: string
          description: read-only. Batch ID.
        name:
          type: string
          description: Batch name (e.g. `foobar`).
        creator_id:
          type: string
          description: read-only. User ID of the creator.
        org_id:
          type: string
          description: read-only. Organization ID.
        status:
          $ref: '#/components/schemas/BatchStatus'
          description: read-only. Current stage in the life-cycle of the batch.
        created_at:
          type: string
          format: date-time
          description: read-only. Creation timestamp.
        updated_at:
          type: string
          format: date-time
          description: read-only. Latest update timestamp.
        input_dataset_id:
          type: string
          description: ID of the dataset the batch reads inputs from.
        output_dataset_id:
          type: string
        input_tokens:
          type: string
          format: int64
          description: read-only. The total number of input tokens in the batch.
        output_tokens:
          type: string
          format: int64
          description: read-only. The total number of output tokens in the batch.
        model:
          type: string
          description: The name of the model the batch uses.
        num_records:
          type: integer
          description: read-only. The total number of records in the batch.
        num_successful_records:
          type: integer
          description: read-only. The current number of successful records in the batch.
        num_failed_records:
          type: integer
          description: read-only. The current number of failed records in the batch.
        status_reason:
          type: string
          description: >-
            read-only. More details about the reason for the status of a batch
            job.
      required:
        - name
        - input_dataset_id
        - model
      description: This resource represents a batch job.
      title: Batch
    ListBatchesResponse:
      type: object
      properties:
        batches:
          type: array
          items:
            $ref: '#/components/schemas/Batch'
          description: The batches that belong to the authenticated user.
        next_page_token:
          type: string
          description: >-
            A token, which can be sent as `page_token` to retrieve the next
            page.

            If this field is omitted, there are no subsequent pages.
      description: Response to a request to list batches.
      title: ListBatchesResponse
    BatchError:
      type: object
      properties:
        message:
          type: string
          description: A developer-facing error message.
      description: Error is the response for any unsuccessful event.
      title: BatchError
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer

```

## SDK Code Examples

```python Default
import cohere

co = cohere.ClientV2()

batches = co.batches.list()
```

```python batches_list_example
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.batches.list()

```

```typescript Default
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const batches = await cohere.batches.list();
  console.log(batches);
})();

```

```typescript batches_list_example
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.batches.list({});
}
main();

```

```go Default
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

	resp, err := co.Batches.List(
		context.TODO(),
		&cohere.BatchesListBatchesRequest{})

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```java Default
import com.cohere.api.Cohere;
import com.cohere.api.resources.batches.types.ListBatchesResponse;

public class BatchGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListBatchesResponse response = cohere.batches().list();

    System.out.println(response);
  }
}
```

```ruby batches_list_example
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/batches")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php batches_list_example
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v2/batches', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp batches_list_example
using RestSharp;

var client = new RestClient("https://api.cohere.com/v2/batches");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift batches_list_example
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/batches")! as URL,
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