# Source: https://www.thundercompute.com/docs/api-reference/instances/modify-instance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Modify instance

> Modify a running compute instance's resources



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json post /instances/{id}/modify
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
  /instances/{id}/modify:
    post:
      tags:
        - instances
      summary: Modify instance
      description: Modify a running compute instance's resources
      parameters:
        - description: Instance ID (index)
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
                - $ref: '#/components/schemas/thundertypes.InstanceModifyRequest'
                  summary: request
                  description: Instance modification parameters
        description: Instance modification parameters
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.InstanceModifyResponse'
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
    thundertypes.InstanceModifyRequest:
      properties:
        add_ports:
          items:
            type: integer
          type: array
          uniqueItems: false
        cpu_cores:
          type: integer
        disk_size_gb:
          type: integer
        gpu_type:
          type: string
        mode:
          $ref: '#/components/schemas/thundertypes.InstanceMode'
        num_gpus:
          type: integer
        remove_ports:
          items:
            type: integer
          type: array
          uniqueItems: false
      type: object
    thundertypes.InstanceModifyResponse:
      properties:
        gpu_type:
          type: string
        http_ports:
          items:
            type: integer
          type: array
          uniqueItems: false
        identifier:
          type: string
        instance_name:
          type: string
        mode:
          type: string
        num_gpus:
          type: integer
      required:
        - identifier
        - instance_name
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