# Source: https://docs.unstructured.io/api-reference/sources/create-source-connection-check.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.unstructured.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Create source connection check

> Initiates a connection check for the specified source connector.



## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json post /api/v1/sources/{source_id}/connection-check
openapi: 3.1.0
info:
  title: Platform API
  version: 3.1.0
servers:
  - url: https://platform.unstructuredapp.io/
    description: Unstructured Platform API
    x-speakeasy-server-id: platform-api
security: []
paths:
  /api/v1/sources/{source_id}/connection-check:
    post:
      tags:
        - sources
      summary: Create source connection check
      description: Initiates a connection check for the specified source connector.
      operationId: create_connection_check_sources
      parameters:
        - name: source_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Source Id
        - name: unstructured-api-key
          in: header
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Unstructured-Api-Key
      responses:
        '202':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DagNodeConnectionCheck'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    DagNodeConnectionCheck:
      properties:
        id:
          type: string
          format: uuid
          title: Id
        status:
          $ref: '#/components/schemas/ConnectionCheckStatus'
        reason:
          anyOf:
            - type: string
            - type: 'null'
          title: Reason
        created_at:
          type: string
          format: date-time
          title: Created At
        reported_at:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Reported At
      type: object
      required:
        - id
        - status
        - created_at
      title: DagNodeConnectionCheck
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ConnectionCheckStatus:
      type: string
      enum:
        - SCHEDULED
        - SUCCESS
        - FAILURE
      title: ConnectionCheckStatus
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