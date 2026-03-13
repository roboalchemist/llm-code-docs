# Source: https://docs.dify.ai/api-reference/files/file-upload-for-workflow.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.dify.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# File Upload for Workflow

> Upload a file for use in workflows. Supports any formats supported by your workflow. Uploaded files are for the current end-user only.



## OpenAPI

````yaml en/api-reference/openapi_workflow.json post /files/upload
openapi: 3.0.1
info:
  title: Workflow App API
  description: >-
    Workflow applications offers non-session support and is ideal for
    translation, article writing, summarization AI, and more.
  version: 1.0.0
servers:
  - url: '{api_base_url}'
    description: >-
      The base URL for the Workflow App API. Replace {api_base_url} with the
      actual API base URL.
    variables:
      api_base_url:
        default: https://api.dify.ai/v1
        description: Actual base URL of the API
security:
  - ApiKeyAuth: []
tags:
  - name: Workflow Execution
    description: Operations related to executing and managing workflows.
  - name: Files
    description: File upload and preview operations specific to workflows.
  - name: End Users
    description: Operations related to end user information.
  - name: Application
    description: Application settings and info for workflow apps.
paths:
  /files/upload:
    post:
      tags:
        - Files
      summary: File Upload for Workflow
      description: >-
        Upload a file for use in workflows. Supports any formats supported by
        your workflow. Uploaded files are for the current end-user only.
      operationId: uploadWorkflowFile
      requestBody:
        required: true
        content:
          multipart/form-data:
            schema:
              type: object
              required:
                - file
                - user
              properties:
                file:
                  type: string
                  format: binary
                  description: The file to be uploaded.
                user:
                  type: string
                  description: User identifier.
      responses:
        '200':
          description: File uploaded successfully.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileUploadResponse'
        '201':
          description: File created successfully (alternative success code).
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FileUploadResponse'
        '400':
          $ref: '#/components/responses/BadRequestFile'
        '413':
          $ref: '#/components/responses/FileTooLarge'
        '415':
          $ref: '#/components/responses/UnsupportedFileTypeFile'
        '500':
          $ref: '#/components/responses/InternalServerError'
        '503':
          $ref: '#/components/responses/S3ErrorFile'
components:
  schemas:
    FileUploadResponse:
      type: object
      properties:
        id:
          type: string
          format: uuid
        name:
          type: string
        size:
          type: integer
        extension:
          type: string
        mime_type:
          type: string
        created_by:
          type: string
          format: uuid
        created_at:
          type: integer
          format: int64
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
  responses:
    BadRequestFile:
      description: Bad Request for file operation.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    FileTooLarge:
      description: File is too large.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    UnsupportedFileTypeFile:
      description: Unsupported file type for upload.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    InternalServerError:
      description: Internal server error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
    S3ErrorFile:
      description: S3 storage error.
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/ErrorResponse'
  securitySchemes:
    ApiKeyAuth:
      type: http
      scheme: bearer
      bearerFormat: API_KEY
      description: API Key authentication.

````

Built with [Mintlify](https://mintlify.com).