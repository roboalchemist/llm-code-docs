# Source: https://docs.promptlayer.com/reference/run-report.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.promptlayer.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Run Full Evaluation

> Run an evaluation pipeline

This endpoint allows you to run an evaluation pipeline. You can optionally update the dataset.


## OpenAPI

````yaml POST /reports/{report_id}/run
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /reports/{report_id}/run:
    post:
      tags:
        - reports
      summary: Run Full Evaluation
      operationId: runReport
      parameters:
        - name: report_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the evaluation pipeline report to run.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: API key to authorize the operation.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: >-
                    The name of the final report to be created. Must be between
                    1 and 255 characters in length.
                  minLength: 1
                  maxLength: 255
                dataset_id:
                  type:
                    - integer
                    - 'null'
                  description: >-
                    The ID of the dataset to use for the report. If not
                    provided, uses the evaluation pipeline's default dataset.
                refresh_dataset:
                  type:
                    - boolean
                    - 'null'
                  description: >-
                    Whether to refresh the dataset before running the report.
                    Only applicable for dynamic datasets.
              required:
                - name
      responses:
        '201':
          description: Report run initiated successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  report_id:
                    type: integer
                    description: The ID of the created final report.
                required:
                  - success
                  - report_id
        '400':
          description: Bad Request - Invalid data or report generation error
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '401':
          description: Unauthorized - No requests found for the given criteria
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '403':
          description: >-
            Forbidden - Can only run evaluation pipeline reports or dataset
            refresh not allowed
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message
        '404':
          description: Not Found - Report or dataset not found
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                required:
                  - success
                  - message

````