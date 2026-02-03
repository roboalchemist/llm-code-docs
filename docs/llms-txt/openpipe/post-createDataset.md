# Source: https://docs.openpipe.ai/api-reference/post-createDataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Dataset

> Create a new dataset.



## OpenAPI

````yaml post /datasets
openapi: 3.0.3
info:
  title: OpenPipe API
  description: The public API for reporting API calls to OpenPipe
  version: 0.1.1
servers:
  - url: https://api.openpipe.ai/api/v1
security: []
paths:
  /datasets:
    post:
      description: Create a new dataset.
      operationId: createDataset
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
              required:
                - name
              additionalProperties: false
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    enum:
                      - dataset
                  id:
                    type: string
                  name:
                    type: string
                  created:
                    type: string
                  updated:
                    type: string
                  dataset_entry_count:
                    type: number
                  fine_tune_count:
                    type: number
                required:
                  - object
                  - id
                  - name
                  - created
                  - updated
                  - dataset_entry_count
                  - fine_tune_count
                additionalProperties: false
        default:
          $ref: '#/components/responses/error'
      security:
        - Authorization: []
components:
  responses:
    error:
      description: Error response
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
              code:
                type: string
              issues:
                type: array
                items:
                  type: object
                  properties:
                    message:
                      type: string
                  required:
                    - message
                  additionalProperties: false
            required:
              - message
              - code
            additionalProperties: false
  securitySchemes:
    Authorization:
      type: http
      scheme: bearer

````