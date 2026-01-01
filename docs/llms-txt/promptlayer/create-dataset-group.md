# Source: https://docs.promptlayer.com/reference/create-dataset-group.md

# Create Dataset Group

Create a new dataset group within a workspace. When a dataset group is created, an initial draft dataset (version\_number = -1) is automatically created. Dataset group names must be unique within a workspace. Supports both JWT and API key authentication.

### Authentication

This endpoint requires JWT or API key authentication.


## OpenAPI

````yaml POST /api/public/v2/dataset-groups
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /api/public/v2/dataset-groups:
    post:
      tags:
        - datasets
      summary: Create Dataset Group
      operationId: createDatasetGroup
      parameters:
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: >-
            API key or JWT token for authentication. Use 'X-API-KEY' header for
            API key or 'Authorization: Bearer' header for JWT.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  minLength: 1
                  description: >-
                    Name of the dataset group. Must be unique within the
                    workspace.
                workspace_id:
                  type: integer
                  minimum: 1
                  description: >-
                    Optional: ID of the workspace where the dataset group will
                    be created. If not provided, uses the workspace associated
                    with your API key.
              required:
                - name
      responses:
        '201':
          description: Dataset group created successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  dataset_group:
                    $ref: '#/components/schemas/DatasetGroup'
                  dataset:
                    $ref: '#/components/schemas/Dataset'
                required:
                  - success
                  - message
                  - dataset_group
                  - dataset
        '400':
          description: >-
            Bad Request - Invalid workspace_id or dataset with this name already
            exists
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorResponse'
components:
  schemas:
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

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt