# Source: https://docs.dify.ai/api-reference/feedback/get-feedbacks-of-application.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get feedbacks of application

> Get application's feedbacks.



## OpenAPI

````yaml en/api-reference/openapi_completion.json get /app/feedbacks
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
  /app/feedbacks:
    get:
      tags:
        - Feedback
      summary: Get feedbacks of application
      description: Get application's feedbacks.
      operationId: getAppFeedbacks
      parameters:
        - name: page
          in: query
          description: '(optional) Pagination page number. Default: 1'
          required: false
          schema:
            type: integer
            default: 1
        - name: limit
          in: query
          description: '(optional) Records per page. Default: 20'
          required: false
          schema:
            type: integer
            default: 20
      responses:
        '200':
          description: A list of application feedbacks.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AppFeedbacksResponse'
              examples:
                success:
                  value:
                    data:
                      - id: 8c0fbed8-e2f9-49ff-9f0e-15a35bdd0e25
                        app_id: f252d396-fe48-450e-94ec-e184218e7346
                        conversation_id: 2397604b-9deb-430e-b285-4726e51fd62d
                        message_id: 709c0b0f-0a96-4a4e-91a4-ec0889937b11
                        rating: like
                        content: message feedback information-3
                        from_source: user
                        from_end_user_id: 74286412-9a1a-42c1-929c-01edb1d381d5
                        from_account_id: null
                        created_at: '2025-04-24T09:24:38'
                        updated_at: '2025-04-24T09:24:38'
components:
  schemas:
    AppFeedbacksResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/FeedbackItem'
          description: List of application feedback items.
    FeedbackItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        app_id:
          type: string
          format: uuid
        conversation_id:
          type: string
          format: uuid
        message_id:
          type: string
          format: uuid
        rating:
          type: string
          enum:
            - like
            - dislike
            - null
          nullable: true
        content:
          type: string
        from_source:
          type: string
        from_end_user_id:
          type: string
          format: uuid
        from_account_id:
          type: string
          format: uuid
          nullable: true
        created_at:
          type: string
          format: date-time
        updated_at:
          type: string
          format: date-time
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