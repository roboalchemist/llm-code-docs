# Source: https://docs.together.ai/reference/get-evaluation-status.md

# Get Evaluation Status



## OpenAPI

````yaml GET /evaluation/{id}/status
openapi: 3.1.0
info:
  title: Together APIs
  description: The Together REST API. Please see https://docs.together.ai for more details.
  version: 2.0.0
  termsOfService: https://www.together.ai/terms-of-service
  contact:
    name: Together Support
    url: https://www.together.ai/contact
  license:
    name: MIT
    url: https://github.com/togethercomputer/openapi/blob/main/LICENSE
servers:
  - url: https://api.together.xyz/v1
security:
  - bearerAuth: []
paths:
  /evaluation/{id}/status:
    get:
      tags:
        - evaluation
      summary: Get evaluation job status and results
      operationId: getEvaluationJobStatusAndResults
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: Evaluation job status and results retrieved successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  status:
                    type: string
                    description: The status of the evaluation job
                    enum:
                      - completed
                      - error
                      - user_error
                      - running
                      - queued
                      - pending
                  results:
                    description: The results of the evaluation job
                    oneOf:
                      - $ref: '#/components/schemas/EvaluationClassifyResults'
                      - $ref: '#/components/schemas/EvaluationScoreResults'
                      - $ref: '#/components/schemas/EvaluationCompareResults'
        '404':
          description: Evaluation job not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Failed to get evaluation job
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    EvaluationClassifyResults:
      type: object
      properties:
        generation_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed generations.
          example: 0
        judge_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed judge generations
          example: 0
        invalid_label_count:
          type: number
          format: float
          nullable: true
          description: Number of invalid labels
          example: 0
        result_file_id:
          type: string
          description: Data File ID
          example: file-1234-aefd
        pass_percentage:
          type: number
          format: integer
          nullable: true
          description: Pecentage of pass labels.
          example: 10
        label_counts:
          type: string
          description: JSON string representing label counts
          example: '{"yes": 10, "no": 0}'
    EvaluationScoreResults:
      type: object
      properties:
        aggregated_scores:
          type: object
          properties:
            mean_score:
              type: number
              format: float
            std_score:
              type: number
              format: float
            pass_percentage:
              type: number
              format: float
        generation_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed generations.
          example: 0
        judge_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed judge generations
          example: 0
        invalid_score_count:
          type: number
          format: integer
          description: number of invalid scores generated from model
        failed_samples:
          type: number
          format: integer
          description: number of failed samples generated from model
        result_file_id:
          type: string
          description: Data File ID
          example: file-1234-aefd
    EvaluationCompareResults:
      type: object
      properties:
        num_samples:
          type: integer
          description: Total number of samples compared
        A_wins:
          type: integer
          description: Number of times model A won
        B_wins:
          type: integer
          description: Number of times model B won
        Ties:
          type: integer
          description: Number of ties
        generation_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed generations.
          example: 0
        judge_fail_count:
          type: number
          format: integer
          nullable: true
          description: Number of failed judge generations
          example: 0
        result_file_id:
          type: string
          description: Data File ID
    ErrorData:
      type: object
      required:
        - error
      properties:
        error:
          type: object
          properties:
            message:
              type: string
              nullable: false
            type:
              type: string
              nullable: false
            param:
              type: string
              nullable: true
              default: null
            code:
              type: string
              nullable: true
              default: null
          required:
            - type
            - message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt