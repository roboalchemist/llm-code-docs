# Source: https://www.quo.com/docs/mdx/api-reference/webhooks/lists-all-webhooks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.quo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Lists all webhooks

> List all webhooks for a user.



## OpenAPI

````yaml https://openphone-public-api-prod.s3.us-west-2.amazonaws.com/public/openphone-public-api-v1-prod.json get /v1/webhooks
openapi: 3.1.0
info:
  title: OpenPhone Public API
  version: 1.0.0
  description: API for connecting with OpenPhone.
  contact:
    name: OpenPhone Support
    email: support@openphone.com
    url: https://support.openphone.com/hc/en-us
  termsOfService: https://www.openphone.com/terms
servers:
  - description: Production server
    url: https://api.openphone.com
security:
  - apiKey: []
tags:
  - description: Operations related to calls
    name: Calls
  - description: >-
      Operations related to call summaries, including AI-generated summaries and
      Sona voice assistant summaries
    name: Call Summaries
  - description: >-
      Operations related to call transcripts, including AI-generated transcripts
      and Sona voice assistant transcripts
    name: Call Transcripts
  - description: Operations related to contacts
    name: Contacts
  - description: Operations related to conversations
    name: Conversations
  - description: Operations related to text messages
    name: Messages
  - description: Operations related to phone numbers
    name: Phone Numbers
  - description: Operations related to users
    name: Users
  - description: Operations related to webhooks
    name: Webhooks
paths:
  /v1/webhooks:
    get:
      tags:
        - Webhooks
      summary: Lists all webhooks
      description: List all webhooks for a user.
      operationId: listWebhooks_v1
      parameters:
        - in: query
          name: userId
          required: false
          schema:
            description: The unique identifier the user. Defaults to the workspace owner.
            examples: U55wgP5I5
            pattern: ^US(.*)$
            type: string
      responses:
        '200':
          description: Success
          content:
            application/json:
              schema:
                type: object
                properties:
                  data:
                    type: array
                    items:
                      anyOf:
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
                                The unique identifier of the user that created
                                the webhook.
                              examples:
                                - US123abc
                              pattern: ^US(.*)$
                              type: string
                            orgId:
                              description: >-
                                The unique identifier of the organization the
                                webhook belongs to
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
                              description: >-
                                The endpoint that receives events from the
                                webhook.
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
                                    The date the webhook was deleted at, in
                                    ISO_8601 format.
                                  examples:
                                    - '2022-01-01T00:00:00Z'
                                  format: date-time
                                  type: string
                                - type: 'null'
                            events:
                              type: array
                              items:
                                type: string
                                enum:
                                  - message.received
                                  - message.delivered
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
                                The unique identifier of the user that created
                                the webhook.
                              examples:
                                - US123abc
                              pattern: ^US(.*)$
                              type: string
                            orgId:
                              description: >-
                                The unique identifier of the organization the
                                webhook belongs to
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
                              description: >-
                                The endpoint that receives events from the
                                webhook.
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
                                    The date the webhook was deleted at, in
                                    ISO_8601 format.
                                  examples:
                                    - '2022-01-01T00:00:00Z'
                                  format: date-time
                                  type: string
                                - type: 'null'
                            events:
                              type: array
                              items:
                                type: string
                                enum:
                                  - call.completed
                                  - call.ringing
                                  - call.recording.completed
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
                                The unique identifier of the user that created
                                the webhook.
                              examples:
                                - US123abc
                              pattern: ^US(.*)$
                              type: string
                            orgId:
                              description: >-
                                The unique identifier of the organization the
                                webhook belongs to
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
                              description: >-
                                The endpoint that receives events from the
                                webhook.
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
                                    The date the webhook was deleted at, in
                                    ISO_8601 format.
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
                                  - call.summary.completed
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
                                The unique identifier of the user that created
                                the webhook.
                              examples:
                                - US123abc
                              pattern: ^US(.*)$
                              type: string
                            orgId:
                              description: >-
                                The unique identifier of the organization the
                                webhook belongs to
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
                              description: >-
                                The endpoint that receives events from the
                                webhook.
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
                                    The date the webhook was deleted at, in
                                    ISO_8601 format.
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
                required:
                  - data
        '400':
          description: Invalid Version
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0305400'
                    type: string
                  status:
                    const: 400
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Invalid Version
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                    const: Invalid Version
                    type: string
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
                  - description
        '401':
          description: Unauthorized
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0300401'
                    type: string
                  status:
                    const: 401
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unauthorized
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '403':
          description: Forbidden
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0300403'
                    type: string
                  status:
                    const: 403
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Forbidden
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0300404'
                    type: string
                  status:
                    const: 404
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Not Found
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
        '500':
          description: Unknown Error
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                  code:
                    const: '0301500'
                    type: string
                  status:
                    const: 500
                    type: number
                  docs:
                    const: https://openphone.com/docs
                    type: string
                  title:
                    const: Unknown
                    type: string
                  trace:
                    type: string
                  errors:
                    type: array
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
                required:
                  - message
                  - code
                  - status
                  - docs
                  - title
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      in: header
      name: Authorization
      type: apiKey

````