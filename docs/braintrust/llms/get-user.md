# Source: https://braintrust.dev/docs/api-reference/users/get-user.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get user

> Get a user object by its id



## OpenAPI

````yaml openapi.yaml get /v1/user/{user_id}
openapi: 3.1.1
info:
  version: 1.0.0
  title: Braintrust API
  description: >-
    API specification for the backend data server. The API is hosted globally at

    https://api.braintrust.dev or in your own environment.


    You can access the OpenAPI spec for this API at
    https://github.com/braintrustdata/braintrust-openapi.
  license:
    name: Apache 2.0
servers:
  - url: https://api.braintrust.dev
security:
  - bearerAuth: []
  - {}
paths:
  /v1/user/{user_id}:
    get:
      tags:
        - Users
      summary: Get user
      description: Get a user object by its id
      operationId: getUserId
      parameters:
        - $ref: '#/components/parameters/UserIdParam'
      responses:
        '200':
          description: Returns the user object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '400':
          description: >-
            The request was unacceptable, often due to missing a required
            parameter
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '401':
          description: No valid API key provided
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '403':
          description: The API key doesn’t have permissions to perform the request
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '429':
          description: >-
            Too many requests hit the API too quickly. We recommend an
            exponential backoff of your requests
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
        '500':
          description: Something went wrong on Braintrust's end. (These are rare.)
          content:
            text/plain:
              schema:
                type: string
            application/json:
              schema:
                nullable: true
      security:
        - bearerAuth: []
        - {}
components:
  parameters:
    UserIdParam:
      schema:
        $ref: '#/components/schemas/UserIdParam'
      required: true
      description: User id
      name: user_id
      in: path
  schemas:
    User:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the user
        given_name:
          type: string
          nullable: true
          description: Given name of the user
        family_name:
          type: string
          nullable: true
          description: Family name of the user
        email:
          type: string
          nullable: true
          description: The user's email
        avatar_url:
          type: string
          nullable: true
          description: URL of the user's Avatar image
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of user creation
      required:
        - id
    UserIdParam:
      type: string
      format: uuid
      description: User id
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: API key or JWT
      description: >-
        Most Braintrust endpoints are authenticated by providing your API key as
        a header `Authorization: Bearer [api_key]` to your HTTP request. You can
        create an API key in the Braintrust [organization settings
        page](https://www.braintrustdata.com/app/settings?subroute=api-keys).

````