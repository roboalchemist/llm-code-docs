# Source: https://docs.together.ai/reference/create-evaluation.md

# Create Evaluation



## OpenAPI

````yaml POST /evaluation
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
    post:
      tags:
        - evaluation
      summary: Create an evaluation job
      operationId: createEvaluationJob
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvaluationTypedRequest'
      responses:
        '200':
          description: Evaluation job created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationResponse'
        '400':
          description: Invalid request format
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
        '500':
          description: Failed to create evaluation job
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorData'
components:
  schemas:
    EvaluationTypedRequest:
      type: object
      required:
        - type
        - parameters
      properties:
        type:
          type: string
          enum:
            - classify
            - score
            - compare
          description: The type of evaluation to perform
          example: classify
        parameters:
          oneOf:
            - $ref: '#/components/schemas/EvaluationClassifyParameters'
            - $ref: '#/components/schemas/EvaluationScoreParameters'
            - $ref: '#/components/schemas/EvaluationCompareParameters'
          description: Type-specific parameters for the evaluation
    EvaluationResponse:
      type: object
      properties:
        workflow_id:
          type: string
          description: The ID of the created evaluation job
          example: eval-1234-1244513
        status:
          type: string
          enum:
            - pending
          description: Initial status of the job
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
    EvaluationClassifyParameters:
      type: object
      required:
        - judge
        - labels
        - pass_labels
        - input_data_file_path
      properties:
        judge:
          $ref: '#/components/schemas/EvaluationJudgeModelConfig'
        labels:
          type: array
          items:
            type: string
          minItems: 2
          description: List of possible classification labels
          example:
            - 'yes'
            - 'no'
        pass_labels:
          type: array
          items:
            type: string
          minItems: 1
          description: List of labels that are considered passing
          example:
            - 'yes'
        model_to_evaluate:
          $ref: '#/components/schemas/EvaluationModelOrString'
        input_data_file_path:
          type: string
          description: Data file ID
          example: file-1234-aefd
    EvaluationScoreParameters:
      type: object
      required:
        - judge
        - min_score
        - max_score
        - pass_threshold
        - input_data_file_path
      properties:
        judge:
          $ref: '#/components/schemas/EvaluationJudgeModelConfig'
        min_score:
          type: number
          format: float
          example: 0
          description: Minimum possible score
        max_score:
          type: number
          format: float
          example: 10
          description: Maximum possible score
        pass_threshold:
          type: number
          format: float
          example: 7
          description: Score threshold for passing
        model_to_evaluate:
          $ref: '#/components/schemas/EvaluationModelOrString'
        input_data_file_path:
          type: string
          example: file-01234567890123456789
          description: Data file ID
    EvaluationCompareParameters:
      type: object
      required:
        - judge
        - input_data_file_path
      properties:
        judge:
          $ref: '#/components/schemas/EvaluationJudgeModelConfig'
        model_a:
          $ref: '#/components/schemas/EvaluationModelOrString'
        model_b:
          $ref: '#/components/schemas/EvaluationModelOrString'
        input_data_file_path:
          type: string
          description: Data file name
    EvaluationJudgeModelConfig:
      type: object
      required:
        - model
        - system_template
        - model_source
      properties:
        model:
          type: string
          description: Name of the judge model
          example: meta-llama/Llama-3-70B-Instruct-Turbo
        system_template:
          type: string
          description: System prompt template for the judge
          example: Imagine you are a helpful assistant
        model_source:
          type: string
          description: Source of the judge model.
          enum:
            - serverless
            - dedicated
            - external
        external_api_token:
          type: string
          description: Bearer/API token for external judge models.
        external_base_url:
          type: string
          description: >-
            Base URL for external judge models. Must be OpenAI-compatible base
            URL.
    EvaluationModelOrString:
      oneOf:
        - type: string
          description: Field name in the input data
        - $ref: '#/components/schemas/EvaluationModelRequest'
    EvaluationModelRequest:
      type: object
      required:
        - model
        - max_tokens
        - temperature
        - system_template
        - input_template
        - model_source
      properties:
        model:
          type: string
          description: Name of the model to evaluate
          example: meta-llama/Llama-3-70B-Instruct-Turbo
        max_tokens:
          type: integer
          minimum: 1
          description: Maximum number of tokens to generate
          example: 512
        temperature:
          type: number
          format: float
          minimum: 0
          maximum: 2
          description: Sampling temperature
          example: 0.7
        system_template:
          type: string
          description: System prompt template
          example: Imagine you are helpful assistant
        input_template:
          type: string
          description: Input prompt template
          example: Please classify {{prompt}} based on the labels below
        model_source:
          type: string
          description: Source of the model.
          enum:
            - serverless
            - dedicated
            - external
        external_api_token:
          type: string
          description: Bearer/API token for external models.
        external_base_url:
          type: string
          description: Base URL for external models. Must be OpenAI-compatible base URL
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      x-bearer-format: bearer
      x-default: default

````

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt