# Source: https://docs.wandb.ai/weave/reference/service-api/calls/trace-usage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Trace Usage

> Compute per-call usage for a trace, with descendant rollup.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /trace/usage
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /trace/usage:
    post:
      tags:
        - Calls
      summary: Trace Usage
      description: Compute per-call usage for a trace, with descendant rollup.
      operationId: trace_usage_trace_usage_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TraceUsageReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/TraceUsageRes'
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
    TraceUsageReq:
      properties:
        project_id:
          type: string
          title: Project Id
        filter:
          anyOf:
            - $ref: '#/components/schemas/CallsFilter'
            - type: 'null'
          description: >-
            Filter to select calls. Typically use trace_ids to get all calls in
            a trace.
        query:
          anyOf:
            - $ref: '#/components/schemas/Query'
            - type: 'null'
          description: Additional query conditions for filtering calls.
        include_costs:
          type: boolean
          title: Include Costs
          description: If true, include cost calculations in the usage.
          default: false
        limit:
          type: integer
          title: Limit
          description: >-
            Maximum number of calls to process. Acts as a safety limit to
            prevent unbounded memory usage.
          default: 10000
      additionalProperties: false
      type: object
      required:
        - project_id
      title: TraceUsageReq
      description: >-
        Request to compute per-call usage for a trace, with descendant rollup.


        This endpoint returns usage metrics for each call in the trace, where
        each

        call's metrics include the sum of its own usage plus all descendants'
        usage.

        Use this for trace view where you want to see rolled-up metrics per
        call.


        Note: All matching calls are loaded into memory for aggregation. For
        very large

        result sets (>10k calls), consider using more specific filters or
        pagination

        at the application layer.
    TraceUsageRes:
      properties:
        call_usage:
          additionalProperties:
            additionalProperties:
              $ref: '#/components/schemas/LLMAggregatedUsage'
            type: object
          type: object
          title: Call Usage
      type: object
      title: TraceUsageRes
      description: >-
        Response with per-call usage metrics (each includes descendant
        contributions).
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    CallsFilter:
      properties:
        op_names:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Op Names
        input_refs:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Input Refs
        output_refs:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Output Refs
        parent_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Parent Ids
        trace_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Trace Ids
        call_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Call Ids
        thread_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Thread Ids
        turn_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Turn Ids
        trace_roots_only:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Trace Roots Only
        wb_user_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Wb User Ids
        wb_run_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Wb Run Ids
      additionalProperties: false
      type: object
      title: CallsFilter
    Query:
      properties:
        $expr:
          anyOf:
            - $ref: '#/components/schemas/AndOperation'
            - $ref: '#/components/schemas/OrOperation'
            - $ref: '#/components/schemas/NotOperation'
            - $ref: '#/components/schemas/EqOperation'
            - $ref: '#/components/schemas/GtOperation'
            - $ref: '#/components/schemas/LtOperation'
            - $ref: '#/components/schemas/GteOperation'
            - $ref: '#/components/schemas/LteOperation'
            - $ref: '#/components/schemas/InOperation'
            - $ref: '#/components/schemas/ContainsOperation'
          title: $Expr
      additionalProperties: false
      type: object
      required:
        - $expr
      title: Query
    LLMAggregatedUsage:
      properties:
        requests:
          type: integer
          title: Requests
          default: 0
        prompt_tokens:
          type: integer
          title: Prompt Tokens
          default: 0
        completion_tokens:
          type: integer
          title: Completion Tokens
          default: 0
        total_tokens:
          type: integer
          title: Total Tokens
          default: 0
        prompt_tokens_total_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Prompt Tokens Total Cost
        completion_tokens_total_cost:
          anyOf:
            - type: number
            - type: 'null'
          title: Completion Tokens Total Cost
      type: object
      title: LLMAggregatedUsage
      description: Aggregated usage metrics for a specific LLM.
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
    AndOperation:
      properties:
        $and:
          items:
            anyOf:
              - $ref: '#/components/schemas/LiteralOperation'
              - $ref: '#/components/schemas/GetFieldOperator'
              - $ref: '#/components/schemas/ConvertOperation'
              - $ref: '#/components/schemas/AndOperation'
              - $ref: '#/components/schemas/OrOperation'
              - $ref: '#/components/schemas/NotOperation'
              - $ref: '#/components/schemas/EqOperation'
              - $ref: '#/components/schemas/GtOperation'
              - $ref: '#/components/schemas/LtOperation'
              - $ref: '#/components/schemas/GteOperation'
              - $ref: '#/components/schemas/LteOperation'
              - $ref: '#/components/schemas/InOperation'
              - $ref: '#/components/schemas/ContainsOperation'
          type: array
          title: $And
      type: object
      required:
        - $and
      title: AndOperation
      description: |-
        Logical AND. All conditions must evaluate to true.

        Example:
            ```
            {
                "$and": [
                    {"$eq": [{"$getField": "op_name"}, {"$literal": "predict"}]},
                    {"$gt": [{"$getField": "summary.usage.tokens"}, {"$literal": 1000}]}
                ]
            }
            ```
    OrOperation:
      properties:
        $or:
          items:
            anyOf:
              - $ref: '#/components/schemas/LiteralOperation'
              - $ref: '#/components/schemas/GetFieldOperator'
              - $ref: '#/components/schemas/ConvertOperation'
              - $ref: '#/components/schemas/AndOperation'
              - $ref: '#/components/schemas/OrOperation'
              - $ref: '#/components/schemas/NotOperation'
              - $ref: '#/components/schemas/EqOperation'
              - $ref: '#/components/schemas/GtOperation'
              - $ref: '#/components/schemas/LtOperation'
              - $ref: '#/components/schemas/GteOperation'
              - $ref: '#/components/schemas/LteOperation'
              - $ref: '#/components/schemas/InOperation'
              - $ref: '#/components/schemas/ContainsOperation'
          type: array
          title: $Or
      type: object
      required:
        - $or
      title: OrOperation
      description: |-
        Logical OR. At least one condition must be true.

        Example:
            ```
            {
                "$or": [
                    {"$eq": [{"$getField": "op_name"}, {"$literal": "a"}]},
                    {"$eq": [{"$getField": "op_name"}, {"$literal": "b"}]}
                ]
            }
            ```
    NotOperation:
      properties:
        $not:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 1
          minItems: 1
          title: $Not
      type: object
      required:
        - $not
      title: NotOperation
      description: |-
        Logical NOT. Inverts the condition.

        Example:
            ```
            {
                "$not": [
                    {"$eq": [{"$getField": "op_name"}, {"$literal": "debug"}]}
                ]
            }
            ```
    EqOperation:
      properties:
        $eq:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 2
          minItems: 2
          title: $Eq
      type: object
      required:
        - $eq
      title: EqOperation
      description: |-
        Equality check between two operands.

        Example:
            ```
            {
                "$eq": [{"$getField": "op_name"}, {"$literal": "predict"}]
            }
            ```
    GtOperation:
      properties:
        $gt:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 2
          minItems: 2
          title: $Gt
      type: object
      required:
        - $gt
      title: GtOperation
      description: |-
        Greater than comparison.

        Example:
            ```
            {
                "$gt": [{"$getField": "summary.usage.tokens"}, {"$literal": 100}]
            }
            ```
    LtOperation:
      properties:
        $lt:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 2
          minItems: 2
          title: $Lt
      type: object
      required:
        - $lt
      title: LtOperation
      description: |-
        Less than comparison.

        Example:
            ```
            {
                "$lt": [{"$getField": "summary.usage.tokens"}, {"$literal": 100}]
            }
            ```
    GteOperation:
      properties:
        $gte:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 2
          minItems: 2
          title: $Gte
      type: object
      required:
        - $gte
      title: GteOperation
      description: |-
        Greater than or equal comparison.

        Example:
            ```
            {
                "$gte": [{"$getField": "summary.usage.tokens"}, {"$literal": 100}]
            }
            ```
    LteOperation:
      properties:
        $lte:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
          type: array
          maxItems: 2
          minItems: 2
          title: $Lte
      type: object
      required:
        - $lte
      title: LteOperation
      description: |-
        Less than or equal comparison.

        Example:
            ```
            {
                "$lte": [{"$getField": "summary.usage.tokens"}, {"$literal": 100}]
            }
            ```
    InOperation:
      properties:
        $in:
          prefixItems:
            - anyOf:
                - $ref: '#/components/schemas/LiteralOperation'
                - $ref: '#/components/schemas/GetFieldOperator'
                - $ref: '#/components/schemas/ConvertOperation'
                - $ref: '#/components/schemas/AndOperation'
                - $ref: '#/components/schemas/OrOperation'
                - $ref: '#/components/schemas/NotOperation'
                - $ref: '#/components/schemas/EqOperation'
                - $ref: '#/components/schemas/GtOperation'
                - $ref: '#/components/schemas/LtOperation'
                - $ref: '#/components/schemas/GteOperation'
                - $ref: '#/components/schemas/LteOperation'
                - $ref: '#/components/schemas/InOperation'
                - $ref: '#/components/schemas/ContainsOperation'
            - items:
                anyOf:
                  - $ref: '#/components/schemas/LiteralOperation'
                  - $ref: '#/components/schemas/GetFieldOperator'
                  - $ref: '#/components/schemas/ConvertOperation'
                  - $ref: '#/components/schemas/AndOperation'
                  - $ref: '#/components/schemas/OrOperation'
                  - $ref: '#/components/schemas/NotOperation'
                  - $ref: '#/components/schemas/EqOperation'
                  - $ref: '#/components/schemas/GtOperation'
                  - $ref: '#/components/schemas/LtOperation'
                  - $ref: '#/components/schemas/GteOperation'
                  - $ref: '#/components/schemas/LteOperation'
                  - $ref: '#/components/schemas/InOperation'
                  - $ref: '#/components/schemas/ContainsOperation'
              type: array
          type: array
          maxItems: 2
          minItems: 2
          title: $In
      type: object
      required:
        - $in
      title: InOperation
      description: >-
        Membership check.


        Returns true if the left operand is in the list provided as the second
        operand.


        Example:
            ```
            {
                "$in": [
                    {"$getField": "op_name"},
                    [{"$literal": "predict"}, {"$literal": "generate"}]
                ]
            }
            ```
    ContainsOperation:
      properties:
        $contains:
          $ref: '#/components/schemas/ContainsSpec'
      type: object
      required:
        - $contains
      title: ContainsOperation
      description: |-
        Case-insensitive substring match.

        Not part of MongoDB. Weave-specific addition.

        Example:
            ```
            {
                "$contains": {
                    "input": {"$getField": "display_name"},
                    "substr": {"$literal": "llm"},
                    "case_insensitive": true
                }
            }
            ```
    LiteralOperation:
      properties:
        $literal:
          anyOf:
            - type: string
            - type: integer
            - type: number
            - type: boolean
            - additionalProperties:
                $ref: '#/components/schemas/LiteralOperation'
              type: object
            - items:
                $ref: '#/components/schemas/LiteralOperation'
              type: array
            - type: 'null'
          title: $Literal
      type: object
      required:
        - $literal
      title: LiteralOperation
      description: |-
        Represents a constant value in the query language.

        This can be any standard JSON-serializable value.

        Example:
            ```
            {"$literal": "predict"}
            ```
    GetFieldOperator:
      properties:
        $getField:
          type: string
          title: $Getfield
      type: object
      required:
        - $getField
      title: GetFieldOperator
      description: |-
        Access a field on the traced call.

        Supports dot notation for nested access, e.g. `summary.usage.tokens`.

        Only works on fields present in the `CallSchema`, including:
        - Top-level fields like `op_name`, `trace_id`, `started_at`
        - Nested fields like `inputs.input_name`, `summary.usage.tokens`, etc.

        Example:
            ```
            {"$getField": "op_name"}
            ```
    ConvertOperation:
      properties:
        $convert:
          $ref: '#/components/schemas/ConvertSpec'
      type: object
      required:
        - $convert
      title: ConvertOperation
      description: >-
        Convert the input value to a specific type (e.g., `int`, `bool`,
        `string`).


        Example:
            ```
            {
                "$convert": {
                    "input": {"$getField": "inputs.value"},
                    "to": "int"
                }
            }
            ```
    ContainsSpec:
      properties:
        input:
          anyOf:
            - $ref: '#/components/schemas/LiteralOperation'
            - $ref: '#/components/schemas/GetFieldOperator'
            - $ref: '#/components/schemas/ConvertOperation'
            - $ref: '#/components/schemas/AndOperation'
            - $ref: '#/components/schemas/OrOperation'
            - $ref: '#/components/schemas/NotOperation'
            - $ref: '#/components/schemas/EqOperation'
            - $ref: '#/components/schemas/GtOperation'
            - $ref: '#/components/schemas/LtOperation'
            - $ref: '#/components/schemas/GteOperation'
            - $ref: '#/components/schemas/LteOperation'
            - $ref: '#/components/schemas/InOperation'
            - $ref: '#/components/schemas/ContainsOperation'
          title: Input
        substr:
          anyOf:
            - $ref: '#/components/schemas/LiteralOperation'
            - $ref: '#/components/schemas/GetFieldOperator'
            - $ref: '#/components/schemas/ConvertOperation'
            - $ref: '#/components/schemas/AndOperation'
            - $ref: '#/components/schemas/OrOperation'
            - $ref: '#/components/schemas/NotOperation'
            - $ref: '#/components/schemas/EqOperation'
            - $ref: '#/components/schemas/GtOperation'
            - $ref: '#/components/schemas/LtOperation'
            - $ref: '#/components/schemas/GteOperation'
            - $ref: '#/components/schemas/LteOperation'
            - $ref: '#/components/schemas/InOperation'
            - $ref: '#/components/schemas/ContainsOperation'
          title: Substr
        case_insensitive:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Case Insensitive
          default: false
      type: object
      required:
        - input
        - substr
      title: ContainsSpec
      description: |-
        Specification for the `$contains` operation.

        - `input`: The string to search.
        - `substr`: The substring to search for.
        - `case_insensitive`: If true, match is case-insensitive.
    ConvertSpec:
      properties:
        input:
          anyOf:
            - $ref: '#/components/schemas/LiteralOperation'
            - $ref: '#/components/schemas/GetFieldOperator'
            - $ref: '#/components/schemas/ConvertOperation'
            - $ref: '#/components/schemas/AndOperation'
            - $ref: '#/components/schemas/OrOperation'
            - $ref: '#/components/schemas/NotOperation'
            - $ref: '#/components/schemas/EqOperation'
            - $ref: '#/components/schemas/GtOperation'
            - $ref: '#/components/schemas/LtOperation'
            - $ref: '#/components/schemas/GteOperation'
            - $ref: '#/components/schemas/LteOperation'
            - $ref: '#/components/schemas/InOperation'
            - $ref: '#/components/schemas/ContainsOperation'
          title: Input
        to:
          type: string
          enum:
            - double
            - string
            - int
            - bool
            - exists
          title: To
      type: object
      required:
        - input
        - to
      title: ConvertSpec
      description: |-
        Specifies conversion details for `$convert`.

        - `input`: The operand to convert.
        - `to`: The type to convert to.
  securitySchemes:
    HTTPBasic:
      type: http
      scheme: basic

````