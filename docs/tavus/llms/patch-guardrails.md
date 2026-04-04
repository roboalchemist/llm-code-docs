# Source: https://docs.tavus.io/api-reference/guardrails/patch-guardrails.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Patch Guardrails

> This endpoint allows you to update specific fields of guardrails using JSON Patch operations.

**Note:** The `path` field is a JSON Pointer string that references a location within the target document where the operation is performed.

For example:

```json
[
  { "op": "replace", "path": "/data/0/guardrails_prompt", "value": "Your updated prompt"},
  { "op": "add", "path": "/data/0/callback_url", "value": "https://your-server.com/webhook" }
]
```


<Note>
  * Ensure the `path` field matches the current guardrails schema.
  * For the `remove` operation, the `value` parameter is not required.
</Note>


## OpenAPI

````yaml patch /v2/guardrails/{guardrails_id}
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
  /v2/guardrails/{guardrails_id}:
    parameters:
      - name: guardrails_id
        in: path
        required: true
        description: The unique identifier of the guardrails.
        schema:
          type: string
          example: g12345
    patch:
      tags:
        - Guardrails
      summary: Patch Guardrails
      description: >
        This endpoint allows you to update specific fields of guardrails using
        JSON Patch operations.


        **Note:** The `path` field is a JSON Pointer string that references a
        location within the target document where the operation is performed.


        For example:


        ```json

        [
          { "op": "replace", "path": "/data/0/guardrails_prompt", "value": "Your updated prompt"},
          { "op": "add", "path": "/data/0/callback_url", "value": "https://your-server.com/webhook" }
        ]

        ```
      operationId: patchGuardrails
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
                    example: replace
                  path:
                    type: string
                    description: >-
                      A JSON Pointer string that references a location within
                      the target document where the operation is performed
                    example: /guardrail_name
                  value:
                    description: >-
                      The value to be used within the operation. **This field is
                      not required for the `remove` operation**.
                    example: Updated Compliance Guardrails
                required:
                  - op
                  - path
            examples:
              Update Guardrails Name:
                value:
                  - op: replace
                    path: /data/0/guardrail_name
                    value: updated_compliance_guardrails
              Update Guardrails Prompt:
                value:
                  - op: replace
                    path: /data/0/guardrail_prompt
                    value: Updated prompt with new restrictions
              Remove Callback URL:
                value:
                  - op: remove
                    path: /data/0/callback_url
      responses:
        '200':
          description: Guardrails updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: Success message
                    example: Guardrails updated successfully
        '304':
          description: No changes were made to the guardrails
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
                    example: Invalid patch operation
        '401':
          description: UNAUTHORIZED
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: The error message.
                    example: Invalid access token
        '404':
          description: Not Found
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
                    description: The error message.
                    example: Guardrails not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````