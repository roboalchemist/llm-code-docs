# Source: https://braintrust.dev/docs/api-reference/spaniframes/list-span_iframes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List span_iframes

> List out all span_iframes. The span_iframes are sorted by creation date, with the most recently-created span_iframes coming first



## OpenAPI

````yaml openapi.yaml get /v1/span_iframe
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
  /v1/span_iframe:
    get:
      tags:
        - SpanIframes
      summary: List span_iframes
      description: >-
        List out all span_iframes. The span_iframes are sorted by creation date,
        with the most recently-created span_iframes coming first
      operationId: getSpanIframe
      parameters:
        - $ref: '#/components/parameters/AppLimitParam'
        - $ref: '#/components/parameters/StartingAfter'
        - $ref: '#/components/parameters/EndingBefore'
        - $ref: '#/components/parameters/Ids'
        - $ref: '#/components/parameters/SpanIframeName'
        - $ref: '#/components/parameters/OrgName'
      responses:
        '200':
          description: Returns a list of span_iframe objects
          content:
            application/json:
              schema:
                type: object
                properties:
                  objects:
                    type: array
                    items:
                      $ref: '#/components/schemas/SpanIFrame'
                    description: A list of span_iframe objects
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
    SpanIframeName:
      schema:
        $ref: '#/components/schemas/SpanIframeName'
      required: false
      description: Name of the span_iframe to search for
      name: span_iframe_name
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
    SpanIFrame:
      type: object
      properties:
        id:
          type: string
          format: uuid
          description: Unique identifier for the span iframe
        project_id:
          type: string
          format: uuid
          description: Unique identifier for the project that the span iframe belongs under
        user_id:
          type: string
          nullable: true
          format: uuid
          description: Identifies the user who created the span iframe
        created:
          type: string
          nullable: true
          format: date-time
          description: Date of span iframe creation
        deleted_at:
          type: string
          nullable: true
          format: date-time
          description: >-
            Date of span iframe deletion, or null if the span iframe is still
            active
        name:
          type: string
          description: Name of the span iframe
        description:
          type: string
          nullable: true
          description: Textual description of the span iframe
        url:
          type: string
          description: URL to embed the project viewer in an iframe
        post_message:
          type: boolean
          nullable: true
          description: >-
            Whether to post messages to the iframe containing the span's data.
            This is useful when you want to render more data than fits in the
            URL.
      required:
        - id
        - project_id
        - name
        - url
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
    SpanIframeName:
      type: string
      description: Name of the span_iframe to search for
    OrgName:
      type: string
      description: Filter search results to within a particular organization
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