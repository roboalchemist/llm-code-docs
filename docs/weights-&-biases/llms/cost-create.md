# Source: https://docs.wandb.ai/weave/reference/service-api/costs/cost-create.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cost Create



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /cost/create
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /cost/create:
    post:
      tags:
        - Costs
      summary: Cost Create
      operationId: cost_create_cost_create_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CostCreateReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CostCreateRes'
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - HTTPBasic: []
components:
  schemas:
    CostCreateReq:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        costs:
          additionalProperties:
            $ref: '#/components/schemas/CostCreateInput'
          type: object
          title: Costs
        wb_user_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Wb User Id
          description: Do not set directly. Server will automatically populate this field.
      additionalProperties: false
      type: object
      required:
        - project_id
        - costs
      title: CostCreateReq
    CostCreateRes:
      properties:
        ids:
          items:
            prefixItems:
              - type: string
              - type: string
            type: array
            maxItems: 2
            minItems: 2
          type: array
          title: Ids
      type: object
      required:
        - ids
      title: CostCreateRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CostCreateInput:
      properties:
        prompt_token_cost:
          type: number
          title: Prompt Token Cost
        completion_token_cost:
          type: number
          title: Completion Token Cost
        prompt_token_cost_unit:
          anyOf:
            - type: string
            - type: 'null'
          title: Prompt Token Cost Unit
          description: The unit of the cost for the prompt tokens
          default: USD
        completion_token_cost_unit:
          anyOf:
            - type: string
            - type: 'null'
          title: Completion Token Cost Unit
          description: The unit of the cost for the completion tokens
          default: USD
        effective_date:
          anyOf:
            - type: string
              format: date-time
            - type: 'null'
          title: Effective Date
          description: >-
            The date after which the cost is effective for, will default to the
            current date if not provided
        provider_id:
          anyOf:
            - type: string
            - type: 'null'
          title: Provider Id
          description: >-
            The provider of the LLM, e.g. 'openai' or 'mistral'. If not
            provided, the provider_id will be set to 'default'
      additionalProperties: false
      type: object
      required:
        - prompt_token_cost
        - completion_token_cost
      title: CostCreateInput
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````