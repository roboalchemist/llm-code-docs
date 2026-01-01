# Source: https://docs.together.ai/reference/deleteendpoint.md

# Delete Endpoint

> Permanently deletes an endpoint. This action cannot be undone.



## OpenAPI

````yaml DELETE /endpoints/{endpointId}
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /endpoints/{endpointId}:
    delete:
      tags:
        - Endpoints
      summary: Delete endpoint
      description: Permanently deletes an endpoint. This action cannot be undone.
      operationId: deleteEndpoint
      parameters:
        - name: endpointId
          in: path
          required: true
          schema:
            type: string
          description: The ID of the endpoint to delete
          example: endpoint-d23901de-ef8f-44bf-b3e7-de9c1ca8f2d7
      responses:
        '204':
          description: No Content - Endpoint successfully deleted
        '403':
          description: Unauthorized
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt