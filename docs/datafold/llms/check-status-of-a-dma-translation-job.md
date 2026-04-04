# Source: https://docs.datafold.com/api-reference/dma_v2/check-status-of-a-dma-translation-job.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Check status of a DMA translation job

> Get the current status and results of a DMA translation job.

Poll this endpoint to monitor translation progress and retrieve results when complete.
Translation jobs can run for several minutes to hours depending on project size.



## OpenAPI

````yaml openapi-public.json get /api/v1/dma/v2/projects/{project_id}/translate/jobs/{job_id}
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
  /api/v1/dma/v2/projects/{project_id}/translate/jobs/{job_id}:
    get:
      tags:
        - DMA_V2
      summary: Check status of a DMA translation job
      description: >-
        Get the current status and results of a DMA translation job.


        Poll this endpoint to monitor translation progress and retrieve results
        when complete.

        Translation jobs can run for several minutes to hours depending on
        project size.
      operationId: get_translation_status
      parameters:
        - in: path
          name: project_id
          required: true
          schema:
            title: Project Id
            type: integer
        - in: path
          name: job_id
          required: true
          schema:
            title: Job Id
            type: string
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