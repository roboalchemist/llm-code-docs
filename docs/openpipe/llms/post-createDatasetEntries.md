# Source: https://docs.openpipe.ai/api-reference/post-createDatasetEntries.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add Entries to Dataset

> Add new dataset entries.



## OpenAPI

````yaml post /datasets/{datasetId}/entries
openapi: 3.0.3
info:
  title: OpenPipe API
  description: The public API for reporting API calls to OpenPipe
  version: 0.1.1
servers:
  - url: https://api.openpipe.ai/api/v1
security: []
paths:
  /datasets/{datasetId}/entries:
    post:
      description: Add new dataset entries.
      operationId: createDatasetEntries
      parameters:
        - name: datasetId
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                entries:
                  type: array
                  items:
                    type: object
                    properties:
                      messages:
                        type: array
                        items:
                          anyOf:
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - system
                                content:
                                  anyOf:
                                    - type: string
                                    - type: array
                                      items:
                                        type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - text
                                          text:
                                            type: string
                                        required:
                                          - type
                                          - text
                                        additionalProperties: false
                                  default: ''
                                name:
                                  type: string
                              required:
                                - role
                              additionalProperties: false
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - user
                                content:
                                  anyOf:
                                    - type: string
                                    - type: array
                                      items:
                                        anyOf:
                                          - type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - text
                                              text:
                                                type: string
                                            required:
                                              - type
                                              - text
                                            additionalProperties: false
                                          - type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - image_url
                                              image_url:
                                                type: object
                                                properties:
                                                  detail:
                                                    anyOf:
                                                      - type: string
                                                        enum:
                                                          - auto
                                                      - type: string
                                                        enum:
                                                          - low
                                                      - type: string
                                                        enum:
                                                          - high
                                                  url:
                                                    type: string
                                                required:
                                                  - url
                                                additionalProperties: false
                                            required:
                                              - type
                                              - image_url
                                            additionalProperties: false
                                          - type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - input_audio
                                              input_audio:
                                                type: object
                                                properties:
                                                  data:
                                                    type: string
                                                  format:
                                                    type: string
                                                    enum:
                                                      - wav
                                                      - mp3
                                                required:
                                                  - data
                                                  - format
                                                additionalProperties: false
                                            required:
                                              - type
                                              - input_audio
                                            additionalProperties: false
                                  default: ''
                                name:
                                  type: string
                              required:
                                - role
                              additionalProperties: false
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - assistant
                                audio:
                                  type: object
                                  properties:
                                    id:
                                      type: string
                                  required:
                                    - id
                                  additionalProperties: false
                                  nullable: true
                                content:
                                  anyOf:
                                    - type: string
                                    - type: array
                                      items:
                                        anyOf:
                                          - type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - text
                                              text:
                                                type: string
                                            required:
                                              - type
                                              - text
                                            additionalProperties: false
                                          - type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - refusal
                                              refusal:
                                                type: string
                                            required:
                                              - type
                                              - refusal
                                            additionalProperties: false
                                    - enum:
                                        - 'null'
                                      nullable: true
                                  default: null
                                function_call:
                                  type: object
                                  properties:
                                    name:
                                      type: string
                                      default: ''
                                    arguments:
                                      type: string
                                      default: ''
                                  additionalProperties: false
                                  nullable: true
                                tool_calls:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      id:
                                        type: string
                                      function:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                          arguments:
                                            type: string
                                        required:
                                          - name
                                          - arguments
                                        additionalProperties: false
                                      type:
                                        type: string
                                        enum:
                                          - function
                                    required:
                                      - id
                                      - function
                                      - type
                                    additionalProperties: false
                                  nullable: true
                                name:
                                  type: string
                                refusal:
                                  type: string
                                  nullable: true
                                annotations:
                                  type: array
                                  items:
                                    type: object
                                    properties:
                                      type:
                                        type: string
                                        enum:
                                          - url_citation
                                      url_citation:
                                        type: object
                                        properties:
                                          start_index:
                                            type: number
                                          end_index:
                                            type: number
                                          title:
                                            type: string
                                          url:
                                            type: string
                                        required:
                                          - start_index
                                          - end_index
                                          - title
                                          - url
                                        additionalProperties: false
                                    required:
                                      - type
                                      - url_citation
                                    additionalProperties: false
                              required:
                                - role
                              additionalProperties: false
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - developer
                                content:
                                  anyOf:
                                    - type: string
                                    - type: array
                                      items:
                                        type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - text
                                          text:
                                            type: string
                                        required:
                                          - type
                                          - text
                                        additionalProperties: false
                                  default: ''
                                name:
                                  type: string
                              required:
                                - role
                              additionalProperties: false
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - tool
                                content:
                                  anyOf:
                                    - type: string
                                    - type: array
                                      items:
                                        type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - text
                                          text:
                                            type: string
                                        required:
                                          - type
                                          - text
                                        additionalProperties: false
                                  default: ''
                                tool_call_id:
                                  type: string
                              required:
                                - role
                                - tool_call_id
                              additionalProperties: false
                            - type: object
                              properties:
                                role:
                                  type: string
                                  enum:
                                    - function
                                name:
                                  type: string
                                content:
                                  anyOf:
                                    - type: string
                                    - enum:
                                        - 'null'
                                      nullable: true
                              required:
                                - role
                                - name
                                - content
                              additionalProperties: false
                      rejected_message:
                        type: object
                        properties:
                          reasoning_content:
                            type: string
                            nullable: true
                          content:
                            type: string
                            nullable: true
                            default: null
                          refusal:
                            type: string
                            nullable: true
                          role:
                            type: string
                            enum:
                              - assistant
                          function_call:
                            type: object
                            properties:
                              name:
                                type: string
                                default: ''
                              arguments:
                                type: string
                                default: ''
                            additionalProperties: false
                            nullable: true
                          tool_calls:
                            type: array
                            items:
                              type: object
                              properties:
                                id:
                                  type: string
                                function:
                                  type: object
                                  properties:
                                    name:
                                      type: string
                                    arguments:
                                      type: string
                                  required:
                                    - name
                                    - arguments
                                  additionalProperties: false
                                type:
                                  type: string
                                  enum:
                                    - function
                              required:
                                - id
                                - function
                                - type
                              additionalProperties: false
                            nullable: true
                        required:
                          - role
                        additionalProperties: false
                      tool_choice:
                        anyOf:
                          - type: string
                            enum:
                              - none
                          - type: string
                            enum:
                              - auto
                          - type: string
                            enum:
                              - required
                          - type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - function
                                default: function
                              function:
                                type: object
                                properties:
                                  name:
                                    type: string
                                required:
                                  - name
                                additionalProperties: false
                                default:
                                  name: ''
                            additionalProperties: false
                      tools:
                        type: array
                        items:
                          type: object
                          properties:
                            function:
                              type: object
                              properties:
                                name:
                                  type: string
                                parameters:
                                  type: object
                                  additionalProperties: {}
                                description:
                                  type: string
                                strict:
                                  type: boolean
                                  nullable: true
                              required:
                                - name
                              additionalProperties: false
                            type:
                              type: string
                              enum:
                                - function
                          required:
                            - function
                            - type
                          additionalProperties: false
                      response_format:
                        anyOf:
                          - type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - text
                            required:
                              - type
                            additionalProperties: false
                          - type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - json_object
                            required:
                              - type
                            additionalProperties: false
                          - type: object
                            properties:
                              type:
                                type: string
                                enum:
                                  - json_schema
                              json_schema:
                                type: object
                                properties:
                                  name:
                                    type: string
                                  description:
                                    type: string
                                  schema:
                                    type: object
                                    additionalProperties: {}
                                  strict:
                                    type: boolean
                                    nullable: true
                                required:
                                  - name
                                additionalProperties: false
                            required:
                              - type
                              - json_schema
                            additionalProperties: false
                      split:
                        type: string
                        enum:
                          - TRAIN
                          - TEST
                      metadata:
                        type: object
                        additionalProperties:
                          type: string
                    required:
                      - messages
                    additionalProperties: false
                  minItems: 1
                  maxItems: 100
              required:
                - entries
              additionalProperties: false
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  object:
                    type: string
                    enum:
                      - dataset.entries.creation
                  entries_created:
                    type: number
                  errors:
                    type: object
                    properties:
                      object:
                        type: string
                        enum:
                          - list
                      data:
                        type: array
                        items:
                          type: object
                          properties:
                            object:
                              type: string
                              enum:
                                - dataset.entries.creation.error
                            entry_index:
                              type: number
                            message:
                              type: string
                          required:
                            - object
                            - entry_index
                            - message
                          additionalProperties: false
                    required:
                      - object
                      - data
                    additionalProperties: false
                required:
                  - object
                  - entries_created
                  - errors
                additionalProperties: false
        default:
          $ref: '#/components/responses/error'
      security:
        - Authorization: []
components:
  responses:
    error:
      description: Error response
      content:
        application/json:
          schema:
            type: object
            properties:
              message:
                type: string
              code:
                type: string
              issues:
                type: array
                items:
                  type: object
                  properties:
                    message:
                      type: string
                  required:
                    - message
                  additionalProperties: false
            required:
              - message
              - code
            additionalProperties: false
  securitySchemes:
    Authorization:
      type: http
      scheme: bearer

````