# Source: https://docs.together.ai/reference/list-evaluations.md

# List All Evaluations



## OpenAPI

````yaml GET /evaluation
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
  /evaluation:
    get:
      tags:
        - evaluation
      summary: Get all evaluation jobs
      operationId: getAllEvaluationJobs
      parameters:
        - name: status
          in: query
          required: false
          schema:
            type: string
            default: pending
        - name: limit
          in: query
          required: false
          schema:
            type: integer
            default: 10
        - name: userId
          in: query
          required: false
          description: >-
            Admin users can specify a user ID to filter jobs. Pass empty string
            to get all jobs.
          schema:
            type: string
      responses:
        '200':
          description: evaluation jobs retrieved successfully
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/EvaluationJob'
        '400':
          description: Invalid request format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Error retrieving jobs from manager
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    EvaluationJob:
      type: object
      properties:
        workflow_id:
          type: string
          description: The evaluation job ID
          example: eval-1234aedf
        type:
          type: string
          enum:
            - classify
            - score
            - compare
          description: The type of evaluation
          example: classify
        owner_id:
          type: string
          description: ID of the job owner (admin only)
        status:
          type: string
          enum:
            - pending
            - queued
            - running
            - completed
            - error
            - user_error
          description: Current status of the job
          example: completed
        status_updates:
          type: array
          items:
            $ref: '#/components/schemas/EvaluationJobStatusUpdate'
          description: History of status updates (admin only)
        parameters:
          type: object
          description: The parameters used for this evaluation
          additionalProperties: true
        created_at:
          type: string
          format: date-time
          description: When the job was created
          example: '2025-07-23T17:10:04.837888Z'
        updated_at:
          type: string
          format: date-time
          description: When the job was last updated
          example: '2025-07-23T17:10:04.837888Z'
        results:
          oneOf:
            - $ref: '#/components/schemas/EvaluationClassifyResults'
            - $ref: '#/components/schemas/EvaluationScoreResults'
            - $ref: '#/components/schemas/EvaluationCompareResults'
            - type: object
              properties:
                error:
                  type: string
          nullable: true
          description: Results of the evaluation (when completed)
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
    EvaluationJobStatusUpdate:
      type: object
      properties:
        status:
          type: string
          description: The status at this update
          example: pending
        message:
          type: string
          description: Additional message for this update
          example: Job is pending evaluation
        timestamp:
          type: string
          format: date-time
          description: When this update occurred
          example: '2025-07-23T17:10:04.837888Z'
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
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt