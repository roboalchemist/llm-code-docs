# Source: https://braintrust.dev/docs/api-reference/projecttags/create-project_tag.md

# Create project_tag

> Create a new project_tag. If there is an existing project_tag in the project with the same name as the one specified in the request, will return the existing project_tag unmodified



## OpenAPI

````yaml openapi.yaml post /v1/project_tag
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
  /v1/project_tag:
    post:
      tags:
        - ProjectTags
      summary: Create project_tag
      description: >-
        Create a new project_tag. If there is an existing project_tag in the
        project with the same name as the one specified in the request, will
        return the existing project_tag unmodified
      operationId: postProjectTag
      requestBody:
        description: Any desired information about the new project_tag object
        required: false
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateProjectTag'
      responses:
        '200':
          description: Returns the new project_tag object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ProjectTag'
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
    CreateProjectTag:
      type: object
      properties:
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the project tag belongs under
        name:
          type: string
          description: Name of the project tag
        description:
          type: string
          nullable: true
          description: Textual description of the project tag
        color:
          type: string
          nullable: true
          description: Color of the tag for the UI
      required:
        - project_id
        - name
    ProjectTag:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the project tag
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the project tag belongs under
        user_id:
          type: string
          format: uuid
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of project tag creation
        name:
          type: string
          description: Name of the project tag
        description:
          type: string
          nullable: true
          description: Textual description of the project tag
        color:
          type: string
          nullable: true
          description: Color of the tag for the UI
        position:
          type: string
          nullable: true
          description: >-
            An optional LexoRank-based string that sets the sort position for
            the tag in the UI
      required:
        - id
        - project_id
        - user_id
        - name
      description: >-
        A project tag is a user-configured tag for tracking and filtering your
        experiments, logs, and other data
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