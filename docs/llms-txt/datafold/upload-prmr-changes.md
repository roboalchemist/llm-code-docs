# Source: https://docs.datafold.com/api-reference/ci/upload-prmr-changes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload PR/MR changes



## OpenAPI

````yaml post /api/v1/ci/{ci_config_id}/{pr_num}
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
  /api/v1/ci/{ci_config_id}/{pr_num}:
    post:
      tags:
        - CI
      summary: Upload PR/MR changes
      operationId: upload_changes_api_v1_ci__ci_config_id___pr_num__post
      parameters:
        - in: path
          name: ci_config_id
          required: true
          schema:
            title: CI config id
            type: integer
        - in: path
          name: pr_num
          required: true
          schema:
            title: Pull request/Merge request number
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              items:
                $ref: '#/components/schemas/CiDiff'
              title: Diffs
              type: array
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SubmitCiJob'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    CiDiff:
      properties:
        exclude_columns:
          default: []
          items:
            type: string
          title: Exclude Columns
          type: array
        include_columns:
          default: []
          items:
            type: string
          title: Include Columns
          type: array
        pk:
          anyOf:
            - items:
                type: string
              type: array
              uniqueItems: true
            - type: 'null'
          title: Pk
        pr:
          title: Pr
          type: string
        prod:
          title: Prod
          type: string
      required:
        - prod
        - pr
      title: CiDiff
      type: object
    SubmitCiJob:
      properties:
        ci_run_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Ci Run Id
        run_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Run Id
      title: SubmitCiJob
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