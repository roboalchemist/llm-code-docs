# Source: https://docs.agent.ai/api-reference/get-data/get-twitter-users.md

# Get Twitter Users

> Search and retrieve Twitter user profiles based on specific keywords for targeted social media analysis.

## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_twitter_users
paths:
  path: /action/get_twitter_users
  method: post
  servers:
    - url: https://api-lr.agent.ai/v1
  request:
    security:
      - title: bearerAuth
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >-
                Bearer token from your account
                ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))
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
              keywords:
                allOf:
                  - type: string
                    description: Keywords to find relevant Twitter users.
                    example: AI experts
              num_users:
                allOf:
                  - type: integer
                    format: int64
                    enum:
                      - 1
                      - 5
                      - 10
                      - 25
                      - 50
                      - 100
                    default: 1
                    description: Number of user profiles to retrieve.
            required: true
            requiredProperties:
              - keywords
              - num_users
        examples:
          example:
            value:
              keywords: AI experts
              num_users: 1
  response:
    '200':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - &ref_0
                    type: integer
                    format: int32
                    description: HTTP status code of the action response
              response:
                allOf:
                  - &ref_1
                    type: object
                    description: Response data from the action
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 200
              response:
                - dharmesh
        description: Retrieved Twitter user profiles
    '403':
      application/json:
        schemaArray:
          - type: object
            properties:
              status:
                allOf:
                  - *ref_0
              response:
                allOf:
                  - *ref_1
            refIdentifier: '#/components/schemas/ActionResponse'
        examples:
          example:
            value:
              status: 403
              response: null
              error: >-
                403 Forbidden

                Authenticating with OAuth 2.0 Application-Only is forbidden for
                this endpoint.  Supported authentication types are [OAuth 1.0a
                User Context, OAuth 2.0 User Context].
        description: Data about the YouTube channel
  deprecated: false
  type: path
components:
  schemas: {}

````