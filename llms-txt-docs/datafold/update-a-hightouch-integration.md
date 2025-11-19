# Source: https://docs.datafold.com/api-reference/bi/update-a-hightouch-integration.md

# Update a Hightouch integration

> It can only update the schedule. Returns the integration with changed fields.

## OpenAPI

````yaml put /api/v1/lineage/bi/hightouch/{bi_datasource_id}/
paths:
  path: /api/v1/lineage/bi/hightouch/{bi_datasource_id}/
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
              title: Hightouch integration id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              bindings:
                allOf:
                  - items:
                      $ref: '#/components/schemas/DataSourceBinding'
                    title: Bindings
                    type: array
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
              token:
                allOf:
                  - format: password
                    title: Token
                    type: string
                    writeOnly: true
              workspace:
                allOf:
                  - anyOf:
                      - type: string
                      - type: 'null'
                    title: Workspace
            required: true
            title: HighTouchDataSourceConfig
            refIdentifier: '#/components/schemas/HighTouchDataSourceConfig'
            requiredProperties:
              - token
              - bindings
        examples:
          example:
            value:
              bindings:
                - boundIds:
                    - 123
                  remoteId: <string>
              indexing_cron: <string>
              name: <string>
              token: <string>
              workspace: <string>
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
    DataSourceBinding:
      properties:
        boundIds:
          items:
            type: integer
          title: Boundids
          type: array
        remoteId:
          title: Remoteid
          type: string
      required:
        - remoteId
        - boundIds
      title: DataSourceBinding
      type: object
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