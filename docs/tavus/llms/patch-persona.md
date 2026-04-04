# Source: https://docs.tavus.io/api-reference/personas/patch-persona.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

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


<Note>
  * Ensure the `path` match the current persona schema.
  * For the `remove` operation, the `value` parameter is not required.
</Note>


## OpenAPI

````yaml patch /v2/personas/{persona_id}
openapi: 3.0.3
info:
  title: Tavus Developer API Collection
  version: 1.0.0
  contact: {}
servers:
  - url: https://tavusapi.com
security:
  - apiKey: []
tags:
  - name: Videos
  - name: Replicas
  - name: Conversations
  - name: Personas
  - name: Replacements
  - name: Transcriptions
  - name: Documents
paths:
  /v2/personas/{persona_id}:
    parameters:
      - name: persona_id
        in: path
        required: true
        description: The unique identifier of the persona.
        schema:
          type: string
          example: pf3073f2dcc1
    patch:
      tags:
        - Personas
      summary: Patch Persona
      description: >
        This endpoint updates a persona using a JSON Patch payload (RFC 6902).
        You can modify **any field within the persona** using supported
        operations like `add`, `remove`, `replace`, `copy`, `move`, and `test`.


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
      operationId: patchPersona
      requestBody:
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
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
                      The value to be used within the operation. **Each request
                      must have a `value` field unless you're using `remove`
                      operation**.
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
                      Here are a few times that you have helped an individual
                      make a breakthrough in...
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
      responses:
        '200':
          description: OK
        '304':
          description: No changes were made to the persona
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: No changes were made to the persona
        '400':
          description: Bad Request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Invalid persona_id
        '422':
          description: Invalid JSON patch format
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid JSON patch format
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````