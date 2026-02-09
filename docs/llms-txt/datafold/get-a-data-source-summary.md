# Source: https://docs.datafold.com/api-reference/data-sources/get-a-data-source-summary.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a data source summary



## OpenAPI

````yaml get /api/v1/data_sources/{data_source_id}/summary
openapi: 3.1.0
info:
  contact:
    email: support@datafold.com
    name: API Support
  description: >-
    The Datafold API reference is a guide to our available endpoints and
    authentication methods.

    If you're just getting started with Datafold, we recommend first checking
    out our [documentation](https://docs.datafold.com).


    :::info
      To use the Datafold API, you should first create a Datafold API Key,
      which should be stored as a local environment variable named DATAFOLD_API_KEY.
      This can be set in your Datafold Cloud's Settings under the Account page.
    :::
  title: Datafold API
  version: latest
servers:
  - description: Default server
    url: https://app.datafold.com
security:
  - ApiKeyAuth: []
paths:
  /api/v1/data_sources/{data_source_id}/summary:
    get:
      tags:
        - Data sources
      summary: Get a data source summary
      operationId: get_data_source_summary_api_v1_data_sources__data_source_id__summary_get
      parameters:
        - in: path
          name: data_source_id
          required: true
          schema:
            title: Data source id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiDataSourceSummary'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiDataSourceSummary:
      description: Used in OSS data-diff with non-admin privileges to get a DS overview.
      properties:
        id:
          title: Id
          type: integer
        name:
          title: Name
          type: string
        type:
          title: Type
          type: string
      required:
        - id
        - name
        - type
      title: ApiDataSourceSummary
      type: object
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          title: Detail
          type: array
      title: HTTPValidationError
      type: object
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          title: Location
          type: array
        msg:
          title: Message
          type: string
        type:
          title: Error Type
          type: string
      required:
        - loc
        - msg
        - type
      title: ValidationError
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````