# Source: https://docs.dify.ai/api-reference/files/file-preview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Preview

> Preview or download uploaded files. This endpoint allows you to access files that have been previously uploaded via the File Upload API. Files can only be accessed if they belong to messages within the requesting application.



## OpenAPI

````yaml en/api-reference/openapi_chatflow.json get /files/{file_id}/preview
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
  /files/{file_id}/preview:
    get:
      tags:
        - Files
      summary: File Preview
      description: >-
        Preview or download uploaded files. This endpoint allows you to access
        files that have been previously uploaded via the File Upload API. Files
        can only be accessed if they belong to messages within the requesting
        application.
      operationId: previewChatFlowFile
      parameters:
        - name: file_id
          in: path
          required: true
          description: >-
            The unique identifier of the file to preview, obtained from the File
            Upload API response.
          schema:
            type: string
            format: uuid
        - name: as_attachment
          in: query
          required: false
          description: >-
            Whether to force download the file as an attachment. Default is
            `false` (preview in browser).
          schema:
            type: boolean
            default: false
      responses:
        '200':
          description: >-
            File content returned successfully. Headers set based on file type
            and request parameters.
          content:
            image/png:
              schema:
                type: string
                format: binary
            image/jpeg:
              schema:
                type: string
                format: binary
            image/webp:
              schema:
                type: string
                format: binary
            image/gif:
              schema:
                type: string
                format: binary
            application/octet-stream:
              schema:
                type: string
                format: binary
          headers:
            Content-Type:
              description: MIME type of the file
              schema:
                type: string
            Content-Length:
              description: File size in bytes (if available)
              schema:
                type: integer
            Content-Disposition:
              description: Set to 'attachment' if as_attachment=true
              schema:
                type: string
            Cache-Control:
              description: Caching headers for performance
              schema:
                type: string
                example: public, max-age=3600
            Accept-Ranges:
              description: Set to 'bytes' for audio/video files
              schema:
                type: string
                example: bytes
        '400':
          description: |-
            Bad Request. Possible error codes:
            - `invalid_param`: Abnormal parameter input.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: >-
            Forbidden. Possible error codes:

            - `file_access_denied`: File access denied or file does not belong
            to current application.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: |-
            Not Found. Possible error codes:
            - `file_not_found`: File not found or has been deleted.
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
    ErrorResponse:
      type: object
      properties:
        status:
          type: integer
          nullable: true
        code:
          type: string
          nullable: true
        message:
          type: string
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).