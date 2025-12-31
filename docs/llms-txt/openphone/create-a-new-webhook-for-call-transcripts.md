# Source: https://www.quo.com/docs/mdx/api-reference/webhooks/create-a-new-webhook-for-call-transcripts.md

# Create a new webhook for call transcripts

> Creates a new webhook that triggers on events from call transcripts.

## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json post /v1/webhooks/call-transcripts
paths:
  path: /v1/webhooks/call-transcripts
  method: post
  servers:
    - url: https://api.openphone.com
      description: Production server
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
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
              events:
                allOf:
                  - minItems: 1
                    type: array
                    items:
                      type: string
                      enum:
                        - call.transcript.completed
              label:
                allOf:
                  - description: The webhook's label.
                    examples:
                      - my webhook label
                    type: string
              resourceIds:
                allOf:
                  - anyOf:
                      - type: array
                        items:
                          pattern: ^PN(.*)$
                          type: string
                      - type: array
                        items:
                          const: '*'
                          type: string
              status:
                allOf:
                  - type: string
                    enum:
                      - enabled
                      - disabled
                    description: The status of the webhook.
                    examples:
                      - enabled
              url:
                allOf:
                  - format: uri
                    description: The endpoint that receives events from the webhook.
                    examples:
                      - https://example.com
                    type: string
              userId:
                allOf:
                  - description: >-
                      The ID of the user that creates the webhook. If not
                      provided, default to workspace owner.
                    examples:
                      - US123abc
                    pattern: ^US(.*)$
                    type: string
            required: true
            requiredProperties:
              - events
              - url
        examples:
          example:
            value:
              events:
                - call.transcript.completed
              label: my webhook label
              resourceIds:
                - <string>
              status: enabled
              url: https://example.com
              userId: US123abc
  response:
    '201':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - type: object
                    properties:
                      id:
                        description: The webhook's ID
                        examples:
                          - WHabcd1234
                        pattern: ^WH(.*)$
                        type: string
                      userId:
                        description: >-
                          The unique identifier of the user that created the
                          webhook.
                        examples:
                          - US123abc
                        pattern: ^US(.*)$
                        type: string
                      orgId:
                        description: >-
                          The unique identifier of the organization the webhook
                          belongs to
                        examples:
                          - OR1223abc
                        pattern: ^OR(.*)$
                        type: string
                      label:
                        anyOf:
                          - description: The webhook's label.
                            examples:
                              - my webhook label
                            type: string
                          - type: 'null'
                      status:
                        type: string
                        enum:
                          - enabled
                          - disabled
                        default: enabled
                        description: The status of the webhook.
                        examples:
                          - enabled
                      url:
                        format: uri
                        description: The endpoint that receives events from the webhook.
                        examples:
                          - https://example.com/
                        type: string
                      key:
                        description: Webhook key
                        examples:
                          - example-key
                        type: string
                      createdAt:
                        description: >-
                          The date the webhook was created at, in ISO_8601
                          format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      updatedAt:
                        description: >-
                          The date the webhook was created at, in ISO_8601
                          format.
                        examples:
                          - '2022-01-01T00:00:00Z'
                        format: date-time
                        type: string
                      deletedAt:
                        anyOf:
                          - description: >-
                              The date the webhook was deleted at, in ISO_8601
                              format.
                            examples:
                              - '2022-01-01T00:00:00Z'
                            format: date-time
                            type: string
                          - type: 'null'
                      events:
                        minItems: 1
                        type: array
                        items:
                          type: string
                          enum:
                            - call.transcript.completed
                      resourceIds:
                        anyOf:
                          - type: array
                            items:
                              pattern: ^PN(.*)$
                              type: string
                          - type: array
                            items:
                              const: '*'
                              type: string
                    required:
                      - id
                      - userId
                      - orgId
                      - label
                      - status
                      - url
                      - key
                      - createdAt
                      - updatedAt
                      - deletedAt
                      - events
                      - resourceIds
            requiredProperties:
              - data
        examples:
          example:
            value:
              data:
                id: WHabcd1234
                userId: US123abc
                orgId: OR1223abc
                label: my webhook label
                status: enabled
                url: https://example.com/
                key: example-key
                createdAt: '2022-01-01T00:00:00Z'
                updatedAt: '2022-01-01T00:00:00Z'
                deletedAt: '2022-01-01T00:00:00Z'
                events:
                  - call.transcript.completed
                resourceIds:
                  - <string>
        description: Success
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0305400'
                    type: string
              status:
                allOf:
                  - const: 400
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Invalid Version
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
              description:
                allOf:
                  - const: Invalid Version
                    type: string
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
              - description
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
              description: <string>
        description: Invalid Version
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0300401'
                    type: string
              status:
                allOf:
                  - const: 401
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unauthorized
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unauthorized
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0300403'
                    type: string
              status:
                allOf:
                  - const: 403
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Forbidden
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Forbidden
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0300404'
                    type: string
              status:
                allOf:
                  - const: 404
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Not Found
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Not Found
    '500':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
              code:
                allOf:
                  - const: '0301500'
                    type: string
              status:
                allOf:
                  - const: 500
                    type: number
              docs:
                allOf:
                  - const: https://openphone.com/docs
                    type: string
              title:
                allOf:
                  - const: Unknown
                    type: string
              trace:
                allOf:
                  - type: string
              errors:
                allOf:
                  - type: array
                    items:
                      type: object
                      properties:
                        path:
                          type: string
                        message:
                          type: string
                        value: {}
                        schema:
                          type: object
                          properties:
                            type:
                              type: string
                          required:
                            - type
                      required:
                        - path
                        - message
                        - schema
            requiredProperties:
              - message
              - code
              - status
              - docs
              - title
        examples:
          example:
            value:
              message: <string>
              code: <string>
              status: 123
              docs: <string>
              title: <string>
              trace: <string>
              errors:
                - path: <string>
                  message: <string>
                  value: <any>
                  schema:
                    type: <string>
        description: Unknown Error
  deprecated: false
  type: path
components:
  schemas: {}

````