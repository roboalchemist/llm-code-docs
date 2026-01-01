# Source: https://braintrust.dev/docs/api-reference/projectautomations/list-project_automations.md

# List project_automations

> List out all project_automations. The project_automations are sorted by creation date, with the most recently-created project_automations coming first



## OpenAPI

````yaml openapi.yaml get /v1/project_automation
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
  /v1/project_automation:
    get:
      tags:
        - ProjectAutomations
      summary: List project_automations
      description: >-
        List out all project_automations. The project_automations are sorted by
        creation date, with the most recently-created project_automations coming
        first
      operationId: getProjectAutomation
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/ProjectAutomationName'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of project_automation objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/ProjectAutomation'
                    description: A list of project_automation objects
                required:
                  - objects
                additionalProperties: false
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
    AppLimitParam:
      schema:
        $ref: '#/components/schemas/AppLimitParam'
      required: false
      description: Limit the number of objects to return
      name: limit
      in: query
    StartingAfter:
      schema:
        $ref: '#/components/schemas/StartingAfter'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
      name: starting_after
      in: query
    EndingBefore:
      schema:
        $ref: '#/components/schemas/EndingBefore'
      required: false
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
      name: ending_before
      in: query
    Ids:
      schema:
        $ref: '#/components/schemas/Ids'
      required: false
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
      name: ids
      in: query
    ProjectAutomationName:
      schema:
        $ref: '#/components/schemas/ProjectAutomationName'
      required: false
      description: Name of the project_automation to search for
      name: project_automation_name
      in: query
      allowReserved: true
    OrgName:
      schema:
        $ref: '#/components/schemas/OrgName'
      required: false
      description: Filter search results to within a particular organization
      name: org_name
      in: query
      allowReserved: true
  schemas:
    ProjectAutomation:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the project automation
        project_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the project that the project automation
            belongs under
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the project automation
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of project automation creation
        name:
          type: string
          description: Name of the project automation
        description:
          type: string
          nullable: true
          description: Textual description of the project automation
        config:
          anyOf:
            - type: object
              properties:
                event_type:
                  type: string
                  enum:
                    - logs
                  description: The type of automation.
                btql_filter:
                  type: string
                  description: BTQL filter to identify rows for the automation rule
                interval_seconds:
                  type: number
                  minimum: 1
                  maximum: 2592000
                  description: >-
                    Perform the triggered action at most once in this interval
                    of seconds
                action:
                  oneOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - webhook
                          description: The type of action to take
                        url:
                          type: string
                          description: The webhook URL to send the request to
                      required:
                        - type
                        - url
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - slack
                          description: The type of action to take
                        workspace_id:
                          type: string
                          description: The Slack workspace ID to post to
                        channel:
                          type: string
                          description: The Slack channel ID to post to
                        message_template:
                          type: string
                          description: Custom message template for the alert
                      required:
                        - type
                        - workspace_id
                        - channel
                  description: The action to take when the automation rule is triggered
              required:
                - event_type
                - btql_filter
                - interval_seconds
                - action
            - type: object
              properties:
                event_type:
                  type: string
                  enum:
                    - btql_export
                  description: The type of automation.
                export_definition:
                  oneOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - log_traces
                      required:
                        - type
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - log_spans
                      required:
                        - type
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - btql_query
                        btql_query:
                          type: string
                          description: The BTQL query to export
                      required:
                        - type
                        - btql_query
                  description: The definition of what to export
                export_path:
                  type: string
                  description: >-
                    The path to export the results to. It should include the
                    storage protocol and prefix, e.g.
                    s3://bucket-name/path/to/export
                format:
                  type: string
                  enum:
                    - jsonl
                    - parquet
                  description: The format to export the results in
                interval_seconds:
                  type: number
                  minimum: 1
                  maximum: 2592000
                  description: >-
                    Perform the triggered action at most once in this interval
                    of seconds
                credentials:
                  oneOf:
                    - type: object
                      properties:
                        type:
                          type: string
                          enum:
                            - aws_iam
                        role_arn:
                          type: string
                          description: The ARN of the IAM role to use
                        external_id:
                          type: string
                          description: >-
                            The automation-specific external id component
                            (auto-generated by default)
                      required:
                        - type
                        - role_arn
                        - external_id
                batch_size:
                  type: number
                  nullable: true
                  description: The number of rows to export in each batch
              required:
                - event_type
                - export_definition
                - export_path
                - format
                - interval_seconds
                - credentials
            - type: object
              properties:
                event_type:
                  type: string
                  enum:
                    - retention
                  description: The type of automation.
                object_type:
                  $ref: '#/components/schemas/RetentionObjectType'
                retention_days:
                  type: number
                  minimum: 0
                  description: The number of days to retain the object
              required:
                - event_type
                - object_type
                - retention_days
          description: The configuration for the automation rule
      required:
        - id
        - project_id
        - name
        - config
    AppLimitParam:
      type: integer
      nullable: true
      minimum: 0
      description: Limit the number of objects to return
    StartingAfter:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the final item in the last page you fetched had an id of
        `foo`, pass `starting_after=foo` to fetch the next page. Note: you may
        only pass one of `starting_after` and `ending_before`
    EndingBefore:
      type: string
      format: uuid
      description: >-
        Pagination cursor id.


        For example, if the initial item in the last page you fetched had an id
        of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you
        may only pass one of `starting_after` and `ending_before`
    Ids:
      anyOf:
        - type: string
          format: uuid
        - type: array
          items:
            type: string
            format: uuid
      description: >-
        Filter search results to a particular set of object IDs. To specify a
        list of IDs, include the query param multiple times
    ProjectAutomationName:
      type: string
      description: Name of the project_automation to search for
    OrgName:
      type: string
      description: Filter search results to within a particular organization
    RetentionObjectType:
      type: string
      enum:
        - project_logs
        - experiment
        - dataset
      description: The object type that the retention policy applies to
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