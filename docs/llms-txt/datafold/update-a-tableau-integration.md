# Source: https://docs.datafold.com/api-reference/bi/update-a-tableau-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a Tableau integration

> It can only update the schedule. Returns the integration with changed fields.



## OpenAPI

````yaml put /api/v1/lineage/bi/tableau/{bi_datasource_id}/
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
  /api/v1/lineage/bi/tableau/{bi_datasource_id}/:
    put:
      tags:
        - BI
        - bi_modified
      summary: Update a Tableau integration
      description: >-
        It can only update the schedule. Returns the integration with changed
        fields.
      operationId: >-
        update_tableau_integration_api_v1_lineage_bi_tableau__bi_datasource_id___put
      parameters:
        - in: path
          name: bi_datasource_id
          required: true
          schema:
            title: Tableau integration id
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TableauDataSourceConfig'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    TableauDataSourceConfig:
      properties:
        indexing_cron:
          anyOf:
            - type: string
            - type: 'null'
          title: Indexing Cron
        name:
          anyOf:
            - type: string
            - type: 'null'
          title: Name
        server_url:
          title: Server Url
          type: string
        site_id:
          title: Site Id
          type: string
        token_name:
          title: Token Name
          type: string
        token_value:
          format: password
          title: Token Value
          type: string
          writeOnly: true
      required:
        - token_name
        - token_value
        - site_id
        - server_url
      title: TableauDataSourceConfig
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