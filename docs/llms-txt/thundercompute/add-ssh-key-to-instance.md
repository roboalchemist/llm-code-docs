# Source: https://www.thundercompute.com/docs/api-reference/instances/add-ssh-key-to-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Add SSH key to instance

> Add an SSH key to an existing instance. If public_key is provided in the request body, it will be added to authorized_keys. If no public_key is provided, a new key pair will be generated and the private key returned.



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json post /instances/{id}/add_key
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
  /instances/{id}/add_key:
    post:
      tags:
        - instances
      summary: Add SSH key to instance
      description: >-
        Add an SSH key to an existing instance. If public_key is provided in the
        request body, it will be added to authorized_keys. If no public_key is
        provided, a new key pair will be generated and the private key returned.
      parameters:
        - description: Instance ID
          in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                - $ref: '#/components/schemas/thundertypes.InstanceAddKeyRequest'
                  summary: request
                  description: 'Optional: provide an existing public key to add'
        description: 'Optional: provide an existing public key to add'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.InstanceAddKeyResponse'
          description: OK
        '400':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Bad Request
        '401':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Unauthorized
        '404':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Not Found
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
    thundertypes.InstanceAddKeyRequest:
      properties:
        public_key:
          description: 'Optional: existing public key to add'
          type: string
      type: object
    thundertypes.InstanceAddKeyResponse:
      properties:
        key:
          description: Private key (only when generated)
          type: string
        message:
          description: Status message
          type: string
        success:
          description: Whether the key was successfully added
          type: boolean
        uuid:
          type: string
      required:
        - success
        - uuid
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