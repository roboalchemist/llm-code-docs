# Source: https://docs.datafold.com/api-reference/ci/trigger-a-prmr-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a PR/MR run



## OpenAPI

````yaml post /api/v1/ci/{ci_config_id}/trigger
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
  /api/v1/ci/{ci_config_id}/trigger:
    post:
      tags:
        - CI
      summary: Trigger a PR/MR run
      operationId: trigger_ci_api_v1_ci__ci_config_id__trigger_post
      parameters:
        - in: path
          name: ci_config_id
          required: true
          schema:
            title: CI config id
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/APIPrDetails'
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
    APIPrDetails:
      properties:
        base_branch:
          title: Base Branch
          type: string
        base_sha:
          title: Base Sha
          type: string
        pr_branch:
          title: Pr Branch
          type: string
        pr_number:
          title: Pr Number
          type: integer
        pr_sha:
          title: Pr Sha
          type: string
      required:
        - pr_number
        - pr_branch
        - base_branch
        - pr_sha
        - base_sha
      title: APIPrDetails
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