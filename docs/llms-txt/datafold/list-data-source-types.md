# Source: https://docs.datafold.com/api-reference/data-sources/list-data-source-types.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List data source types



## OpenAPI

````yaml get /api/v1/data_sources/types
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
  /api/v1/data_sources/types:
    get:
      tags:
        - Data sources
      summary: List data source types
      operationId: get_data_source_types_api_v1_data_sources_types_get
      responses:
        '200':
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/ApiDataSourceType'
                title: Response Get Data Source Types Api V1 Data Sources Types Get
                type: array
          description: Successful Response
components:
  schemas:
    ApiDataSourceType:
      properties:
        configuration_schema:
          additionalProperties: true
          title: Configuration Schema
          type: object
        features:
          items:
            type: string
          title: Features
          type: array
        name:
          title: Name
          type: string
        type:
          title: Type
          type: string
      required:
        - name
        - type
        - configuration_schema
        - features
      title: ApiDataSourceType
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````