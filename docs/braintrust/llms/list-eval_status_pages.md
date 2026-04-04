# Source: https://braintrust.dev/docs/api-reference/evalstatuspages/list-eval_status_pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List eval_status_pages

> List out all eval_status_pages. The eval_status_pages are sorted by creation date, with the most recently-created eval_status_pages coming first



## OpenAPI

````yaml openapi.yaml get /v1/eval_status_page
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
  /v1/eval_status_page:
    get:
      tags:
        - EvalStatusPages
      summary: List eval_status_pages
      description: >-
        List out all eval_status_pages. The eval_status_pages are sorted by
        creation date, with the most recently-created eval_status_pages coming
        first
      operationId: getEvalStatusPage
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/EvalStatusPageName'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of eval_status_page objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/EvalStatusPage'
                    description: A list of eval_status_page objects
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
    EvalStatusPageName:
      schema:
        $ref: '#/components/schemas/EvalStatusPageName'
      required: false
      description: Name of the eval_status_page to search for
      name: eval_status_page_name
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
    EvalStatusPage:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the eval status page
        project_id:
          type: string
          format: uuid
          description: >-
            Unique identifier for the project that the eval status page belongs
            under
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the eval status page
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of eval status page creation
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: >-
            Date of eval status page deletion, or null if the eval status page
            is still active
        name:
          type: string
          description: Name of the eval status page
        description:
          type: string
          nullable: true
          description: Textual description of the eval status page
        logo_url:
          type: string
          nullable: true
          description: URL of the logo to display on the page
        theme:
          $ref: '#/components/schemas/EvalStatusPageTheme'
        config:
          $ref: '#/components/schemas/EvalStatusPageConfig'
      required:
        - id
        - project_id
        - name
        - theme
        - config
      description: A public eval status page that displays aggregate experiment results
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
    EvalStatusPageName:
      type: string
      description: Name of the eval_status_page to search for
    OrgName:
      type: string
      description: Filter search results to within a particular organization
    EvalStatusPageTheme:
      type: string
      enum:
        - light
        - dark
      description: The theme for the page
    EvalStatusPageConfig:
      type: object
      properties:
        score_columns:
          type: array
          nullable: true
          items:
            type: string
          description: The score columns to display on the page
        metric_columns:
          type: array
          nullable: true
          items:
            type: string
          description: The metric columns to display on the page
        grouping_field:
          type: string
          nullable: true
          description: The metadata field to use for grouping experiments (model)
        filter:
          type: string
          nullable: true
          description: BTQL filter to apply to experiment data
        sort_by:
          type: string
          nullable: true
          description: 'Field to sort results by (format: ''score:<name>'' or ''metric:<name>'')'
        sort_order:
          type: string
          nullable: true
          enum:
            - asc
            - desc
            - null
          description: Sort order (ascending or descending)
        api_key:
          type: string
          nullable: true
          description: The API key used for fetching experiment data
      description: Configuration for what data to display
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