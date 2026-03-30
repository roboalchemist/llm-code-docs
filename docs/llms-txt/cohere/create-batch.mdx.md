# Source: https://docs.cohere.com/reference/create-batch.mdx

# Create a batch

POST https://api.cohere.com/v2/batches
Content-Type: application/json

Creates and executes a batch from an uploaded dataset of requests

Reference: https://docs.cohere.com/reference/create-batch

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v2/batches:
    post:
      operationId: create
      summary: Create a batch
      description: Creates and executes a batch from an uploaded dataset of requests
      tags:
        - subpackage_batches
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
          description: A successful response.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateBatchResponse'
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
      requestBody:
        description: |-
          Information about the batch. Must contain name, input_dataset_id, and
          model. Output-only fields are ignored.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/Batch'
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
    CreateBatchResponse:
      type: object
      properties:
        batch:
          $ref: '#/components/schemas/Batch'
          description: Information about the batch.
      required:
        - batch
      description: Response to request to create a batch.
      title: CreateBatchResponse
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

batch_job = co.batches.create(
    name="<batch_job_name>",
    input_dataset_id="<input_dataset_id>",
    model="<model_name>",
)

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.batches.create(
    request={
        "name": "Customer Support Batch Q2",
        "input_dataset_id": "ds_8f7a6b3c9d2e4f1a",
        "model": "command-xlarge-nightly"
    }
)

```

```typescript Default
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const batchJob = await cohere.batches.create({
    name: '<my_job_name>',
    inputDatasetId: '<input_dataset_id>',
    model: '<model_name>',
  });

  console.log(batchJob);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.batches.create({
        name: "Customer Support Batch Q2",
        inputDatasetId: "ds_8f7a6b3c9d2e4f1a",
        model: "command-xlarge-nightly",
    });
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

	resp, err := co.Batches.Create(
		context.TODO(),
		&cohere.Batch{
			Name:           "<batch_job_name>",
			InputDatasetId: "<input_dataset_id>",
			Model:          "<model_name>",
		},
	)

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```java Default
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.batches.types.CreateBatchResponse;
import com.cohere.api.resources.batches.types.Batch;

public class BatchPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateBatchResponse response =
        cohere
            .batches()
            .create(
                Batch.builder()
                    .name("<batch_job_name>")
                    .inputDatasetId("<input_dataset_id>")
                    .model("<model_name>")
                    .build());

    System.out.println(response);
  }
}

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v2/batches")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"Customer Support Batch Q2\",\n  \"input_dataset_id\": \"ds_8f7a6b3c9d2e4f1a\",\n  \"model\": \"command-xlarge-nightly\"\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v2/batches', [
  'body' => '{
  "name": "Customer Support Batch Q2",
  "input_dataset_id": "ds_8f7a6b3c9d2e4f1a",
  "model": "command-xlarge-nightly"
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

var client = new RestClient("https://api.cohere.com/v2/batches");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"Customer Support Batch Q2\",\n  \"input_dataset_id\": \"ds_8f7a6b3c9d2e4f1a\",\n  \"model\": \"command-xlarge-nightly\"\n}", ParameterType.RequestBody);
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
  "name": "Customer Support Batch Q2",
  "input_dataset_id": "ds_8f7a6b3c9d2e4f1a",
  "model": "command-xlarge-nightly"
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v2/batches")! as URL,
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