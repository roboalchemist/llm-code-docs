# Source: https://docs.helicone.ai/rest/ai-gateway/post-v1-chat-completions.md

# Chat Completions (Gateway)

> Create chat completions via the AI Gateway

## OpenAPI

````yaml post /v1/chat/completions
paths:
  path: /v1/chat/completions
  method: post
  servers:
    - url: https://ai-gateway.helicone.ai
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
              metadata:
                allOf:
                  - anyOf:
                      - type: object
                        additionalProperties: {}
                      - type: string
                        nullable: true
                        enum:
                          - null
              top_logprobs:
                allOf:
                  - nullable: true
                    type: integer
                    minimum: 0
                    maximum: 20
              temperature:
                allOf:
                  - anyOf:
                      - type: number
                      - type: string
                        nullable: true
                        enum:
                          - null
              top_p:
                allOf:
                  - anyOf:
                      - type: number
                      - type: string
                        nullable: true
                        enum:
                          - null
              user:
                allOf:
                  - type: string
              safety_identifier:
                allOf:
                  - type: string
              prompt_cache_key:
                allOf:
                  - type: string
              cache_control:
                allOf:
                  - type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - ephemeral
                      ttl:
                        type: string
              service_tier:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - auto
                          - default
                          - flex
                          - scale
                          - priority
                      - type: string
                        nullable: true
                        enum:
                          - null
              messages:
                allOf:
                  - minItems: 1
                    type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
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
                            role:
                              type: string
                              enum:
                                - developer
                            name:
                              type: string
                          required:
                            - content
                            - role
                        - type: object
                          properties:
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
                            role:
                              type: string
                              enum:
                                - system
                            name:
                              type: string
                          required:
                            - content
                            - role
                        - type: object
                          properties:
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
                                      - type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - image_url
                                          image_url:
                                            type: object
                                            properties:
                                              url:
                                                type: string
                                                format: uri
                                              detail:
                                                default: auto
                                                type: string
                                                enum:
                                                  - auto
                                                  - low
                                                  - high
                                            required:
                                              - url
                                        required:
                                          - type
                                          - image_url
                                      - type: object
                                        properties:
                                          type:
                                            type: string
                                            enum:
                                              - document
                                          source:
                                            type: object
                                            properties:
                                              type:
                                                type: string
                                                enum:
                                                  - text
                                              media_type:
                                                type: string
                                              data:
                                                type: string
                                            required:
                                              - type
                                              - media_type
                                              - data
                                          title:
                                            type: string
                                          citations:
                                            type: object
                                            properties:
                                              enabled:
                                                type: boolean
                                            required:
                                              - enabled
                                        required:
                                          - type
                                          - source
                            role:
                              type: string
                              enum:
                                - user
                            name:
                              type: string
                          required:
                            - content
                            - role
                        - type: object
                          properties:
                            content:
                              anyOf:
                                - anyOf:
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
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                            refusal:
                              anyOf:
                                - type: string
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                            role:
                              type: string
                              enum:
                                - assistant
                            name:
                              type: string
                            audio:
                              anyOf:
                                - type: object
                                  properties:
                                    id:
                                      type: string
                                  required:
                                    - id
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                            tool_calls:
                              type: array
                              items:
                                anyOf:
                                  - type: object
                                    properties:
                                      id:
                                        type: string
                                      type:
                                        type: string
                                        enum:
                                          - function
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
                                    required:
                                      - id
                                      - type
                                      - function
                                  - type: object
                                    properties:
                                      id:
                                        type: string
                                      type:
                                        type: string
                                        enum:
                                          - custom
                                      custom:
                                        type: object
                                        properties:
                                          name:
                                            type: string
                                          input:
                                            type: string
                                        required:
                                          - name
                                          - input
                                    required:
                                      - id
                                      - type
                                      - custom
                            function_call:
                              anyOf:
                                - type: object
                                  properties:
                                    arguments:
                                      type: string
                                    name:
                                      type: string
                                  required:
                                    - arguments
                                    - name
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                          required:
                            - role
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
                            tool_call_id:
                              type: string
                          required:
                            - role
                            - content
                            - tool_call_id
                        - type: object
                          properties:
                            role:
                              type: string
                              enum:
                                - function
                            content:
                              anyOf:
                                - type: string
                                - type: string
                                  nullable: true
                                  enum:
                                    - null
                            name:
                              type: string
                          required:
                            - role
                            - content
                            - name
              model:
                allOf:
                  - type: string
              modalities:
                allOf:
                  - anyOf:
                      - type: array
                        items:
                          type: string
                          enum:
                            - text
                      - type: string
                        nullable: true
                        enum:
                          - null
              verbosity:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - low
                          - medium
                          - high
                      - type: string
                        nullable: true
                        enum:
                          - null
              reasoning_effort:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - minimal
                          - low
                          - medium
                          - high
                      - type: string
                        nullable: true
                        enum:
                          - null
              max_completion_tokens:
                allOf:
                  - nullable: true
                    type: integer
                    minimum: -9007199254740991
                    maximum: 9007199254740991
              frequency_penalty:
                allOf:
                  - default: 0
                    nullable: true
                    type: number
                    minimum: -2
                    maximum: 2
              presence_penalty:
                allOf:
                  - default: 0
                    nullable: true
                    type: number
                    minimum: -2
                    maximum: 2
              response_format:
                allOf:
                  - anyOf:
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - text
                        required:
                          - type
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - json_schema
                          json_schema:
                            type: object
                            properties:
                              description:
                                type: string
                              name:
                                type: string
                              schema:
                                type: object
                                properties: {}
                              strict:
                                anyOf:
                                  - type: boolean
                                  - type: string
                                    nullable: true
                                    enum:
                                      - null
                            required:
                              - name
                        required:
                          - type
                          - json_schema
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - json_object
                        required:
                          - type
              store:
                allOf:
                  - default: false
                    nullable: true
                    type: boolean
              stream:
                allOf:
                  - default: false
                    nullable: true
                    type: boolean
              stop:
                allOf:
                  - nullable: true
                    anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
              logit_bias:
                allOf:
                  - default: null
                    nullable: true
                    type: object
                    additionalProperties:
                      type: integer
                      minimum: -9007199254740991
                      maximum: 9007199254740991
              logprobs:
                allOf:
                  - default: false
                    nullable: true
                    type: boolean
              max_tokens:
                allOf:
                  - nullable: true
                    type: integer
                    minimum: -9007199254740991
                    maximum: 9007199254740991
              'n':
                allOf:
                  - default: 1
                    nullable: true
                    type: integer
                    minimum: 1
                    maximum: 128
              prediction:
                allOf:
                  - nullable: true
                    type: object
                    properties:
                      type:
                        type: string
                        enum:
                          - content
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
                    required:
                      - type
                      - content
              seed:
                allOf:
                  - nullable: true
                    type: integer
                    minimum: -9007199254740991
                    maximum: 9007199254740991
              stream_options:
                allOf:
                  - anyOf:
                      - type: object
                        properties:
                          include_usage:
                            type: boolean
                          include_obfuscation:
                            type: boolean
                      - type: string
                        nullable: true
                        enum:
                          - null
              tools:
                allOf:
                  - type: array
                    items:
                      anyOf:
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - function
                            function:
                              type: object
                              properties:
                                description:
                                  type: string
                                name:
                                  type: string
                                parameters:
                                  type: object
                                  properties: {}
                                strict:
                                  anyOf:
                                    - type: boolean
                                    - type: string
                                      nullable: true
                                      enum:
                                        - null
                              required:
                                - name
                          required:
                            - type
                            - function
                        - type: object
                          properties:
                            type:
                              type: string
                              enum:
                                - custom
                            custom:
                              type: object
                              properties:
                                name:
                                  type: string
                                description:
                                  type: string
                                format:
                                  anyOf:
                                    - type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - text
                                      required:
                                        - type
                                    - type: object
                                      properties:
                                        type:
                                          type: string
                                          enum:
                                            - grammar
                                        grammar:
                                          type: object
                                          properties:
                                            definition:
                                              type: string
                                            syntax:
                                              type: string
                                              enum:
                                                - lark
                                                - regex
                                          required:
                                            - definition
                                            - syntax
                                      required:
                                        - type
                                        - grammar
                              required:
                                - name
                          required:
                            - type
                            - custom
              tool_choice:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - none
                          - auto
                          - required
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - allowed_tools
                          allowed_tools:
                            type: object
                            properties:
                              mode:
                                type: string
                                enum:
                                  - auto
                                  - required
                              tools:
                                type: array
                                items:
                                  type: object
                                  properties: {}
                            required:
                              - mode
                              - tools
                        required:
                          - type
                          - allowed_tools
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - function
                          function:
                            type: object
                            properties:
                              name:
                                type: string
                            required:
                              - name
                        required:
                          - type
                          - function
                      - type: object
                        properties:
                          type:
                            type: string
                            enum:
                              - custom
                          custom:
                            type: object
                            properties:
                              name:
                                type: string
                            required:
                              - name
                        required:
                          - type
                          - custom
              parallel_tool_calls:
                allOf:
                  - default: true
                    type: boolean
              function_call:
                allOf:
                  - anyOf:
                      - type: string
                        enum:
                          - none
                          - auto
                      - type: object
                        properties:
                          name:
                            type: string
                        required:
                          - name
              functions:
                allOf:
                  - minItems: 1
                    maxItems: 128
                    type: array
                    items:
                      type: object
                      properties:
                        description:
                          type: string
                        name:
                          type: string
                        parameters:
                          type: object
                          properties: {}
                      required:
                        - name
            required: true
            requiredProperties:
              - messages
              - model
            additionalProperties: false
        examples:
          example:
            value:
              metadata: {}
              top_logprobs: 10
              temperature: 123
              top_p: 123
              user: <string>
              safety_identifier: <string>
              prompt_cache_key: <string>
              cache_control:
                type: ephemeral
                ttl: <string>
              service_tier: auto
              messages:
                - content: <string>
                  role: developer
                  name: <string>
              model: <string>
              modalities:
                - text
              verbosity: low
              reasoning_effort: minimal
              max_completion_tokens: 0
              frequency_penalty: 0
              presence_penalty: 0
              response_format:
                type: text
              store: false
              stream: false
              stop: <string>
              logit_bias: null
              logprobs: false
              max_tokens: 0
              'n': 1
              prediction:
                type: content
                content: <string>
              seed: 0
              stream_options:
                include_usage: true
                include_obfuscation: true
              tools:
                - type: function
                  function:
                    description: <string>
                    name: <string>
                    parameters: {}
                    strict: true
              tool_choice: none
              parallel_tool_calls: true
              function_call: none
              functions:
                - description: <string>
                  name: <string>
                  parameters: {}
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Request accepted
        examples: {}
        description: Request accepted
  deprecated: false
  type: path
components:
  schemas: {}

````