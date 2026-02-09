# Source: https://docs.argil.ai/api-reference/endpoint/videos.delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.argil.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Video by id

> Delete a single Video identified by its id



## OpenAPI

````yaml delete /videos/{id}
openapi: 3.0.1
info:
  title: Argil API
  description: API for AI clone video generation
  version: 1.0.0
  license:
    name: MIT
servers:
  - url: https://api.argil.ai/v1
security:
  - ApiKeyAuth: []
paths:
  /videos/{id}:
    delete:
      summary: Delete a Video by id
      description: Delete a single Video identified by its id
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            description: The id of the Video to delete
      responses:
        '200':
          description: Success message.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Success'
        '404':
          description: Video not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Success:
      type: object
      properties:
        message:
          type: string
    Error:
      type: object
      properties:
        code:
          type: integer
          format: int32
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: x-api-key
      description: API key to be included in the x-api-key header

````