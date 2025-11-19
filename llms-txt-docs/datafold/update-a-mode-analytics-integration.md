# Source: https://docs.datafold.com/api-reference/bi/update-a-mode-analytics-integration.md

# Update a Mode Analytics integration

> It can only update the schedule. Returns the integration with changed fields.

## OpenAPI

````yaml put /api/v1/lineage/bi/mode/{bi_datasource_id}/
paths:
  path: /api/v1/lineage/bi/mode/{bi_datasource_id}/
  method: put
  servers:
    - url: https://app.datafold.com
      description: Default server
  request:
    security:
      - title: ApiKeyAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: Use the 'Authorization' header with the format 'Key <api-key>'
          cookie: {}
    parameters:
      path:
        bi_datasource_id:
          schema:
            - type: integer
              required: true
              title: Mode integration id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              indexing_cron:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Indexing Cron
              name:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Name
              password:
                allOf:
                  - format: password
                    title: Password
                    type: string
                    writeOnly: true
              token:
                allOf:
                  - format: password
                    title: Token
                    type: string
                    writeOnly: true
              workspace:
                allOf:
                  - default: ''
                    title: Workspace
                    type: string
            required: true
            title: ModeDataSourceConfig
            refIdentifier: '#/components/schemas/ModeDataSourceConfig'
            requiredProperties:
              - token
              - password
        examples:
          example:
            value:
              indexing_cron: <string>
              name: <string>
              password: <string>
              token: <string>
              workspace: ''
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
                    title: Detail
                    type: array
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
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object

````