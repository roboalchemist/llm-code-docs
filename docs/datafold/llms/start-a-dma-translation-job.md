# Source: https://docs.datafold.com/api-reference/dma_v2/start-a-dma-translation-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Start a DMA translation job

> Start a translation job for a DMA project.

Executes the DMA translation pipeline to convert source SQL code to target dialect.
The pipeline processes code through multiple stages (file operations, reference extraction,
template creation, SQL translation, validation, and bundling).

This endpoint launches a long-running background workflow and returns immediately with
a job_id. Use the get_translation_status endpoint to poll for progress and results.



## OpenAPI

````yaml openapi-public.json post /api/v1/dma/v2/projects/{project_id}/translate/jobs
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
  /api/v1/dma/v2/projects/{project_id}/translate/jobs:
    post:
      tags:
        - DMA_V2
      summary: Start a DMA translation job
      description: >-
        Start a translation job for a DMA project.


        Executes the DMA translation pipeline to convert source SQL code to
        target dialect.

        The pipeline processes code through multiple stages (file operations,
        reference extraction,

        template creation, SQL translation, validation, and bundling).


        This endpoint launches a long-running background workflow and returns
        immediately with

        a job_id. Use the get_translation_status endpoint to poll for progress
        and results.
      operationId: start_translation
      parameters:
        - in: path
          name: project_id
          required: true
          schema:
            title: Project Id
            type: integer
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ApiTranslateRequest'
              default:
                concurrency: 12
                fail_fast: false
                preserve_dbt_temp_dirs: false
                recreate_all: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiTranslateTask'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiTranslateRequest:
      description: Request to run translation pipeline.
      properties:
        asset_paths:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Asset Paths
        concurrency:
          default: 12
          title: Concurrency
          type: integer
        drop_unresolved:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Drop Unresolved
        fail_fast:
          default: false
          title: Fail Fast
          type: boolean
        identity:
          anyOf:
            - additionalProperties:
                type: string
              type: object
            - type: 'null'
          title: Identity
        include_unverified:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Include Unverified
        max_iterations:
          anyOf:
            - type: integer
            - type: 'null'
          title: Max Iterations
        preserve_dbt_temp_dirs:
          default: false
          title: Preserve Dbt Temp Dirs
          type: boolean
        recreate_all:
          default: false
          title: Recreate All
          type: boolean
        stages:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Stages
        transform_group_ids:
          anyOf:
            - items:
                type: string
              type: array
            - type: 'null'
          title: Transform Group Ids
      title: ApiTranslateRequest
      type: object
    ApiTranslateTask:
      description: Response for translation task.
      properties:
        status:
          $ref: '#/components/schemas/JobStatus'
        task_id:
          title: Task Id
          type: string
        translated_models:
          anyOf:
            - items:
                $ref: '#/components/schemas/ApiTranslatedModel'
              type: array
            - type: 'null'
          title: Translated Models
      required:
        - task_id
        - status
      title: ApiTranslateTask
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
    JobStatus:
      enum:
        - needs_confirmation
        - needs_authentication
        - waiting
        - processing
        - done
        - failed
        - cancelled
      title: JobStatus
      type: string
    ApiTranslatedModel:
      description: Information about a translated model.
      properties:
        asset_id:
          title: Asset Id
          type: string
        asset_name:
          title: Asset Name
          type: string
        datadiff_id:
          anyOf:
            - type: integer
            - type: 'null'
          title: Datadiff Id
        failure_summary:
          anyOf:
            - $ref: '#/components/schemas/ApiFailureSummary'
            - type: 'null'
        source_filename:
          anyOf:
            - type: string
            - type: 'null'
          title: Source Filename
        source_sql:
          anyOf:
            - type: string
            - type: 'null'
          title: Source Sql
        target_sql:
          anyOf:
            - type: string
            - type: 'null'
          title: Target Sql
        translation_status:
          $ref: '#/components/schemas/ApiTranslationStatus'
      required:
        - asset_name
        - asset_id
        - translation_status
      title: ApiTranslatedModel
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
    ApiFailureSummary:
      description: Structured failure summary with problem, error, and solution sections.
      properties:
        error_message:
          title: Error Message
          type: string
        location:
          anyOf:
            - type: string
            - type: 'null'
          title: Location
        problem:
          title: Problem
          type: string
        reason:
          $ref: '#/components/schemas/ApiFailureReason'
        solution:
          title: Solution
          type: string
      required:
        - problem
        - error_message
        - solution
        - reason
      title: ApiFailureSummary
      type: object
    ApiTranslationStatus:
      enum:
        - no_translation_attempts
        - validation_pending
        - invalid_translation
        - valid_translation
      title: ApiTranslationStatus
      type: string
    ApiFailureReason:
      description: Reasons why a translation agent failed to complete its task.
      enum:
        - max_iterations
        - tool_error
        - resignation
      title: ApiFailureReason
      type: string
  securitySchemes:
    ApiKeyAuth:
      description: Use the 'Authorization' header with the format 'Key <api-key>'
      in: header
      name: Authorization
      type: apiKey

````