# Source: https://docs.cohere.com/reference/get-dataset.mdx

# Get a Dataset

GET https://api.cohere.com/v1/datasets/{id}

Retrieve a dataset by ID. See ['Datasets'](https://docs.cohere.com/docs/datasets) for more information.

Reference: https://docs.cohere.com/reference/get-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/datasets/{id}:
    get:
      operationId: get
      summary: Get a Dataset
      description: >-
        Retrieve a dataset by ID. See
        ['Datasets'](https://docs.cohere.com/docs/datasets) for more
        information.
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
                $ref: '#/components/schemas/datasets_get_Response_200'
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
                $ref: '#/components/schemas/Get-datasetRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestNotFoundError'
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
                  #/components/schemas/Get-datasetRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Get-datasetRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestServiceUnavailableError'
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Get-datasetRequestGatewayTimeoutError'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    DatasetType:
      type: string
      enum:
        - embed-input
        - embed-result
        - cluster-result
        - cluster-outliers
        - reranker-finetune-input
        - single-label-classification-finetune-input
        - chat-finetune-input
        - multi-label-classification-finetune-input
        - batch-chat-input
        - batch-openai-chat-input
        - batch-embed-v2-input
        - batch-chat-v2-input
      description: The type of the dataset
      title: DatasetType
    DatasetValidationStatus:
      type: string
      enum:
        - unknown
        - queued
        - processing
        - failed
        - validated
        - skipped
      description: The validation status of the dataset
      title: DatasetValidationStatus
    DatasetPart:
      type: object
      properties:
        id:
          type: string
          description: The dataset part ID
        name:
          type: string
          description: The name of the dataset part
        url:
          type: string
          description: The download url of the file
        index:
          type: integer
          description: The index of the file
        size_bytes:
          type: integer
          description: The size of the file in bytes
        num_rows:
          type: integer
          description: The number of rows in the file
        original_url:
          type: string
          description: The download url of the original file
        samples:
          type: array
          items:
            type: string
          description: The first few rows of the parsed file
      required:
        - id
        - name
      title: DatasetPart
    ParseInfo:
      type: object
      properties:
        separator:
          type: string
        delimiter:
          type: string
      title: ParseInfo
    RerankerDataMetrics:
      type: object
      properties:
        num_train_queries:
          type: integer
          format: int64
          description: The number of training queries.
        num_train_relevant_passages:
          type: integer
          format: int64
          description: The sum of all relevant passages of valid training examples.
        num_train_hard_negatives:
          type: integer
          format: int64
          description: The sum of all hard negatives of valid training examples.
        num_eval_queries:
          type: integer
          format: int64
          description: The number of evaluation queries.
        num_eval_relevant_passages:
          type: integer
          format: int64
          description: The sum of all relevant passages of valid eval examples.
        num_eval_hard_negatives:
          type: integer
          format: int64
          description: The sum of all hard negatives of valid eval examples.
      title: RerankerDataMetrics
    ChatDataMetrics:
      type: object
      properties:
        num_train_turns:
          type: integer
          format: int64
          description: The sum of all turns of valid train examples.
        num_eval_turns:
          type: integer
          format: int64
          description: The sum of all turns of valid eval examples.
        preamble:
          type: string
          description: The preamble of this dataset.
      title: ChatDataMetrics
    LabelMetric:
      type: object
      properties:
        total_examples:
          type: integer
          format: int64
          description: Total number of examples for this label
        label:
          type: string
          description: value of the label
        samples:
          type: array
          items:
            type: string
          description: samples for this label
      title: LabelMetric
    ClassifyDataMetrics:
      type: object
      properties:
        label_metrics:
          type: array
          items:
            $ref: '#/components/schemas/LabelMetric'
      title: ClassifyDataMetrics
    FinetuneDatasetMetrics:
      type: object
      properties:
        trainable_token_count:
          type: integer
          format: int64
          description: >-
            The number of tokens of valid examples that can be used for
            training.
        total_examples:
          type: integer
          format: int64
          description: The overall number of examples.
        train_examples:
          type: integer
          format: int64
          description: The number of training examples.
        train_size_bytes:
          type: integer
          format: int64
          description: The size in bytes of all training examples.
        eval_examples:
          type: integer
          format: int64
          description: Number of evaluation examples.
        eval_size_bytes:
          type: integer
          format: int64
          description: The size in bytes of all eval examples.
        reranker_data_metrics:
          $ref: '#/components/schemas/RerankerDataMetrics'
        chat_data_metrics:
          $ref: '#/components/schemas/ChatDataMetrics'
        classify_data_metrics:
          $ref: '#/components/schemas/ClassifyDataMetrics'
      title: FinetuneDatasetMetrics
    Metrics:
      type: object
      properties:
        finetune_dataset_metrics:
          $ref: '#/components/schemas/FinetuneDatasetMetrics'
      title: Metrics
    Dataset:
      type: object
      properties:
        id:
          type: string
          description: The dataset ID
        name:
          type: string
          description: The name of the dataset
        created_at:
          type: string
          format: date-time
          description: The creation date
        updated_at:
          type: string
          format: date-time
          description: The last update date
        dataset_type:
          $ref: '#/components/schemas/DatasetType'
        validation_status:
          $ref: '#/components/schemas/DatasetValidationStatus'
        validation_error:
          type: string
          description: Errors found during validation
        schema:
          type: string
          description: the avro schema of the dataset
        required_fields:
          type: array
          items:
            type: string
        preserve_fields:
          type: array
          items:
            type: string
        dataset_parts:
          type: array
          items:
            $ref: '#/components/schemas/DatasetPart'
          description: the underlying files that make up the dataset
        validation_warnings:
          type: array
          items:
            type: string
          description: warnings found during validation
        parse_info:
          $ref: '#/components/schemas/ParseInfo'
        metrics:
          $ref: '#/components/schemas/Metrics'
      required:
        - id
        - name
        - created_at
        - updated_at
        - dataset_type
        - validation_status
      title: Dataset
    datasets_get_Response_200:
      type: object
      properties:
        dataset:
          $ref: '#/components/schemas/Dataset'
      required:
        - dataset
      title: datasets_get_Response_200
    Get-datasetRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestBadRequestError
    Get-datasetRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestUnauthorizedError
    Get-datasetRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestForbiddenError
    Get-datasetRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestNotFoundError
    Get-datasetRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestUnprocessableEntityError
    Get-datasetRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestTooManyRequestsError
    Get-datasetRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestInvalidTokenError
    Get-datasetRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestClientClosedRequestError
    Get-datasetRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestInternalServerError
    Get-datasetRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestNotImplementedError
    Get-datasetRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestServiceUnavailableError
    Get-datasetRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Get-datasetRequestGatewayTimeoutError
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

	resp, err := co.Datasets.Get(context.TODO(), "dataset_id")

	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp)
}

```

```python Sync
import cohere

co = cohere.Client()

# get dataset
response = co.datasets.get(id="<<datasetId>>")

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.datasets.get(id="<<datasetId>>")

    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.datasets.get(
    id="id"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.types.DatasetsGetResponse;

public class DatasetGet {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsGetResponse response = cohere.datasets().get("dataset_id");

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const cohere = new CohereClient({});

(async () => {
  const datasets = await cohere.datasets.get('<<datasetId>>');

  console.log(datasets);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.datasets.get("id");
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets/id")

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

$response = $client->request('GET', 'https://api.cohere.com/v1/datasets/id', [
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

var client = new RestClient("https://api.cohere.com/v1/datasets/id");
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

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets/id")! as URL,
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