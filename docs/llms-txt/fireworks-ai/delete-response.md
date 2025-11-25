# Source: https://docs.fireworks.ai/api-reference/delete-response.md

# Delete Response

> Deletes a model response by its ID. Once deleted, the response data will be gone immediately and permanently.

The response cannot be recovered and any conversations that reference this response ID will no longer be able to access it.

## OpenAPI

````yaml delete /v1/responses/{response_id}
paths:
  path: /v1/responses/{response_id}
  method: delete
  servers:
    - url: https://api.fireworks.ai/inference
  request:
    security:
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer authentication using your Fireworks API key. Format:
                Bearer <API_KEY>
          cookie: {}
    parameters:
      path:
        response_id:
          schema:
            - type: string
              required: true
              title: Response Id
              description: The ID of the response to delete
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    title: Message
                    description: Confirmation message
                    example: Response deleted successfully
            title: DeleteResponse
            description: Response model for deleting a response.
            refIdentifier: '#/components/schemas/DeleteResponse'
            requiredProperties:
              - message
        examples:
          example:
            value:
              message: Response deleted successfully
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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