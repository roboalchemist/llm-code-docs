# Source: https://docs.helicone.ai/rest/user/post-v1usermetricsquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query User Metrics

> Search and filter through user-specific metrics

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/user/metrics/query
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
  /v1/user/metrics/query:
    post:
      tags:
        - User
      operationId: GetUserMetrics
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserMetricsQueryParams'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Result__users-UserMetricsResult-Array--count-number--hasUsers-boolean_.string_
      security:
        - api_key: []
components:
  schemas:
    UserMetricsQueryParams:
      properties:
        filter:
          $ref: '#/components/schemas/UserFilterNode'
        offset:
          type: number
          format: double
        limit:
          type: number
          format: double
        timeFilter:
          properties:
            endTimeUnixSeconds:
              type: number
              format: double
            startTimeUnixSeconds:
              type: number
              format: double
          required:
            - endTimeUnixSeconds
            - startTimeUnixSeconds
          type: object
        timeZoneDifferenceMinutes:
          type: number
          format: double
        sort:
          $ref: '#/components/schemas/SortLeafUsers'
      required:
        - filter
        - offset
        - limit
      type: object
      additionalProperties: false
    Result__users-UserMetricsResult-Array--count-number--hasUsers-boolean_.string_:
      anyOf:
        - $ref: >-
            #/components/schemas/ResultSuccess__users-UserMetricsResult-Array--count-number--hasUsers-boolean__
        - $ref: '#/components/schemas/ResultError_string_'
    UserFilterNode:
      anyOf:
        - $ref: >-
            #/components/schemas/FilterLeafSubset_users_view-or-request_response_rmt_
        - $ref: '#/components/schemas/UserFilterBranch'
        - type: string
          enum:
            - all
    SortLeafUsers:
      properties:
        id:
          $ref: '#/components/schemas/SortDirection'
        user_id:
          $ref: '#/components/schemas/SortDirection'
        active_for:
          $ref: '#/components/schemas/SortDirection'
        first_active:
          $ref: '#/components/schemas/SortDirection'
        last_active:
          $ref: '#/components/schemas/SortDirection'
        total_requests:
          $ref: '#/components/schemas/SortDirection'
        average_requests_per_day_active:
          $ref: '#/components/schemas/SortDirection'
        average_tokens_per_request:
          $ref: '#/components/schemas/SortDirection'
        total_prompt_tokens:
          $ref: '#/components/schemas/SortDirection'
        total_completion_tokens:
          $ref: '#/components/schemas/SortDirection'
        cost:
          $ref: '#/components/schemas/SortDirection'
        rate_limited_count:
          $ref: '#/components/schemas/SortDirection'
      type: object
    ResultSuccess__users-UserMetricsResult-Array--count-number--hasUsers-boolean__:
      properties:
        data:
          properties:
            hasUsers:
              type: boolean
            count:
              type: number
              format: double
            users:
              items:
                $ref: '#/components/schemas/UserMetricsResult'
              type: array
          required:
            - hasUsers
            - count
            - users
          type: object
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
    FilterLeafSubset_users_view-or-request_response_rmt_:
      $ref: '#/components/schemas/Pick_FilterLeaf.users_view-or-request_response_rmt_'
    UserFilterBranch:
      properties:
        right:
          $ref: '#/components/schemas/UserFilterNode'
        operator:
          type: string
          enum:
            - or
            - and
        left:
          $ref: '#/components/schemas/UserFilterNode'
      required:
        - right
        - operator
        - left
      type: object
    SortDirection:
      type: string
      enum:
        - asc
        - desc
    UserMetricsResult:
      properties:
        id:
          type: string
        user_id:
          type: string
        active_for:
          type: number
          format: double
        first_active:
          type: string
        last_active:
          type: string
        total_requests:
          type: number
          format: double
        average_requests_per_day_active:
          type: number
          format: double
        average_tokens_per_request:
          type: number
          format: double
        total_completion_tokens:
          type: number
          format: double
        total_prompt_tokens:
          type: number
          format: double
        cost:
          type: number
          format: double
      required:
        - id
        - user_id
        - active_for
        - first_active
        - last_active
        - total_requests
        - average_requests_per_day_active
        - average_tokens_per_request
        - total_completion_tokens
        - total_prompt_tokens
        - cost
      type: object
      additionalProperties: false
    Pick_FilterLeaf.users_view-or-request_response_rmt_:
      properties:
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
        users_view:
          $ref: '#/components/schemas/Partial_UserViewToOperators_'
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
    Partial_UserViewToOperators_:
      properties:
        user_user_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        user_active_for:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_first_active:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        user_last_active:
          $ref: '#/components/schemas/Partial_TimestampOperatorsTyped_'
        user_total_requests:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_average_requests_per_day_active:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_average_tokens_per_request:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_total_completion_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_total_prompt_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        user_cost:
          $ref: '#/components/schemas/Partial_NumberOperators_'
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