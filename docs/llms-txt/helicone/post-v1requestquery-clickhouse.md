# Source: https://docs.helicone.ai/rest/request/post-v1requestquery-clickhouse.md

# Get Requests

> Retrieve all requests visible in the request table at Helicone.

## OpenAPI

````yaml post /v1/request/query-clickhouse
paths:
  path: /v1/request/query-clickhouse
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
                  - $ref: '#/components/schemas/RequestFilterNode'
              offset:
                allOf:
                  - type: number
                    format: double
              limit:
                allOf:
                  - type: number
                    format: double
              sort:
                allOf:
                  - $ref: '#/components/schemas/SortLeafRequest'
              isCached:
                allOf:
                  - type: boolean
              includeInputs:
                allOf:
                  - type: boolean
              isPartOfExperiment:
                allOf:
                  - type: boolean
              isScored:
                allOf:
                  - type: boolean
            required: true
            refIdentifier: '#/components/schemas/RequestQueryParams'
            requiredProperties:
              - filter
            additionalProperties: false
        examples:
          example:
            value:
              filter:
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
                response:
                  body_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  body_model:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  body_completion:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  status:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  model:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                request:
                  prompt:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  created_at:
                    equals: <string>
                    gte: <string>
                    lte: <string>
                    lt: <string>
                    gt: <string>
                  user_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  auth_hash:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  org_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  id:
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
                  model:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  modelOverride:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  path:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  country_code:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  prompt_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                feedback:
                  id:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  created_at:
                    equals: <string>
                    gte: <string>
                    lte: <string>
                    lt: <string>
                    gt: <string>
                  rating:
                    equals: true
                  response_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                sessions_request_response_rmt:
                  session_session_id:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  session_session_name:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                  session_total_cost:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  session_total_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  session_prompt_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  session_completion_tokens:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  session_total_requests:
                    not-equals: 123
                    equals: 123
                    gte: 123
                    lte: 123
                    lt: 123
                    gt: 123
                  session_created_at:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  session_latest_request_created_at:
                    equals: '2023-11-07T05:31:56Z'
                    gte: '2023-11-07T05:31:56Z'
                    lte: '2023-11-07T05:31:56Z'
                    lt: '2023-11-07T05:31:56Z'
                    gt: '2023-11-07T05:31:56Z'
                  session_tag:
                    not-equals: <string>
                    equals: <string>
                    like: <string>
                    ilike: <string>
                    contains: <string>
                    not-contains: <string>
                properties: {}
                values: {}
              offset: 123
              limit: 123
              sort:
                random: true
                created_at: asc
                cache_created_at: asc
                latency: asc
                last_active: asc
                total_tokens: asc
                completion_tokens: asc
                prompt_tokens: asc
                user_id: asc
                body_model: asc
                is_cached: asc
                request_prompt: asc
                response_text: asc
                properties: {}
                values: {}
                cost: asc
              isCached: true
              includeInputs: true
              isPartOfExperiment: true
              isScored: true
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - items:
                      $ref: '#/components/schemas/HeliconeRequest'
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_HeliconeRequest-Array_'
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
          Example 1:
            value:
              filter: {}
              isCached: false
              limit: 10
              offset: 0
              sort:
                created_at: desc
              isScored: false
              isPartOfExperiment: false
        description: Ok
  deprecated: false
  type: path
components:
  schemas:
    Record_string.any_:
      properties: {}
      additionalProperties: {}
      type: object
      description: Construct a type with a set of properties K of type T
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
    SortDirection:
      type: string
      enum:
        - asc
        - desc
    Record_string.string_:
      properties: {}
      additionalProperties:
        type: string
      type: object
      description: Construct a type with a set of properties K of type T
    Record_string.number_:
      properties: {}
      additionalProperties:
        type: number
        format: double
      type: object
      description: Construct a type with a set of properties K of type T
    Partial_ResponseTableToOperators_:
      properties:
        body_tokens:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        body_model:
          $ref: '#/components/schemas/Partial_TextOperators_'
        body_completion:
          $ref: '#/components/schemas/Partial_TextOperators_'
        status:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        model:
          $ref: '#/components/schemas/Partial_TextOperators_'
      type: object
      description: Make all properties in T optional
    Partial_TimestampOperators_:
      properties:
        equals:
          type: string
        gte:
          type: string
        lte:
          type: string
        lt:
          type: string
        gt:
          type: string
      type: object
      description: Make all properties in T optional
    Partial_RequestTableToOperators_:
      properties:
        prompt:
          $ref: '#/components/schemas/Partial_TextOperators_'
        created_at:
          $ref: '#/components/schemas/Partial_TimestampOperators_'
        user_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        auth_hash:
          $ref: '#/components/schemas/Partial_TextOperators_'
        org_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        node_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
        model:
          $ref: '#/components/schemas/Partial_TextOperators_'
        modelOverride:
          $ref: '#/components/schemas/Partial_TextOperators_'
        path:
          $ref: '#/components/schemas/Partial_TextOperators_'
        country_code:
          $ref: '#/components/schemas/Partial_TextOperators_'
        prompt_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
      type: object
      description: Make all properties in T optional
    Partial_FeedbackTableToOperators_:
      properties:
        id:
          $ref: '#/components/schemas/Partial_NumberOperators_'
        created_at:
          $ref: '#/components/schemas/Partial_TimestampOperators_'
        rating:
          $ref: '#/components/schemas/Partial_BooleanOperators_'
        response_id:
          $ref: '#/components/schemas/Partial_TextOperators_'
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
    Pick_FilterLeaf.feedback-or-request-or-response-or-properties-or-values-or-request_response_rmt-or-sessions_request_response_rmt_:
      properties:
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
        response:
          $ref: '#/components/schemas/Partial_ResponseTableToOperators_'
        request:
          $ref: '#/components/schemas/Partial_RequestTableToOperators_'
        feedback:
          $ref: '#/components/schemas/Partial_FeedbackTableToOperators_'
        sessions_request_response_rmt:
          $ref: '#/components/schemas/Partial_SessionsRequestResponseRMTToOperators_'
        properties:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/Partial_TextOperators_'
          type: object
        values:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/Partial_TextOperators_'
          type: object
      type: object
      description: From T, pick a set of properties whose keys are in the union K
    FilterLeafSubset_feedback-or-request-or-response-or-properties-or-values-or-request_response_rmt-or-sessions_request_response_rmt_:
      $ref: >-
        #/components/schemas/Pick_FilterLeaf.feedback-or-request-or-response-or-properties-or-values-or-request_response_rmt-or-sessions_request_response_rmt_
    RequestFilterNode:
      anyOf:
        - $ref: >-
            #/components/schemas/FilterLeafSubset_feedback-or-request-or-response-or-properties-or-values-or-request_response_rmt-or-sessions_request_response_rmt_
        - $ref: '#/components/schemas/RequestFilterBranch'
        - type: string
          enum:
            - all
    RequestFilterBranch:
      properties:
        right:
          $ref: '#/components/schemas/RequestFilterNode'
        operator:
          type: string
          enum:
            - or
            - and
        left:
          $ref: '#/components/schemas/RequestFilterNode'
      required:
        - right
        - operator
        - left
      type: object
    SortLeafRequest:
      properties:
        random:
          type: boolean
          enum:
            - true
          nullable: false
        created_at:
          $ref: '#/components/schemas/SortDirection'
        cache_created_at:
          $ref: '#/components/schemas/SortDirection'
        latency:
          $ref: '#/components/schemas/SortDirection'
        last_active:
          $ref: '#/components/schemas/SortDirection'
        total_tokens:
          $ref: '#/components/schemas/SortDirection'
        completion_tokens:
          $ref: '#/components/schemas/SortDirection'
        prompt_tokens:
          $ref: '#/components/schemas/SortDirection'
        user_id:
          $ref: '#/components/schemas/SortDirection'
        body_model:
          $ref: '#/components/schemas/SortDirection'
        is_cached:
          $ref: '#/components/schemas/SortDirection'
        request_prompt:
          $ref: '#/components/schemas/SortDirection'
        response_text:
          $ref: '#/components/schemas/SortDirection'
        properties:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/SortDirection'
          type: object
        values:
          properties: {}
          additionalProperties:
            $ref: '#/components/schemas/SortDirection'
          type: object
        cost:
          $ref: '#/components/schemas/SortDirection'
      type: object
      additionalProperties: false
    ProviderName:
      type: string
      enum:
        - OPENAI
        - ANTHROPIC
        - AZURE
        - LOCAL
        - HELICONE
        - AMDBARTEK
        - ANYSCALE
        - CLOUDFLARE
        - 2YFV
        - TOGETHER
        - LEMONFOX
        - FIREWORKS
        - PERPLEXITY
        - GOOGLE
        - OPENROUTER
        - WISDOMINANUTSHELL
        - GROQ
        - COHERE
        - MISTRAL
        - DEEPINFRA
        - QSTASH
        - FIRECRAWL
        - AWS
        - BEDROCK
        - DEEPSEEK
        - X
        - AVIAN
        - NEBIUS
        - NOVITA
        - OPENPIPE
        - CHUTES
        - LLAMA
        - NVIDIA
        - VERCEL
        - CEREBRAS
        - BASETEN
    ModelProviderName:
      type: string
      enum:
        - baseten
        - anthropic
        - azure
        - bedrock
        - cerebras
        - chutes
        - deepinfra
        - deepseek
        - fireworks
        - google-ai-studio
        - groq
        - helicone
        - mistral
        - nebius
        - novita
        - openai
        - openrouter
        - perplexity
        - vertex
        - xai
      nullable: false
    Provider:
      anyOf:
        - $ref: '#/components/schemas/ProviderName'
        - $ref: '#/components/schemas/ModelProviderName'
        - type: string
          enum:
            - CUSTOM
    LlmType:
      type: string
      enum:
        - chat
        - completion
    FunctionCall:
      properties:
        id:
          type: string
        name:
          type: string
        arguments:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - name
        - arguments
      type: object
      additionalProperties: false
    Message:
      properties:
        ending_event_id:
          type: string
        trigger_event_id:
          type: string
        start_timestamp:
          type: string
        annotations:
          items:
            properties:
              content:
                type: string
              title:
                type: string
              url:
                type: string
              type:
                type: string
                enum:
                  - url_citation
                nullable: false
            required:
              - title
              - url
              - type
            type: object
          type: array
        reasoning:
          type: string
        deleted:
          type: boolean
        contentArray:
          items:
            $ref: '#/components/schemas/Message'
          type: array
        idx:
          type: number
          format: double
        detail:
          type: string
        filename:
          type: string
        file_id:
          type: string
        file_data:
          type: string
        type:
          type: string
          enum:
            - input_image
            - input_text
            - input_file
        audio_data:
          type: string
        image_url:
          type: string
        timestamp:
          type: string
        tool_call_id:
          type: string
        tool_calls:
          items:
            $ref: '#/components/schemas/FunctionCall'
          type: array
        mime_type:
          type: string
        content:
          type: string
        name:
          type: string
        instruction:
          type: string
        role:
          anyOf:
            - type: string
            - type: string
              enum:
                - user
                - assistant
                - system
                - developer
        id:
          type: string
        _type:
          type: string
          enum:
            - functionCall
            - function
            - image
            - file
            - message
            - autoInput
            - contentArray
            - audio
      required:
        - _type
      type: object
    Tool:
      properties:
        name:
          type: string
        description:
          type: string
        parameters:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - name
        - description
      type: object
      additionalProperties: false
    HeliconeEventTool:
      properties:
        _type:
          type: string
          enum:
            - tool
          nullable: false
        toolName:
          type: string
        input: {}
      required:
        - _type
        - toolName
        - input
      type: object
      additionalProperties: {}
    HeliconeEventVectorDB:
      properties:
        _type:
          type: string
          enum:
            - vector_db
          nullable: false
        operation:
          type: string
          enum:
            - search
            - insert
            - delete
            - update
        text:
          type: string
        vector:
          items:
            type: number
            format: double
          type: array
        topK:
          type: number
          format: double
        filter:
          additionalProperties: false
          type: object
        databaseName:
          type: string
      required:
        - _type
        - operation
      type: object
      additionalProperties: {}
    HeliconeEventData:
      properties:
        _type:
          type: string
          enum:
            - data
          nullable: false
        name:
          type: string
        meta:
          $ref: '#/components/schemas/Record_string.any_'
      required:
        - _type
        - name
      type: object
      additionalProperties: {}
    LLMRequestBody:
      properties:
        llm_type:
          $ref: '#/components/schemas/LlmType'
        provider:
          type: string
        model:
          type: string
        messages:
          items:
            $ref: '#/components/schemas/Message'
          type: array
          nullable: true
        prompt:
          type: string
          nullable: true
        instructions:
          type: string
          nullable: true
        max_tokens:
          type: number
          format: double
          nullable: true
        temperature:
          type: number
          format: double
          nullable: true
        top_p:
          type: number
          format: double
          nullable: true
        seed:
          type: number
          format: double
          nullable: true
        stream:
          type: boolean
          nullable: true
        presence_penalty:
          type: number
          format: double
          nullable: true
        frequency_penalty:
          type: number
          format: double
          nullable: true
        stop:
          anyOf:
            - items:
                type: string
              type: array
            - type: string
          nullable: true
        reasoning_effort:
          type: string
          enum:
            - minimal
            - low
            - medium
            - high
            - null
          nullable: true
        verbosity:
          type: string
          enum:
            - low
            - medium
            - high
            - null
          nullable: true
        tools:
          items:
            $ref: '#/components/schemas/Tool'
          type: array
        parallel_tool_calls:
          type: boolean
          nullable: true
        tool_choice:
          properties:
            name:
              type: string
            type:
              type: string
              enum:
                - none
                - auto
                - any
                - tool
          required:
            - type
          type: object
        response_format:
          properties:
            json_schema: {}
            type:
              type: string
          required:
            - type
          type: object
        toolDetails:
          $ref: '#/components/schemas/HeliconeEventTool'
        vectorDBDetails:
          $ref: '#/components/schemas/HeliconeEventVectorDB'
        dataDetails:
          $ref: '#/components/schemas/HeliconeEventData'
        input:
          anyOf:
            - type: string
            - items:
                type: string
              type: array
        'n':
          type: number
          format: double
          nullable: true
        size:
          type: string
        quality:
          type: string
      type: object
      additionalProperties: false
    Response:
      properties:
        contentArray:
          items:
            $ref: '#/components/schemas/Response'
          type: array
        detail:
          type: string
        filename:
          type: string
        file_id:
          type: string
        file_data:
          type: string
        idx:
          type: number
          format: double
        audio_data:
          type: string
        image_url:
          type: string
        timestamp:
          type: string
        tool_call_id:
          type: string
        tool_calls:
          items:
            $ref: '#/components/schemas/FunctionCall'
          type: array
        text:
          type: string
        type:
          type: string
          enum:
            - input_image
            - input_text
            - input_file
        name:
          type: string
        role:
          type: string
          enum:
            - user
            - assistant
            - system
            - developer
        id:
          type: string
        _type:
          type: string
          enum:
            - functionCall
            - function
            - image
            - text
            - file
            - contentArray
      required:
        - type
        - role
        - _type
      type: object
    LLMResponseBody:
      properties:
        dataDetailsResponse:
          properties:
            name:
              type: string
            _type:
              type: string
              enum:
                - data
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
              additionalProperties: {}
              required:
                - timestamp
              type: object
            message:
              type: string
            status:
              type: string
          additionalProperties: {}
          required:
            - name
            - _type
            - metadata
            - message
            - status
          type: object
        vectorDBDetailsResponse:
          properties:
            _type:
              type: string
              enum:
                - vector_db
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
                destination_parsed:
                  type: boolean
                destination:
                  type: string
              required:
                - timestamp
              type: object
            actualSimilarity:
              type: number
              format: double
            similarityThreshold:
              type: number
              format: double
            message:
              type: string
            status:
              type: string
          required:
            - _type
            - metadata
            - message
            - status
          type: object
        toolDetailsResponse:
          properties:
            toolName:
              type: string
            _type:
              type: string
              enum:
                - tool
              nullable: false
            metadata:
              properties:
                timestamp:
                  type: string
              required:
                - timestamp
              type: object
            tips:
              items:
                type: string
              type: array
            message:
              type: string
            status:
              type: string
          required:
            - toolName
            - _type
            - metadata
            - tips
            - message
            - status
          type: object
        error:
          properties:
            heliconeMessage: {}
          required:
            - heliconeMessage
          type: object
        model:
          type: string
          nullable: true
        instructions:
          type: string
          nullable: true
        responses:
          items:
            $ref: '#/components/schemas/Response'
          type: array
          nullable: true
        messages:
          items:
            $ref: '#/components/schemas/Message'
          type: array
          nullable: true
      type: object
    LlmSchema:
      properties:
        request:
          $ref: '#/components/schemas/LLMRequestBody'
        response:
          allOf:
            - $ref: '#/components/schemas/LLMResponseBody'
          nullable: true
      required:
        - request
      type: object
      additionalProperties: false
    HeliconeRequest:
      properties:
        response_id:
          type: string
          nullable: true
        response_created_at:
          type: string
          nullable: true
        response_body: {}
        response_status:
          type: number
          format: double
        response_model:
          type: string
          nullable: true
        request_id:
          type: string
        request_created_at:
          type: string
        request_body: {}
        request_path:
          type: string
        request_user_id:
          type: string
          nullable: true
        request_properties:
          allOf:
            - $ref: '#/components/schemas/Record_string.string_'
          nullable: true
        request_model:
          type: string
          nullable: true
        model_override:
          type: string
          nullable: true
        helicone_user:
          type: string
          nullable: true
        provider:
          $ref: '#/components/schemas/Provider'
        delay_ms:
          type: number
          format: double
          nullable: true
        time_to_first_token:
          type: number
          format: double
          nullable: true
        total_tokens:
          type: number
          format: double
          nullable: true
        prompt_tokens:
          type: number
          format: double
          nullable: true
        prompt_cache_write_tokens:
          type: number
          format: double
          nullable: true
        prompt_cache_read_tokens:
          type: number
          format: double
          nullable: true
        completion_tokens:
          type: number
          format: double
          nullable: true
        prompt_audio_tokens:
          type: number
          format: double
          nullable: true
        completion_audio_tokens:
          type: number
          format: double
          nullable: true
        cost:
          type: number
          format: double
          nullable: true
        prompt_id:
          type: string
          nullable: true
        prompt_version:
          type: string
          nullable: true
        feedback_created_at:
          type: string
          nullable: true
        feedback_id:
          type: string
          nullable: true
        feedback_rating:
          type: boolean
          nullable: true
        signed_body_url:
          type: string
          nullable: true
        llmSchema:
          allOf:
            - $ref: '#/components/schemas/LlmSchema'
          nullable: true
        country_code:
          type: string
          nullable: true
        asset_ids:
          items:
            type: string
          type: array
          nullable: true
        asset_urls:
          allOf:
            - $ref: '#/components/schemas/Record_string.string_'
          nullable: true
        scores:
          allOf:
            - $ref: '#/components/schemas/Record_string.number_'
          nullable: true
        costUSD:
          type: number
          format: double
          nullable: true
        properties:
          $ref: '#/components/schemas/Record_string.string_'
        assets:
          items:
            type: string
          type: array
        target_url:
          type: string
        model:
          type: string
        cache_reference_id:
          type: string
          nullable: true
        cache_enabled:
          type: boolean
        updated_at:
          type: string
        request_referrer:
          type: string
          nullable: true
        ai_gateway_body_mapping:
          type: string
          nullable: true
        storage_location:
          type: string
      required:
        - response_id
        - response_created_at
        - response_status
        - response_model
        - request_id
        - request_created_at
        - request_body
        - request_path
        - request_user_id
        - request_properties
        - request_model
        - model_override
        - helicone_user
        - provider
        - delay_ms
        - time_to_first_token
        - total_tokens
        - prompt_tokens
        - prompt_cache_write_tokens
        - prompt_cache_read_tokens
        - completion_tokens
        - prompt_audio_tokens
        - completion_audio_tokens
        - cost
        - prompt_id
        - prompt_version
        - llmSchema
        - country_code
        - asset_ids
        - asset_urls
        - scores
        - properties
        - assets
        - target_url
        - model
        - cache_reference_id
        - cache_enabled
        - ai_gateway_body_mapping
      type: object
      additionalProperties: false

````