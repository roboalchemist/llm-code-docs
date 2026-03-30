# Source: https://docs.wandb.ai/weave/reference/service-api/feedback/feedback-query.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Feedback Query

> Query for feedback.



## OpenAPI

````yaml /weave/reference/service-api/openapi.json post /feedback/query
openapi: 3.1.0
info:
  title: FastAPI
  version: 0.1.0
servers: []
security: []
paths:
  /feedback/query:
    post:
      tags:
        - Feedback
      summary: Feedback Query
      description: Query for feedback.
      operationId: feedback_query_feedback_query_post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/FeedbackQueryReq'
        required: true
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FeedbackQueryRes'
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
    FeedbackQueryReq:
      properties:
        project_id:
          type: string
          title: Project Id
          examples:
            - entity/project
        fields:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Fields
          examples:
            - - id
              - feedback_type
              - payload.note
        query:
          anyOf:
            - $ref: '#/components/schemas/Query'
            - type: 'null'
        sort_by:
          anyOf:
            - items:
                $ref: '#/components/schemas/SortBy'
              type: array
            - type: 'null'
          title: Sort By
        limit:
          anyOf:
            - type: integer
            - type: 'null'
          title: Limit
          examples:
            - 10
        offset:
          anyOf:
            - type: integer
            - type: 'null'
          title: Offset
          examples:
            - 0
      additionalProperties: false
      type: object
      required:
        - project_id
      title: FeedbackQueryReq
    FeedbackQueryRes:
      properties:
        result:
          items:
            additionalProperties: true
            type: object
          type: array
          title: Result
      type: object
      required:
        - result
      title: FeedbackQueryRes
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
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
    SortBy:
      properties:
        field:
          type: string
          title: Field
        direction:
          type: string
          enum:
            - asc
            - desc
          title: Direction
      additionalProperties: false
      type: object
      required:
        - field
        - direction
      title: SortBy
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