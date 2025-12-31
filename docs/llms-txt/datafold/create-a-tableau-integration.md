# Source: https://docs.datafold.com/api-reference/bi/create-a-tableau-integration.md

# Create a Tableau integration

## OpenAPI

````yaml post /api/v1/lineage/bi/tableau/
paths:
  path: /api/v1/lineage/bi/tableau/
  method: post
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
      path: {}
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
              server_url:
                allOf:
                  - title: Server Url
                    type: string
              site_id:
                allOf:
                  - title: Site Id
                    type: string
              token_name:
                allOf:
                  - title: Token Name
                    type: string
              token_value:
                allOf:
                  - format: password
                    title: Token Value
                    type: string
                    writeOnly: true
            required: true
            title: TableauDataSourceConfig
            refIdentifier: '#/components/schemas/TableauDataSourceConfig'
            requiredProperties:
              - token_name
              - token_value
              - site_id
              - server_url
        examples:
          example:
            value:
              indexing_cron: <string>
              name: <string>
              server_url: <string>
              site_id: <string>
              token_name: <string>
              token_value: <string>
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