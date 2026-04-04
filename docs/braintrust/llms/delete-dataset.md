# Source: https://braintrust.dev/docs/api-reference/datasets/delete-dataset.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete dataset

> Delete a dataset object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/dataset/{dataset_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/dataset/{dataset_id}:
    delete:
      tags:
        - Datasets
      summary: Delete dataset
      description: Delete a dataset object by its id
      operationId: deleteDatasetId
      parameters:
        - $ref: '#/components/parameters/DatasetIdParam'
      responses:
        '200':
          description: Returns the deleted dataset object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Dataset'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    DatasetIdParam:
      schema:
        $ref: '#/components/schemas/DatasetIdParam'
      required: true
      description: Dataset id
      name: dataset_id
      in: path
  schemas:
    Dataset:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the dataset
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the dataset belongs under
        name:
          type: string
          description: Name of the dataset. Within a project, dataset names are unique
        description:
          type: string
          nullable: true
          description: Textual description of the dataset
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of dataset creation
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: Date of dataset deletion, or null if the dataset is still active
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the dataset
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: User-controlled metadata about the dataset
        url_slug:
          type: string
          description: URL slug for the dataset. used to construct dataset URLs
      required:
        - id
        - project_id
        - name
        - url_slug
    DatasetIdParam:
      type: string
      format: uuid
      description: Dataset id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````