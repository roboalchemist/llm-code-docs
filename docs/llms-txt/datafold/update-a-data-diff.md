# Source: https://docs.datafold.com/api-reference/data-diffs/update-a-data-diff.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a data diff



## OpenAPI

````yaml patch /api/v1/datadiffs/{datadiff_id}
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
  /api/v1/datadiffs/{datadiff_id}:
    patch:
      tags:
        - Data diffs
      summary: Update a data diff
      operationId: update_datadiff_api_v1_datadiffs__datadiff_id__patch
      parameters:
        - in: path
          name: datadiff_id
          required: true
          schema:
            title: Data diff id
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_update_datadiff_api_v1_datadiffs__datadiff_id__patch
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
    Body_update_datadiff_api_v1_datadiffs__datadiff_id__patch:
      properties:
        archived:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Archived
        purged:
          anyOf:
            - type: boolean
            - type: 'null'
          title: Purged
      title: Body_update_datadiff_api_v1_datadiffs__datadiff_id__patch
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