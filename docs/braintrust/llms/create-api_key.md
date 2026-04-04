# Source: https://braintrust.dev/docs/api-reference/apikeys/create-api_key.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Create api_key

> Create a new api_key. It is possible to have multiple API keys with the same name. There is no de-duplication



## OpenAPI

````yaml openapi.yaml post /v1/api_key
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
  /v1/api_key:
    post:
      tags:
        - ApiKeys
      summary: Create api_key
      description: >-
        Create a new api_key. It is possible to have multiple API keys with the
        same name. There is no de-duplication
      operationId: postApiKey
      requestBody:
        description: Any desired information about the new api_key object
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Name of the api key. Does not have to be unique
                org_name:
                  type: string
                  nullable: true
                  description: >-
                    For nearly all users, this parameter should be unnecessary.
                    But in the rare case that your API key belongs to multiple
                    organizations, you may specify the name of the organization
                    the API key belongs in.
              required:
                - name
      responses:
        '200':
          description: >-
            Returns an object containing the raw API key. This is the only time
            the raw API key will be exposed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateApiKeyOutput'
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
  schemas:
    CreateApiKeyOutput:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the api key
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of api key creation
        name:
          type: string
          description: Name of the api key
        preview_name:
          type: string
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Unique identifier for the user
        user_email:
          type: string
          nullable: true
          description: The user's email
        user_given_name:
          type: string
          nullable: true
          description: Given name of the user
        user_family_name:
          type: string
          nullable: true
          description: Family name of the user
        org_id:
          type: string
          nullable: true
          format: uuid
          description: Unique identifier for the organization
        key:
          type: string
          description: The raw API key. It will only be exposed this one time
      required:
        - id
        - name
        - preview_name
        - key
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