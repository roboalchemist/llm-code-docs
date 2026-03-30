# Source: https://www.thundercompute.com/docs/api-reference/instances/list-instances.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List instances

> Get a list of user's compute instances



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json get /instances/list
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
  /instances/list:
    get:
      tags:
        - instances
      summary: List instances
      description: Get a list of user's compute instances
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
                $ref: '#/components/schemas/thundertypes.InstanceListResponse'
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
    thundertypes.InstanceListResponse:
      additionalProperties:
        $ref: '#/components/schemas/thundertypes.InstanceListItem'
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
    thundertypes.InstanceListItem:
      properties:
        cpuCores:
          type: string
        createdAt:
          type: string
        gpuType:
          type: string
        httpPorts:
          items:
            type: integer
          type: array
          uniqueItems: false
        id:
          description: Populated from map key by client
          type: string
        ip:
          type: string
        k8s:
          type: boolean
        memory:
          type: string
        mode:
          type: string
        name:
          type: string
        numGpus:
          type: string
        port:
          type: integer
        promoted:
          type: boolean
        provisioningTime:
          type: string
        restoringTime:
          type: string
        snapshotSize:
          type: integer
        sshPublicKeys:
          items:
            type: string
          type: array
          uniqueItems: false
        status:
          type: string
        storage:
          type: integer
        template:
          type: string
        uuid:
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