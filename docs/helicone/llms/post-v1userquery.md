# Source: https://docs.helicone.ai/rest/user/post-v1userquery.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.helicone.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get User Data

> Retrieve user data based on specified user IDs and time filters

<Warning>
  <strong>For users in the European Union:</strong> Please use `eu.api.helicone.ai` instead of
  `api.helicone.ai`.
</Warning>


## OpenAPI

````yaml post /v1/user/query
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
  /v1/user/query:
    post:
      tags:
        - User
      operationId: GetUsers
      parameters: []
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserQueryParams'
      responses:
        '200':
          description: Ok
          content:
            application/json:
              schema:
                $ref: >-
                  #/components/schemas/Result__count-number--prompt_tokens-number--completion_tokens-number--user_id-string--cost-number_-Array.string_
      security:
        - api_key: []
components:
  schemas:
    UserQueryParams:
      properties:
        userIds:
          items:
            type: string
          type: array
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
      type: object
      additionalProperties: false
    Result__count-number--prompt_tokens-number--completion_tokens-number--user_id-string--cost-number_-Array.string_:
      anyOf:
        - $ref: >-
            #/components/schemas/ResultSuccess__count-number--prompt_tokens-number--completion_tokens-number--user_id-string--cost-number_-Array_
        - $ref: '#/components/schemas/ResultError_string_'
    ResultSuccess__count-number--prompt_tokens-number--completion_tokens-number--user_id-string--cost-number_-Array_:
      properties:
        data:
          items:
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
  securitySchemes:
    api_key:
      type: apiKey
      name: Authorization
      in: header
      description: 'Bearer token authentication. Format: ''Bearer YOUR_API_KEY'''

````