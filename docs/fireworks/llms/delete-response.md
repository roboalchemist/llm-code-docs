# Source: https://docs.fireworks.ai/api-reference/delete-response.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.fireworks.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Response

> Deletes a model response by its ID. Once deleted, the response data will be gone immediately and permanently.

The response cannot be recovered and any conversations that reference this response ID will no longer be able to access it.



## OpenAPI

````yaml delete /v1/responses/{response_id}
openapi: 3.1.0
info:
  title: Gateway REST API
  version: 4.21.6
servers: []
security: []
tags:
  - name: gateway.openapi_Gateway
    x-displayName: Gateway
  - name: gateway-extra.openapi_Gateway
    x-displayName: Gateway
  - name: responses.openapi_other
    x-displayName: other
  - name: text-completion.openapi_other
    x-displayName: other
paths:
  /v1/responses/{response_id}:
    servers:
      - url: https://api.fireworks.ai/inference
    delete:
      tags:
        - responses.openapi_other
      summary: Delete Response
      description: >-
        Deletes a model response by its ID. Once deleted, the response data will
        be gone immediately and permanently.


        The response cannot be recovered and any conversations that reference
        this response ID will no longer be able to access it.
      operationId: delete_response_v1_responses__response_id__delete
      parameters:
        - name: response_id
          in: path
          required: true
          schema:
            type: string
            description: The ID of the response to delete
            title: Response Id
          description: The ID of the response to delete
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DeleteResponse'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - BearerAuth: []
components:
  schemas:
    DeleteResponse:
      properties:
        message:
          type: string
          title: Message
          description: Confirmation message
          example: Response deleted successfully
      type: object
      required:
        - message
      title: DeleteResponse
      description: Response model for deleting a response.
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
    BearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        Bearer authentication using your Fireworks API key. Format: Bearer
        <API_KEY>

````