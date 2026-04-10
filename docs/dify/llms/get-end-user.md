# Source: https://docs.dify.ai/api-reference/end-users/get-end-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get End User

> Retrieve an end user by ID.

This is useful when other APIs return an end-user ID (e.g. `created_by` from File Upload).



## OpenAPI

````yaml en/api-reference/openapi_completion.json get /end-users/{end_user_id}
openapi: 3.0.1
info:
  title: Completion App API
  description: >-
    The text generation application offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Completion App API. Replace {api_base_url} with the
      actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Completion
    description: Operations related to text generation and completion.
  - name: Files
    description: Operations related to file management.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: Operations related to user feedback.
  - name: TTS
    description: Operations related to Text-to-Speech.
  - name: Application
    description: Operations to retrieve application settings and information.
paths:
  /end-users/{end_user_id}:
    get:
      tags:
        - End Users
      summary: Get End User
      description: >-
        Retrieve an end user by ID.


        This is useful when other APIs return an end-user ID (e.g. `created_by`
        from File Upload).
      operationId: getEndUserCompletion
      parameters:
        - name: end_user_id
          in: path
          required: true
          description: End user ID.
          schema:
            type: string
            format: uuid
      responses:
        '200':
          description: End user retrieved successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EndUserDetail'
        '404':
          description: 'End user not found. Error code: `end_user_not_found`'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    EndUserDetail:
      type: object
      properties:
        id:
          type: string
          format: uuid
        tenant_id:
          type: string
          format: uuid
        app_id:
          type: string
          format: uuid
          nullable: true
        type:
          type: string
          example: service_api
        external_user_id:
          type: string
          nullable: true
        name:
          type: string
          nullable: true
        is_anonymous:
          type: boolean
        session_id:
          type: string
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          description: HTTP status code.
        code:
          type: string
          description: Error code specific to the application.
        message:
          type: string
          description: A human-readable error message.
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: >-
        API Key authentication. For all API requests, include your API Key in
        the `Authorization` HTTP Header, prefixed with 'Bearer '. Example:
        `Authorization: Bearer {API_KEY}`. **Strongly recommend storing your API
        Key on the server-side, not shared or stored on the client-side, to
        avoid possible API-Key leakage that can lead to serious consequences.**

````

Built with [Mintlify](https://mintlify.com).