# Source: https://braintrust.dev/docs/api-reference/spaniframes/get-span_iframe.md

# Get span_iframe

> Get a span_iframe object by its id



## OpenAPI

````yaml openapi.yaml get /v1/span_iframe/{span_iframe_id}
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
  /v1/span_iframe/{span_iframe_id}:
    get:
      tags:
        - SpanIframes
      summary: Get span_iframe
      description: Get a span_iframe object by its id
      operationId: getSpanIframeId
      parameters:
        - $ref: '#/components/parameters/SpanIframeIdParam'
      responses:
        '200':
          description: Returns the span_iframe object
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SpanIFrame'
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
    SpanIframeIdParam:
      schema:
        $ref: '#/components/schemas/SpanIframeIdParam'
      required: true
      description: SpanIframe id
      name: span_iframe_id
      in: path
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
    SpanIframeIdParam:
      type: string
      format: uuid
      description: SpanIframe id
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