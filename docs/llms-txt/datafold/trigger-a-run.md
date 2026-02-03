# Source: https://docs.datafold.com/api-reference/monitors/trigger-a-run.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.datafold.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Trigger a run



## OpenAPI

````yaml openapi-public.json post /api/v1/monitors/{id}/run
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
  /api/v1/monitors/{id}/run:
    post:
      tags:
        - Monitors
      summary: Trigger a run
      operationId: start_monitor_run_api_v1_monitors__id__run_post
      parameters:
        - description: The unique identifier of the monitor for which to start the run.
          in: path
          name: id
          required: true
          schema:
            description: The unique identifier of the monitor for which to start the run.
            title: Id
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ApiPublicMonitorTriggerRunResultOut'
          description: Successful Response
        '422':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
          description: Validation Error
components:
  schemas:
    ApiPublicMonitorTriggerRunResultOut:
      properties:
        run_id:
          description: Unique identifier for the monitor run result.
          title: Run Id
          type: integer
      required:
        - run_id
      title: ApiPublicMonitorTriggerRunResultOut
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