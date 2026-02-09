# Source: https://docs.helicone.ai/rest/evals/post-v1evalsscore-distributionsquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Score Distributions

> Analyze distribution of evaluation scores

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/evals/score-distributions/query
openapi: 3.0.0
info:
  title: helicone-api
  version: 1.0.0
  license:
    name: MIT
  contact: {}
servers:
  - url: https://api.helicone.ai/
  - url: http://localhost:8585/
security: []
paths:
  /v1/evals/score-distributions/query:
    post:
      tags:
        - Evals
      operationId: QueryScoreDistributions
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/EvalQueryParams'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_ScoreDistribution-Array.string_'
      security:
        - api_key: []
components:
  schemas:
    EvalQueryParams:
      properties:
        filter:
          $ref: '#/components/schemas/EvalFilterNode'
        timeFilter:
          properties:
            end:
              type: string
            start:
              type: string
          required:
            - end
            - start
          type: object
        offset:
          type: number
          format: double
        limit:
          type: number
          format: double
        timeZoneDifference:
          type: number
          format: double
      required:
        - filter
        - timeFilter
      type: object
      additionalProperties: false
    Result_ScoreDistribution-Array.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_ScoreDistribution-Array_'
        - $ref: '#/components/schemas/ResultError_string_'
    EvalFilterNode:
      anyOf:
        - $ref: '#/components/schemas/FilterLeafSubset_request_response_rmt_'
        - $ref: '#/components/schemas/EvalFilterBranch'
        - type: string
          enum:
            - all
    ResultSuccess_ScoreDistribution-Array_:
      properties:
        data:
          items:
            $ref: '#/components/schemas/ScoreDistribution'
          type: array
        error:
          type: number
          enum:
            - null
          nullable: true
      required:
        - data
        - error
      type: object
      additionalProperties: false
    ResultError_string_:
      properties:
        data:
          type: number
          enum:
            - null
          nullable: true
        error:
          type: string
      required:
        - data
        - error
      type: object
      additionalProperties: false
    FilterLeafSubset_request_response_rmt_:
      $ref: '#/components/schemas/Pick_FilterLeaf.request_response_rmt_'
    EvalFilterBranch:
      properties:
        right:
          $ref: '#/components/schemas/EvalFilterNode'
        operator:
          type: string
          enum:
            - or
            - and
        left:
          $ref: '#/components/schemas/EvalFilterNode'
      required:
        - right
        - operator
        - left
      type: object
    ScoreDistribution:
      properties:
        name:
          type: string
        distribution:
          items:
            properties:
              value:
                type: number
                format: double
              upper:
                type: number
                format: double
              lower:
                type: number
                format: double
            required:
              - value
              - upper
              - lower
            type: object
          type: array
      required:
        - name
        - distribution
      type: object
      additionalProperties: false
    Pick_FilterLeaf.request_response_rmt_:
      properties:
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
      type: object
      description: From T, pick a set of properties whose keys are in the union K
    Partial_RequestResponseRMTToOperators_:
      properties:
        country_code:
          $ref: '#/components/schemas/Partial_TextOperators_'
        latency:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        cost:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        provider:
          $ref: '#/components/schemas/Partial_TextOperators_'
        time_to_first_token:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        status:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        request_created_at:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        response_created_at:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        model:
          $ref: '#/components/schemas/Partial_TextOperators_'
        user_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        organization_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        node_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        job_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        threat:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
        request_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        prompt_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        completion_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        prompt_cache_read_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        prompt_cache_write_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        total_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        target_url:
          $ref: '#/components/schemas/Partial_TextOperators_'
        property_key:
          properties:
            equals:
              type: string
          required:
            - equals
          type: object
        properties:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/Partial_TextOperators_'
          type: object
        search_properties:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/Partial_TextOperators_'
          type: object
        scores:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/Partial_TextOperators_'
          type: object
        scores_column:
          $ref: '#/components/schemas/Partial_TextOperators_'
        request_body:
          $ref: '#/components/schemas/Partial_TextOperators_'
        response_body:
          $ref: '#/components/schemas/Partial_TextOperators_'
        cache_enabled:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
        cache_reference_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        cached:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
        assets:
          $ref: '#/components/schemas/Partial_TextOperators_'
        helicone-score-feedback:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
        prompt_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        prompt_version:
          $ref: '#/components/schemas/Partial_TextOperators_'
        request_referrer:
          $ref: '#/components/schemas/Partial_TextOperators_'
        is_passthrough_billing:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
      type: object
      description: Make all properties in T optional
    Partial_TextOperators_:
      properties:
        not-equals:
          type: string
        equals:
          type: string
        like:
          type: string
        ilike:
          type: string
        contains:
          type: string
        not-contains:
          type: string
      type: object
      description: Make all properties in T optional
    Partial_NumberOperators_:
      properties:
        not-equals:
          type: number
          format: double
        equals:
          type: number
          format: double
        gte:
          type: number
          format: double
        lte:
          type: number
          format: double
        lt:
          type: number
          format: double
        gt:
          type: number
          format: double
      type: object
      description: Make all properties in T optional
    Partial_TimestampOperatorsTyped_:
      properties:
        equals:
          type: string
          format: date-time
        gte:
          type: string
          format: date-time
        lte:
          type: string
          format: date-time
        lt:
          type: string
          format: date-time
        gt:
          type: string
          format: date-time
      type: object
      description: Make all properties in T optional
    Partial_BooleanOperators_:
      properties:
        equals:
          type: boolean
      type: object
      description: Make all properties in T optional
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````