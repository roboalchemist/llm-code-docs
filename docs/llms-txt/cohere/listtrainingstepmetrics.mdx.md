# Source: https://docs.cohere.com/reference/listtrainingstepmetrics.mdx

# Retrieve training metrics for fine-tuned models.

GET https://api.cohere.com/v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics

Returns a list of metrics measured during the training of a fine-tuned model.
The metrics are ordered by step number, with the most recent step first.
The list can be paginated using `page_size` and `page_token` parameters.

Reference: https://docs.cohere.com/reference/listtrainingstepmetrics

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/finetuning/finetuned-models/{finetuned_model_id}/training-step-metrics:
    get:
      operationId: list-training-step-metrics
      summary: Retrieve training metrics for fine-tuned models.
      description: >-
        Returns a list of metrics measured during the training of a fine-tuned
        model.

        The metrics are ordered by step number, with the most recent step first.

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
                $ref: '#/components/schemas/ListTrainingStepMetricsResponse'
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
    TrainingStepMetrics:
      type: object
      properties:
        created_at:
          type: string
          format: date-time
          description: Creation timestamp.
        step_number:
          type: integer
          description: Step number.
        metrics:
          type: object
          additionalProperties:
            type: number
            format: double
          description: Map of names and values for each evaluation metrics.
      description: >-
        The evaluation metrics at a given step of the training of a fine-tuned
        model.
      title: TrainingStepMetrics
    ListTrainingStepMetricsResponse:
      type: object
      properties:
        step_metrics:
          type: array
          items:
            $ref: '#/components/schemas/TrainingStepMetrics'
          description: The metrics for each step the evaluation was run on.
        next_page_token:
          type: string
          description: >-
            Pagination token to retrieve the next page of results. If the value
            is "",

            it means no further results for the request.
      description: >-
        Response to a request to list training-step metrics of a fine-tuned
        model.
      title: ListTrainingStepMetricsResponse
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
import com.cohere.api.resources.finetuning.finetuning.types.ListTrainingStepMetricsResponse;

public class ListTrainingStepMetrics {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    ListTrainingStepMetricsResponse response =
        cohere.finetuning().listTrainingStepMetrics("test-id");

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

	resp, err := co.Finetuning.ListTrainingStepMetrics(
		context.TODO(),
		"test-finetuned-model-id",
		nil,
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.StepMetrics)
}

```

```typescript Cohere TypeScript SDK
const { CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const trainingStepMetrics = await cohere.finetuning.listTrainingStepMetrics(
    'test-finetuned-model-id'
  );

  console.log(trainingStepMetrics);
})();

```

```typescript /finetuning_ListTrainingStepMetrics_example
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.finetuning.listTrainingStepMetrics("finetuned_model_id", {});
}
main();

```

```python Sync
import cohere

co = cohere.Client()
train_step_metrics = co.finetuning.list_training_step_metrics(
    finetuned_model_id="test-id"
)
print(train_step_metrics)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.list_train_step_metrics(finetuned_model_id="test-id")
    print(response)


asyncio.run(main())

```

```python /finetuning_ListTrainingStepMetrics_example
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.finetuning.list_training_step_metrics(
    finetuned_model_id="finetuned_model_id"
)

```

```ruby /finetuning_ListTrainingStepMetrics_example
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Get.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'

response = http.request(request)
puts response.read_body
```

```php /finetuning_ListTrainingStepMetrics_example
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('GET', 'https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics', [
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp /finetuning_ListTrainingStepMetrics_example
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics");
var request = new RestRequest(Method.GET);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
IRestResponse response = client.Execute(request);
```

```swift /finetuning_ListTrainingStepMetrics_example
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>"
]

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models/finetuned_model_id/training-step-metrics")! as URL,
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