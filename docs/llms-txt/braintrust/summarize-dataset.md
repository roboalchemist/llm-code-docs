# Source: https://braintrust.dev/docs/api-reference/datasets/summarize-dataset.md

# Summarize dataset

> Summarize dataset



## OpenAPI

````yaml openapi.yaml get /v1/dataset/{dataset_id}/summarize
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
  /v1/dataset/{dataset_id}/summarize:
    get:
      tags:
        - Datasets
      summary: Summarize dataset
      description: Summarize dataset
      operationId: getDatasetIdSummarize
      parameters:
        - $ref: '#/components/parameters/DatasetIdParam'
        - $ref: '#/components/parameters/SummarizeData'
      responses:
        '200':
          description: Dataset summary
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SummarizeDatasetResponse'
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
components:
  parameters:
    DatasetIdParam:
      schema:
        $ref: '#/components/schemas/DatasetIdParam'
      required: true
      description: Dataset id
      name: dataset_id
      in: path
    SummarizeData:
      schema:
        $ref: '#/components/schemas/SummarizeData'
      required: false
      description: >-
        Whether to summarize the data. If false (or omitted), only the metadata
        will be returned.
      name: summarize_data
      in: query
  schemas:
    SummarizeDatasetResponse:
      type: object
      properties:
        project_name:
          type: string
          description: Name of the project that the dataset belongs to
        dataset_name:
          type: string
          description: Name of the dataset
        project_url:
          type: string
          format: uri
          description: URL to the project's page in the Braintrust app
        dataset_url:
          type: string
          format: uri
          description: URL to the dataset's page in the Braintrust app
        data_summary:
          $ref: '#/components/schemas/DataSummary'
      required:
        - project_name
        - dataset_name
        - project_url
        - dataset_url
      description: Summary of a dataset
    DatasetIdParam:
      type: string
      format: uuid
      description: Dataset id
    SummarizeData:
      type: boolean
      nullable: true
      description: >-
        Whether to summarize the data. If false (or omitted), only the metadata
        will be returned.
    DataSummary:
      type: object
      nullable: true
      properties:
        total_records:
          type: integer
          minimum: 0
          description: Total number of records in the dataset
      required:
        - total_records
      description: Summary of a dataset's data
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt