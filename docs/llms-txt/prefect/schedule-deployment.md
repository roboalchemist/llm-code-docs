# Source: https://docs.prefect.io/v3/api-ref/rest-api/server/deployments/schedule-deployment.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Schedule Deployment

> Schedule runs for a deployment. For backfills, provide start/end times in the past.

This function will generate the minimum number of runs that satisfy the min
and max times, and the min and max counts. Specifically, the following order
will be respected.

    - Runs will be generated starting on or after the `start_time`
    - No more than `max_runs` runs will be generated
    - No runs will be generated after `end_time` is reached
    - At least `min_runs` runs will be generated
    - Runs will be generated until at least `start_time + min_time` is reached



## OpenAPI

````yaml post /deployments/{id}/schedule
openapi: 3.1.0
info:
  title: Prefect Prefect REST API
  version: v3
  x-logo:
    url: static/prefect-logo-mark-gradient.png
servers: []
security: []
paths:
  /deployments/{id}/schedule:
    post:
      tags:
        - Deployments
      summary: Schedule Deployment
      description: >-
        Schedule runs for a deployment. For backfills, provide start/end times
        in the past.


        This function will generate the minimum number of runs that satisfy the
        min

        and max times, and the min and max counts. Specifically, the following
        order

        will be respected.

            - Runs will be generated starting on or after the `start_time`
            - No more than `max_runs` runs will be generated
            - No runs will be generated after `end_time` is reached
            - At least `min_runs` runs will be generated
            - Runs will be generated until at least `start_time + min_time` is reached
      operationId: schedule_deployment_deployments__id__schedule_post
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
            format: uuid
            description: The deployment id
            title: Id
          description: The deployment id
        - name: x-prefect-api-version
          in: header
          required: false
          schema:
            type: string
            title: X-Prefect-Api-Version
      requestBody:
        content:
          application/json:
            schema:
              $ref: >-
                #/components/schemas/Body_schedule_deployment_deployments__id__schedule_post
      responses:
        '200':
          description: Successful Response
          content:
            application/json:
              schema: {}
        '422':
          description: Validation Error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/HTTPValidationError'
components:
  schemas:
    Body_schedule_deployment_deployments__id__schedule_post:
      properties:
        start_time:
          type: string
          format: date-time
          title: Start Time
          description: The earliest date to schedule
        end_time:
          type: string
          format: date-time
          title: End Time
          description: The latest date to schedule
        min_time:
          type: number
          format: time-delta
          title: Min Time
          description: >-
            Runs will be scheduled until at least this long after the
            `start_time`
        min_runs:
          type: integer
          title: Min Runs
          description: The minimum number of runs to schedule
        max_runs:
          type: integer
          title: Max Runs
          description: The maximum number of runs to schedule
      type: object
      title: Body_schedule_deployment_deployments__id__schedule_post
    HTTPValidationError:
      properties:
        detail:
          items:
            $ref: '#/components/schemas/ValidationError'
          type: array
          title: Detail
      type: object
      title: HTTPValidationError
    ValidationError:
      properties:
        loc:
          items:
            anyOf:
              - type: string
              - type: integer
          type: array
          title: Location
        msg:
          type: string
          title: Message
        type:
          type: string
          title: Error Type
        input:
          title: Input
        ctx:
          type: object
          title: Context
      type: object
      required:
        - loc
        - msg
        - type
      title: ValidationError

````

Built with [Mintlify](https://mintlify.com).