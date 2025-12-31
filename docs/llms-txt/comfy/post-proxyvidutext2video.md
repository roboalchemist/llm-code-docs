# Source: https://docs.comfy.org/api-reference/api-nodes/post-proxyvidutext2video.md

# Post proxyvidutext2video

## OpenAPI

````yaml https://api.comfy.org/openapi post /proxy/vidu/text2video
paths:
  path: /proxy/vidu/text2video
  method: post
  servers:
    - url: https://api.comfy.org
  request:
    security: []
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
              aspect_ratio:
                allOf:
                  - type: string
              callback_url:
                allOf:
                  - type: string
              duration:
                allOf:
                  - format: int32
                    type: integer
              enhance:
                allOf:
                  - type: boolean
              images:
                allOf:
                  - items:
                      type: string
                    type: array
              model:
                allOf:
                  - type: string
              movement_amplitude:
                allOf:
                  - enum:
                      - auto
                      - small
                      - medium
                      - large
                    type: string
              priority:
                allOf:
                  - format: int32
                    type: integer
              prompt:
                allOf:
                  - type: string
              resolution:
                allOf:
                  - type: string
              seed:
                allOf:
                  - format: int32
                    type: integer
              style:
                allOf:
                  - enum:
                      - general
                      - anime
                    type: string
            required: true
            refIdentifier: '#/components/schemas/ViduTaskRequest'
        examples:
          example:
            value:
              aspect_ratio: <string>
              callback_url: <string>
              duration: 123
              enhance: true
              images:
                - <string>
              model: <string>
              movement_amplitude: auto
              priority: 123
              prompt: <string>
              resolution: <string>
              seed: 123
              style: general
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              aspect_ratio:
                allOf:
                  - type: string
              created_at:
                allOf:
                  - format: date-time
                    type: string
              credits:
                allOf:
                  - format: int32
                    type: integer
              duration:
                allOf:
                  - format: int32
                    type: integer
              images:
                allOf:
                  - items:
                      type: string
                    type: array
              model:
                allOf:
                  - type: string
              movement_amplitude:
                allOf:
                  - enum:
                      - auto
                      - small
                      - medium
                      - large
                    type: string
              prompt:
                allOf:
                  - type: string
              resolution:
                allOf:
                  - type: string
              seed:
                allOf:
                  - format: int32
                    type: integer
              state:
                allOf:
                  - $ref: '#/components/schemas/ViduState'
              style:
                allOf:
                  - enum:
                      - general
                      - anime
                    type: string
              task_id:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ViduTaskReply'
            requiredProperties:
              - task_id
              - state
              - credits
        examples:
          example:
            value:
              aspect_ratio: <string>
              created_at: '2023-11-07T05:31:56Z'
              credits: 123
              duration: 123
              images:
                - <string>
              model: <string>
              movement_amplitude: auto
              prompt: <string>
              resolution: <string>
              seed: 123
              state: created
              style: general
              task_id: <string>
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
    ViduState:
      enum:
        - created
        - processing
        - queueing
        - success
        - failed
      type: string

````