# Source: https://docs.ultravox.ai/api-reference/corpora/corpora-uploads-post.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.ultravox.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Corpus File Upload

> Creates a new URL and document ID to use for uploading a static file

<Warning>Upload URLs expire after 5 minutes. You can request a new URL if needed.</Warning>


## OpenAPI

````yaml post /api/corpora/{corpus_id}/uploads
openapi: 3.0.3
info:
  title: Ultravox
  version: 0.1.0
  description: API for the Ultravox service.
servers:
  - url: https://api.ultravox.ai
security: []
paths:
  /api/corpora/{corpus_id}/uploads:
    post:
      tags:
        - corpora
      description: Request a presigned URL for uploading a document.
      operationId: corpora_uploads_create
      parameters:
        - in: path
          name: corpus_id
          schema:
            type: string
            format: uuid
          required: true
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CorpusUploadsRequest'
        required: true
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CorpusUploadsResponse'
          description: ''
      security:
        - apiKeyAuth: []
components:
  schemas:
    CorpusUploadsRequest:
      type: object
      properties:
        mimeType:
          type: string
          description: The MIME type of the file to be uploaded.
          minLength: 1
        fileName:
          type: string
          default: ''
          description: The name of the file to be uploaded.
      required:
        - mimeType
    CorpusUploadsResponse:
      type: object
      properties:
        documentId:
          type: string
        presignedUrl:
          type: string
          format: uri
      required:
        - documentId
        - presignedUrl
  securitySchemes:
    apiKeyAuth:
      type: apiKey
      in: header
      name: X-API-Key
      description: API key

````