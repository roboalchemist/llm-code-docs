# Source: https://docs.helicone.ai/rest/session/post-v1sessionmetricsquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Session Metrics

> Search and analyze session performance metrics

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/session/metrics/query
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
  /v1/session/metrics/query:
    post:
      tags:
        - Session
      operationId: GetMetrics
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SessionMetricsQueryParams'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Result_SessionMetrics.string_'
      security:
        - api_key: []
components:
  schemas:
    SessionMetricsQueryParams:
      properties:
        nameContains:
          type: string
        timezoneDifference:
          type: number
          format: double
        pSize:
          type: string
          enum:
            - p50
            - p75
            - p95
            - p99
            - p99.9
        useInterquartile:
          type: boolean
        timeFilter:
          $ref: '#/components/schemas/TimeFilterMs'
        filter:
          $ref: '#/components/schemas/SessionFilterNode'
      required:
        - nameContains
        - timezoneDifference
      type: object
      additionalProperties: false
    Result_SessionMetrics.string_:
      anyOf:
        - $ref: '#/components/schemas/ResultSuccess_SessionMetrics_'
        - $ref: '#/components/schemas/ResultError_string_'
    TimeFilterMs:
      properties:
        startTimeUnixMs:
          type: number
          format: double
        endTimeUnixMs:
          type: number
          format: double
      required:
        - startTimeUnixMs
        - endTimeUnixMs
      type: object
      additionalProperties: false
    SessionFilterNode:
      anyOf:
        - $ref: >-
            #/components/schemas/FilterLeafSubset_request_response_rmt-or-sessions_request_response_rmt_
        - $ref: '#/components/schemas/SessionFilterBranch'
        - type: string
          enum:
            - all
    ResultSuccess_SessionMetrics_:
      properties:
        data:
          $ref: '#/components/schemas/SessionMetrics'
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
    FilterLeafSubset_request_response_rmt-or-sessions_request_response_rmt_:
      $ref: >-
        #/components/schemas/Pick_FilterLeaf.request_response_rmt-or-sessions_request_response_rmt_
    SessionFilterBranch:
      properties:
        right:
          $ref: '#/components/schemas/SessionFilterNode'
        operator:
          type: string
          enum:
            - or
            - and
        left:
          $ref: '#/components/schemas/SessionFilterNode'
      required:
        - right
        - operator
        - left
      type: object
    SessionMetrics:
      properties:
        session_count:
          items:
            $ref: '#/components/schemas/HistogramRow'
          type: array
        session_duration:
          items:
            $ref: '#/components/schemas/HistogramRow'
          type: array
        session_cost:
          items:
            $ref: '#/components/schemas/HistogramRow'
          type: array
        average:
          properties:
            session_cost:
              items:
                $ref: '#/components/schemas/AverageRow'
              type: array
            session_duration:
              items:
                $ref: '#/components/schemas/AverageRow'
              type: array
            session_count:
              items:
                $ref: '#/components/schemas/AverageRow'
              type: array
          required:
            - session_cost
            - session_duration
            - session_count
          type: object
      required:
        - session_count
        - session_duration
        - session_cost
        - average
      type: object
      additionalProperties: false
    Pick_FilterLeaf.request_response_rmt-or-sessions_request_response_rmt_:
      properties:
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
        sessions_request_response_rmt:
          $ref: '#/components/schemas/Partial_SessionsRequestResponseRMTToOperators_'
      type: object
      description: From T, pick a set of properties whose keys are in the union K
    HistogramRow:
      properties:
        range_start:
          type: string
        range_end:
          type: string
        value:
          type: number
          format: double
      required:
        - range_start
        - range_end
        - value
      type: object
      additionalProperties: false
    AverageRow:
      properties:
        average:
          type: number
          format: double
      required:
        - average
      type: object
      additionalProperties: false
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
    Partial_SessionsRequestResponseRMTToOperators_:
      properties:
        session_session_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        session_session_name:
          $ref: '#/components/schemas/Partial_TextOperators_'
        session_total_cost:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        session_total_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        session_prompt_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        session_completion_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        session_total_requests:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        session_created_at:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        session_latest_request_created_at:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        session_tag:
          $ref: '#/components/schemas/Partial_TextOperators_'
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