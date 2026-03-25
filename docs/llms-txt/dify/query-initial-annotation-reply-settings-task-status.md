# Source: https://docs.dify.ai/api-reference/annotations/query-initial-annotation-reply-settings-task-status.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Initial Annotation Reply Settings Task Status



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /apps/annotation-reply/{action}/status/{job_id}
openapi: 3.0.1
info:
  title: Advanced Chat App API
  description: >-
    Chat applications support session persistence, allowing previous chat
    history to be used as context for responses. This can be applicable for
    chatbot, customer service AI, etc. This version includes advanced features
    like workflow events and more detailed file type support.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Advanced Chat App API. Replace {api_base_url} with
      the actual API base URL provided for your application (e.g., from
      props.appDetail.api_base_url).
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Chatflow
    description: Advanced chat operations with workflow events.
  - name: Files
    description: File upload and preview operations for advanced chat.
  - name: End Users
    description: Operations related to end user information.
  - name: Feedback
    description: User feedback operations for advanced chat.
  - name: Conversations
    description: Conversation management for advanced chat.
  - name: TTS
    description: Speech and Text conversion for advanced chat.
  - name: Application
    description: Application settings and info for advanced chat.
  - name: Annotations
    description: Annotation management for advanced chat.
paths:
  /apps/annotation-reply/{action}/status/{job_id}:
    get:
      tags:
        - Annotations
      summary: Query Initial Annotation Reply Settings Task Status
      operationId: getAdvancedInitialAnnotationReplySettingsStatus
      parameters:
        - $ref: '#/components/parameters/AnnotationActionPathParam'
        - $ref: '#/components/parameters/JobIdPathParam'
      responses:
        '200':
          description: Task status.
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/InitialAnnotationReplySettingsStatusResponse
components:
  parameters:
    AnnotationActionPathParam:
      name: action
      in: path
      required: true
      description: 'Action: ''enable'' or ''disable''.'
      schema:
        type: string
        enum:
          - enable
          - disable
    JobIdPathParam:
      name: job_id
      in: path
      required: true
      description: Job ID.
      schema:
        type: string
        format: uuid
  schemas:
    InitialAnnotationReplySettingsStatusResponse:
      type: object
      properties:
        job_id:
          type: string
          format: uuid
        job_status:
          type: string
        error_msg:
          type: string
          nullable: true
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).