# Source: https://docs.promptlayer.com/reference/get-report-score.md

# Get Evaluation Score

> Retrieve the score of a specific report.

This endpoint allows you to retrieve the score of a specific report by its ID.


## OpenAPI

````yaml GET /reports/{report_id}/score
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /reports/{report_id}/score:
    get:
      tags:
        - reports
      summary: Get Evaluation Score
      operationId: getReportScore
      parameters:
        - name: report_id
          in: path
          required: true
          schema:
            type: integer
          description: ID of the report to get the score for.
        - name: X-API-KEY
          in: header
          required: true
          schema:
            type: string
          description: API key to authorize the operation.
      responses:
        '200':
          description: Report score retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  success:
                    type: boolean
                  message:
                    type: string
                  score:
                    type: object
                    properties:
                      overall_score:
                        type:
                          - number
                          - 'null'
                        description: The overall score of the report
                      score_type:
                        type: string
                        enum:
                          - single_column
                          - multi_column
                          - custom
                          - none
                        description: Type of scoring used for this report
                      has_custom_scoring:
                        type: boolean
                        description: Whether custom scoring logic was used
                      details:
                        type: object
                        oneOf:
                          - description: Single column score details
                            properties:
                              column_name:
                                type: string
                              score:
                                type:
                                  - number
                                  - 'null'
                              score_type:
                                type:
                                  - string
                                  - 'null'
                              num_skipped:
                                type: integer
                          - description: Multi-column score details
                            properties:
                              columns:
                                type: array
                                items:
                                  type: object
                                  properties:
                                    column_name:
                                      type: string
                                    score:
                                      type:
                                        - number
                                        - 'null'
                                    score_type:
                                      type:
                                        - string
                                        - 'null'
                                    num_skipped:
                                      type: integer
                          - description: Custom score details
                            properties:
                              matrix:
                                type: array
                                description: Score matrix from custom scoring logic
                              configuration:
                                type:
                                  - object
                                  - 'null'
                                description: Custom scoring configuration
                          - description: No score details
                            properties:
                              message:
                                type: string
                    required:
                      - overall_score
                      - score_type
                      - has_custom_scoring
                      - details
                required:
                  - success
                  - message
                  - score
        '400':
          description: Bad Request - Blueprint reports do not have scores
        '401':
          description: Unauthorized
        '403':
          description: Forbidden - Invalid workspace
        '404':
          description: Report not found

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt