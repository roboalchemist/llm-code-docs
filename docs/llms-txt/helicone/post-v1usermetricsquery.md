# Source: https://docs.helicone.ai/rest/user/post-v1usermetricsquery.md

# Query User Metrics

> Search and filter through user-specific metrics

## OpenAPI

````yaml post /v1/user/metrics/query
paths:
  path: /v1/user/metrics/query
  method: post
  servers:
    - url: https://api.helicone.ai/
    - url: http://localhost:8585/
  request:
    security:
      - title: api key
        parameters:
          query: {}
          header:
            Authorization:
              type: apiKey
              description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''
          cookie: {}
    parameters:
      path: {}
      query: {}
      header: {}
      cookie: {}
    body:
      application/json:
        schemaArray:
          - type: object
            properties:
              filter:
                allOf:
                  - $ref: '#/components/schemas/UserFilterNode'
              offset:
                allOf:
                  - type: number
                    format: double
              limit:
                allOf:
                  - type: number
                    format: double
              timeFilter:
                allOf:
                  - properties:
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
                allOf:
                  - type: number
                    format: double
              sort:
                allOf:
                  - $ref: '#/components/schemas/SortLeafUsers'
            required: true
            refIdentifier: '#/components/schemas/UserMetricsQueryParams'
            requiredProperties:
              - filter
              - offset
              - limit
            additionalProperties: false
        examples:
          example:
            value:
              filter:
                users_view:
                  user_user_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  user_active_for:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_first_active:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  user_last_active:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  user_total_requests:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_average_requests_per_day_active:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_average_tokens_per_request:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_total_completion_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_total_prompt_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  user_cost:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                request_response_rmt:
                  country_code:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  latency:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  cost:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  provider:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  time_to_first_token:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  status:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  request_created_at:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  response_created_at:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  model:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  user_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  organization_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  node_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  job_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  threat:
                    equals: true
                  request_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  prompt_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  completion_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  prompt_cache_read_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  prompt_cache_write_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  total_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  target_url:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  property_key:
                    equals: <string>
                  properties: {}
                  search_properties: {}
                  scores: {}
                  scores_column:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  request_body:
                    contains: <string>
                  response_body:
                    contains: <string>
                  cache_enabled:
                    equals: true
                  cache_reference_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  cached:
                    equals: true
                  assets:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  helicone-score-feedback:
                    equals: true
                  prompt_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  prompt_version:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  request_referrer:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  is_passthrough_billing:
                    equals: true
              offset: 123
              limit: 123
              timeFilter:
                endTimeUnixSeconds: 123
                startTimeUnixSeconds: 123
              timeZoneDifferenceMinutes: 123
              sort:
                id: asc
                user_id: asc
                active_for: asc
                first_active: asc
                last_active: asc
                total_requests: asc
                average_requests_per_day_active: asc
                average_tokens_per_request: asc
                total_prompt_tokens: asc
                total_completion_tokens: asc
                cost: asc
                rate_limited_count: asc
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - properties:
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
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ResultSuccess__users-UserMetricsResult-Array--count-number--hasUsers-boolean__
            requiredProperties:
              - data
              - error
            additionalProperties: false
          - type: object
            properties:
              data:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
              error:
                allOf:
                  - type: string
            refIdentifier: '#/components/schemas/ResultError_string_'
            requiredProperties:
              - data
              - error
            additionalProperties: false
        examples:
          example:
            value:
              data:
                hasUsers: true
                count: 123
                users:
                  - id: <string>
                    user_id: <string>
                    active_for: 123
                    first_active: <string>
                    last_active: <string>
                    total_requests: 123
                    average_requests_per_day_active: 123
                    average_tokens_per_request: 123
                    total_completion_tokens: 123
                    total_prompt_tokens: 123
                    cost: 123
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
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
    Partial_BooleanOperators_:
      properties:
        equals:
          type: boolean
      type: object
      description: Make all properties in T optional
    Partial_VectorOperators_:
      properties:
        contains:
          type: string
      type: object
      description: Make all properties in T optional
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
          $ref: '#/components/schemas/Partial_VectorOperators_'
        response_body:
          $ref: '#/components/schemas/Partial_VectorOperators_'
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
    Pick_FilterLeaf.users_view-or-request_response_rmt_:
      properties:
        users_view:
          $ref: '#/components/schemas/Partial_UserViewToOperators_'
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
      type: object
      description: From T, pick a set of properties whose keys are in the union K
    FilterLeafSubset_users_view-or-request_response_rmt_:
      $ref: '#/components/schemas/Pick_FilterLeaf.users_view-or-request_response_rmt_'
    UserFilterNode:
      anyOf:
        - $ref: >-
            #/components/schemas/FilterLeafSubset_users_view-or-request_response_rmt_
        - $ref: '#/components/schemas/UserFilterBranch'
        - type: string
          enum:
            - all
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
    SortDirection:
      type: string
      enum:
        - asc
        - desc
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

````