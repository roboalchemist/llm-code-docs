# Source: https://docs.tavus.io/api-reference/objectives/patch-objectives.md

# Patch Objective

> This endpoint allows you to update specific fields of an objective using JSON Patch operations.

**Note:** The `path` field is a JSON Pointer string that references a location within the target document where the operation is performed.

For example:

```json
[
  { "op": "replace", "path": "/data/0/objective_name", "value": "updated_objective_name" },
  { "op": "replace", "path": "/data/0/objective_prompt", "value": "Updated prompt for the objective" },
  { "op": "replace", "path": "/data/0/confirmation_mode", "value": "manual" },
  { "op": "add", "path": "/data/0/output_variables", "value": ["new_variable"] },
  { "op": "replace", "path": "/data/0/modality", "value": "visual" },
  { "op": "remove", "path": "/data/0/callback_url" }
]
```


## OpenAPI

````yaml patch /v2/objectives/{objectives_id}
paths:
  path: /v2/objectives/{objectives_id}
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
        objectives_id:
          schema:
            - type: string
              required: true
              description: The unique identifier of the objective.
              example: o12345
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
                      example: /objective_name
                    value:
                      description: >-
                        The value to be used within the operation. **This field
                        is not required for the `remove` operation**.
                      example: updated_objective_name
                  required:
                    - op
                    - path
        examples:
          Update Objective Name:
            value:
              - op: replace
                path: /objective_name
                value: updated_objective_name
          Update Objective Prompt:
            value:
              - op: replace
                path: /objective_prompt
                value: Updated prompt for the objective
          Add Output Variables:
            value:
              - op: add
                path: /output_variables
                value:
                  - new_variable
                  - another_variable
          Remove Callback URL:
            value:
              - op: remove
                path: /callback_url
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
                    example: Objective updated successfully
        examples:
          example:
            value:
              message: Objective updated successfully
        description: Objective updated successfully
    '304':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: No changes were made to the objective
        examples: {}
        description: No changes were made to the objective
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
                    example: Objective not found
        examples:
          example:
            value:
              error: Objective not found
        description: Not Found
  deprecated: false
  type: path
components:
  schemas: {}

````