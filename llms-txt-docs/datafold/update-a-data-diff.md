# Source: https://docs.datafold.com/api-reference/data-diffs/update-a-data-diff.md

# Update a data diff

## OpenAPI

````yaml patch /api/v1/datadiffs/{datadiff_id}
paths:
  path: /api/v1/datadiffs/{datadiff_id}
  method: patch
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
        datadiff_id:
          schema:
            - type: integer
              required: true
              title: Data diff id
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              archived:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Archived
              purged:
                allOf:
                  - anyOf:
                      - type: boolean
                      - type: 'null'
                    title: Purged
            title: Body_update_datadiff_api_v1_datadiffs__datadiff_id__patch
            refIdentifier: >-
              #/components/schemas/Body_update_datadiff_api_v1_datadiffs__datadiff_id__patch
        examples:
          example:
            value:
              archived: true
              purged: true
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