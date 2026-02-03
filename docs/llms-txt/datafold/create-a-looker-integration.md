# Source: https://docs.datafold.com/api-reference/bi/create-a-looker-integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a Looker integration



## OpenAPI

````yaml post /api/v1/lineage/bi/looker/
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
  /api/v1/lineage/bi/looker/:
    post:
      tags:
        - BI
        - bi_added
      summary: Create a Looker integration
      operationId: create_looker_integration_api_v1_lineage_bi_looker__post
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/LookerDataSourceConfig'
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
    LookerDataSourceConfig:
      properties:
        base_url:
          title: Base Url
          type: string
        bindings:
          default: []
          items:
            $ref: '#/components/schemas/DataSourceBinding'
          title: Bindings
          type: array
        client_id:
          title: Client Id
          type: string
        client_secret:
          format: password
          title: Client Secret
          type: string
          writeOnly: true
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
        project_ids:
          default: []
          items:
            type: string
          title: Project Ids
          type: array
        repo_id:
          title: Repo Id
          type: integer
      required:
        - base_url
        - client_id
        - repo_id
        - client_secret
      title: LookerDataSourceConfig
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
    DataSourceBinding:
      properties:
        boundIds:
          items:
            type: integer
          title: Boundids
          type: array
        remoteId:
          title: Remoteid
          type: string
      required:
        - remoteId
        - boundIds
      title: DataSourceBinding
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