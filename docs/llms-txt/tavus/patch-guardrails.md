# Source: https://docs.tavus.io/api-reference/guardrails/patch-guardrails.md

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


## OpenAPI

````yaml patch /v2/guardrails/{guardrails_id}
paths:
  path: /v2/guardrails/{guardrails_id}
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
        guardrails_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the guardrails.
              example: g12345
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
                      example: replace
                    path:
                      type: string
                      description: >-
                        A JSON Pointer string that references a location within
                        the target document where the operation is performed
                      example: /guardrail_name
                    value:
                      description: >-
                        The value to be used within the operation. **This field
                        is not required for the `remove` operation**.
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
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: Success message
                    example: Guardrails updated successfully
        examples:
          example:
            value:
              message: Guardrails updated successfully
        description: Guardrails updated successfully
    '304':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No changes were made to the guardrails
        examples: {}
        description: No changes were made to the guardrails
    '400':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid patch operation
        examples:
          example:
            value:
              error: Invalid patch operation
        description: Bad Request
    '401':
      application/json:
        schemaArray:
          - type: object
            properties:
              message:
                allOf:
                  - type: string
                    description: The error message.
                    example: Invalid access token
        examples:
          example:
            value:
              message: Invalid access token
        description: UNAUTHORIZED
    '404':
      application/json:
        schemaArray:
          - type: object
            properties:
              error:
                allOf:
                  - type: string
                    description: The error message.
                    example: Guardrails not found
        examples:
          example:
            value:
              error: Guardrails not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````