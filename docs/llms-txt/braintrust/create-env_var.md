# Source: https://braintrust.dev/docs/api-reference/envvars/create-env_var.md

# Create env_var

> Create a new env_var. If there is an existing env_var with the same name as the one specified in the request, will return the existing env_var unmodified



## OpenAPI

````yaml openapi.yaml post /v1/env_var
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
  /v1/env_var:
    post:
      tags:
        - EnvVars
      summary: Create env_var
      description: >-
        Create a new env_var. If there is an existing env_var with the same name
        as the one specified in the request, will return the existing env_var
        unmodified
      operationId: postEnvVar
      requestBody:
        description: Any desired information about the new env_var object
        required: false
        content:
          application/json:
            schema:
              type: object
              properties:
                object_type:
                  type: string
                  enum:
                    - organization
                    - project
                    - function
                  description: >-
                    The type of the object the environment variable is scoped
                    for
                object_id:
                  type: string
                  format: uuid
                  description: The id of the object the environment variable is scoped for
                name:
                  type: string
                  description: The name of the environment variable
                value:
                  type: string
                  nullable: true
                  description: >-
                    The value of the environment variable. Will be encrypted at
                    rest.
              required:
                - object_type
                - object_id
                - name
      responses:
        '200':
          description: Returns the new env_var object
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
      required:
        - id
        - object_type
        - object_id
        - name
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