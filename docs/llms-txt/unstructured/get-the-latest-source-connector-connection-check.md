# Source: https://docs.unstructured.io/api-reference/sources/get-the-latest-source-connector-connection-check.md

# Get the latest source connector connection check

> Retrieves the most recent connection check for the specified source connector.

## OpenAPI

````yaml https://platform.unstructuredapp.io/openapi.json get /api/v1/sources/{source_id}/connection-check
paths:
  path: /api/v1/sources/{source_id}/connection-check
  method: get
  servers:
    - url: https://platform.unstructuredapp.io/
      description: Unstructured Platform API
  request:
    security:
      - title: HTTPBearer
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path:
        source_id:
          schema:
            - type: string
              required: true
              title: Source Id
              format: uuid
      query: {}
      header:
        unstructured-api-key:
          schema:
            - type: string
              required: false
              title: Unstructured-Api-Key
            - type: 'null'
              required: false
              title: Unstructured-Api-Key
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              id:
                allOf:
                  - type: string
                    format: uuid
                    title: Id
              status:
                allOf:
                  - $ref: '#/components/schemas/ConnectionCheckStatus'
              reason:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Reason
              created_at:
                allOf:
                  - type: string
                    format: date-time
                    title: Created At
              reported_at:
                allOf:
                  - anyOf:
                      - type: string
                        format: date-time
                      - type: 'null'
                    title: Reported At
            title: DagNodeConnectionCheck
            refIdentifier: '#/components/schemas/DagNodeConnectionCheck'
            requiredProperties:
              - id
              - status
              - created_at
        examples:
          example:
            value:
              id: 3c90c3cc-0d44-4b50-8888-8dd25736052a
              status: SCHEDULED
              reason: <string>
              created_at: '2023-11-07T05:31:56Z'
              reported_at: '2023-11-07T05:31:56Z'
        description: Successful Response
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              detail:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ValidationError'
                    type: array
                    title: Detail
            title: HTTPValidationError
            refIdentifier: '#/components/schemas/HTTPValidationError'
        examples:
          example:
            value:
              detail:
                - loc:
                    - <string>
                  msg: <string>
                  type: <string>
        description: Validation Error
  deprecated: false
  type: path
components:
  schemas:
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