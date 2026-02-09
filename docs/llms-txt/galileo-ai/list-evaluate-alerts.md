# Source: https://docs.galileo.ai/api-reference/evaluate-alerts/list-evaluate-alerts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.galileo.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List Evaluate Alerts



## OpenAPI

````yaml https://api.staging.galileo.ai/public/v1/openapi.json get /v1/projects/{project_id}/runs/{run_id}/prompts/alerts
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers:
  - url: https://api.staging.galileo.ai
    description: Galileo Public APIs - staging
security: []
paths:
  /v1/projects/{project_id}/runs/{run_id}/prompts/alerts:
    get:
      tags:
        - evaluate-alerts
      summary: List Evaluate Alerts
      operationId: >-
        list_evaluate_alerts_v1_projects__project_id__runs__run_id__prompts_alerts_get
      parameters:
        - name: run_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Run Id
        - name: project_id
          in: path
          required: true
          schema:
            type: string
            format: uuid4
            title: Project Id
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/EvaluateAlertDB'
                title: >-
                  Response List Evaluate Alerts V1 Projects  Project Id  Runs 
                  Run Id  Prompts Alerts Get
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
      security:
        - APIKeyHeader: []
        - OAuth2PasswordBearer: []
        - HTTPBasic: []
components:
  schemas:
    EvaluateAlertDB:
      properties:
        project_id:
          type: string
          format: uuid4
          title: Project Id
        run_id:
          type: string
          format: uuid4
          title: Run Id
        alert_name:
          type: string
          title: Alert Name
        filter:
          oneOf:
            - $ref: '#/components/schemas/RangePromptFilterParam'
            - $ref: '#/components/schemas/ValuePromptFilterParam'
            - $ref: '#/components/schemas/CategoricalPromptFilterParam'
          title: Filter
          discriminator:
            propertyName: filter_type
            mapping:
              category: '#/components/schemas/CategoricalPromptFilterParam'
              range: '#/components/schemas/RangePromptFilterParam'
              value: '#/components/schemas/ValuePromptFilterParam'
        field_name:
          type: string
          title: Field Name
        description:
          type: string
          title: Description
        extra:
          anyOf:
            - additionalProperties: true
              type: object
            - type: 'null'
          title: Extra
        id:
          type: string
          format: uuid4
          title: Id
        created_at:
          type: string
          format: date-time
          title: Created At
        updated_at:
          type: string
          format: date-time
          title: Updated At
      type: object
      required:
        - project_id
        - run_id
        - alert_name
        - filter
        - field_name
        - description
        - id
        - created_at
        - updated_at
      title: EvaluateAlertDB
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    RangePromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: range
          title: Filter Type
        low:
          type: number
          title: Low
        high:
          type: number
          title: High
      type: object
      required:
        - column
        - filter_type
        - low
        - high
      title: RangePromptFilterParam
    ValuePromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: value
          title: Filter Type
        value:
          anyOf:
            - type: integer
            - type: number
            - type: boolean
            - type: string
          title: Value
        relation:
          $ref: '#/components/schemas/Operator'
      type: object
      required:
        - column
        - filter_type
        - value
        - relation
      title: ValuePromptFilterParam
    CategoricalPromptFilterParam:
      properties:
        column:
          type: string
          title: Column
        filter_type:
          type: string
          const: category
          title: Filter Type
        categories:
          items:
            type: string
          type: array
          title: Categories
        operator:
          $ref: '#/components/schemas/CategoryFilterOperator'
          description: >-
            Operator to use when checking if the value is in the categories. If
            None, we default to 'or'.
          default: any
      type: object
      required:
        - column
        - filter_type
        - categories
      title: CategoricalPromptFilterParam
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
    Operator:
      type: string
      enum:
        - eq
        - ne
        - gt
        - gte
        - lt
        - lte
        - in
        - not_in
        - contains
        - has_all
        - between
        - like
      title: Operator
    CategoryFilterOperator:
      type: string
      enum:
        - any
        - all
        - exact
        - none
      title: CategoryFilterOperator
  securitySchemes:
    APIKeyHeader:
      type: apiKey
      in: header
      name: Galileo-API-Key
    OAuth2PasswordBearer:
      type: oauth2
      flows:
        password:
          scopes: {}
          tokenUrl: https://api.staging.galileo.ai/login
    HTTPBasic:
      type: http
      scheme: basic

````