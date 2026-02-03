# Source: https://docs.promptlayer.com/reference/create-dataset-version-from-file.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create Dataset Version from File

Create a new dataset version by uploading a CSV or JSON file. The file is processed asynchronously and webhooks are sent when complete. Files are uploaded to AWS S3 for processing.

### Authentication

This endpoint requires API key authentication only.

### Asynchronous Processing

This endpoint initiates an asynchronous job to process the uploaded file. The actual dataset version creation happens in the background. A draft dataset (version\_number = -1) is created immediately, and upon successful processing, it's assigned a proper version number.

### Webhooks

The following webhooks are triggered during the process:

* `dataset_version_created_by_file` - Sent when the dataset version is successfully created
* `dataset_version_created_by_file_failed` - Sent if the dataset creation fails

### Notes

* Maximum file size: 100MB
* Failed drafts are automatically cleaned up


## OpenAPI

````yaml POST /api/public/v2/dataset-versions/from-file
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/dataset-versions/from-file:
    post:
      tags:
        - datasets
      summary: Create Dataset Version from File
      operationId: createDatasetVersionFromFile
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: >-
            API key for authentication. This endpoint supports API key
            authentication only.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                dataset_group_id:
                  type: integer
                  minimum: 1
                  description: >-
                    ID of the dataset group where the new version will be
                    created
                file_name:
                  type: string
                  minLength: 1
                  maxLength: 255
                  description: >-
                    Name of the file being uploaded (must end with .csv or
                    .json)
                file_content_base64:
                  type: string
                  minLength: 1
                  description: >-
                    Base64 encoded content of the file. Maximum file size:
                    100MB. Supported formats: CSV, JSON
              required:
                - dataset_group_id
                - file_name
                - file_content_base64
      responses:
        '201':
          description: Dataset version creation job queued
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  dataset_id:
                    type: integer
                    description: ID of the created draft dataset
                required:
                  - success
                  - message
                  - dataset_id
        '400':
          description: >-
            Bad Request - Invalid file format, file too large, or invalid base64
            encoding
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '403':
          description: Access denied to this dataset group
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '404':
          description: Dataset group not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
        '500':
          description: Failed to upload file or create dataset version
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    ErrorResponse:
      type: object
      properties:
        success:
          type: boolean
          default: false
          description: Indicates that the request failed.
        error:
          type: string
          description: Error message explaining why the request failed.
      required:
        - success
        - error
      description: Error response format.

````