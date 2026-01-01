# Source: https://docs.promptlayer.com/reference/get-report.md

# Get Evaluation

> Retrieve the info about a report.

This endpoint allows you to retrieve the info about a report.

Please note that if you want to get the score of a report, you should use the `GET /reports/{report_id}/score` endpoint instead ([link](./reference/get-report-score)).


## OpenAPI

````yaml GET /reports/{report_id}
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /reports/{report_id}:
    get:
      tags:
        - reports
      summary: Get Evaluation
      operationId: getReport
      parameters:
        - name: report_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the report to retrieve.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: API key to authorize the operation.
      responses:
        '200':
          description: Report retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  report:
                    type: object
                    description: The report data with all fields
                    properties:
                      id:
                        type: integer
                      name:
                        type: string
                      comment:
                        type:
                          - string
                          - 'null'
                      is_blueprint:
                        type:
                          - boolean
                          - 'null'
                      deleted:
                        type: boolean
                      created_at:
                        type: string
                        format: date-time
                      updated_at:
                        type: string
                        format: date-time
                      score:
                        type:
                          - object
                          - 'null'
                        description: Report score data
                      score_configuration:
                        type:
                          - object
                          - 'null'
                        description: Score configuration settings
                      score_matrix:
                        type:
                          - array
                          - 'null'
                        description: Score matrix for custom scoring
                      score_calculation_error:
                        type:
                          - string
                          - 'null'
                        description: Error message if score calculation failed
                      parent_report_id:
                        type:
                          - integer
                          - 'null'
                      dataset_id:
                        type:
                          - integer
                          - 'null'
                      user_id:
                        type:
                          - integer
                          - 'null'
                      workspace_id:
                        type: integer
                      prompt_registry_id:
                        type:
                          - integer
                          - 'null'
                        description: ID of associated prompt registry
                      prompt_version_number:
                        type:
                          - integer
                          - 'null'
                        description: Version number of associated prompt
                    required:
                      - id
                      - name
                      - deleted
                      - created_at
                      - updated_at
                      - workspace_id
                  status:
                    type: string
                    enum:
                      - RUNNING
                      - COMPLETED
                    description: Overall status of the report execution
                  stats:
                    type: object
                    properties:
                      status_counts:
                        type: object
                        description: Count of cells in each status
                        properties:
                          COMPLETED:
                            type: integer
                            description: Number of completed cells
                          FAILED:
                            type: integer
                            description: Number of failed cells
                          QUEUED:
                            type: integer
                            description: Number of queued cells
                          RUNNING:
                            type: integer
                            description: Number of running cells
                        required:
                          - COMPLETED
                          - FAILED
                          - QUEUED
                          - RUNNING
                    required:
                      - status_counts
                required:
                  - success
                  - message
                  - report
                  - status
                  - stats
        '401':
          description: Unauthorized - Invalid or missing authentication
        '404':
          description: Report not found or not accessible

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt