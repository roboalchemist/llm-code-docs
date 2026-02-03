# Source: https://docs.datafold.com/api-reference/ci/list-ci-runs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# List CI runs



## OpenAPI

````yaml get /api/v1/ci/{ci_config_id}/runs
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
  /api/v1/ci/{ci_config_id}/runs:
    get:
      tags:
        - CI
      summary: List CI runs
      operationId: get_ci_api_v1_ci__ci_config_id__runs_get
      parameters:
        - in: path
          name: ci_config_id
          required: true
          schema:
            title: CI config id
            type: integer
        - in: query
          name: pr_sha
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Pr Sha
        - in: query
          name: pr_num
          required: false
          schema:
            anyOf:
              - type: string
              - type: 'null'
            title: Pr Num
        - in: query
          name: limit
          required: false
          schema:
            default: 100
            title: Limit
            type: integer
        - in: query
          name: offset
          required: false
          schema:
            default: 0
            title: Offset
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                items:
                  $ref: '#/components/schemas/ApiCiRun'
                title: Response Get Ci Api V1 Ci  Ci Config Id  Runs Get
                type: array
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiCiRun:
      properties:
        base_branch:
          title: Base Branch
          type: string
        base_sha:
          title: Base Sha
          type: string
        id:
          title: Id
          type: integer
        pr_branch:
          title: Pr Branch
          type: string
        pr_num:
          title: Pr Num
          type: string
        pr_sha:
          title: Pr Sha
          type: string
        source:
          title: Source
          type: string
        status:
          title: Status
          type: string
      required:
        - id
        - base_branch
        - base_sha
        - pr_branch
        - pr_sha
        - pr_num
        - status
        - source
      title: ApiCiRun
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