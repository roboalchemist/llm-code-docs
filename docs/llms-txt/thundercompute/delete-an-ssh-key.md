# Source: https://www.thundercompute.com/docs/api-reference/ssh-keys/delete-an-ssh-key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete an SSH key

> Delete an SSH key by ID



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json delete /keys/{id}
openapi: 3.1.0
info:
  contact:
    email: support@thundercompute.com
    name: Thunder Compute API Support
    url: https://thundercompute.com/support
  description: >-
    This is the Thunder Compute API server for managing compute resources and
    GPU workloads.
  license:
    name: Apache 2.0
    url: http://www.apache.org/licenses/LICENSE-2.0.html
  termsOfService: http://swagger.io/terms/
  title: Thunder Compute API
  version: '1.0'
servers:
  - description: Production server
    url: https://api.thundercompute.com:8443/v1
security: []
externalDocs:
  description: ''
  url: ''
paths:
  /keys/{id}:
    delete:
      tags:
        - ssh-keys
      summary: Delete an SSH key
      description: Delete an SSH key by ID
      parameters:
        - description: SSH Key ID
          in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              type: object
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.SSHKeyDeleteResponse'
          description: OK
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Unauthorized
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Internal Server Error
      security:
        - ApiKeyAuth: []
components:
  schemas:
    thundertypes.SSHKeyDeleteResponse:
      properties:
        message:
          type: string
      type: object
    thundertypes.ErrorResponse:
      properties:
        code:
          example: 400
          type: integer
        error:
          example: invalid_request
          type: string
        message:
          example: The request is malformed
          type: string
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: >-
        Bearer token authentication. Provide your API token prefixed with
        "Bearer ", e.g. "Bearer your-api-token".
      in: header
      name: Authorization
      type: apiKey

````