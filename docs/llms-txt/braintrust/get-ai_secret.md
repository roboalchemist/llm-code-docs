# Source: https://braintrust.dev/docs/api-reference/aisecrets/get-ai_secret.md

# Get ai_secret

> Get an ai_secret object by its id



## OpenAPI

````yaml openapi.yaml get /v1/ai_secret/{ai_secret_id}
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
  /v1/ai_secret/{ai_secret_id}:
    get:
      tags:
        - AiSecrets
      summary: Get ai_secret
      description: Get an ai_secret object by its id
      operationId: getAiSecretId
      parameters:
        - $ref: '#/components/parameters/AiSecretIdParam'
      responses:
        '200':
          description: Returns the ai_secret object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AISecret'
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
    AiSecretIdParam:
      schema:
        $ref: '#/components/schemas/AiSecretIdParam'
      required: true
      description: AiSecret id
      name: ai_secret_id
      in: path
  schemas:
    AISecret:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the AI secret
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of AI secret creation
        updated_at:
          type: string
          nullable: true
          format: date-time
          description: Date of last AI secret update
        org_id:
          type: string
          format: uuid
          description: Unique identifier for the organization
        name:
          type: string
          description: Name of the AI secret
        type:
          type: string
          nullable: true
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
        preview_secret:
          type: string
          nullable: true
      required:
        - id
        - org_id
        - name
    AiSecretIdParam:
      type: string
      format: uuid
      description: AiSecret id
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