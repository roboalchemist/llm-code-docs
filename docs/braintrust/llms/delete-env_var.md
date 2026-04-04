# Source: https://braintrust.dev/docs/api-reference/envvars/delete-env_var.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete env_var

> Delete an env_var object by its id



## OpenAPI

````yaml openapi.yaml delete /v1/env_var/{env_var_id}
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
  /v1/env_var/{env_var_id}:
    delete:
      tags:
        - EnvVars
      summary: Delete env_var
      description: Delete an env_var object by its id
      operationId: deleteEnvVarId
      parameters:
        - $ref: '#/components/parameters/EnvVarIdParam'
      responses:
        '200':
          description: Returns the deleted env_var object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EnvVar'
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
    EnvVarIdParam:
      schema:
        $ref: '#/components/schemas/EnvVarIdParam'
      required: true
      description: EnvVar id
      name: env_var_id
      in: path
  schemas:
    EnvVar:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the environment variable
        object_type:
          type: string
          enum:
            - organization
            - project
            - function
          description: The type of the object the environment variable is scoped for
        object_id:
          type: string
          format: uuid
          description: The id of the object the environment variable is scoped for
        name:
          type: string
          description: The name of the environment variable
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of environment variable creation
        used:
          type: string
          nullable: true
          format: date-time
          description: Date the environment variable was last used
        metadata:
          type: object
          nullable: true
          additionalProperties:
            nullable: true
          description: >-
            Optional metadata associated with the environment variable when
            managed via the function secrets API
        secret_type:
          type: string
          nullable: true
          description: >-
            Optional classification for the secret (for example, the AI provider
            name)
        secret_category:
          type: string
          enum:
            - env_var
            - ai_provider
          default: env_var
          description: >-
            The category of the secret: env_var for regular environment
            variables, ai_provider for AI provider API keys
      required:
        - id
        - object_type
        - object_id
        - name
    EnvVarIdParam:
      type: string
      format: uuid
      description: EnvVar id
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