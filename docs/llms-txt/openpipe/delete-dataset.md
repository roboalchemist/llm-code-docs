# Source: https://docs.openpipe.ai/api-reference/delete-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Dataset

> Delete a dataset.



## OpenAPI

````yaml delete /datasets/{datasetId}
openapi: 3.0.3
info:
  title: OpenPipe API
  description: The public API for reporting API calls to OpenPipe
  version: 0.1.1
servers:
  - url: https://api.openpipe.ai/api/v1
security: []
paths:
  /datasets/{datasetId}:
    delete:
      description: Delete a dataset.
      operationId: deleteDataset
      parameters:
        - name: datasetId
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  id:
                    type: string
                  object:
                    type: string
                    enum:
                      - dataset
                  deleted:
                    type: boolean
                required:
                  - id
                  - object
                  - deleted
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