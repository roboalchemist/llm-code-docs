# Source: https://docs.infera.org/api-reference/endpoint/get-unique-nodes.md

# Get Unique Nodes

## OpenAPI

````yaml get /unique_nodes
paths:
  path: /unique_nodes
  method: get
  servers:
    - url: https://api.infera.org/
      description: Infera production servers
  request:
    security: []
    parameters:
      path: {}
      query:
        model_name:
          schema:
            - type: string
              required: true
              title: Model Name
        start_date:
          schema:
            - type: string
              required: false
              title: Start Date
              description: Start date for the range (ISO format)
              format: date-time
            - type: 'null'
              required: false
              title: Start Date
              description: Start date for the range (ISO format)
        end_date:
          schema:
            - type: string
              required: false
              title: End Date
              description: End date for the range (ISO format)
              format: date-time
            - type: 'null'
              required: false
              title: End Date
              description: End date for the range (ISO format)
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: any
        examples:
          example:
            value: <any>
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