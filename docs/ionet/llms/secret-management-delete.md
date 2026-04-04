# Source: https://io.net/docs/reference/ai-agents/secret-management-delete.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete a Secret

> Deletes an existing secret and its associated configuration.

This endpoint allows you to permanently remove a registered secret from storage, revoking access for any tool previously authorized to use it. Once deleted, the secret and its associations cannot be recovered.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>


## OpenAPI

````yaml openapi/ai-agents/secret-management-delete.json delete /api/v1/secrets/{secret_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/v1/secrets/{secret_id}:
    delete:
      tags:
        - agents
      summary: Delete Secret
      operationId: delete_secret_v1_secrets__secret_id__delete
      parameters:
        - name: secret_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Secret Id
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
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
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````