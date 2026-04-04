# Source: https://docs.cohere.com/reference/create-dataset.mdx

# Create a Dataset

POST https://api.cohere.com/v1/datasets
Content-Type: multipart/form-data

Create a dataset by uploading a file. See ['Dataset Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for more information.

Reference: https://docs.cohere.com/reference/create-dataset

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/datasets:
    post:
      operationId: create
      summary: Create a Dataset
      description: >-
        Create a dataset by uploading a file. See ['Dataset
        Creation'](https://docs.cohere.com/docs/datasets#dataset-creation) for
        more information.
      tags:
        - subpackage_datasets
      parameters:
        - name: name
          in: query
          description: The name of the uploaded dataset.
          required: true
          schema:
            type: string
        - name: type
          in: query
          description: >-
            The dataset type, which is used to validate the data. The only valid
            type is `embed-input` used in conjunction with the Embed Jobs API.
          required: true
          schema:
            $ref: '#/components/schemas/DatasetType'
        - name: keep_original_file
          in: query
          description: Indicates if the original file should be stored.
          required: false
          schema:
            type: boolean
        - name: skip_malformed_input
          in: query
          description: >-
            Indicates whether rows with malformed input should be dropped
            (instead of failing the validation check). Dropped rows will be
            returned in the warnings field.
          required: false
          schema:
            type: boolean
        - name: keep_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `keep_fields` are missing from the uploaded file, Dataset validation
            will fail.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: optional_fields
          in: query
          description: >-
            List of names of fields that will be persisted in the Dataset. By
            default the Dataset will retain only the required fields indicated
            in the [schema for the corresponding Dataset
            type](https://docs.cohere.com/docs/datasets#dataset-types). For
            example, Datasets of type `embed-input` will drop all fields other
            than the required `text` field. If any of the fields in
            `optional_fields` are missing from the uploaded file, Dataset
            validation will pass.
          required: false
          schema:
            type: array
            items:
              type: string
        - name: text_separator
          in: query
          description: >-
            Raw .txt uploads will be split into entries using the text_separator
            value.
          required: false
          schema:
            type: string
        - name: csv_delimiter
          in: query
          description: The delimiter used for .csv uploads.
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
                $ref: '#/components/schemas/datasets_create_Response_200'
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
                $ref: '#/components/schemas/Create-datasetRequestBadRequestError'
        '401':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestUnauthorizedError'
        '403':
          description: >
            This error indicates that the operation attempted to be performed is
            not allowed. This could be because:
              - The api token is invalid
              - The user does not have the necessary permissions
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestForbiddenError'
        '404':
          description: >
            This error is returned when a resource is not found. This could be
            because:
              - The endpoint does not exist
              - The resource does not exist eg model id, dataset id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestNotFoundError'
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
                  #/components/schemas/Create-datasetRequestUnprocessableEntityError
        '429':
          description: Too many requests
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestTooManyRequestsError'
        '498':
          description: >
            This error is returned when a request or response contains a
            deny-listed token.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestInvalidTokenError'
        '499':
          description: |
            This error is returned when a request is cancelled by the user.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-datasetRequestClientClosedRequestError
        '500':
          description: >
            This error is returned when an uncategorised internal server error
            occurs.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestInternalServerError'
        '501':
          description: >
            This error is returned when the requested feature is not
            implemented.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestNotImplementedError'
        '503':
          description: >
            This error is returned when the service is unavailable. This could
            be due to:
              - Too many users trying to access the service at the same time
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Create-datasetRequestServiceUnavailableError
        '504':
          description: >
            This error is returned when a request to the server times out. This
            could be due to:
              - An internal services taking too long to respond
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Create-datasetRequestGatewayTimeoutError'
      requestBody:
        content:
          multipart/form-data:
            schema:
              type: object
              properties:
                data:
                  type: string
                  format: binary
                  description: The file to upload
                eval_data:
                  type: string
                  format: binary
                  description: An optional evaluation file to upload
              required:
                - data
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
    datasets_create_Response_200:
      type: object
      properties:
        id:
          type: string
          description: The dataset ID
      title: datasets_create_Response_200
    Create-datasetRequestBadRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestBadRequestError
    Create-datasetRequestUnauthorizedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestUnauthorizedError
    Create-datasetRequestForbiddenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestForbiddenError
    Create-datasetRequestNotFoundError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestNotFoundError
    Create-datasetRequestUnprocessableEntityError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestUnprocessableEntityError
    Create-datasetRequestTooManyRequestsError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestTooManyRequestsError
    Create-datasetRequestInvalidTokenError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestInvalidTokenError
    Create-datasetRequestClientClosedRequestError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestClientClosedRequestError
    Create-datasetRequestInternalServerError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestInternalServerError
    Create-datasetRequestNotImplementedError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestNotImplementedError
    Create-datasetRequestServiceUnavailableError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestServiceUnavailableError
    Create-datasetRequestGatewayTimeoutError:
      type: object
      properties:
        message:
          type: string
        id:
          type: string
      title: Create-datasetRequestGatewayTimeoutError
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
	"io"
	"log"
	"os"
	"strings"

	cohere "github.com/cohere-ai/cohere-go/v2"
	client "github.com/cohere-ai/cohere-go/v2/client"
)

type MyReader struct {
	io.Reader
	name string
}

func (m *MyReader) Name() string {
	return m.name
}

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Datasets.Create(
		context.TODO(),
		&cohere.DatasetsCreateRequest{
			Name:     "embed-dataset",
			Type:     cohere.DatasetTypeEmbedInput,
			Data:     &MyReader{Reader: strings.NewReader(`{"text": "The quick brown fox jumps over the lazy dog"}`), name: "test.jsonl"},
			EvalData: &MyReader{Reader: strings.NewReader(""), name: "a.jsonl"},
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

# upload a dataset
my_dataset = co.datasets.create(
    name="embed-dataset",
    data=open("./embed.jsonl", "rb"),
    type="embed-input",
)

# wait for validation to complete
response = co.wait(my_dataset)

print(response)

```

```python Async
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    # upload a dataset
    response = await co.datasets.create(
        name="embed-dataset",
        data=open("./embed.jsonl", "rb"),
        type="embed-input",
    )

    # wait for validation to complete
    response = await co.wait(response)

    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.datasets.create(
    name="name",
    type="embed-input",
    data="example_data",
    eval_data="example_eval_data"
)

```

```java Cohere java SDK
/* (C)2024 */
import com.cohere.api.Cohere;
import com.cohere.api.resources.datasets.requests.DatasetsCreateRequest;
import com.cohere.api.resources.datasets.types.DatasetsCreateResponse;
import com.cohere.api.types.DatasetType;
import java.util.Optional;

public class DatasetPost {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    DatasetsCreateResponse response =
        cohere
            .datasets()
            .create(
                null,
                Optional.empty(),
                DatasetsCreateRequest.builder()
                    .name("embed-dataset")
                    .type(DatasetType.EMBED_INPUT)
                    .build());

    System.out.println(response);
  }
}

```

```typescript Cohere TypeScript SDK
import { CohereClient } from 'cohere-ai';

const fs = require('fs');

const cohere = new CohereClient({});

(async () => {
  const file = fs.createReadStream('embed_jobs_sample_data.jsonl'); // {"text": "The quick brown fox jumps over the lazy dog"}

  const dataset = await cohere.datasets.create({ name: 'my-dataset', type: 'embed-input' }, file);

  console.log(dataset);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.datasets.create(, , {
        name: "name",
        type: "embed-input",
    });
}
main();

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/datasets?name=name&type=embed-input")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'multipart/form-data; boundary=---011000010111000001101001'
request.body = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"; filename=\"embed_dataset.jsonl\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"eval_data\"; filename=\"eval_dataset.jsonl\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/datasets?name=name&type=embed-input', [
  'multipart' => [
    [
        'name' => 'data',
        'filename' => 'embed_dataset.jsonl',
        'contents' => null
    ],
    [
        'name' => 'eval_data',
        'filename' => 'eval_dataset.jsonl',
        'contents' => null
    ]
  ]
  'headers' => [
    'Authorization' => 'Bearer <token>',
    'X-Client-Name' => 'my-cool-project',
  ],
]);

echo $response->getBody();
```

```csharp
using RestSharp;

var client = new RestClient("https://api.cohere.com/v1/datasets?name=name&type=embed-input");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddParameter("multipart/form-data; boundary=---011000010111000001101001", "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"data\"; filename=\"embed_dataset.jsonl\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"eval_data\"; filename=\"eval_dataset.jsonl\"\r\nContent-Type: application/octet-stream\r\n\r\n\r\n-----011000010111000001101001--\r\n", ParameterType.RequestBody);
IRestResponse response = client.Execute(request);
```

```swift
import Foundation

let headers = [
  "X-Client-Name": "my-cool-project",
  "Authorization": "Bearer <token>",
  "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"
]
let parameters = [
  [
    "name": "data",
    "fileName": "embed_dataset.jsonl"
  ],
  [
    "name": "eval_data",
    "fileName": "eval_dataset.jsonl"
  ]
]

let boundary = "---011000010111000001101001"

var body = ""
var error: NSError? = nil
for param in parameters {
  let paramName = param["name"]!
  body += "--\(boundary)\r\n"
  body += "Content-Disposition:form-data; name=\"\(paramName)\""
  if let filename = param["fileName"] {
    let contentType = param["content-type"]!
    let fileContent = String(contentsOfFile: filename, encoding: String.Encoding.utf8)
    if (error != nil) {
      print(error as Any)
    }
    body += "; filename=\"\(filename)\"\r\n"
    body += "Content-Type: \(contentType)\r\n\r\n"
    body += fileContent
  } else if let paramValue = param["value"] {
    body += "\r\n\r\n\(paramValue)"
  }
}

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/datasets?name=name&type=embed-input")! as URL,
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