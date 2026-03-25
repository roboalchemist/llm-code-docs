# Source: https://docs.dify.ai/api-reference/feedback/message-feedback.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Message Feedback

> End-users can provide feedback messages, facilitating application developers to optimize expected outputs.



## OpenAPI

````yaml en/api-reference/openapi_completion.json post /messages/{message_id}/feedbacks
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
  /messages/{message_id}/feedbacks:
    post:
      tags:
        - Feedback
      summary: Message Feedback
      description: >-
        End-users can provide feedback messages, facilitating application
        developers to optimize expected outputs.
      operationId: postMessageFeedback
      parameters:
        - name: message_id
          in: path
          required: true
          description: Message ID for which feedback is being provided.
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/MessageFeedbackRequest'
            examples:
              like_example:
                value:
                  rating: like
                  user: abc-123
                  content: message feedback information
      responses:
        '200':
          description: Feedback submitted successfully.
          content:
            application/json:
              schema:
                type: object
                properties:
                  result:
                    type: string
                    example: success
              examples:
                success:
                  value:
                    result: success
components:
  schemas:
    MessageFeedbackRequest:
      type: object
      properties:
        rating:
          type: string
          enum:
            - like
            - dislike
            - null
          nullable: true
          description: >-
            Upvote as `like`, downvote as `dislike`, revoke upvote/downvote as
            `null`.
        user:
          type: string
          description: >-
            User identifier, defined by the developer's rules, must be unique
            within the application.
        content:
          type: string
          description: The specific content of message feedback.
      required:
        - user
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