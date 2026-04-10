# Source: https://docs.dify.ai/api-reference/annotations/delete-annotation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete Annotation



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json delete /apps/annotations/{annotation_id}
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
  /apps/annotations/{annotation_id}:
    delete:
      tags:
        - Annotations
      summary: Delete Annotation
      operationId: deleteAdvancedAnnotation
      parameters:
        - $ref: '#/components/parameters/AnnotationIdPathParam'
      responses:
        '204':
          description: Annotation deleted.
components:
  parameters:
    AnnotationIdPathParam:
      name: annotation_id
      in: path
      required: true
      description: Annotation ID.
      schema:
        type: string
        format: uuid
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).