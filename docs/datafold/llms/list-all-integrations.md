# Source: https://docs.datafold.com/api-reference/bi/list-all-integrations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List all integrations

> Return all integrations for Mode/Tableau/Looker



## OpenAPI

````yaml get /api/v1/lineage/bi/
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
  /api/v1/lineage/bi/:
    get:
      tags:
        - BI
      summary: List all integrations
      description: Return all integrations for Mode/Tableau/Looker
      operationId: get_all_integrations_api_v1_lineage_bi__get
      responses:
        '200':
          content:
            application/json:
              schema: {}
          description: Successful Response
components:
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````