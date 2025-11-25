# Source: https://docs.helicone.ai/rest/dashboard/post-v1dashboardscoresquery.md

# Query Dashboard Scores

> Retrieve and filter dashboard scoring metrics

## OpenAPI

````yaml post /v1/dashboard/scores/query
paths:
  path: /v1/dashboard/scores/query
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
              timeFilter:
                allOf:
                  - properties:
                      end:
                        type: string
                      start:
                        type: string
                    required:
                      - end
                      - start
                    type: object
              userFilter:
                allOf:
                  - $ref: '#/components/schemas/RequestClickhouseFilterNode'
              dbIncrement:
                allOf:
                  - $ref: '#/components/schemas/TimeIncrement'
              timeZoneDifference:
                allOf:
                  - type: number
                    format: double
            required: true
            refIdentifier: '#/components/schemas/DataOverTimeRequest'
            requiredProperties:
              - timeFilter
              - userFilter
              - dbIncrement
              - timeZoneDifference
            additionalProperties: false
        examples:
          example:
            value:
              timeFilter:
                end: <string>
                start: <string>
              userFilter:
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
              dbIncrement: min
              timeZoneDifference: 123
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              data:
                allOf:
                  - items:
                      properties:
                        created_at_trunc:
                          type: string
                        score_sum:
                          type: number
                          format: double
                        score_key:
                          type: string
                      required:
                        - created_at_trunc
                        - score_sum
                        - score_key
                      type: object
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ResultSuccess__score_key-string--score_sum-number--created_at_trunc-string_-Array_
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
              userFilter: all
              timeFilter:
                start: '2024-01-01'
                end: '2024-01-31'
              dbIncrement: day
              timeZoneDifference: 0
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
    Pick_FilterLeaf.request_response_rmt_:
      properties:
        request_response_rmt:
          $ref: '#/components/schemas/Partial_RequestResponseRMTToOperators_'
      type: object
      description: From T, pick a set of properties whose keys are in the union K
    FilterLeafSubset_request_response_rmt_:
      $ref: '#/components/schemas/Pick_FilterLeaf.request_response_rmt_'
    RequestClickhouseFilterNode:
      anyOf:
        - $ref: '#/components/schemas/FilterLeafSubset_request_response_rmt_'
        - $ref: '#/components/schemas/RequestClickhouseFilterBranch'
        - type: string
          enum:
            - all
    RequestClickhouseFilterBranch:
      properties:
        right:
          $ref: '#/components/schemas/RequestClickhouseFilterNode'
        operator:
          type: string
          enum:
            - or
            - and
        left:
          $ref: '#/components/schemas/RequestClickhouseFilterNode'
      required:
        - right
        - operator
        - left
      type: object
    TimeIncrement:
      type: string
      enum:
        - min
        - hour
        - day
        - week
        - month
        - year

````