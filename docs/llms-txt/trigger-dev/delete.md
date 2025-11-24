# Source: https://trigger.dev/docs/management/schedules/delete.md

# Source: https://trigger.dev/docs/management/envvars/delete.md

# Source: https://trigger.dev/docs/management/schedules/delete.md

# Delete Schedule

> Delete a schedule by its ID. This will only work on `IMPERATIVE` schedules that were created in the dashboard or using the imperative SDK functions like `schedules.create()`.

## OpenAPI

````yaml v3-openapi DELETE /api/v1/schedules/{schedule_id}
paths:
  path: /api/v1/schedules/{schedule_id}
  method: delete
  servers:
    - url: https://api.trigger.dev
      description: Trigger.dev API
  request:
    security:
      - title: secretKey
        parameters:
          query: {}
          header:
            Authorization:
              type: http
              scheme: bearer
              description: >
                Use your project-specific Secret API key. Will start with
                `tr_dev_`, `tr_prod`, `tr_stg`, etc.


                You can find your Secret API key in the API Keys section of your
                Trigger.dev project dashboard.


                Our TypeScript SDK will default to using the value of the
                `TRIGGER_SECRET_KEY` environment variable if it is set. If you
                are using the SDK in a different environment, you can set the
                key using the `configure` function.


                ```typescript

                import { configure } from "@trigger.dev/sdk";


                configure({ accessToken: "tr_dev_1234" });

                ```
          cookie: {}
    parameters:
      path:
        schedule_id:
          schema:
            - type: string
              required: true
              description: The ID of the schedule.
      query: {}
      header: {}
      cookie: {}
    body: {}
    codeSamples:
      - lang: typescript
        source: |-
          import { schedules } from "@trigger.dev/sdk";

          await schedules.del(scheduleId);
  response:
    '200':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Schedule deleted successfully
        examples: {}
        description: Schedule deleted successfully
    '401':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Unauthorized request
        examples: {}
        description: Unauthorized request
    '404':
      _mintlify/placeholder:
        schemaArray:
          - type: any
            description: Resource not found
        examples: {}
        description: Resource not found
  deprecated: false
  type: path
components:
  schemas: {}

````