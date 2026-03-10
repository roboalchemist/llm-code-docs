# Source: https://docs.cohere.com/reference/createfinetunedmodel.mdx

# Trains and deploys a fine-tuned model.

POST https://api.cohere.com/v1/finetuning/finetuned-models
Content-Type: application/json

Creates a new fine-tuned model. The model will be trained on the dataset specified in the request body. The training process may take some time, and the model will be available once the training is complete.

Reference: https://docs.cohere.com/reference/createfinetunedmodel

## OpenAPI Specification

```yaml
openapi: 3.1.0
info:
  title: v2
  version: 1.0.0
paths:
  /v1/finetuning/finetuned-models:
    post:
      operationId: create-finetuned-model
      summary: Trains and deploys a fine-tuned model.
      description: >-
        Creates a new fine-tuned model. The model will be trained on the dataset
        specified in the request body. The training process may take some time,
        and the model will be available once the training is complete.
      tags:
        - subpackage_finetuning
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
                $ref: '#/components/schemas/CreateFinetunedModelResponse'
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
      requestBody:
        description: >-
          Information about the fine-tuned model. Must contain name and
          settings.
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FinetunedModel'
servers:
  - url: https://api.cohere.com
components:
  schemas:
    BaseType:
      type: string
      enum:
        - BASE_TYPE_UNSPECIFIED
        - BASE_TYPE_GENERATIVE
        - BASE_TYPE_CLASSIFICATION
        - BASE_TYPE_RERANK
        - BASE_TYPE_CHAT
      default: BASE_TYPE_UNSPECIFIED
      description: |-
        The possible types of fine-tuned models.

         - BASE_TYPE_UNSPECIFIED: Unspecified model.
         - BASE_TYPE_GENERATIVE: Deprecated: Generative model.
         - BASE_TYPE_CLASSIFICATION: Classification model.
         - BASE_TYPE_RERANK: Rerank model.
         - BASE_TYPE_CHAT: Chat model.
      title: BaseType
    Strategy:
      type: string
      enum:
        - STRATEGY_UNSPECIFIED
        - STRATEGY_VANILLA
        - STRATEGY_TFEW
      default: STRATEGY_UNSPECIFIED
      description: |-
        The possible strategy used to serve a fine-tuned models.

         - STRATEGY_UNSPECIFIED: Unspecified strategy.
         - STRATEGY_VANILLA: Deprecated: Serve the fine-tuned model on a dedicated GPU.
         - STRATEGY_TFEW: Deprecated: Serve the fine-tuned model on a shared GPU.
      title: Strategy
    BaseModel:
      type: object
      properties:
        name:
          type: string
          description: The name of the base model.
        version:
          type: string
          description: read-only. The version of the base model.
        base_type:
          $ref: '#/components/schemas/BaseType'
          description: The type of the base model.
        strategy:
          $ref: '#/components/schemas/Strategy'
          description: 'Deprecated: The fine-tuning strategy.'
      required:
        - base_type
      description: The base model used for fine-tuning.
      title: BaseModel
    LoraTargetModules:
      type: string
      enum:
        - LORA_TARGET_MODULES_UNSPECIFIED
        - LORA_TARGET_MODULES_QV
        - LORA_TARGET_MODULES_QKVO
        - LORA_TARGET_MODULES_QKVO_FFN
      default: LORA_TARGET_MODULES_UNSPECIFIED
      description: |-
        The possible combinations of LoRA modules to target.

         - LORA_TARGET_MODULES_UNSPECIFIED: Unspecified LoRA target modules.
         - LORA_TARGET_MODULES_QV: LoRA adapts the query and value matrices in transformer attention layers.
         - LORA_TARGET_MODULES_QKVO: LoRA adapts query, key, value, and output matrices in attention layers.
         - LORA_TARGET_MODULES_QKVO_FFN: LoRA adapts attention projection matrices and feed-forward networks (FFN).
      title: LoraTargetModules
    Hyperparameters:
      type: object
      properties:
        early_stopping_patience:
          type: integer
          description: >-
            Stops training if the loss metric does not improve beyond the value
            of

            `early_stopping_threshold` after this many times of evaluation.
        early_stopping_threshold:
          type: number
          format: double
          description: How much the loss must improve to prevent early stopping.
        train_batch_size:
          type: integer
          description: >-
            The batch size is the number of training examples included in a
            single

            training pass.
        train_epochs:
          type: integer
          description: The number of epochs to train for.
        learning_rate:
          type: number
          format: double
          description: The learning rate to be used during training.
        lora_alpha:
          type: integer
          description: |-
            Controls the scaling factor for LoRA updates. Higher values make the
            updates more impactful.
        lora_rank:
          type: integer
          description: >-
            Specifies the rank for low-rank matrices. Lower ranks reduce
            parameters

            but may limit model flexibility.
        lora_target_modules:
          $ref: '#/components/schemas/LoraTargetModules'
          description: The combination of LoRA modules to target.
      description: The fine-tuning hyperparameters.
      title: Hyperparameters
    WandbConfig:
      type: object
      properties:
        project:
          type: string
          description: The WandB project name to be used during training.
        api_key:
          type: string
          description: The WandB API key to be used during training.
        entity:
          type: string
          description: The WandB entity name to be used during training.
      required:
        - project
        - api_key
      description: The Weights & Biases configuration.
      title: WandbConfig
    Settings:
      type: object
      properties:
        base_model:
          $ref: '#/components/schemas/BaseModel'
          description: The base model to fine-tune.
        dataset_id:
          type: string
          description: The data used for training and evaluating the fine-tuned model.
        hyperparameters:
          $ref: '#/components/schemas/Hyperparameters'
          description: Fine-tuning hyper-parameters.
        multi_label:
          type: boolean
          description: >-
            read-only. Whether the model is single-label or multi-label (only
            for classification).
        wandb:
          $ref: '#/components/schemas/WandbConfig'
          description: The Weights & Biases configuration (Chat fine-tuning only).
      required:
        - base_model
        - dataset_id
      description: The configuration used for fine-tuning.
      title: Settings
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
    FinetunedModel:
      type: object
      properties:
        id:
          type: string
          description: read-only. FinetunedModel ID.
        name:
          type: string
          description: FinetunedModel name (e.g. `foobar`).
        creator_id:
          type: string
          description: read-only. User ID of the creator.
        organization_id:
          type: string
          description: read-only. Organization ID.
        settings:
          $ref: '#/components/schemas/Settings'
          description: FinetunedModel settings such as dataset, hyperparameters...
        status:
          $ref: '#/components/schemas/Status'
          description: read-only. Current stage in the life-cycle of the fine-tuned model.
        created_at:
          type: string
          format: date-time
          description: read-only. Creation timestamp.
        updated_at:
          type: string
          format: date-time
          description: read-only. Latest update timestamp.
        completed_at:
          type: string
          format: date-time
          description: read-only. Timestamp for the completed fine-tuning.
        last_used:
          type: string
          format: date-time
          description: >-
            read-only. Deprecated: Timestamp for the latest request to this
            fine-tuned model.
      required:
        - name
        - settings
      description: This resource represents a fine-tuned model.
      title: FinetunedModel
    CreateFinetunedModelResponse:
      type: object
      properties:
        finetuned_model:
          $ref: '#/components/schemas/FinetunedModel'
          description: Information about the fine-tuned model.
      description: Response to request to create a fine-tuned model.
      title: CreateFinetunedModelResponse
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
import com.cohere.api.resources.finetuning.finetuning.types.*;

public class CreateFinetunedModel {
  public static void main(String[] args) {
    Cohere cohere = Cohere.builder().clientName("snippet").build();

    CreateFinetunedModelResponse response =
        cohere
            .finetuning()
            .createFinetunedModel(
                FinetunedModel.builder()
                    .name("test-finetuned-model")
                    .settings(
                        Settings.builder()
                            .baseModel(
                                BaseModel.builder().baseType(BaseType.BASE_TYPE_CHAT).build())
                            .datasetId("my-dataset-id")
                            .build())
                    .build());

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
	"github.com/cohere-ai/cohere-go/v2/finetuning"
)

func main() {
	co := client.NewClient(client.WithToken(os.Getenv("CO_API_KEY")))

	resp, err := co.Finetuning.CreateFinetunedModel(
		context.TODO(),
		&finetuning.FinetunedModel{
			Name: "test-finetuned-model",
			Settings: &finetuning.Settings{
				DatasetId: "my-dataset-id",
				BaseModel: &finetuning.BaseModel{
					BaseType: finetuning.BaseTypeBaseTypeChat,
				},
			},
		},
	)
	if err != nil {
		log.Fatal(err)
	}

	log.Printf("%+v", resp.FinetunedModel)
}

```

```typescript Cohere TypeScript SDK
const { Cohere, CohereClient } = require('cohere-ai');

const cohere = new CohereClient({
  token: '<<apiKey>>',
});

(async () => {
  const finetunedModel = await cohere.finetuning.createFinetunedModel({
    name: 'test-finetuned-model',
    settings: {
      base_model: {
        base_type: Cohere.Finetuning.BaseType.BaseTypeChat,
      },
      dataset_id: 'test-dataset-id',
    },
  });

  console.log(finetunedModel);
})();

```

```typescript
import { CohereClient } from "cohere-ai";

async function main() {
    const client = new CohereClient({
        token: "YOUR_TOKEN_HERE",
    });
    await client.finetuning.createFinetunedModel({
        name: "customer-support-chatbot-v1",
        settings: {
            baseModel: {
                baseType: "BASE_TYPE_CHAT",
            },
            datasetId: "customer-support-dataset-2024",
        },
    });
}
main();

```

```python Sync
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Hyperparameters,
    Settings,
    WandbConfig,
)
import cohere

co = cohere.Client()
hp = Hyperparameters(
    early_stopping_patience=10,
    early_stopping_threshold=0.001,
    train_batch_size=16,
    train_epochs=1,
    learning_rate=0.01,
)
wnb_config = WandbConfig(
    project="test-project",
    api_key="<<wandbApiKey>>",
    entity="test-entity",
)
finetuned_model = co.finetuning.create_finetuned_model(
    request=FinetunedModel(
        name="test-finetuned-model",
        settings=Settings(
            base_model=BaseModel(
                base_type="BASE_TYPE_CHAT",
            ),
            dataset_id="my-dataset-id",
            hyperparameters=hp,
            wandb=wnb_config,
        ),
    )
)
print(finetuned_model)

```

```python Async
from cohere.finetuning import (
    BaseModel,
    FinetunedModel,
    Settings,
)
import cohere
import asyncio

co = cohere.AsyncClient()


async def main():
    response = await co.finetuning.create_finetuned_model(
        request=FinetunedModel(
            name="test-finetuned-model",
            settings=Settings(
                base_model=BaseModel(
                    base_type="BASE_TYPE_CHAT",
                ),
                dataset_id="my-dataset-id",
            ),
        )
    )
    print(response)


asyncio.run(main())

```

```python
from cohere import Client

client = Client(
    token="YOUR_TOKEN_HERE"
)

client.finetuning.create_finetuned_model(
    request={
        "name": "customer-support-chatbot-v1",
        "settings": {
            "base_model": {
                "base_type": "BASE_TYPE_CHAT"
            },
            "dataset_id": "customer-support-dataset-2024"
        }
    }
)

```

```ruby
require 'uri'
require 'net/http'

url = URI("https://api.cohere.com/v1/finetuning/finetuned-models")

http = Net::HTTP.new(url.host, url.port)
http.use_ssl = true

request = Net::HTTP::Post.new(url)
request["X-Client-Name"] = 'my-cool-project'
request["Authorization"] = 'Bearer <token>'
request["Content-Type"] = 'application/json'
request.body = "{\n  \"name\": \"customer-support-chatbot-v1\",\n  \"settings\": {\n    \"base_model\": {\n      \"base_type\": \"BASE_TYPE_CHAT\"\n    },\n    \"dataset_id\": \"customer-support-dataset-2024\"\n  }\n}"

response = http.request(request)
puts response.read_body
```

```php
<?php
require_once('vendor/autoload.php');

$client = new \GuzzleHttp\Client();

$response = $client->request('POST', 'https://api.cohere.com/v1/finetuning/finetuned-models', [
  'body' => '{
  "name": "customer-support-chatbot-v1",
  "settings": {
    "base_model": {
      "base_type": "BASE_TYPE_CHAT"
    },
    "dataset_id": "customer-support-dataset-2024"
  }
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

var client = new RestClient("https://api.cohere.com/v1/finetuning/finetuned-models");
var request = new RestRequest(Method.POST);
request.AddHeader("X-Client-Name", "my-cool-project");
request.AddHeader("Authorization", "Bearer <token>");
request.AddHeader("Content-Type", "application/json");
request.AddParameter("application/json", "{\n  \"name\": \"customer-support-chatbot-v1\",\n  \"settings\": {\n    \"base_model\": {\n      \"base_type\": \"BASE_TYPE_CHAT\"\n    },\n    \"dataset_id\": \"customer-support-dataset-2024\"\n  }\n}", ParameterType.RequestBody);
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
  "name": "customer-support-chatbot-v1",
  "settings": [
    "base_model": ["base_type": "BASE_TYPE_CHAT"],
    "dataset_id": "customer-support-dataset-2024"
  ]
] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.cohere.com/v1/finetuning/finetuned-models")! as URL,
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