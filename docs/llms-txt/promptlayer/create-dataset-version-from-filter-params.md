# Source: https://docs.promptlayer.com/reference/create-dataset-version-from-filter-params.md

# Create Dataset Version from Request History

Create a new dataset version by filtering existing request logs. The dataset is populated asynchronously based on the provided filter parameters.

### Authentication

This endpoint requires API key authentication only.

### Asynchronous Processing

This endpoint initiates an asynchronous job to process the request logs based on the filter parameters. The actual dataset version creation happens in the background. A draft dataset (version\_number = -1) is created immediately.

### Webhooks

The following webhook is triggered when the process completes:

* `dataset_version_created_from_filter_params` - Sent when the dataset version is successfully created, includes:
  * `dataset_id`: ID of the created dataset
  * `rows_added`: Number of rows added to the dataset
  * `dataset_version_number`: Final version number assigned

### Notes

* If an existing draft dataset exists for the dataset group, it will be updated with new filter params
* If no matching request logs are found, an empty dataset version is created
* Failed drafts are automatically cleaned up


## OpenAPI

````yaml POST /api/public/v2/dataset-versions/from-filter-params
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/dataset-versions/from-filter-params:
    post:
      tags:
        - datasets
      summary: Create Dataset Version from Filter Params
      operationId: createDatasetVersionFromFilterParams
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
                variables_to_parse:
                  type: array
                  items:
                    type: string
                  description: List of variables to parse from the request logs
                prompt_id:
                  type: integer
                  description: Filter by specific prompt ID
                prompt_version_id:
                  type: integer
                  description: Filter by specific prompt version ID
                prompt_label_id:
                  type: integer
                  description: Filter by specific prompt label ID
                workspace_id:
                  type: integer
                  description: Filter by specific workspace ID
                start_time:
                  type: string
                  format: date-time
                  description: Filter logs after this timestamp (ISO format)
                end_time:
                  type: string
                  format: date-time
                  description: Filter logs before this timestamp (ISO format)
                tags:
                  type: array
                  items:
                    type: string
                  description: Filter by specific tags
                metadata:
                  type: object
                  additionalProperties:
                    type: string
                  description: Filter by metadata key-value pairs
                scores:
                  type: object
                  additionalProperties:
                    type: object
                    properties:
                      min:
                        type: number
                      max:
                        type: number
                  description: Filter by score ranges
              required:
                - dataset_group_id
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
                  dataset_group_id:
                    type: integer
                    description: ID of the dataset group
                  version_number:
                    type: integer
                    description: Version number of the dataset (-1 for draft)
                required:
                  - success
                  - message
                  - dataset_id
                  - dataset_group_id
                  - version_number
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt