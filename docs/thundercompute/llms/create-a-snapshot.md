# Source: https://www.thundercompute.com/docs/api-reference/snapshots/create-a-snapshot.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.thundercompute.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a snapshot

> Create a new snapshot from a running instance



## OpenAPI

````yaml https://api.thundercompute.com:8443/openapi.json post /snapshots/create
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
  /snapshots/create:
    post:
      tags:
        - snapshots
      summary: Create a snapshot
      description: Create a new snapshot from a running instance
      requestBody:
        content:
          application/json:
            schema:
              oneOf:
                - type: object
                - $ref: '#/components/schemas/thundertypes.CreateSnapshotRequest'
                  summary: body
                  description: Snapshot creation request
        description: Snapshot creation request
        required: true
      responses:
        '202':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/thundertypes.CreateSnapshotResponse'
          description: Accepted
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
    thundertypes.CreateSnapshotRequest:
      properties:
        instanceId:
          type: string
        name:
          type: string
      required:
        - instanceId
        - name
      type: object
    thundertypes.CreateSnapshotResponse:
      properties:
        message:
          type: string
      required:
        - message
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