# Source: https://docs.dify.ai/api-reference/annotations/get-annotation-list.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Annotation List



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /apps/annotations
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
  /apps/annotations:
    get:
      tags:
        - Annotations
      summary: Get Annotation List
      operationId: getAdvancedAnnotationList
      parameters:
        - $ref: '#/components/parameters/PageQueryParam'
        - $ref: '#/components/parameters/LimitQueryParamDefault20Max100'
      responses:
        '200':
          description: Annotation list.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AnnotationListResponse'
components:
  parameters:
    PageQueryParam:
      name: page
      in: query
      description: Page number.
      schema:
        type: integer
        default: 1
    LimitQueryParamDefault20Max100:
      name: limit
      in: query
      description: Number of items per page (Default 20, Max 100).
      schema:
        type: integer
        default: 20
        minimum: 1
        maximum: 100
  schemas:
    AnnotationListResponse:
      type: object
      properties:
        data:
          type: array
          items:
            $ref: '#/components/schemas/AnnotationItem'
        has_more:
          type: boolean
        limit:
          type: integer
        total:
          type: integer
        page:
          type: integer
    AnnotationItem:
      type: object
      properties:
        id:
          type: string
          format: uuid
        question:
          type: string
        answer:
          type: string
        hit_count:
          type: integer
        created_at:
          type: integer
          format: int64
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).