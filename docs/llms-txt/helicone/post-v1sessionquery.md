# Source: https://docs.helicone.ai/rest/session/post-v1sessionquery.md

# Query Sessions

> Search and filter through session data

## OpenAPI

````yaml post /v1/session/query
paths:
  path: /v1/session/query
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
              search:
                allOf:
                  - type: string
              timeFilter:
                allOf:
                  - properties:
                      endTimeUnixMs:
                        type: number
                        format: double
                      startTimeUnixMs:
                        type: number
                        format: double
                    required:
                      - endTimeUnixMs
                      - startTimeUnixMs
                    type: object
              nameEquals:
                allOf:
                  - type: string
              timezoneDifference:
                allOf:
                  - type: number
                    format: double
              filter:
                allOf:
                  - $ref: '#/components/schemas/SessionFilterNode'
              offset:
                allOf:
                  - type: number
                    format: double
              limit:
                allOf:
                  - type: number
                    format: double
            required: true
            refIdentifier: '#/components/schemas/SessionQueryParams'
            requiredProperties:
              - search
              - timeFilter
              - timezoneDifference
              - filter
            additionalProperties: false
        examples:
          example:
            value:
              search: <string>
              timeFilter:
                endTimeUnixMs: 123
                startTimeUnixMs: 123
              nameEquals: <string>
              timezoneDifference: 123
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
              offset: 123
              limit: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - items:
                      $ref: '#/components/schemas/SessionResult'
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: '#/components/schemas/ResultSuccess_SessionResult-Array_'
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
                - created_at: <string>
                  latest_request_created_at: <string>
                  session_id: <string>
                  session_name: <string>
                  total_cost: 123
                  total_requests: 123
                  prompt_tokens: 123
                  completion_tokens: 123
                  total_tokens: 123
                  avg_latency: 123
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
    SessionResult:
      properties:
        created_at:
          type: string
        latest_request_created_at:
          type: string
        session_id:
          type: string
        session_name:
          type: string
        total_cost:
          type: number
          format: double
        total_requests:
          type: number
          format: double
        prompt_tokens:
          type: number
          format: double
        completion_tokens:
          type: number
          format: double
        total_tokens:
          type: number
          format: double
        avg_latency:
          type: number
          format: double
      required:
        - created_at
        - latest_request_created_at
        - session_id
        - session_name
        - total_cost
        - total_requests
        - prompt_tokens
        - completion_tokens
        - total_tokens
        - avg_latency
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
    FilterLeafSubset_request_response_rmt-or-sessions_request_response_rmt_:
      $ref: >-
        #/components/schemas/Pick_FilterLeaf.request_response_rmt-or-sessions_request_response_rmt_
    SessionFilterNode:
      anyOf:
        - $ref: >-
            #/components/schemas/FilterLeafSubset_request_response_rmt-or-sessions_request_response_rmt_
        - $ref: '#/components/schemas/SessionFilterBranch'
        - type: string
          enum:
            - all
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

````