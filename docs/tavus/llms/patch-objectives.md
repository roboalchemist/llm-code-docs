# Source: https://docs.tavus.io/api-reference/objectives/patch-objectives.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavus.io/llms.txt
> Use this file to discover all available pages before exploring further.

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
  /v2/objectives/{objectives_id}:
    parameters:
      - name: objectives_id
        in: path
        required: true
        description: The unique identifier of the objective.
        schema:
          type: string
          example: o12345
    patch:
      tags:
        - Objectives
      summary: Patch Objective
      description: >
        This endpoint allows you to update specific fields of an objective using
        JSON Patch operations.


        **Note:** The `path` field is a JSON Pointer string that references a
        location within the target document where the operation is performed.


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
      operationId: patchObjective
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
                    example: /objective_name
                  value:
                    description: >-
                      The value to be used within the operation. **This field is
                      not required for the `remove` operation**.
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
      responses:
        '200':
          description: Objective updated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
                    description: Success message
                    example: Objective updated successfully
        '304':
          description: No changes were made to the objective
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
                    example: Objective not found
      security:
        - apiKey: []
components:
  securitySchemes:
    apiKey:
      type: apiKey
      in: header
      name: x-api-key

````