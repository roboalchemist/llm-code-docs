# Source: https://docs.comfy.org/api-reference/api-nodes/get-proxyvidutasks-creations.md

# Get proxyvidutasks creations

## OpenAPI

````yaml https://api.comfy.org/openapi get /proxy/vidu/tasks/{id}/creations
paths:
  path: /proxy/vidu/tasks/{id}/creations
  method: get
  servers:
    - url: https://api.comfy.org
  request:
    security: []
    parameters:
      path:
        id:
          schema:
            - type: string
              required: true
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
              creations:
                allOf:
                  - items:
                      $ref: '#/components/schemas/ViduCreation'
                    type: array
              err_code:
                allOf:
                  - type: string
              id:
                allOf:
                  - type: string
              state:
                allOf:
                  - $ref: '#/components/schemas/ViduState'
            refIdentifier: '#/components/schemas/ViduGetCreationsReply'
        examples:
          example:
            value:
              creations:
                - cover_url: <string>
                  id: <string>
                  moderation_url:
                    - <string>
                  url: <string>
                  watermarked_url: <string>
              err_code: <string>
              id: <string>
              state: created
        description: OK
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - &ref_0
                    description: >-
                      Optional detailed information about the error or hints for
                      resolving it.
                    items:
                      type: string
                    type: array
              message:
                allOf:
                  - &ref_1
                    description: A clear and concise description of the error.
                    type: string
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              details:
                - <string>
              message: <string>
        description: Error 4xx/5xx
    default:
      application/json:
        schemaArray:
          - type: object
            properties:
              details:
                allOf:
                  - *ref_0
              message:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/Error'
        examples:
          example:
            value:
              details:
                - <string>
              message: <string>
        description: Error 4xx/5xx
  deprecated: false
  type: path
components:
  schemas:
    ViduCreation:
      properties:
        cover_url:
          type: string
        id:
          type: string
        moderation_url:
          items:
            type: string
          type: array
        url:
          type: string
        watermarked_url:
          type: string
      type: object
    ViduState:
      enum:
        - created
        - processing
        - queueing
        - success
        - failed
      type: string

````