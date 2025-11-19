# Source: https://dev.writer.com/api-reference/completion-api/list-models.md

# List models

> Retrieve a list of available models that can be used for text generation, chat completions, and other AI tasks.

## OpenAPI

````yaml get /v1/models
paths:
  path: /v1/models
  method: get
  servers:
    - url: https://api.writer.com
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication header of the form `Bearer <token>`, where
                `<token>` is your [Writer API
                key](https://dev.writer.com/api-reference/api-keys).
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: cURL
        source: |-
          curl --location --request GET https://api.writer.com/v1/models \
           --header "Authorization: Bearer <token>"
      - lang: JavaScript
        source: |-
          import Writer from 'writer-sdk';

          const client = new Writer({
            apiKey: process.env['WRITER_API_KEY'], // This is the default and can be omitted
          });

          async function main() {
            const model = await client.models.list();

            console.log(model.models);
          }

          main();
      - lang: Python
        source: |-
          import os
          from writerai import Writer

          client = Writer(
              # This is the default and can be omitted
              api_key=os.environ.get("WRITER_API_KEY"),
          )
          model = client.models.list()
          print(model.models)
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              models:
                allOf:
                  - type: array
                    description: >-
                      The [ID of the model](https://dev.writer.com/home/models)
                      to use for processing the request.
                    items:
                      $ref: '#/components/schemas/model_info'
            refIdentifier: '#/components/schemas/models_response'
            requiredProperties:
              - models
            example:
              models:
                - name: Palmyra X 003 Instruct
                  id: palmyra-x-003-instruct
                - name: Palmyra Med
                  id: palmyra-med
                - name: Palmyra Financial
                  id: palmyra-fin
                - name: Palmyra X4
                  id: palmyra-x4
                - name: Palmyra X5
                  id: palmyra-x5
                - name: Palmyra Creative
                  id: palmyra-creative
        examples:
          example:
            value:
              models:
                - name: Palmyra X 003 Instruct
                  id: palmyra-x-003-instruct
                - name: Palmyra Med
                  id: palmyra-med
                - name: Palmyra Financial
                  id: palmyra-fin
                - name: Palmyra X4
                  id: palmyra-x4
                - name: Palmyra X5
                  id: palmyra-x5
                - name: Palmyra Creative
                  id: palmyra-creative
        description: Successful response
  deprecated: false
  type: path
  xMcp: &ref_0
    enabled: true
    name: list-models
    description: Get a list of available Writer AI models
  xMint:
    mcp: *ref_0
components:
  schemas:
    model_info:
      required:
        - name
        - id
      type: object
      properties:
        name:
          type: string
          description: The name of the particular LLM that you want to use.
        id:
          type: string
          description: The ID of the particular LLM that you want to use

````