# Source: https://braintrust.dev/docs/api-reference/servicetokens/create-or-replace-service_token.md

# Create or replace service_token

> Create or replace service_token. If there is an existing service_token with the same name as the one specified in the request, will replace the existing service_token with the provided fields



## OpenAPI

````yaml openapi.yaml put /v1/service_token
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
  /v1/service_token:
    put:
      tags:
        - ServiceTokens
      summary: Create or replace service_token
      description: >-
        Create or replace service_token. If there is an existing service_token
        with the same name as the one specified in the request, will replace the
        existing service_token with the provided fields
      operationId: putServiceToken
      requestBody:
        description: Any desired information about the new service_token object
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                name:
                  type: string
                  description: Name of the service token. Does not have to be unique
                org_name:
                  type: string
                  nullable: true
                  description: >-
                    For nearly all users, this parameter should be unnecessary.
                    But in the rare case that your API key belongs to multiple
                    organizations, you may specify the name of the organization
                    the Service token belongs in.
                service_account_id:
                  type: string
                  description: The service account ID this service token should belong to.
              required:
                - name
                - service_account_id
      responses:
        '200':
          description: >-
            Returns an object containing the raw service token. This is the only
            time the raw API key will be exposed
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CreateServiceTokenOutput'
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
    CreateServiceTokenOutput:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the service token
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of service token creation
        name:
          type: string
          description: Name of the service token
        preview_name:
          type: string
        service_account_id:
          type: string
          nullable: true
          format: uuid
          description: Unique identifier for the service token
        service_account_email:
          type: string
          nullable: true
          description: The service account email (not routable)
        service_account_name:
          type: string
          nullable: true
          description: The service account name
        org_id:
          type: string
          nullable: true
          format: uuid
          description: Unique identifier for the organization
        key:
          type: string
          description: The raw service token. It will only be exposed this one time
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

---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://braintrust.dev/docs/llms.txt