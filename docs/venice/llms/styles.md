# Source: https://docs.venice.ai/api-reference/endpoint/image/styles.md

# Image Styles

> List available image styles that can be used with the generate API.

## OpenAPI

````yaml GET /image/styles
paths:
  path: /image/styles
  method: get
  servers:
    - url: https://api.venice.ai/api/v1
  request:
    security:
      - title: ''
        parameters:
          query: {}
          header: {}
          cookie: {}
      - title: BearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body: {}
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: array
                    items:
                      type: string
                    description: List of available image styles
                    example:
                      - 3D Model
                      - Analog Film
                      - Anime
                      - Cinematic
                      - Comic Book
              object:
                allOf:
                  - type: string
                    enum:
                      - list
            requiredProperties:
              - data
              - object
        examples:
          example:
            value:
              data:
                - 3D Model
                - Analog Film
                - Anime
                - Cinematic
                - Comic Book
              object: list
        description: OK
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - &ref_0
                    type: string
                    description: A description of the error
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: &ref_1
              - error
        examples:
          example:
            value:
              error: <string>
        description: Authentication failed
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - *ref_0
            refIdentifier: '#/components/schemas/StandardError'
            requiredProperties: *ref_1
        examples:
          example:
            value:
              error: <string>
        description: An unknown error occurred
  deprecated: false
  type: path
components:
  schemas: {}

````