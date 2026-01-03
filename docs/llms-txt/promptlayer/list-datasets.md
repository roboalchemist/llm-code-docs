# Source: https://docs.promptlayer.com/reference/list-datasets.md

# List Datasets

Retrieve a paginated list of datasets based on various filtering criteria. This endpoint allows you to retrieve datasets with various filtering options including dataset group, prompt, report, workspace, and name filters. Supports both JWT and API key authentication.

### Authentication

This endpoint requires JWT or API key authentication.

### Filtering by Name

Use the `name` parameter to search for datasets by their dataset group name. The search is case-insensitive and matches partial names. This is useful for discovering existing datasets programmatically before creating new ones.

### Filtering by Status

Use the `status` parameter to control which datasets are returned based on their deletion status:

* `active` (default): Returns only active datasets
* `deleted`: Returns only deleted/archived datasets
* `all`: Returns both active and deleted datasets


## OpenAPI

````yaml GET /api/public/v2/datasets
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/datasets:
    get:
      tags:
        - datasets
      summary: List Datasets
      operationId: listDatasets
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: >-
            API key or JWT token for authentication. Use 'X-API-KEY' header for
            API key or 'Authorization: Bearer' header for JWT.
        - name: dataset_group_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: Filter by specific dataset group ID
        - name: prompt_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: Filter by specific prompt ID
        - name: prompt_version_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: Filter by specific prompt version ID
        - name: prompt_label_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: Filter by specific prompt label ID
        - name: workspace_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: >-
            Filter by specific workspace ID. If not provided, uses the current
            user's workspace
        - name: report_id
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
          description: Filter by specific report ID (includes parent report ID)
        - name: name
          in: query
          required: false
          schema:
            type: string
          description: >-
            Filter datasets by name (case-insensitive partial match on dataset
            group name)
        - name: status
          in: query
          required: false
          schema:
            type: string
            enum:
              - active
              - deleted
              - all
            default: active
          description: >-
            Filter datasets by status: 'active' (default) returns only active
            datasets, 'deleted' returns only deleted/archived datasets, 'all'
            returns both
        - name: page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            default: 1
          description: Page number for pagination
        - name: per_page
          in: query
          required: false
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 10
          description: Number of items per page
      responses:
        '200':
          description: Successful response
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  datasets:
                    type: array
                    items:
                      $ref: '#/components/schemas/Dataset'
                  page:
                    type: integer
                  per_page:
                    type: integer
                  total:
                    type: integer
                  pages:
                    type: integer
                required:
                  - success
                  - message
                  - datasets
                  - page
                  - per_page
                  - total
                  - pages
        '400':
          description: Invalid workspace_id
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
    Dataset:
      type: object
      properties:
        id:
          type: integer
          description: Dataset ID
        dataset_group_id:
          type: integer
          description: Associated dataset group ID
        version_number:
          type: integer
          description: Version number of the dataset
        column_names:
          type: array
          items:
            type: string
          description: Array of column names in the dataset
        filter_params:
          type: object
          nullable: true
          description: Filter parameters used to create the dataset
        is_deleted:
          type: boolean
          description: Whether the dataset is deleted
        user_id:
          type: integer
          description: ID of the user who created the dataset
        dataset_group:
          $ref: '#/components/schemas/DatasetGroup'
          description: Associated dataset group information
      required:
        - id
        - dataset_group_id
        - version_number
        - column_names
        - is_deleted
        - user_id
      title: Dataset
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
    DatasetGroup:
      type: object
      properties:
        id:
          type: integer
          description: Dataset group ID
        name:
          type: string
          description: Dataset group name
        workspace_id:
          type: integer
          description: Associated workspace ID
        is_deleted:
          type: boolean
          description: Whether the dataset group is deleted
      required:
        - id
        - name
        - workspace_id
        - is_deleted
      title: DatasetGroup

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt