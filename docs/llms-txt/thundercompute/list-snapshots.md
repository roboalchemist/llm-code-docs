# Source: https://www.thundercompute.com/docs/api-reference/snapshots/list-snapshots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List snapshots

> Get a list of all snapshots for the authenticated user's organization



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json get /snapshots/list
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
  /snapshots/list:
    get:
      tags:
        - snapshots
      summary: List snapshots
      description: Get a list of all snapshots for the authenticated user's organization
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
                items:
                  $ref: '#/components/schemas/thundertypes.Snapshot'
                type: array
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
    thundertypes.Snapshot:
      properties:
        createdAt:
          type: integer
        id:
          type: string
        minimumDiskSizeGb:
          type: integer
        name:
          type: string
        status:
          type: string
      required:
        - createdAt
        - id
        - minimumDiskSizeGb
        - name
        - status
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