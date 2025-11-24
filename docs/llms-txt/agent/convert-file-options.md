# Source: https://docs.agent.ai/api-reference/advanced/convert-file-options.md

# Convert file options

> Gets the full set of options that a file extension can be converted to.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/convert_file_options
paths:
  path: /action/convert_file_options
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
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
              extension:
                allOf:
                  - type: string
                    description: File extension
                    example: txt
            required: true
            requiredProperties:
              - extension
        examples:
          example:
            value:
              extension: txt
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                - doc
                - docx
                - html
                - md
                - odt
                - pdf
                - rtf
                - tex
                - azw3
                - epub
                - lrf
                - mobi
                - oeb
                - pdb
                - jpg
                - png
        description: Convert file options
  deprecated: false
  type: path
components:
  schemas: {}

````