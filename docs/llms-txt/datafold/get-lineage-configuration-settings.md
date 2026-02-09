# Source: https://docs.datafold.com/api-reference/lineagev2/get-lineage-configuration-settings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get lineage configuration settings

> Returns configuration values used by the lineage system.



## OpenAPI

````yaml openapi-public.json get /api/v1/lineagev2/config
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
  /api/v1/lineagev2/config:
    get:
      tags:
        - lineagev2
      summary: Get lineage configuration settings
      description: Returns configuration values used by the lineage system.
      operationId: lineagev2_config
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ConfigResponse'
          description: Successful Response
components:
  schemas:
    ConfigResponse:
      properties:
        lineage:
          additionalProperties:
            type: integer
          title: Lineage
          type: object
      required:
        - lineage
      title: ConfigResponse
      type: object
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````