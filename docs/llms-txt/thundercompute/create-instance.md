# Source: https://www.thundercompute.com/docs/api-reference/instances/create-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create instance

> Create a new compute instance



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json post /instances/create
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
  /instances/create:
    post:
      tags:
        - instances
      summary: Create instance
      description: Create a new compute instance
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                - $ref: '#/components/schemas/thundertypes.InstanceCreateRequest'
                  summary: request
                  description: Instance creation parameters
        description: Instance creation parameters
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.InstanceCreateResponse'
          description: Created
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
    thundertypes.InstanceCreateRequest:
      properties:
        cpu_cores:
          example: 4
          type: integer
        disk_size_gb:
          example: 100
          type: integer
        gpu_type:
          example: H100
          type: string
        mode:
          $ref: '#/components/schemas/thundertypes.InstanceMode'
        num_gpus:
          example: 1
          type: integer
        public_key:
          type: string
        template:
          example: ubuntu-22.04
          type: string
      required:
        - cpu_cores
        - disk_size_gb
        - gpu_type
        - mode
        - num_gpus
        - template
      type: object
    thundertypes.InstanceCreateResponse:
      properties:
        identifier:
          type: integer
        key:
          type: string
        uuid:
          type: string
      required:
        - identifier
        - key
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
    thundertypes.InstanceMode:
      enum:
        - prototyping
        - production
      type: string
      x-enum-varnames:
        - InstanceMode_Prototyping
        - InstanceMode_Production
  securitySchemes:
    ApiKeyAuth:
      description: >-
        Bearer token authentication. Provide your API token prefixed with
        "Bearer ", e.g. "Bearer your-api-token".
      in: header
      name: Authorization
      type: apiKey

````