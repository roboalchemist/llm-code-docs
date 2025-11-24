# Source: https://docs.tavus.io/api-reference/personas/patch-persona.md

# Patch Persona

> This endpoint updates a persona using a JSON Patch payload (RFC 6902). You can modify **any field within the persona** using supported operations like `add`, `remove`, `replace`, `copy`, `move`, and `test`.

For example:


```json
[
  { "op": "replace", "path": "/persona_name", "value": "Wellness Advisor" },
  { "op": "replace", "path": "/default_replica_id", "value": "r79e1c033f" },
  { "op": "replace", "path": "/context", "value": "Here are a few times that you have helped an individual make a breakthrough in..." },
  { "op": "replace", "path": "/layers/llm/model", "value": "tavus-gpt-4o" },
  { "op": "replace", "path": "/layers/tts/tts_engine", "value": "cartesia" },
  { "op": "add", "path": "/layers/tts/tts_emotion_control", "value": "true" },
  { "op": "remove", "path": "/layers/stt/hotwords" },
  { "op": "replace", "path": "/layers/perception/perception_tool_prompt", "value": "Use tools when identity documents are clearly shown." }
]
```


## OpenAPI

````yaml patch /v2/personas/{persona_id}
paths:
  path: /v2/personas/{persona_id}
  method: patch
  servers:
    - url: https://tavusapi.com
  request:
    security:
      - title: apiKey
        parameters:
          query: {}
          header:
            x-api-key:
              type: apiKey
          cookie: {}
    parameters:
      path:
        persona_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the persona.
              example: pf3073f2dcc1
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: array
            items:
              allOf:
                - type: object
                  properties:
                    op:
                      type: string
                      description: >-
                        The operation to perform. Must be one of: add, remove,
                        replace, copy, move, test
                      enum:
                        - add
                        - remove
                        - replace
                        - copy
                        - move
                        - test
                      example: add
                    path:
                      type: string
                      description: >-
                        A JSON Pointer string that references a location within
                        the target document where the operation is performed
                      example: /layers/llm/model
                    value:
                      type: string
                      description: >-
                        The value to be used within the operation. **Each
                        request must have a `value` field unless you're using
                        `remove` operation**.
                      example: tavus-llama-4
                  required:
                    - op
                    - path
                    - value
        examples:
          Add Persona Context:
            value:
              - op: add
                path: /context
                value: >-
                  Here are a few times that you have helped an individual make a
                  breakthrough in...
          Replace Persona System Prompt:
            value:
              - op: replace
                path: /system_prompt
                value: >-
                  As a Life Coach, you are a dedicated professional who
                  specializes in...
          Remove STT Hotwords:
            value:
              - op: remove
                path: /layers/stt/hotwords
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: OK
        examples: {}
        description: OK
    '304':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: No changes were made to the persona
        examples:
          example:
            value:
              message: No changes were made to the persona
        description: No changes were made to the persona
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid persona_id
        examples:
          example:
            value:
              error: Invalid persona_id
        description: Bad Request
    '422':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid JSON patch format
        examples:
          example:
            value:
              message: Invalid JSON patch format
        description: Invalid JSON patch format
  deprecated: false
  type: path
components:
  schemas: {}

````