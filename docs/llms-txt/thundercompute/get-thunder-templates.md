# Source: https://www.thundercompute.com/docs/api-reference/utilities/get-thunder-templates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get thunder templates

> Get available thunder templates for instance creation



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json get /thunder-templates
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
  /thunder-templates:
    get:
      tags:
        - utilities
      summary: Get thunder templates
      description: Get available thunder templates for instance creation
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
                $ref: '#/components/schemas/thundertypes.ThunderTemplatesResponse'
          description: OK
        '500':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.ErrorResponse'
          description: Internal Server Error
components:
  schemas:
    thundertypes.ThunderTemplatesResponse:
      additionalProperties:
        $ref: '#/components/schemas/thundertypes.EnvironmentTemplate'
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
    thundertypes.EnvironmentTemplate:
      properties:
        automountFolders:
          items:
            type: string
          type: array
          uniqueItems: false
        cleanupCommands:
          items:
            type: string
          type: array
          uniqueItems: false
        default:
          type: boolean
        defaultSpecs:
          $ref: '#/components/schemas/thundertypes.TemplateDefaultSpecs'
        displayName:
          type: string
        extendedDescription:
          type: string
        openPorts:
          items:
            type: integer
          type: array
          uniqueItems: false
        startupCommands:
          items:
            type: string
          type: array
          uniqueItems: false
        startupMinutes:
          type: integer
        version:
          type: integer
      type: object
    thundertypes.TemplateDefaultSpecs:
      properties:
        cores:
          type: integer
        gpu_type:
          type: string
        num_gpus:
          type: integer
        storage:
          type: integer
        template:
          type: string
      type: object

````