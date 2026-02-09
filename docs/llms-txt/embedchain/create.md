# Source: https://docs.embedchain.ai/examples/rest-api/create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.embedchain.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create app

> Create a new app using App ID

<RequestExample>
  ```bash Request theme={null}
  curl --request POST \
    --url http://localhost:8080/create?app_id=app1 \
    -F "config=@/path/to/config.yaml"
  ```
</RequestExample>

<ResponseExample>
  ```json Response theme={null}
  { "response": "App created successfully. App ID: app1" }
  ```
</ResponseExample>

By default we will use the opensource **gpt4all** model to get started. You can also specify your own config by uploading a config YAML file.

For example, create a `config.yaml` file (adjust according to your requirements):

```yaml  theme={null}
app:
  config:
    id: "default-app"

llm:
  provider: openai
  config:
    model: "gpt-4o-mini"
    temperature: 0.5
    max_tokens: 1000
    top_p: 1
    stream: false
    prompt: |
      Use the following pieces of context to answer the query at the end.
      If you don't know the answer, just say that you don't know, don't try to make up an answer.

      $context

      Query: $query

      Helpful Answer:

vectordb:
  provider: chroma
  config:
    collection_name: "rest-api-app"
    dir: db
    allow_reset: true

embedder:
  provider: openai
  config:
    model: "text-embedding-ada-002"
```

To learn more about custom configurations, check out the [custom configurations docs](https://docs.embedchain.ai/advanced/configuration). To explore more examples of config yamls for embedchain, visit [embedchain/configs](https://github.com/embedchain/embedchain/tree/main/configs).

Now, you can upload this config file in the request body.

For example,

```bash Request theme={null}
curl --request POST \
  --url http://localhost:8080/create?app_id=my-app \
  -F "config=@/path/to/config.yaml"
```

**Note:** To use custom models, an **API key** might be required. Refer to the table below to determine the necessary API key for your provider.

| Keys                       | Providers                      |
| -------------------------- | ------------------------------ |
| `OPENAI_API_KEY `          | OpenAI, Azure OpenAI, Jina etc |
| `OPENAI_API_TYPE`          | Azure OpenAI                   |
| `OPENAI_API_BASE`          | Azure OpenAI                   |
| `OPENAI_API_VERSION`       | Azure OpenAI                   |
| `COHERE_API_KEY`           | Cohere                         |
| `TOGETHER_API_KEY`         | Together                       |
| `ANTHROPIC_API_KEY`        | Anthropic                      |
| `JINACHAT_API_KEY`         | Jina                           |
| `HUGGINGFACE_ACCESS_TOKEN` | Huggingface                    |
| `REPLICATE_API_TOKEN`      | LLAMA2                         |

To add env variables, you can simply run the docker command with the `-e` flag.

For example,

```bash  theme={null}
docker run --name embedchain -p 8080:8080 -e OPENAI_API_KEY=<YOUR_OPENAI_API_KEY> embedchain/rest-api:latest
```


## OpenAPI

````yaml post /create
openapi: 3.1.0
info:
  title: Embedchain REST API
  description: This is the REST API for Embedchain.
  license:
    name: Apache 2.0
    url: https://github.com/embedchain/embedchain/blob/main/LICENSE
  version: 0.0.1
servers: []
security: []
paths:
  /create:
    post:
      tags:
        - Apps
      summary: Create app
      description: Create a new app using App ID
      operationId: create_app_using_default_config_create_post
      parameters:
        - name: app_id
          in: query
          required: true
          schema:
            type: string
            title: App Id
      requestBody:
        content:
          multipart/form-data:
            schema:
              allOf:
                - $ref: >-
                    #/components/schemas/Body_create_app_using_default_config_create_post
              title: Body
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DefaultResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_create_app_using_default_config_create_post:
      properties:
        config:
          type: string
          format: binary
          title: Config
      type: object
      title: Body_create_app_using_default_config_create_post
    DefaultResponse:
      properties:
        response:
          type: string
          title: Response
      type: object
      required:
        - response
      title: DefaultResponse
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````