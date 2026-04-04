# Source: https://io.net/docs/reference/ai-agents/secret-management-get.md

> ## Documentation Index
> Fetch the complete documentation index at: https://io.net/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Secret Details

> Retrieves details for a specific secret.

This endpoint allows you to access detailed information about a registered secret, including its associated tool, argument, and configuration details. The actual secret value is never returned in the response for security reasons.

<Note>
  The API supports multiple authentication mechanisms, but only **one** needs to be provided per request. You may authenticate using **any** of the following headers, a browser-issued JWT `token`, an `Authorization` header, or an `x-api-key` header (io.net API key).
</Note>

<Note>
  The `display` field returned in the response provides a partially masked representation of the secret value. It shows only the first and last few characters, ensuring that at least part of the value remains hidden. Complete visibility is only possible for very short secrets (typically 4 characters or fewer).
</Note>

<Tip>
  When retrieving secrets, wildcard patterns can be used to simplify configuration. For example, instead of specifying each *Linear* subtool individually (such as `agno__linear__get_user_details`, `agno__linear__get_issue_details`, and others), a single wildcard pattern like `agno__linear__*` can be used to apply the secret across all related Linear tools.
</Tip>


## OpenAPI

````yaml openapi/ai-agents/secret-management-get.json get /api/v1/secrets/{secret_id}
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
    get:
      tags:
        - agents
      summary: Get Secret Info
      operationId: get_secret_info_v1_secrets__secret_id__get
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
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SecretInfo'
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
    SecretInfo:
      properties:
        secret_id:
          type: string
          format: uuid
          title: Secret Id
        user_id:
          type: string
          format: uuid
          title: User Id
        secret_name:
          type: string
          title: Secret Name
        display:
          anyOf:
            - type: string
            - type: 'null'
          title: Display
        tool_name:
          anyOf:
            - type: string
            - type: 'null'
          title: Tool Name
        tool_arg:
          anyOf:
            - type: string
            - type: 'null'
          title: Tool Arg
        is_default_for_tool:
          type: boolean
          title: Is Default For Tool
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - secret_id
        - user_id
        - secret_name
        - display
        - tool_name
        - tool_arg
        - is_default_for_tool
        - created_at
        - updated_at
      title: SecretInfo
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