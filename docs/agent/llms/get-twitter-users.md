# Source: https://docs.agent.ai/api-reference/get-data/get-twitter-users.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Twitter Users

> Search and retrieve Twitter user profiles based on specific keywords for targeted social media analysis.



## OpenAPI

````yaml api-reference/v1/v1.0.1_openapi.json post /action/get_twitter_users
openapi: 3.0.0
info:
  version: 1.0.0
  title: AI Actions - Get Data
  description: API specifications for 'Get Data' category AI actions.
  license:
    name: MIT
servers:
  - url: https://api-lr.agent.ai/v1
security:
  - bearerAuth: []
paths:
  /action/get_twitter_users:
    post:
      tags:
        - Get Data
      summary: Get Twitter Users
      description: >-
        Search and retrieve Twitter user profiles based on specific keywords for
        targeted social media analysis.
      operationId: getTwitterUsers
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                keywords:
                  type: string
                  description: Keywords to find relevant Twitter users.
                  example: AI experts
                num_users:
                  type: integer
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
              required:
                - keywords
                - num_users
      responses:
        '200':
          description: Retrieved Twitter user profiles
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 200
                response:
                  - dharmesh
        '403':
          description: Data about the YouTube channel
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ActionResponse'
              example:
                status: 403
                response: null
                error: >-
                  403 Forbidden

                  Authenticating with OAuth 2.0 Application-Only is forbidden
                  for this endpoint.  Supported authentication types are [OAuth
                  1.0a User Context, OAuth 2.0 User Context].
components:
  schemas:
    ActionResponse:
      type: object
      properties:
        status:
          type: integer
          format: int32
          description: HTTP status code of the action response
        response:
          type: object
          description: Response data from the action
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      description: >-
        Bearer token from your account
        ([https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api))

````