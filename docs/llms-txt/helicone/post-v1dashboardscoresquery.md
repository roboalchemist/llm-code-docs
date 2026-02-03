# Source: https://docs.helicone.ai/rest/dashboard/post-v1dashboardscoresquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Query Dashboard Scores

> Retrieve and filter dashboard scoring metrics

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/dashboard/scores/query
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
  /v1/dashboard/scores/query:
    post:
      tags:
        - Dashboard
      operationId: GetScoresOverTime
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/DataOverTimeRequest'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Result__score_key-string--score_sum-number--created_at_trunc-string_-Array.string_
              examples:
                Example 1:
                  value:
                    userFilter: all
                    timeFilter:
                      start: '2024-01-01'
                      end: '2024-01-31'
                    dbIncrement: day
                    timeZoneDifference: 0
      security:
        - api_key: []
components:
  schemas:
    DataOverTimeRequest:
      properties:
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
        userFilter:
          $ref: '#/components/schemas/RequestClickhouseFilterNode'
        dbIncrement:
          $ref: '#/components/schemas/TimeIncrement'
        timeZoneDifference:
          type: number
          format: double
      required:
        - timeFilter
        - userFilter
        - dbIncrement
        - timeZoneDifference
      type: object
      additionalProperties: false
    Result__score_key-string--score_sum-number--created_at_trunc-string_-Array.string_:
      anyOf:
        - $ref: >-
            #/components/schemas/ResultSuccess__score_key-string--score_sum-number--created_at_trunc-string_-Array_
        - $ref: '#/components/schemas/ResultError_string_'
    RequestClickhouseFilterNode:
      anyOf:
        - $ref: '#/components/schemas/FilterLeafSubset_request_response_rmt_'
        - $ref: '#/components/schemas/RequestClickhouseFilterBranch'
        - type: string
          enum:
            - all
    TimeIncrement:
      type: string
      enum:
        - min
        - hour
        - day
        - week
        - month
        - year
    ResultSuccess__score_key-string--score_sum-number--created_at_trunc-string_-Array_:
      properties:
        data:
          items:
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