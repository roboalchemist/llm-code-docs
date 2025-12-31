# Source: https://docs.helicone.ai/rest/user/post-v1userquery.md

# Get User Data

> Retrieve user data based on specified user IDs and time filters

## OpenAPI

````yaml post /v1/user/query
paths:
  path: /v1/user/query
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
              userIds:
                allOf:
                  - items:
                      type: string
                    type: array
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
            required: true
            refIdentifier: '#/components/schemas/UserQueryParams'
            additionalProperties: false
        examples:
          example:
            value:
              userIds:
                - <string>
              timeFilter:
                endTimeUnixSeconds: 123
                startTimeUnixSeconds: 123
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
                        cost:
                          type: number
                          format: double
                        user_id:
                          type: string
                        completion_tokens:
                          type: number
                          format: double
                        prompt_tokens:
                          type: number
                          format: double
                        count:
                          type: number
                          format: double
                      required:
                        - cost
                        - user_id
                        - completion_tokens
                        - prompt_tokens
                        - count
                      type: object
                    type: array
              error:
                allOf:
                  - type: number
                    enum:
                      - null
                    nullable: true
            refIdentifier: >-
              #/components/schemas/ResultSuccess__count-number--prompt_tokens-number--completion_tokens-number--user_id-string--cost-number_-Array_
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
                - cost: 123
                  user_id: <string>
                  completion_tokens: 123
                  prompt_tokens: 123
                  count: 123
        description: Ok
  deprecated: false
  type: path
components:
  schemas: {}

````