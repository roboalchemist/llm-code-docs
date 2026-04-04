# Source: https://docs.pinecone.io/reference/api/2025-10/assistant/describe_file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Describe a file upload

> Get the status and metadata of a file uploaded to an assistant.

For guidance and examples, see [Manage files](https://docs.pinecone.io/guides/assistant/manage-files#get-the-status-of-a-file).

<RequestExample>
  ```bash curl theme={null}
  PINECONE_API_KEY="YOUR_API_KEY"
  ASSISTANT_NAME="example-assistant"
  FILE_ID="3c90c3cc-0d44-4b50-8888-8dd25736052a"

  # Describe a file. 
  # To get a signed URL in the response, set `include_url` to `true`.
  curl -X GET "https://prod-1-data.ke.pinecone.io/assistant/files/$ASSISTANT_NAME/$FILE_ID?include_url=true" \
    -H "Api-Key: $PINECONE_API_KEY" \
    -H "X-Pinecone-Api-Version: 2025-10"
  ```
</RequestExample>


## OpenAPI

````yaml https://raw.githubusercontent.com/pinecone-io/pinecone-api/refs/heads/main/2025-10/assistant_data_2025-10.oas.yaml get /files/{assistant_name}/{assistant_file_id}
openapi: 3.0.3
info:
  title: Pinecone Assistant Data Plane API
  description: >-
    Pinecone Assistant Engine is a context engine to store and retrieve relevant
    knowledge from millions of documents at scale. This API supports
    interactions with assistants.
  contact:
    name: Pinecone Support
    url: https://support.pinecone.io
    email: support@pinecone.io
  license:
    name: Apache 2.0
    url: https://www.apache.org/licenses/LICENSE-2.0
  version: 2025-10
servers:
  - url: https://{assistant_host}
    variables:
      assistant_host:
        default: unknown
        description: host of the created assistant
security:
  - ApiKeyAuth: []
tags:
  - name: Manage Assistants
    description: Actions that manage Assistants
paths:
  /files/{assistant_name}/{assistant_file_id}:
    get:
      tags:
        - Manage Assistants
      summary: Describe a file upload
      description: >-
        Get the status and metadata of a file uploaded to an assistant.


        For guidance and examples, see [Manage
        files](https://docs.pinecone.io/guides/assistant/manage-files#get-the-status-of-a-file).
      operationId: describe_file
      parameters:
        - in: header
          name: X-Pinecone-Api-Version
          description: Required date-based version header
          required: true
          schema:
            default: 2025-10
            type: string
          style: simple
        - in: path
          name: assistant_name
          description: The name of the assistant to upload files to.
          required: true
          schema:
            type: string
          example: test-model
          style: simple
        - in: path
          name: assistant_file_id
          description: The uuid of the file to be described.
          required: true
          schema:
            type: string
          example: 72490b32-46d9-4db1-b48b-666e9176d9be
          style: simple
        - in: query
          name: include_url
          description: Include the signed URL of the file in the response.
          schema:
            x-enum:
              - 'true'
              - 'false'
            type: string
          style: form
      responses:
        '200':
          description: Poll request successful.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AssistantFileModel'
        '401':
          description: 'Unauthorized. Possible causes: Invalid API key.'
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                unauthorized:
                  summary: Unauthorized
                  value:
                    error:
                      code: UNAUTHENTICATED
                      message: Invalid API key.
                    status: 401
        '404':
          description: File not found.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                file-not-found:
                  summary: File not found.
                  value:
                    error:
                      code: NOT_FOUND
                      message: >-
                        File with id 72490b32-46d9-4db1-b48b-666e9176d9be  not
                        found in provided assistant
                    status: 404
        '500':
          description: Internal server error.
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
              examples:
                internal-server-error:
                  summary: Internal server error
                  value:
                    error:
                      code: UNKNOWN
                      message: Internal server error
                    status: 500
components:
  schemas:
    AssistantFileModel:
      description: The response format for a successful file upload request.
      type: object
      properties:
        name:
          type: string
        id:
          type: string
          format: uuid
        metadata:
          nullable: true
          type: object
        created_on:
          type: string
          format: date-time
        updated_on:
          type: string
          format: date-time
        status:
          description: >-
            The current state of the uploaded file. Possible values:

            - `Processing`: File is being processed (parsed, chunked, embedded)

            - `Available`: Processing completed successfully; file is ready for
            use

            - `Deleting`: Deletion has been initiated but not yet completed

            - `ProcessingFailed`: Processing failed with an error


            Note: Once a file is deleted, the API returns 404 Not Found instead
            of a file object.
          x-enum:
            - Processing
            - Available
            - Deleting
            - ProcessingFailed
          type: string
        percent_done:
          nullable: true
          description: The percentage of the file that has been processed
          type: number
          format: double
        signed_url:
          nullable: true
          example: https://storage.googleapis.com/bucket/file.pdf?...
          description: >-
            A [signed
            URL](https://cloud.google.com/storage/docs/access-control/signed-urls)
            that provides temporary, read-only access to the underlying file.
            Anyone with the link can access the file, so treat it as sensitive
            data. Expires after a short time.
          type: string
        error_message:
          nullable: true
          description: >-
            A message describing any error during file processing. Provided only
            if an error occurs.
          type: string
        multimodal:
          description: Indicates whether the file was processed as multimodal.
          type: boolean
      required:
        - id
        - name
    ErrorResponse:
      example:
        error:
          code: QUOTA_EXCEEDED
          message: >-
            The index exceeds the project quota of 5 pods by 2 pods. Upgrade
            your account or change the project settings to increase the quota.
        status: 429
      description: The response shape used for all error responses.
      type: object
      properties:
        status:
          example: 500
          description: The HTTP status code of the error.
          type: integer
        error:
          example:
            code: INVALID_ARGUMENT
            message: Uploaded file can only currently be either a pdf or txt file
          description: Detailed information about the error that occurred.
          type: object
          properties:
            code:
              x-enum:
                - OK
                - UNKNOWN
                - INVALID_ARGUMENT
                - DEADLINE_EXCEEDED
                - QUOTA_EXCEEDED
                - NOT_FOUND
                - ALREADY_EXISTS
                - PERMISSION_DENIED
                - UNAUTHENTICATED
                - RESOURCE_EXHAUSTED
                - FAILED_PRECONDITION
                - ABORTED
                - OUT_OF_RANGE
                - UNIMPLEMENTED
                - INTERNAL
                - UNAVAILABLE
                - DATA_LOSS
                - FORBIDDEN
              type: string
            message:
              example: >-
                Index name must contain only lowercase alphanumeric characters
                or hyphens, and must not begin or end with a hyphen.
              type: string
            details:
              description: >-
                Additional information about the error. This field is not
                guaranteed to be present.
              type: object
          required:
            - code
            - message
      required:
        - status
        - error
  securitySchemes:
    ApiKeyAuth:
      type: apiKey
      in: header
      name: Api-Key
      description: Pinecone API Key

````