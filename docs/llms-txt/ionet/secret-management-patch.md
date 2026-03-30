# Source: https://io.net/docs/reference/ai-agents/secret-management-patch.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Update Secret Details

> Updates an existing secret or its associated metadata.Updates an existing secret or its associated metadata.

This endpoint allows you to modify one or more properties of a previously registered secret, such as its value, linked tool, or default configuration. Only the fields provided in the request body will be updated, and omitted fields will remain unchanged.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>

<Note>
  The system imposes an overall implementation-specific limit on the total size of stored secrets. If a request attempts to store a secret, or a combination of secrets, that exceeds this limit, the API will return an **HTTP 413 (Payload Too Large)** error.
</Note>

<Tip>
  When updating secrets, wildcard patterns can be used. For example, instead of specifying each *Linear* subtool individually (such as `agno__linear__get_user_details`, `agno__linear__get_issue_details`, and others), a single wildcard pattern like `agno__linear__*` can be used to apply the secret across all related Linear tools.
</Tip>

### Request body parameters:

`secret_name` – A user-defined identifier for the secret. This value is used to reference and manage the secret in subsequent operations.

`secret_value` – The confidential value associated with the secret. This value is securely stored and made available to the designated tool when access is authorized.

`tool_name` – The name of the single tool that is granted access to this secret. This field accepts only one tool identifier, not an array or list.

`tool_arg` – The specific argument of the tool that this secret applies to.

`is_default_for_tool` – A boolean flag specifying whether this secret should be automatically applied when the associated tool does not receive a value for the argument. This field is optional when using secrets in workflow YAML configurations, but required when defining secrets for built-in agents.


## OpenAPI

````yaml openapi/ai-agents/secret-management-patch.json patch /api/v1/secrets/{secret_id}
openapi: 3.1.0
info:
  title: IO Intelligence
  version: '1.0'
servers:
  - url: https://api.intelligence.io.solutions
security:
  - sec0: []
paths:
  /api/v1/secrets/{secret_id}:
    patch:
      tags:
        - agents
      summary: Update a Secret
      operationId: update_secret_v1_secrets__secret_id__patch
      parameters:
        - name: secret_id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            title: Secret Id
        - name: token
          in: header
          required: false
          schema:
            type: string
            description: JWT token
            title: Token
          description: JWT token
        - name: Authorization
          in: header
          required: false
          schema:
            type: string
            description: io.net provided API Key
            title: Authorization
          description: io.net provided API Key
        - name: x-api-key
          in: header
          required: false
          schema:
            type: string
            description: API key set by an SDK client
            title: X-Api-Key
          description: API key set by an SDK client
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_update_secret_v1_secrets__secret_id__patch
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '404':
          description: Not found
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_update_secret_v1_secrets__secret_id__patch:
      properties:
        secret_name:
          anyOf:
            - type: string
              maxLength: 1024
              minLength: 1
            - type: 'null'
          title: Secret Name
        secret_value:
          anyOf:
            - type: string
              maxLength: 1024
              minLength: 4
            - type: 'null'
          title: Secret Value
        tool_name:
          anyOf:
            - type: string
              maxLength: 1024
              minLength: 1
            - type: 'null'
          title: Tool Name
        tool_arg:
          anyOf:
            - type: string
              maxLength: 1024
              minLength: 1
            - type: 'null'
          title: Tool Arg
        is_default_for_tool:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Is Default For Tool
      type: object
      title: Body_update_secret_v1_secrets__secret_id__patch
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    sec0:
      type: oauth2
      flows: {}

````