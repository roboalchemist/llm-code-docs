# Source: https://braintrust.dev/docs/api-reference/servicetokens/delete-service_token.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete service_token

> Delete a service_token object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/service_token/{service_token_id}
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
  /v1/service_token/{service_token_id}:
    delete:
      tags:
        - ServiceTokens
      summary: Delete service_token
      description: Delete a service_token object by its id
      operationId: deleteServiceTokenId
      parameters:
        - $ref: '#/components/parameters/ServiceTokenIdParam'
      responses:
        '200':
          description: Returns the deleted service_token object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ServiceToken'
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
    ServiceTokenIdParam:
      schema:
        $ref: '#/components/schemas/ServiceTokenIdParam'
      required: true
      description: ServiceToken id
      name: service_token_id
      in: path
  schemas:
    ServiceToken:
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
      required:
        - id
        - name
        - preview_name
    ServiceTokenIdParam:
      type: string
      format: uuid
      description: ServiceToken id
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