# Source: https://www.traceloop.com/docs/api-reference/auto-monitor-setups/get-an-auto-monitor-setup-by-id.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.traceloop.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get an auto monitor setup by ID

> Get a specific auto monitor setup by its ID



## OpenAPI

````yaml get /v2/auto-monitor-setups/{setup_id}
openapi: 3.0.0
info:
  title: Traceloop API
  version: 1.0.0
  contact: {}
servers:
  - url: https://api.traceloop.com
security: []
paths:
  /v2/auto-monitor-setups/{setup_id}:
    get:
      tags:
        - auto-monitor-setups
      summary: Get an auto monitor setup by ID
      description: Get a specific auto monitor setup by its ID
      parameters:
        - description: Auto monitor setup ID
          in: path
          name: setup_id
          required: true
          schema:
            type: string
      responses:
        '200':
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.AutoMonitorSetupResponse'
        '404':
          description: Not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
        '500':
          description: Internal error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/response.ErrorResponse'
components:
  schemas:
    response.AutoMonitorSetupResponse:
      properties:
        created_at:
          type: string
        entity_type:
          type: string
        entity_value:
          type: string
        env_project_id:
          type: string
        evaluators:
          items:
            $ref: '#/components/schemas/response.AutoMonitorEvaluatorResponse'
          type: array
        external_id:
          type: string
        id:
          type: string
        init_rules:
          items:
            $ref: '#/components/schemas/evaluator.Rule'
          type: array
        org_id:
          type: string
        project_id:
          type: string
        status:
          type: string
        updated_at:
          type: string
      type: object
    response.ErrorResponse:
      description: Standard error response structure
      properties:
        error:
          example: error message
          type: string
      type: object
    response.AutoMonitorEvaluatorResponse:
      properties:
        binding_id:
          type: string
        error_message:
          type: string
        evaluator_id:
          type: string
        evaluator_type:
          type: string
        input_schema:
          items:
            $ref: '#/components/schemas/evaluator.Property'
          type: array
        output_schema:
          items:
            $ref: '#/components/schemas/evaluator.Property'
          type: array
        processed_at:
          type: string
        status:
          type: string
      type: object
    evaluator.Rule:
      properties:
        key:
          type: string
        op:
          $ref: '#/components/schemas/evaluator.ComparisonOperator'
        source:
          type: string
        value:
          type: string
        value_type:
          type: string
      required:
        - op
        - source
      type: object
    evaluator.Property:
      properties:
        description:
          type: string
        label:
          type: string
        name:
          type: string
        type:
          type: string
      required:
        - name
        - type
      type: object
    evaluator.ComparisonOperator:
      enum:
        - equals
        - not_equals
        - contains
        - exists
        - not_exists
        - greater_than
        - less_than
        - starts_with
      type: string
      x-enum-varnames:
        - ComparisonOperatorEquals
        - ComparisonOperatorNotEquals
        - ComparisonOperatorContains
        - ComparisonOperatorExists
        - ComparisonOperatorNotExists
        - ComparisonOperatorGreaterThan
        - ComparisonOperatorLessThan
        - ComparisonOperatorStartsWith

````